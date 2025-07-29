import ast
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional

from jinja2 import Template
from numpydoc.docscrape import FunctionDoc


@dataclass
class ParameterInfo:
    name: str
    type_annotation: str
    description: str
    default_value: Optional[str] = None
    is_required: bool = True
    type_info: Optional[Dict[str, Any]] = None


@dataclass
class ReturnInfo:
    name: str
    type: str
    description: str
    type_info: Optional[Dict[str, Any]] = None


@dataclass
class FunctionInfo:
    name: str
    signature: str
    docstring: str
    enhanced_description: str
    parameters: List[ParameterInfo]
    returns: List[ReturnInfo]
    examples: List[str]
    module: str
    is_method: bool = False


@dataclass
class FieldInfo:
    name: str
    type_annotation: str
    description: str
    default_value: Optional[str] = None
    is_required: bool = True
    is_optional: bool = False
    field_type: str = "string"  # string, number, boolean, object, array
    enum_values: Optional[List[str]] = None
    nested_type: Optional[str] = None
    type_info: Optional[Dict[str, Any]] = None


@dataclass
class TypeInfo:
    name: str
    docstring: str
    enhanced_description: str
    fields: Optional[List[FieldInfo]] = None
    enum_values: Optional[List[Dict[str, str]]] = None
    is_enum: bool = False
    is_manifest: bool = False
    module: str = ""
    client_module: str = ""
    base_classes: Optional[List[str]] = None
    is_response_type: bool = False
    is_input_type: bool = False
    structure_example: str = ""
    link_to_type: str = ""


@dataclass
class ClientModuleInfo:
    name: str
    display_name: str
    description: str
    methods: List[FunctionInfo]


