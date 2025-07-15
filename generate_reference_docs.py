import inspect

import jinja2
from numpydoc.docscrape import FunctionDoc

from truefoundry_sdk import TrueFoundry

ignore_attrs = ["with_raw_response", "internal"]
ignore_params = ["request_options"]
method_ranking = {
    "apply": 1,
    "create_or_update": 2,
    "get": 3,
    "get_by_fqn": 4,
    "list": 5,
    "delete": 6,
}

_METHOD_TEMPLATE = """\
<Accordion title="{{ method }}">
  {{ summary }}

  {%- if parameters %}

  #### Parameters

  {%- for parameter in parameters %}
    <ParamField 
      body="{{ parameter.name }}"
      type="{{ parameter.type }}"
      {% if parameter.default %}default="{{ parameter.default }}"{% endif %}
      {% if parameter.required %}required{% endif %}
    >
      {{ parameter.description }}
    </ParamField>
  {% endfor %}
  {%- endif %}

  {%- if returns %}

  #### Returns

  {% for return in returns %}
    <ResponseField 
      name="{{ return.name }}"
      type="{{ return.type }}"
    >
      {{ return.description }}
    </ResponseField>
  {% endfor %}
  {%- endif %}

  {%- if yields %}

  #### Yields
  {% for yield in yields %}
    {{ yield }}
  {% endfor %}
  {%- endif %}

  {%- if raises %}

  #### Raises
  {% for raise in raises %}
    {{ raise }}
  {% endfor %}
  {%- endif %}

  {%- if examples %}

  #### Usage

  {% for example in examples %}
    ```python
    {{ example | indent(4) }}
    ```

  {% endfor %}
  {%- endif %}
</Accordion>
"""


METHOD_TEMPLATE = jinja2.Template(_METHOD_TEMPLATE)


def _gen_for_client(client, rendered_docs, prefix=""):
    attrs = []
    for attr_name in dir(client):
        if attr_name.startswith("_"):
            continue
        if attr_name in ignore_attrs:
            continue
        if callable(getattr(client, attr_name)):
            attrs.append((attr_name, (0, method_ranking.get(attr_name, 99999))))
        else:
            attrs.append((attr_name, (1, 0)))
    attrs.sort(key=lambda x: x[1])
    for attr_name, _ in attrs:
        attr = getattr(client, attr_name)
        if callable(attr):
            doc = FunctionDoc(attr)
            sig = inspect.signature(attr)
            _defaults = {}
            _required = {}
            for name, parameter in sig.parameters.items():
                if parameter.default is inspect.Parameter.empty:
                    _required[name] = True
                else:
                    _required[name] = False
                    if parameter.default is not ...:
                        _defaults[name] = parameter.default
            method_name = f"{prefix}.{attr_name}"
            # TODO (chiragjn): Handle multiple examples if present
            examples = ["\n".join(doc["Examples"])]
            examples = [example for example in examples if example.strip()]
            rendered = METHOD_TEMPLATE.render(
                method=method_name,
                summary="\n".join(doc["Summary"]),
                parameters=[
                    {
                        "name": param.name,
                        "type": param.type,
                        "description": "\n".join(param.desc),
                        "default": repr(_defaults.get(param.name)) if param.name in _defaults else None,
                        "required": bool(_required.get(param.name)),
                    }
                    for param in doc["Parameters"]
                    if param.name not in ignore_params
                ],
                returns=[
                    {
                        "name": param.type,
                        "type": param.type,
                        "description": "\n".join(param.desc),
                    }
                    for param in doc["Returns"]
                ],
                examples=examples,
            )
            # print(rendered)
            rendered_docs.append((method_name, rendered))
        else:
            _gen_for_client(attr, rendered_docs, prefix=f"{prefix}.{attr_name}")


def main():
    rendered_docs = []
    client = TrueFoundry(base_url="", api_key="")
    _gen_for_client(client, rendered_docs, prefix="client")
    all_rendered = "\n\n".join(rendered for _, rendered in rendered_docs)
    content = f"""\
<AccordionGroup>
{all_rendered}
</AccordionGroup>
"""
    print(content)

    # with open('reference_docs.md', 'w') as f:
    #     f.write('\n'.join(rendered_docs))


if __name__ == "__main__":
    main()
