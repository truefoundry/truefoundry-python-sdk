# Reference
## V1 Clusters
<details><summary><code>client.v1.clusters.<a href="src/truefoundry_sdk/v1/clusters/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a list of all latest Clusters. Pagination is available based on query parameters.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
response = client.v1.clusters.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**offset:** `typing.Optional[float]` — Number of Items Skipped. Defaults to 0 if not provided.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — The maximum number of items to return per page. Defaults to a pre-defined value if not provided.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.clusters.<a href="src/truefoundry_sdk/v1/clusters/client.py">create_or_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or Update cluster with provided manifest
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import ClusterManifest, Collaborator, TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.clusters.create_or_update(
    manifest=ClusterManifest(
        name="name",
        cluster_type="aws-eks",
        environment_names=["environment_names"],
        collaborators=[
            Collaborator(
                subject="subject",
                role_id="role_id",
            )
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**manifest:** `ClusterManifest` — Cluster manifest
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` — Dry run the cluster creation/update
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.clusters.<a href="src/truefoundry_sdk/v1/clusters/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get cluster associated with provided id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.clusters.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Cluster id of the cluster
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.clusters.<a href="src/truefoundry_sdk/v1/clusters/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete cluster associated with provided cluster id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.clusters.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Cluster id of the cluster
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V1 Environments
<details><summary><code>client.v1.environments.<a href="src/truefoundry_sdk/v1/environments/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List environments, if no environments are found, default environments are created and returned. Pagination is available based on query parameters
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
response = client.v1.environments.list(
    limit=10,
    offset=0,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of items per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.environments.<a href="src/truefoundry_sdk/v1/environments/client.py">create_or_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new Environment or updates an existing Environment.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import EnvironmentColor, EnvironmentManifest, TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.environments.create_or_update(
    manifest=EnvironmentManifest(
        name="name",
        color=EnvironmentColor(),
        is_production=True,
        optimize_for="COST",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**manifest:** `EnvironmentManifest` — Environment Manifest
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` — Dry run
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.environments.<a href="src/truefoundry_sdk/v1/environments/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Environment associated with the provided id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.environments.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Environment id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.environments.<a href="src/truefoundry_sdk/v1/environments/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Environment associated with the provided id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.environments.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Environment id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V1 Workspaces
<details><summary><code>client.v1.workspaces.<a href="src/truefoundry_sdk/v1/workspaces/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List workspaces associated with the user. Optional filters include clusterId, fqn, and workspace name. Pagination is available based on query parameters.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
response = client.v1.workspaces.list(
    limit=10,
    offset=0,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of items per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip
    
</dd>
</dl>

<dl>
<dd>

**cluster_id:** `typing.Optional[str]` — ClusterId of the Cluster
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Workspace Name
    
</dd>
</dl>

<dl>
<dd>

**fqn:** `typing.Optional[str]` — Workspace FQN
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.workspaces.<a href="src/truefoundry_sdk/v1/workspaces/client.py">create_or_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new workspace or updates an existing one based on the provided manifest.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry, WorkspaceManifest

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.workspaces.create_or_update(
    manifest=WorkspaceManifest(
        cluster_fqn="cluster_fqn",
        name="name",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**manifest:** `WorkspaceManifest` — Workspace manifest
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` — Dry run the request
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.workspaces.<a href="src/truefoundry_sdk/v1/workspaces/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get workspace associated with provided workspace id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.workspaces.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Workspace id of the space
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.workspaces.<a href="src/truefoundry_sdk/v1/workspaces/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the workspace with the given workspace ID.
    - Removes the associated namespace from the cluster.
    - Deletes the corresponding authorization entry.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.workspaces.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Workspace id of the space
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V1 Artifacts
<details><summary><code>client.v1.artifacts.<a href="src/truefoundry_sdk/v1/artifacts/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.artifacts.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.artifacts.<a href="src/truefoundry_sdk/v1/artifacts/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.artifacts.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.artifacts.<a href="src/truefoundry_sdk/v1/artifacts/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
response = client.v1.artifacts.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ml_repo_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.artifacts.<a href="src/truefoundry_sdk/v1/artifacts/client.py">create_or_update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import ModelManifest, TrueFoundry, TrueFoundryManagedSource

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.artifacts.create_or_update(
    manifest=ModelManifest(
        name="name",
        metadata={"key": "value"},
        ml_repo="ml_repo",
        source=TrueFoundryManagedSource(),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**manifest:** `Manifest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V1 Agents
<details><summary><code>client.v1.agents.<a href="src/truefoundry_sdk/v1/agents/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.agents.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.agents.<a href="src/truefoundry_sdk/v1/agents/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.agents.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.agents.<a href="src/truefoundry_sdk/v1/agents/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
response = client.v1.agents.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ml_repo_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.agents.<a href="src/truefoundry_sdk/v1/agents/client.py">create_or_update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import ModelManifest, TrueFoundry, TrueFoundryManagedSource

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.agents.create_or_update(
    manifest=ModelManifest(
        name="name",
        metadata={"key": "value"},
        ml_repo="ml_repo",
        source=TrueFoundryManagedSource(),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**manifest:** `Manifest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V1 Prompts
<details><summary><code>client.v1.prompts.<a href="src/truefoundry_sdk/v1/prompts/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.prompts.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.prompts.<a href="src/truefoundry_sdk/v1/prompts/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.prompts.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.prompts.<a href="src/truefoundry_sdk/v1/prompts/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
response = client.v1.prompts.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ml_repo_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.prompts.<a href="src/truefoundry_sdk/v1/prompts/client.py">create_or_update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import ModelManifest, TrueFoundry, TrueFoundryManagedSource

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.prompts.create_or_update(
    manifest=ModelManifest(
        name="name",
        metadata={"key": "value"},
        ml_repo="ml_repo",
        source=TrueFoundryManagedSource(),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**manifest:** `Manifest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V1 Tools
<details><summary><code>client.v1.tools.<a href="src/truefoundry_sdk/v1/tools/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.tools.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.tools.<a href="src/truefoundry_sdk/v1/tools/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.tools.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.tools.<a href="src/truefoundry_sdk/v1/tools/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
response = client.v1.tools.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ml_repo_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.tools.<a href="src/truefoundry_sdk/v1/tools/client.py">create_or_update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import ModelManifest, TrueFoundry, TrueFoundryManagedSource

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.tools.create_or_update(
    manifest=ModelManifest(
        name="name",
        metadata={"key": "value"},
        ml_repo="ml_repo",
        source=TrueFoundryManagedSource(),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**manifest:** `Manifest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V1 Models
<details><summary><code>client.v1.models.<a href="src/truefoundry_sdk/v1/models/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.models.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.models.<a href="src/truefoundry_sdk/v1/models/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.models.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.models.<a href="src/truefoundry_sdk/v1/models/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
response = client.v1.models.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ml_repo_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.models.<a href="src/truefoundry_sdk/v1/models/client.py">create_or_update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import ModelManifest, TrueFoundry, TrueFoundryManagedSource

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.models.create_or_update(
    manifest=ModelManifest(
        name="name",
        metadata={"key": "value"},
        ml_repo="ml_repo",
        source=TrueFoundryManagedSource(),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**manifest:** `Manifest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V1 ArtifactVersions
<details><summary><code>client.v1.artifact_versions.<a href="src/truefoundry_sdk/v1/artifact_versions/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get artifact version API
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.artifact_versions.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.artifact_versions.<a href="src/truefoundry_sdk/v1/artifact_versions/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete artifact versions API
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.artifact_versions.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.artifact_versions.<a href="src/truefoundry_sdk/v1/artifact_versions/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List artifact version API
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
response = client.v1.artifact_versions.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**artifact_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**fqn:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**run_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**run_steps:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` 
    
</dd>
</dl>

<dl>
<dd>

**include_internal_metadata:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.artifact_versions.<a href="src/truefoundry_sdk/v1/artifact_versions/client.py">get_signed_urls</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.artifact_versions.get_signed_urls(
    id="id",
    paths=["paths"],
    operation="READ",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**paths:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**operation:** `Operation` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.artifact_versions.<a href="src/truefoundry_sdk/v1/artifact_versions/client.py">create_multi_part_upload</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.artifact_versions.create_multi_part_upload(
    id="id",
    path="path",
    num_parts=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**num_parts:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.artifact_versions.<a href="src/truefoundry_sdk/v1/artifact_versions/client.py">stage</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import ModelManifest, TrueFoundry, TrueFoundryManagedSource

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.artifact_versions.stage(
    manifest=ModelManifest(
        name="name",
        metadata={"key": "value"},
        ml_repo="ml_repo",
        source=TrueFoundryManagedSource(),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**manifest:** `Manifest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.artifact_versions.<a href="src/truefoundry_sdk/v1/artifact_versions/client.py">list_files</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
response = client.v1.artifact_versions.list_files(
    id="id",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**path:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V1 ModelVersions
<details><summary><code>client.v1.model_versions.<a href="src/truefoundry_sdk/v1/model_versions/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get model version API
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.model_versions.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.model_versions.<a href="src/truefoundry_sdk/v1/model_versions/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete model versions API
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.model_versions.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.model_versions.<a href="src/truefoundry_sdk/v1/model_versions/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List model version API
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
response = client.v1.model_versions.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**model_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**fqn:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**run_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**run_steps:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` 
    
</dd>
</dl>

<dl>
<dd>

**include_internal_metadata:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V1 PromptVersions
<details><summary><code>client.v1.prompt_versions.<a href="src/truefoundry_sdk/v1/prompt_versions/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get prompt version API
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.prompt_versions.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.prompt_versions.<a href="src/truefoundry_sdk/v1/prompt_versions/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete prompt versions API
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.prompt_versions.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.prompt_versions.<a href="src/truefoundry_sdk/v1/prompt_versions/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List prompt version API
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
response = client.v1.prompt_versions.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prompt_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**fqn:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V1 ToolVersions
<details><summary><code>client.v1.tool_versions.<a href="src/truefoundry_sdk/v1/tool_versions/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get tool version API
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.tool_versions.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.tool_versions.<a href="src/truefoundry_sdk/v1/tool_versions/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete tool versions API
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.tool_versions.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.tool_versions.<a href="src/truefoundry_sdk/v1/tool_versions/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List tool versions API
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
response = client.v1.tool_versions.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tool_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**fqn:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V1 AgentVersions
<details><summary><code>client.v1.agent_versions.<a href="src/truefoundry_sdk/v1/agent_versions/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get agent version API
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.agent_versions.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.agent_versions.<a href="src/truefoundry_sdk/v1/agent_versions/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete agent versions API
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.agent_versions.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.agent_versions.<a href="src/truefoundry_sdk/v1/agent_versions/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List agent versions API
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
response = client.v1.agent_versions.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**fqn:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.agent_versions.<a href="src/truefoundry_sdk/v1/agent_versions/client.py">resolve</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.agent_versions.resolve(
    fqn="fqn",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fqn:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V1 DataDirectories
<details><summary><code>client.v1.data_directories.<a href="src/truefoundry_sdk/v1/data_directories/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a data directory by its ID.

Args:
    id (str): The ID of the data directory to retrieve
    user_info: Current authenticated user info

Returns:
    DataDirectoryResponse: Response containing the retrieved data directory
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.data_directories.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.data_directories.<a href="src/truefoundry_sdk/v1/data_directories/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a data directory and optionally its contents.

Args:
    id: Unique identifier of the data directory to delete
    delete_contents: If True, also deletes the data directory's contents
    user_info: Authenticated user information

Returns:
    EmptyResponse: Empty response indicating successful deletion
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.data_directories.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**delete_contents:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.data_directories.<a href="src/truefoundry_sdk/v1/data_directories/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all data directories with optional filtering and pagination.

Args:
    filters: Query parameters for filtering and pagination
        - ml_repo_id: Filter data directories by ml repo ID
        - name: Optional filter data directories by name
        - limit: Optional maximum number of data directories to return
        - offset: Optional number of data directories to skip
    user_info: Authenticated user information

Returns:
    ListDataDirectoriesResponse: List of data directories and pagination info
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
response = client.v1.data_directories.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ml_repo_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.data_directories.<a href="src/truefoundry_sdk/v1/data_directories/client.py">create_or_update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import ModelManifest, TrueFoundry, TrueFoundryManagedSource

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.data_directories.create_or_update(
    manifest=ModelManifest(
        name="name",
        metadata={"key": "value"},
        ml_repo="ml_repo",
        source=TrueFoundryManagedSource(),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**manifest:** `Manifest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.data_directories.<a href="src/truefoundry_sdk/v1/data_directories/client.py">get_signed_urls</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get signed URLs for a dataset.

Args:
    request_dto: Request containing dataset ID, paths and operation
    user_info: Authenticated user information

Returns:
    GetSignedURLsResponse: Response containing signed URLs
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.data_directories.get_signed_urls(
    id="id",
    paths=["paths"],
    operation="READ",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**paths:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**operation:** `Operation` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.data_directories.<a href="src/truefoundry_sdk/v1/data_directories/client.py">list_files</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List files in a dataset.

Args:
    request_dto: Request containing dataset ID, path, page token and limit
    user_info: Authenticated user information

Returns:
    ListFilesResponse: Response containing files and pagination info
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
response = client.v1.data_directories.list_files(
    id="id",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**path:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.data_directories.<a href="src/truefoundry_sdk/v1/data_directories/client.py">delete_files</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete files from the dataset.

Args:
    request_dto: Request containing dataset ID and paths
    user_info: Authenticated user information

Returns:
    EmptyResponse: Empty response indicating successful deletion
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.data_directories.delete_files(
    id="id",
    paths=["paths"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**paths:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.data_directories.<a href="src/truefoundry_sdk/v1/data_directories/client.py">create_multipart_upload</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a multipart upload for a dataset

Args:
    request_dto: Request containing dataset ID, path and number of parts
    user_info: Authenticated user information

Returns:
    MultiPartUploadResponse: Response containing multipart upload info
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.data_directories.create_multipart_upload(
    id="id",
    path="path",
    num_parts=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**num_parts:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V1 MlRepos
<details><summary><code>client.v1.ml_repos.<a href="src/truefoundry_sdk/v1/ml_repos/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a ml repo by id
Args:
    id: Unique identifier of the ml repo to get
    user_info: Authenticated user information

Returns:
    GetMLRepoResponse: The ml repo
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.ml_repos.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.ml_repos.<a href="src/truefoundry_sdk/v1/ml_repos/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a ml repo
Args:
    id: Unique identifier of the ml repo to delete
    user_info: Authenticated user information

Returns:
    EmptyResponse: Empty response indicating successful deletion
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.ml_repos.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1.ml_repos.<a href="src/truefoundry_sdk/v1/ml_repos/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List ml repos
Args:
    filters: Filters for the ml repos
    user_info: Authenticated user information

Returns:
    ListMLReposResponse: List of ml repos
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
response = client.v1.ml_repos.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V1 Internal ArtifactVersions
<details><summary><code>client.v1.internal.artifact_versions.<a href="src/truefoundry_sdk/v1/internal/artifact_versions/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List artifact version API
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
response = client.v1.internal.artifact_versions.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**artifact_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**fqn:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**run_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**run_steps:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` 
    
</dd>
</dl>

<dl>
<dd>

**include_internal_metadata:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**include_model_versions:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