class TrueFoundrySDKDocGenerator:
    def __init__(self, sdk_path: str, output_path: str = "truefoundry_sdk_docs"):
        self.sdk_path = Path(sdk_path)
        self.output_path = Path(output_path)
        self.types: Dict[str, TypeInfo] = {}
        self.types_docs_path = f"docs/{output_path}/types"
        self.enums_docs_path = f"docs/{output_path}/enums"
        self.clients_docs_path = f"{output_path}/"

        # Define client modules and their categories
        # Get all directories from sdk_path as module names
        module_dirs = [
            item.name
            for item in self.sdk_path.iterdir()
            if item.is_dir() and not item.name.startswith("_") and not item.name in ["core", "errors", "types"]
        ]

        self.client_modules = {
            module_name: {
                "display_name": module_name.replace("_", " ").title(),
                "description": f"Manage {module_name.replace('_', ' ')}",
            }
            for module_name in module_dirs
        }

    def extract_all_documentation(self) -> Dict[str, ClientModuleInfo]:
        client_modules = {}

        # Discover all types dynamically
        all_types = self._discover_all_types()
        self.types = all_types
        print(f"Discovered {len(all_types)} types")

        # Extract main client documentation
        main_client_info = self._extract_main_client_info()
        client_modules["main_client"] = main_client_info

        # Extract each client module
        for module_name, module_config in self.client_modules.items():
            module_info = self._extract_client_module_info(module_name, module_config, all_types)
            if module_info:
                client_modules[module_name] = module_info

        return client_modules

    def _extract_main_client_info(self) -> ClientModuleInfo:
        # Read the main client file
        client_file = self.sdk_path / "client.py"
        with open(client_file, "r", encoding="utf-8") as f:
            content = f.read()
        tree = ast.parse(content)

        base_client_file = self.sdk_path / "base_client.py"
        with open(base_client_file, "r", encoding="utf-8") as f:
            base_client_content = f.read()
        base_tree = ast.parse(base_client_content)

        # Extract methods from TrueFoundry class
        methods = []
        methods_map = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == "TrueFoundry":
                for child in node.body:
                    if isinstance(child, ast.FunctionDef) and not child.name.startswith("_"):
                        method_info = self._extract_function_info(child, "client", is_method=True, all_types=self.types)
                        if method_info and method_info.name not in methods_map:
                            methods.append(method_info)
                            methods_map[method_info.name] = method_info
                break

        for node in ast.walk(base_tree):
            if isinstance(node, ast.ClassDef) and node.name == "BaseTrueFoundry":
                for child in node.body:
                    if isinstance(child, ast.FunctionDef) and not child.name.startswith("_"):
                        method_info = self._extract_function_info(child, "client", is_method=True, all_types=self.types)
                        if method_info and method_info.name not in methods_map:
                            methods.append(method_info)
                            methods_map[method_info.name] = method_info

        return ClientModuleInfo(
            name="main_client",
            display_name="TrueFoundry Client",
            description="Main client for TrueFoundry SDK operations",
            methods=methods,
        )

    def _extract_client_module_info(
        self, module_name: str, module_config: Dict, all_types: Dict[str, TypeInfo]
    ) -> Optional[ClientModuleInfo]:
        """Extract documentation for a specific client module"""

        # Read the client file
        client_file = self.sdk_path / module_name / "client.py"
        if not client_file.exists():
            return None

        with open(client_file, "r", encoding="utf-8") as f:
            content = f.read()

        tree = ast.parse(content)

        # Extract methods from the main client class (not Async)
        methods = []
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and not node.name.startswith("Async"):
                for child in node.body:
                    if isinstance(child, ast.FunctionDef) and not child.name.startswith("_"):
                        method_info = self._extract_function_info(
                            child, f"{module_name}.client", is_method=True, all_types=all_types
                        )
                        if method_info:
                            methods.append(method_info)
                break

        # Also extract get_by_fqn methods from wrapped clients if they exist
        wrapped_methods = self._extract_wrapped_client_methods(module_name, all_types)
        methods.extend(wrapped_methods)

        return ClientModuleInfo(
            name=module_name,
            display_name=module_config["display_name"],
            description=module_config["description"],
            methods=methods,
        )

    def _extract_wrapped_client_methods(self, module_name: str, all_types: Dict[str, TypeInfo]) -> List[FunctionInfo]:
        """Extract get_by_fqn methods from wrapped clients"""
        methods = []

        # Read the wrapped clients file
        wrapped_clients_file = self.sdk_path / "_wrapped_clients.py"
        if not wrapped_clients_file.exists():
            return methods

        try:
            with open(wrapped_clients_file, "r", encoding="utf-8") as f:
                content = f.read()

            tree = ast.parse(content)

            # Look for the wrapped client class for this module
            wrapped_class_name = f"Wrapped{module_name.replace('_', ' ').title().replace(' ', '')}Client"

            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef) and node.name == wrapped_class_name:
                    for child in node.body:
                        if isinstance(child, ast.FunctionDef) and child.name == "get_by_fqn":
                            method_info = self._extract_function_info(
                                child, f"{module_name}.client", is_method=True, all_types=all_types
                            )
                            if method_info:
                                methods.append(method_info)
                    break

        except Exception as e:
            print(f"Error extracting wrapped client methods for {module_name}: {e}")

        return methods

    def _extract_type_info(
        self, node: ast.ClassDef, module_name: str, client_module: str, all_types: Dict[str, TypeInfo]
    ) -> Optional[TypeInfo]:
        """Extract detailed information about a type/class"""
        try:
            # Get docstring
            docstring = ast.get_docstring(node) or ""

            # Get base classes
            base_classes = []
            for base in node.bases:
                if isinstance(base, ast.Name):
                    base_classes.append(base.id)
                elif isinstance(base, ast.Attribute):
                    if hasattr(base.value, "id") and isinstance(base.value, ast.Name):
                        base_classes.append(f"{base.value.id}.{base.attr}")
                    else:
                        base_classes.append(base.attr)

            # Check if it's an enum
            is_enum = any("enum" in base.lower() for base in base_classes)

            # Only process enums or types with user-settable values
            if not is_enum:
                return None

            # Extract enum values
            enum_values = []

            for child in node.body:
                if isinstance(child, ast.Assign):
                    for target in child.targets:
                        if isinstance(target, ast.Name):
                            attr_name = target.id
                            attr_value = self._get_node_value(child.value)

                            if attr_value:
                                enum_values.append({"name": attr_name, "value": attr_value, "description": ""})

            return TypeInfo(
                name=node.name,
                docstring=docstring,
                enhanced_description="",
                enum_values=enum_values if enum_values else None,
                is_enum=is_enum,
                module=module_name,
                client_module=client_module,
                link_to_type=self._get_link_to_type(node.name, is_enum),
            )

        except Exception as e:
            print(f"Error extracting type {node.name}: {e}")
            return None

    def _get_link_to_type(self, type_name: str, is_enum: bool = False) -> str:
        """Get the link to a type"""
        if is_enum:
            return f"/{self.enums_docs_path}#{type_name.lower()}"
        else:
            return f"/{self.types_docs_path}#{type_name.lower()}"

    def _extract_function_info(
        self,
        node: ast.FunctionDef,
        module_name: str,
        is_method: bool = False,
        all_types: Optional[Dict[str, TypeInfo]] = None,
    ) -> Optional[FunctionInfo]:
        """Extract detailed information about a function using numpydoc"""
        try:
            # Skip __init__ methods and with_raw_response methods
            if node.name == "__init__" or node.name == "with_raw_response":
                return None

            # Get docstring
            docstring = ast.get_docstring(node) or ""

            # Create a mock function object for numpydoc
            class MockFunction:
                def __init__(self, name, docstring, signature):
                    self.__name__ = name
                    self.__doc__ = docstring
                    self.__signature__ = signature

            # Get function signature
            signature = self._create_signature_from_node(node)
            mock_func = MockFunction(node.name, docstring, signature)

            # Parse with numpydoc
            try:
                doc = FunctionDoc(mock_func)

                # Extract parameters
                parameters = []
                for param in doc["Parameters"]:
                    if param.name not in ["request_options"]:  # Skip internal parameters
                        # Extract type information and create links
                        type_info = self._extract_type_info_from_param(param.type, all_types or {})

                        param_info = ParameterInfo(
                            name=param.name,
                            type_annotation=param.type,
                            description="\n".join(param.desc),
                            is_required="Optional" not in param.type,
                            type_info=type_info,
                        )
                        parameters.append(param_info)

                # Extract returns
                returns = []
                for ret in doc["Returns"]:
                    return_info = ReturnInfo(
                        name=ret.type,
                        type=ret.type,
                        description="\n".join(ret.desc),
                        type_info=self._extract_type_info_from_param(ret.type, all_types or {}),
                    )
                    returns.append(return_info)

                # Generate proper Python examples based on method signature
                examples = []
                # Create a proper Python example
                example_lines = [
                    "from truefoundry import TrueFoundry",
                    "",
                    "client = TrueFoundry(",
                    '    api_key="YOUR_API_KEY",',
                    '    base_url="https://yourhost.com/path/to/api",',
                    ")",
                    "",
                ]

                # Add method call based on parameters
                # For main client methods, use client.method_name
                # For module methods, use client.module_name.method_name
                if module_name == "client":
                    method_call = f"client.{node.name}("
                else:
                    # Extract module name from module_name (e.g., "ml_repos.client" -> "ml_repos")
                    module_part = module_name.split(".")[0]
                    method_call = f"client.{module_part}.{node.name}("

                # Add parameters based on what we have
                param_lines = []
                for param in parameters:
                    if param.name == "manifest":
                        param_lines.append(f'    {param.name}={{"key": "value"}},')
                    elif param.name in ["id", "application_id", "cluster_id", "workspace_id"]:
                        param_lines.append(f'    {param.name}="{param.name}_value",')
                    elif param.name in ["limit", "offset"]:
                        param_lines.append(f"    {param.name}=10,")
                    elif param.name in ["dry_run", "force_deploy", "trigger_on_deploy"]:
                        param_lines.append(f"    {param.name}=False,")
                    else:
                        param_lines.append(f'    {param.name}="value",')

                if param_lines:
                    method_call += "\n" + "\n".join(param_lines)

                method_call += "\n)"
                example_lines.append(method_call)

                # Add response handling if it's a list method
                if node.name == "list":
                    example_lines.extend(
                        [
                            "",
                            "# Iterate through results",
                            "for item in response:",
                            "    print(item.name)",
                            "",
                            "# Or paginate page by page",
                            "for page in response.iter_pages():",
                            "    for item in page:",
                            "        print(item.name)",
                        ]
                    )

                examples.append("\n".join(example_lines))

                # Get signature from AST
                signature = self._create_signature_from_node(node)

                # Clean up the enhanced description to avoid MDX parsing issues
                summary_lines = doc.get("Summary", [])
                enhanced_description = ""
                if summary_lines:
                    # Only take the first line of summary to avoid raw docstring content
                    enhanced_description = summary_lines[0].strip()

                return FunctionInfo(
                    name=node.name,
                    signature=signature,
                    docstring=docstring,
                    enhanced_description=enhanced_description,
                    parameters=parameters,
                    returns=returns,
                    examples=examples,
                    module=module_name,
                    is_method=is_method,
                )

            except Exception as e:
                # Fallback to basic extraction if numpydoc fails
                print(f"Warning: numpydoc failed for {node.name}, using fallback: {e}")
                # return self._extract_function_info_fallback(node, module_name, is_method, all_types)
                return None

        except Exception as e:
            print(f"Error extracting function {node.name}: {e}")
            return None

    def _get_type_annotation(self, annotation) -> str:
        """Extract type annotation as string"""
        if annotation is None:
            return "Any"

        if isinstance(annotation, ast.Name):
            return annotation.id
        elif isinstance(annotation, ast.Attribute):
            if hasattr(annotation.value, "id") and isinstance(annotation.value, ast.Name):
                return f"{annotation.value.id}.{annotation.attr}"
            else:
                return annotation.attr
        elif isinstance(annotation, ast.Subscript):
            # Handle generic types like List[str], Dict[str, int]
            value = self._get_type_annotation(annotation.value)
            slice_value = self._get_type_annotation(annotation.slice)
            return f"{value}[{slice_value}]"
        elif isinstance(annotation, ast.Tuple):
            # Handle tuple types
            elements = [self._get_type_annotation(el) for el in annotation.elts]
            return f"({', '.join(elements)})"
        else:
            return "Any"

    def _get_node_value(self, node) -> str:
        """Get string representation of a node value"""
        if isinstance(node, ast.Constant):
            return repr(node.value)
        elif isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Attribute):
            if hasattr(node.value, "id") and isinstance(node.value, ast.Name):
                return f"{node.value.id}.{node.attr}"
            else:
                return node.attr
        else:
            return "..."

    def _create_signature_from_node(self, node: ast.FunctionDef) -> str:
        """Create a readable function signature from AST node"""
        params = []

        for arg in node.args.args:
            if arg.arg == "self":
                continue

            param_str = arg.arg
            if arg.annotation:
                param_str += f": {self._get_type_annotation(arg.annotation)}"
            params.append(param_str)

        # Handle defaults
        defaults = node.args.defaults
        if defaults:
            num_defaults = len(defaults)
            num_params = len(params)
            for i, default in enumerate(defaults):
                param_index = num_params - num_defaults + i
                if param_index < len(params):
                    default_value = self._get_node_value(default)
                    params[param_index] += f" = {default_value}"

        return f"{node.name}({', '.join(params)})"

    def _extract_type_info_from_param(self, type_str: str, all_types: Dict[str, TypeInfo]) -> Optional[Dict[str, Any]]:
        for type_name, type_info in all_types.items():
            if type_name == type_str:
                link = self._get_link_to_type(type_info.name, type_info.is_enum)
                return {"name": type_info.name, "description": type_info.enhanced_description or "", "link": link}

        best_match = None
        best_match_length = 0

        for type_name, type_info in all_types.items():
            # Check if type_name is a complete word within type_str
            # This prevents "ApplyMlEntityResponse" from matching "ApplyMlEntityResponseData"
            if type_name in type_str:
                # Prefer longer type names as they're more specific
                if len(type_name) > best_match_length:
                    best_match = type_info
                    best_match_length = len(type_name)

        if best_match:
            link = self._get_link_to_type(best_match.name, best_match.is_enum)
            return {"name": best_match.name, "description": best_match.enhanced_description or "", "link": link}

        return None

    def _is_manifest_relevant_to_module(self, manifest_type_name: str, module_name: str) -> bool:
        base_name = manifest_type_name.replace("Manifest", "").lower()
        module_name_lower = module_name.lower()

        # Direct match
        if base_name == module_name_lower:
            return True

        # Check for partial matches
        if module_name_lower in base_name or base_name in module_name_lower:
            return True

        # Special cases for compound names
        if module_name_lower == "applications" and "application" in base_name:
            return True
        elif module_name_lower == "data_directories" and "datadirectory" in base_name:
            return True
        elif module_name_lower == "personal_access_tokens" and "personalaccesstoken" in base_name:
            return True
        elif module_name_lower == "virtual_accounts" and "virtualaccount" in base_name:
            return True
        elif module_name_lower == "tracing_projects" and "tracingproject" in base_name:
            return True

        return False

    def _discover_all_types(self) -> Dict[str, TypeInfo]:
        """Dynamically discover all types from the types directory"""
        all_types = {}

        # Discover types from main types directory
        main_types_dir = self.sdk_path / "types"
        if main_types_dir.exists():
            for type_file in main_types_dir.glob("*.py"):
                if type_file.name.startswith("_"):
                    continue

                types_from_file = self._extract_types_from_file(type_file, "types")
                all_types.update(types_from_file)

        # Discover types from client-specific type directories
        for module_name in self.client_modules.keys():
            types_dir = self.sdk_path / module_name / "types"
            if types_dir.exists():
                for type_file in types_dir.glob("*.py"):
                    if type_file.name.startswith("_"):
                        continue

                    types_from_file = self._extract_types_from_file(type_file, f"{module_name}.types")
                    all_types.update(types_from_file)

        return all_types

    def _extract_types_from_file(self, type_file: Path, module_name: str) -> Dict[str, TypeInfo]:
        types = {}

        try:
            with open(type_file, "r", encoding="utf-8") as f:
                content = f.read()

            tree = ast.parse(content)

            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    type_info = self._extract_detailed_type_info(node, f"{module_name}.{type_file.stem}")
                    if type_info:
                        types[type_info.name] = type_info
                elif isinstance(node, ast.Assign):
                    # Handle type aliases like TypeName = typing.Union[...]
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            type_name = target.id
                            if isinstance(node.value, ast.Attribute) and node.value.attr == "Union":
                                # This is a typing.Union type alias
                                type_info = self._extract_union_type_info(
                                    type_name, node.value, f"{module_name}.{type_file.stem}"
                                )
                                if type_info:
                                    types[type_info.name] = type_info
                            elif (
                                isinstance(node.value, ast.Subscript)
                                and isinstance(node.value.value, ast.Attribute)
                                and node.value.value.attr == "Union"
                            ):
                                # This is a typing.Union[...] type alias
                                type_info = self._extract_union_type_info(
                                    type_name, node.value, f"{module_name}.{type_file.stem}"
                                )
                                if type_info:
                                    types[type_info.name] = type_info

        except Exception as e:
            print(f"Error extracting types from {type_file}: {e}")

        return types

    def _extract_union_type_info(self, type_name: str, union_node, module_name: str) -> Optional[TypeInfo]:
        """Extract information about a union type alias"""
        try:
            # Get the union types
            union_types = []
            if isinstance(union_node, ast.Subscript):
                # Handle typing.Union[Type1, Type2, ...]
                if isinstance(union_node.slice, ast.Tuple):
                    for elt in union_node.slice.elts:
                        if isinstance(elt, ast.Name):
                            union_types.append(elt.id)
                        elif isinstance(elt, ast.Attribute):
                            union_types.append(f"{elt.value.id}.{elt.attr}" if hasattr(elt.value, "id") else elt.attr)
                else:
                    # Single type in Union
                    if isinstance(union_node.slice, ast.Name):
                        union_types.append(union_node.slice.id)
                    elif isinstance(union_node.slice, ast.Attribute):
                        union_types.append(
                            f"{union_node.slice.value.id}.{union_node.slice.attr}"
                            if hasattr(union_node.slice.value, "id")
                            else union_node.slice.attr
                        )

            # Create a description for the union type
            description = f"Union type that can be one of: {', '.join(union_types)}"

            return TypeInfo(
                name=type_name,
                docstring=description,
                enhanced_description=description,
                fields=None,
                enum_values=None,
                is_enum=False,
                is_manifest="Manifest" in type_name,
                module=module_name,
                base_classes=union_types,
                is_response_type=any(
                    word in type_name.lower() for word in ["response", "get", "list", "create", "update", "delete"]
                ),
                is_input_type=any(word in type_name.lower() for word in ["request", "input", "manifest"]),
                structure_example=f"One of: {', '.join(union_types)}",
                link_to_type=self._get_link_to_type(type_name, False),
            )

        except Exception as e:
            print(f"Error extracting union type {type_name}: {e}")
            return None

    def _extract_detailed_type_info(self, node: ast.ClassDef, module_name: str) -> Optional[TypeInfo]:
        try:
            # Get docstring
            docstring = ast.get_docstring(node) or ""
            # Clean up the docstring
            cleaned_docstring = self._clean_description(docstring)

            # Get base classes
            base_classes = []
            for base in node.bases:
                if isinstance(base, ast.Name):
                    base_classes.append(base.id)
                elif isinstance(base, ast.Attribute):
                    if hasattr(base.value, "id") and isinstance(base.value, ast.Name):
                        base_classes.append(f"{base.value.id}.{base.attr}")
                    else:
                        base_classes.append(base.attr)

            # Check if it's an enum
            is_enum = any("enum" in base.lower() for base in base_classes)

            # Check if it's a manifest type
            is_manifest = "Manifest" in node.name

            # Check if it's a response type
            is_response_type = any(
                word in node.name.lower() for word in ["response", "get", "list", "create", "update", "delete"]
            )

            # Check if it's an input type
            is_input_type = any(word in node.name.lower() for word in ["request", "input", "manifest"])

            # Extract fields
            fields = []
            enum_values = []

            if is_enum:
                # Extract enum values
                for child in node.body:
                    if isinstance(child, ast.Assign):
                        for target in child.targets:
                            if isinstance(target, ast.Name):
                                attr_name = target.id
                                attr_value = self._get_node_value(child.value)

                                if attr_value:
                                    enum_values.append({"name": attr_name, "value": attr_value, "description": ""})
            else:
                # Extract fields from class attributes
                for child in node.body:
                    if isinstance(child, ast.AnnAssign) and child.target:
                        field_info = self._extract_field_info(child, node)
                        if field_info:
                            fields.append(field_info)

            # Generate a structure example for the type
            structure_example = self._generate_structure_example(fields)

            return TypeInfo(
                name=node.name,
                docstring=cleaned_docstring,
                enhanced_description=cleaned_docstring.split(".")[0] if cleaned_docstring else "",
                fields=fields if fields else None,
                enum_values=enum_values if enum_values else None,
                is_enum=is_enum,
                is_manifest=is_manifest,
                module=module_name,
                base_classes=base_classes,
                is_response_type=is_response_type,
                is_input_type=is_input_type,
                structure_example=structure_example,
                link_to_type=self._get_link_to_type(node.name, is_enum),
            )

        except Exception as e:
            print(f"Error extracting type {node.name}: {e}")
            return None

    def _is_global_constant(self, node: ast.Assign) -> bool:
        """Check if an assignment node represents a global constant (uppercase screaming ones)"""
        try:
            # Check if all targets are uppercase names (global constants)
            for target in node.targets:
                if isinstance(target, ast.Name):
                    # If the target name is all uppercase, it's likely a global constant
                    if target.id.isupper():
                        return True
                elif isinstance(target, ast.Tuple):
                    # Check all elements in a tuple assignment
                    for elt in target.elts:
                        if isinstance(elt, ast.Name) and elt.id.isupper():
                            return True
            return False
        except Exception:
            return False

    def _extract_type_alias_info(self, node: ast.Assign, module_name: str) -> Optional[TypeInfo]:
        """Extract information about a type alias (like Union types)"""
        try:
            # Check if this is a type alias assignment
            if len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                type_name = node.targets[0].id

                # Get the type annotation
                type_annotation = self._get_type_annotation(node.value)

                # Create a basic TypeInfo for the type alias
                return TypeInfo(
                    name=type_name,
                    docstring="",  # Type aliases typically don't have docstrings
                    enhanced_description=f"Type alias: {type_annotation}",
                    fields=None,  # Type aliases don't have fields
                    enum_values=None,
                    is_enum=False,
                    is_manifest=False,
                    module=module_name,
                    base_classes=None,
                    is_response_type=False,
                    is_input_type=False,
                    structure_example=type_annotation,
                    link_to_type=self._get_link_to_type(type_name, False),
                )

        except Exception as e:
            print(f"Error extracting type alias info: {e}")

        return None

    def _extract_field_info(self, node: ast.AnnAssign, class_node: ast.ClassDef) -> Optional[FieldInfo]:
        """Extract detailed information about a field"""
        try:
            if not isinstance(node.target, ast.Name):
                return None

            field_name = node.target.id
            type_annotation = self._get_type_annotation(node.annotation)

            # Get field description from the docstring that follows the field
            description = ""

            # Look for docstring after this field assignment
            if node.value and hasattr(node.value, "keywords") and isinstance(node.value, ast.Call):
                for keyword in node.value.keywords:
                    if keyword.arg == "description":
                        raw_description = self._get_node_value(keyword.value)
                        description = self._clean_description(raw_description)
                        break

            # If no description found in pydantic.Field, look for docstring in the class
            if not description:
                # Find the docstring that follows this field assignment
                for i, child in enumerate(class_node.body):
                    if child == node and i + 1 < len(class_node.body):
                        next_child = class_node.body[i + 1]
                        if isinstance(next_child, ast.Expr) and isinstance(next_child.value, ast.Constant):
                            docstring = next_child.value.value
                            if isinstance(docstring, str):
                                description = self._clean_description(docstring)
                                break

            # Determine field properties
            is_optional = "Optional" in type_annotation or "typing.Optional" in type_annotation
            is_required = not is_optional

            # Determine field type
            field_type = self._determine_field_type(type_annotation)

            # Extract nested type information
            nested_type = self._extract_nested_type(type_annotation)

            # Get default value
            default_value = None
            if node.value:
                default_value = self._get_node_value(node.value)

            return FieldInfo(
                name=field_name,
                type_annotation=type_annotation,
                description=re.sub(r"([<>\{\}\[\]\(\)])", r"\\\1", description),
                default_value=default_value,
                is_required=is_required,
                is_optional=is_optional,
                field_type=field_type,
                enum_values=[],
                nested_type=nested_type,
            )

        except Exception as e:
            print(f"Error extracting field info: {e}")
            return None

    def _add_type_info_to_field(self, field: FieldInfo, all_types: Dict[str, TypeInfo]) -> FieldInfo:
        """Add type information to a field"""
        type_info = self._extract_type_info_from_param(
            field.nested_type if field.nested_type else field.type_annotation, all_types
        )
        if type_info:
            field.type_info = type_info
        return field

    def _clean_description(self, description: str) -> str:
        """Clean up description by removing metadata and formatting"""
        if not description:
            return ""

        # Remove metadata lines that start with +
        lines = description.split("\n")
        cleaned_lines = []

        for line in lines:
            line = line.strip()
            # Skip metadata lines
            if line.startswith("+"):
                continue
            # Skip empty lines
            if not line:
                continue
            # Skip lines that are just metadata
            if (
                line.startswith("+label=")
                or line.startswith("+icon=")
                or line.startswith("+sort=")
                or line.startswith("+usage=")
                or line.startswith("+message=")
                or line.startswith("+placeholder=")
                or line.startswith("+uiType=")
                or line.startswith("+uiProps=")
            ):
                continue
            # Skip lines that contain only metadata patterns
            if any(
                pattern in line
                for pattern in [
                    "+label=",
                    "+icon=",
                    "+sort=",
                    "+usage=",
                    "+message=",
                    "+placeholder=",
                    "+uiType=",
                    "+uiProps=",
                ]
            ):
                continue
            cleaned_lines.append(line)

        result = " ".join(cleaned_lines)

        # Remove any remaining metadata patterns
        import re

        result = re.sub(r"\+[a-zA-Z_]+=[^,\s]+", "", result)
        result = re.sub(r"\+[a-zA-Z_]+=\{[^}]+\}", "", result)

        # Clean up extra whitespace
        result = re.sub(r"\s+", " ", result).strip()

        # Extract usage information if available
        usage_match = re.search(r"\+usage=([^+]+)", description)
        if usage_match:
            usage_text = usage_match.group(1).strip()
            if usage_text:
                result = usage_text

        # Extract message information if available
        message_match = re.search(r"\+message=([^+]+)", description)
        if message_match:
            message_text = message_match.group(1).strip()
            if message_text:
                result = message_text

        return result

    def _determine_field_type(self, type_annotation: str) -> str:
        """Determine the basic field type from type annotation"""
        type_lower = type_annotation.lower()

        if any(t in type_lower for t in ["str", "string"]):
            return "string"
        elif any(t in type_lower for t in ["int", "float", "number"]):
            return "number"
        elif any(t in type_lower for t in ["bool", "boolean"]):
            return "boolean"
        elif any(t in type_lower for t in ["list", "array", "typing.list"]):
            return "array"
        elif any(t in type_lower for t in ["dict", "typing.dict"]):
            return "object"
        else:
            return "object"  # Default to object for complex types

    def _extract_nested_type(self, type_annotation: str) -> Optional[str]:
        """Extract nested type from type annotation"""
        # Handle List[Type] and Optional[Type]
        if "List[" in type_annotation:
            start = type_annotation.find("List[") + 5
            end = type_annotation.rfind("]")
            if start > 4 and end > start:
                return type_annotation[start:end]
        elif "Optional[" in type_annotation:
            start = type_annotation.find("Optional[") + 9
            end = type_annotation.rfind("]")
            if start > 8 and end > start:
                return type_annotation[start:end]

        return None

    def _generate_structure_example(self, fields: List[FieldInfo]) -> str:
        """Generate a more realistic structure example based on field types"""
        if not fields:
            return "{}"

        lines = ["{"]
        for i, field in enumerate(fields):
            example_value = self._get_field_example_value(field)
            comma = "," if i < len(fields) - 1 else ""
            lines.append(f'  "{field.name}": {example_value}{comma}')
        lines.append("}")

        return "\n".join(lines)

    def _get_field_example_value(self, field: FieldInfo) -> str:
        """Get a realistic example value for a field"""
        if field.field_type == "string":
            if "name" in field.name.lower():
                return '"my-name"'
            elif "url" in field.name.lower():
                return '"https://example.com"'
            elif "id" in field.name.lower():
                return '"id-123"'
            elif "type" in field.name.lower():
                return '"type"'
            else:
                return '"example_string"'
        elif field.field_type == "number":
            if "port" in field.name.lower():
                return "8080"
            elif "limit" in field.name.lower() or "offset" in field.name.lower():
                return "10"
            else:
                return "123"
        elif field.field_type == "boolean":
            return "true"
        elif field.field_type == "array":
            if field.nested_type:
                if "str" in field.nested_type.lower():
                    if "domain" in field.name.lower():
                        return '["example.com", "*.example.com"]'
                    elif "name" in field.name.lower():
                        return '["dev", "staging", "prod"]'
                    else:
                        return '["item1", "item2"]'
                elif "int" in field.nested_type.lower():
                    return "[1, 2, 3]"
                elif "bool" in field.nested_type.lower():
                    return "[true, false]"
                else:
                    return '[{"nested_key": "nested_value"}]'
            else:
                return '["item1", "item2"]'
        else:  # object
            if field.nested_type:
                if "str" in field.nested_type.lower():
                    return '"example_string"'
                elif "int" in field.nested_type.lower():
                    return "123"
                elif "bool" in field.nested_type.lower():
                    return "true"
                else:
                    return '{"nested_key": "nested_value"}'
            else:
                return '{"key": "value"}'

    def generate_mintlify_docs(self):
        """Generate comprehensive Mintlify documentation"""
        output_path = Path(self.output_path)

        # Clean up existing directory
        if output_path.exists():
            shutil.rmtree(output_path)
        output_path.mkdir(exist_ok=True)

        # Extract all documentation
        client_modules = self.extract_all_documentation()

        # Add type information to fields
        for type_info in self.types.values():
            if type_info.fields:
                for field in type_info.fields:
                    field = self._add_type_info_to_field(field, self.types)

        # Generate home page
        self._generate_home_page(client_modules, output_path)

        # Generate main client documentation
        self._generate_main_client_docs(client_modules["main_client"], output_path)

        # Generate documentation for each client module
        for module_name, module_info in client_modules.items():
            if module_name != "main_client":
                self._generate_client_module_docs(module_info, output_path)

        # Generate types documentation
        self._generate_types_docs(output_path)

        # Generate enums documentation
        self._generate_enum_docs(output_path)

    def _generate_home_page(self, client_modules: Dict[str, ClientModuleInfo], output_path: Path):
        """Generate a beautiful home page showcasing all clients"""

        # Define clients to ignore
        ignore_clients = ["internal"]

        # Get all non-main clients, excluding ignored ones
        all_clients = [
            module_info
            for module_name, module_info in client_modules.items()
            if module_name != "main_client" and module_name not in ignore_clients
        ]

        template = Template("""---
title: "TrueFoundry Python SDK"
description: "Complete Python SDK for TrueFoundry - Build, deploy, and manage ML applications"
---
## Installation

```bash
pip install truefoundry
```

## Quick Example

```python
from truefoundry import TrueFoundry

# Initialize the client
client = TrueFoundry(
    base_url="https://api.truefoundry.com",
    api_key="your_api_key"
)

# List your applications
applications = client.applications.list()
for app in applications:
    print(f"Application: {app.name}")
```

## Available Clients

<div className="space-y-0">
  <a href="{{ clients_docs_path }}main_client" className="group flex items-center justify-between py-1 px-2 bg-white border-b border-gray-200 hover:bg-gray-50 transition-colors">
    <h3 className="font-medium text-gray-900 group-hover:text-blue-700 transition-colors">TrueFoundry Client</h3>
    <div className="flex items-center space-x-2">
      <span className="text-xs text-gray-500">Main client</span>
      <span className="text-blue-500 group-hover:text-blue-700 transition-colors">→</span>
    </div>
  </a>
{% for client in all_clients %}
  <a href="{{ clients_docs_path }}{{ client.name }}" className="group flex items-center justify-between py-1 px-2 bg-white border-b border-gray-200 hover:bg-gray-50 transition-colors">
    <h3 className="font-medium text-gray-900 group-hover:text-blue-700 transition-colors">{{ client.display_name }}</h3>
    <div className="flex items-center space-x-2">
      <span className="text-xs text-gray-500">{{ client.methods|length }} methods</span>
      <span className="text-blue-500 group-hover:text-blue-700 transition-colors">→</span>
    </div>
  </a>
{% endfor %}
</div>

## Additional Resources

<div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-8">
  <a href="{{ clients_docs_path }}types" className="block p-4 bg-gray-50 border border-gray-200 rounded-lg hover:bg-gray-100 transition-colors">
    <h3 className="font-semibold text-gray-900 mb-2">📋 Data Types</h3>
    <p className="text-sm text-gray-600">Explore all input and output types used in the SDK</p>
  </a>
  
  <a href="{{ clients_docs_path }}enums" className="block p-4 bg-gray-50 border border-gray-200 rounded-lg hover:bg-gray-100 transition-colors">
    <h3 className="font-semibold text-gray-900 mb-2">🔢 Enums</h3>
    <p className="text-sm text-gray-600">View all available enum values and constants</p>
  </a>
</div>

## Getting Help

- **Documentation**: Browse through the client documentation above
- **GitHub**: [TrueFoundry Python SDK](https://github.com/truefoundry/truefoundry-python-sdk)
- **Support**: Reach out to our support team for assistance

---

<div className="text-center text-sm text-gray-500 mt-12">
  Built with ❤️ by the TrueFoundry team
</div>
""")

        content = template.render(
            client_modules=client_modules,
            all_clients=sorted(all_clients, key=lambda x: x.name.lower()),
            clients_docs_path=self.clients_docs_path,
        )

        with open(output_path / "index.mdx", "w", encoding="utf-8") as f:
            f.write(content)

    def _generate_main_client_docs(self, client_info: ClientModuleInfo, output_path: Path):
        template = Template("""---
title: "TrueFoundry Client"
description: "Main client for TrueFoundry SDK operations"
---
The main client for TrueFoundry SDK operations. This client provides access to all SDK functionality through organized sub-clients.

## Client Methods

{% for method in client_info.methods %}
<Accordion title="{{ method.name }}">
  {% if method.enhanced_description and method.enhanced_description.strip() %}
  {{ method.enhanced_description }}
  {% else %}
  {{ method.docstring.split('\n')[0] if method.docstring else 'No description available.' }}
  {% endif %}

  {%- if method.parameters %}
  #### Parameters
  {%- for parameter in method.parameters %}
    <ParamField 
      body="{{ parameter.name }}"
      type="{{ parameter.type_annotation }}"
      {% if parameter.default_value %}default="{{ parameter.default_value }}"{% endif %}
      {% if parameter.is_required %}required{% endif %}
    >
      {{ parameter.description or 'No description' }}
      {%- if parameter.type_info %}
      
      **Type Details:** [{{ parameter.type_info.name }}]({{ parameter.type_info.link }})
      {%- endif %}
    </ParamField>
  {% endfor %}
  {%- endif %}

  {%- if method.returns %}
  #### Returns
  {% for return in method.returns %}
    <ResponseField 
      name="{{ return.name }}"
      type="{{ return.type }}"
    >
      {{ return.description or 'No description' }}
      {%- if return.type_info %}

      **Type Details:** [{{ return.type_info.name }}]({{ return.type_info.link }})
      {%- endif %}
    </ResponseField>
  {% endfor %}
  {%- endif %}

  {%- if method.examples %}
  #### Usage
  {% for example in method.examples %}
```python
{{ example | safe }}
```
  {% endfor %}
  {%- endif %}
</Accordion>

{% endfor %}
""")

        content = template.render(client_info=client_info)

        with open(output_path / "main_client.mdx", "w", encoding="utf-8") as f:
            f.write(content)

    def _generate_types_docs(self, output_path: Path):
        template = Template("""---
title: "SDK Types"
description: "All types in the SDK"
---
{% for type_info in sorted_types %}
{% if type_info.fields %}
## {{ type_info.name }}

{% for field in type_info.fields %}

<ParamField 
    body="{{ field.name }}"
    type="{{ field.type_annotation }}"
    {% if field.default_value %}default="{{ field.default_value }}"{% endif %}
    {% if field.is_required %}required{% endif %}
>
    {{ field.description or 'No description' }}
    {% if field.type_info %}

    **Type Details:** [{{ field.type_info.name }}]({{ field.type_info.link }})
    {% endif %}
</ParamField>

{% endfor %}
{% elif type_info.base_classes and not type_info.is_enum %}
## {{ type_info.name }}

{{ type_info.enhanced_description }}

**Union Types:** 
{%- for base_class in type_info.base_classes %}
[{{ base_class }}](/docs/truefoundry_sdk_docs/types#{{ base_class.lower() }}){{ "," if not loop.last else "" }}
{%- endfor %}

{% endif %}
{% endfor %}

""")
        # Sort types by name
        sorted_types = sorted(self.types.values(), key=lambda x: x.name.lower())
        content = template.render(types=self.types, sorted_types=sorted_types)
        with open(output_path / "types.mdx", "w", encoding="utf-8") as f:
            f.write(content)

    def _generate_enum_docs(self, output_path: Path):
        template = Template("""---
title: "All enums"
description: "All enums in the SDK"
---
{% for type_info in sorted_enums %}
{% if type_info.is_enum and type_info.enum_values %}
## {{ type_info.name }}
**Available Values:**
{% for value in type_info.enum_values %}
- **{{ value.name }}** = `{{ value.value }}`{% if value.description %} - {{ value.description }}{% endif %}
{% endfor %}
{% endif %}
{% endfor %}
""")
        # Sort enums by name
        sorted_enums = sorted(
            [t for t in self.types.values() if t.is_enum and t.enum_values], key=lambda x: x.name.lower()
        )
        content = template.render(types=self.types, sorted_enums=sorted_enums)
        with open(output_path / "enums.mdx", "w", encoding="utf-8") as f:
            f.write(content)

    def _generate_client_module_docs(self, module_info: ClientModuleInfo, output_path: Path):
        template = Template("""---
title: "{{ module_info.display_name }}"
description: "{{ module_info.description }}"
---
## Methods

{% for method in module_info.methods %}
<Accordion title="{{ method.name }}">
  {% if method.enhanced_description and method.enhanced_description.strip() %}
  {{ method.enhanced_description }}
  {% else %}
  {{ method.docstring.split('\n')[0] if method.docstring else 'No description available.' }}
  {% endif %}

  {%- if method.parameters %}
  #### Parameters
  {%- for parameter in method.parameters %}
    <ParamField 
      body="{{ parameter.name }}"
      type="{{ parameter.type_annotation }}"
      {% if parameter.default_value %}default="{{ parameter.default_value }}"{% endif %}
      {% if parameter.is_required %}required{% endif %}
    >
      {{ parameter.description or 'No description' }}
      {%- if parameter.type_info %}
      
      **Type Details:** [{{ parameter.type_info.name }}]({{ parameter.type_info.link }})
      {%- endif %}
    </ParamField>
  {% endfor %}
  {%- endif %}

  {%- if method.returns %}
  #### Returns
  {% for return in method.returns %}
    <ResponseField 
      name="{{ return.name }}"
      type="{{ return.type }}"
    >
      {{ return.description or 'No description' }}
      {%- if return.type_info %}
                            
      **Type Details:** [{{ return.type_info.name }}]({{ return.type_info.link }})
      {%- endif %}
    </ResponseField>
  {% endfor %}
  {%- endif %}

  {%- if method.examples %}
  #### Usage
  {% for example in method.examples %}
```python
{{ example | safe }}
```
  {% endfor %}
  {%- endif %}
</Accordion>

{% endfor %}
""")

        content = template.render(module_info=module_info)

        with open(output_path / f"{module_info.name}.mdx", "w", encoding="utf-8") as f:
            f.write(content)


if __name__ == "__main__":
    generator = TrueFoundrySDKDocGenerator(sdk_path="src/truefoundry_sdk", output_path="truefoundry_sdk_docs")

    generator.generate_mintlify_docs()
    print("✅ Enhanced documentation generated successfully!")
