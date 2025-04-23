# Reference
## V1 Secrets
<details><summary><code>client.v1.secrets.<a href="src/truefoundry_sdk/v1/secrets/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List secrets associated with a user filtered with optional parameters passed in the body.
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
response = client.v1.secrets.list()
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

**secret_id:** `typing.Optional[str]` — Secret Id of the secret.
    
</dd>
</dl>

<dl>
<dd>

**secret_fqns:** `typing.Optional[typing.Sequence[str]]` — Array of FQNs
    
</dd>
</dl>

<dl>
<dd>

**secret_group_id:** `typing.Optional[str]` — Secret Group Id of the secret gourp.
    
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

<details><summary><code>client.v1.secrets.<a href="src/truefoundry_sdk/v1/secrets/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Secret associated with provided id
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
client.v1.secrets.get(
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

**id:** `str` — Secret Id of the secret.
    
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

<details><summary><code>client.v1.secrets.<a href="src/truefoundry_sdk/v1/secrets/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a secret and its versions along with its values.
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
client.v1.secrets.delete(
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

**id:** `str` — Secret Id of the secret.
    
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

## V1 SecretGroups
<details><summary><code>client.v1.secret_groups.<a href="src/truefoundry_sdk/v1/secret_groups/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the secret groups associated with a user along with the associated secrets for each group. Filtered with the options passed in the query fields.
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
response = client.v1.secret_groups.list(
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

**secret_group_id:** `typing.Optional[str]` — Secret Group Id of secret group.
    
</dd>
</dl>

<dl>
<dd>

**secret_group_fqn:** `typing.Optional[str]` — Fqn of secret group.
    
</dd>
</dl>

<dl>
<dd>

**secret_attributes:** `typing.Optional[str]` — Attributes to return for secret object provided as comma separated values (`secretAttributes=id,fqn`)
    
</dd>
</dl>

<dl>
<dd>

**secret_group_attributes:** `typing.Optional[str]` — Attributes returned for secret group object provided as comma separated values (`secretGroupAttributes=id,fqn`)
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Search query - filters by secret group names that contain the search string
    
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

<details><summary><code>client.v1.secret_groups.<a href="src/truefoundry_sdk/v1/secret_groups/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a secret group with secrets in it. A secret version for each of the created secret is created with version number as 1. The returned secret group does not have any secrets in the <em>associatedSecrets</em> field. A separate API call should be made to fetch the associated secrets.
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
from truefoundry_sdk import SecretInput, TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.secret_groups.create(
    name="name",
    integration_id="integrationId",
    secrets=[
        SecretInput(
            key="key",
            value="value",
        )
    ],
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

**name:** `str` — Name of the secret group.
    
</dd>
</dl>

<dl>
<dd>

**integration_id:** `str` — Id of the provider integration.
    
</dd>
</dl>

<dl>
<dd>

**secrets:** `typing.Sequence[SecretInput]` — The secrets to be associated with the secret group
    
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

<details><summary><code>client.v1.secret_groups.<a href="src/truefoundry_sdk/v1/secret_groups/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Secret Group associated with provided secretGroup id
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
client.v1.secret_groups.get(
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

**id:** `str` — Secret Id of the secret group.
    
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

<details><summary><code>client.v1.secret_groups.<a href="src/truefoundry_sdk/v1/secret_groups/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the secrets in a secret group with new values. A new secret version is created for every secret that has a modified value. Returns the updated secret group. The returned secret group does not have any secrets in the <em>associatedSecrets</em> field. A separate API call should be made to fetch the associated secrets.
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
from truefoundry_sdk import TrueFoundry, UpdateSecretDto

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.secret_groups.update(
    id="id",
    secrets=[
        UpdateSecretDto(
            key="key",
            value="value",
        )
    ],
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

**id:** `str` — Secret Id of the secret group.
    
</dd>
</dl>

<dl>
<dd>

**secrets:** `typing.Sequence[UpdateSecretDto]` 
    
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

<details><summary><code>client.v1.secret_groups.<a href="src/truefoundry_sdk/v1/secret_groups/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the secret group, its associated secrets and secret versions of those secrets.
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
client.v1.secret_groups.delete(
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

**id:** `str` — Secret Id of the secret group.
    
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

<details><summary><code>client.v1.secret_groups.<a href="src/truefoundry_sdk/v1/secret_groups/client.py">list_secrets</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Secrets associated with a Secret Group.
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
client.v1.secret_groups.list_secrets(
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

**id:** `str` — Secret Id of the secret group.
    
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
response = client.v1.clusters.list(
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
from truefoundry_sdk import (
    ClusterManifest,
    ClusterManifestClusterType,
    Collaborator,
    TrueFoundry,
)

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.clusters.create_or_update(
    manifest=ClusterManifest(
        name="name",
        cluster_type=ClusterManifestClusterType.AWS_EKS,
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

<details><summary><code>client.v1.clusters.<a href="src/truefoundry_sdk/v1/clusters/client.py">get_addons</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List addons for the provided cluster.Pagination is available based on query parameters.
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
client.v1.clusters.get_addons(
    id="id",
    limit=10,
    offset=0,
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

<details><summary><code>client.v1.clusters.<a href="src/truefoundry_sdk/v1/clusters/client.py">is_connected</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the status of provided cluster
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
client.v1.clusters.is_connected(
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
from truefoundry_sdk import (
    EnvironmentColor,
    EnvironmentManifest,
    EnvironmentOptimizeFor,
    TrueFoundry,
)

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.environments.create_or_update(
    manifest=EnvironmentManifest(
        name="name",
        color=EnvironmentColor(),
        is_production=True,
        optimize_for=EnvironmentOptimizeFor.COST,
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

## V1 Applications
<details><summary><code>client.v1.applications.<a href="src/truefoundry_sdk/v1/applications/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a list of all latest applications. Supports filtering by application ID, name, type, and other parameters. Pagination is available based on query parameters.
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
response = client.v1.applications.list(
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

**application_id:** `typing.Optional[str]` — Application id of the application
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `typing.Optional[str]` — Workspace id of the application (comma separated for multiple)
    
</dd>
</dl>

<dl>
<dd>

**application_name:** `typing.Optional[str]` — Name of application
    
</dd>
</dl>

<dl>
<dd>

**application_type:** `typing.Optional[str]` — Type of application (comma separated for multiple). Allowed Values: async-service, service, job, spark-job, helm, notebook, codeserver, rstudio, ssh-server, volume, application, application-set, intercept, workflow
    
</dd>
</dl>

<dl>
<dd>

**name_search_query:** `typing.Optional[str]` — Search query for application name
    
</dd>
</dl>

<dl>
<dd>

**environment_id:** `typing.Optional[str]` — Filter by Environment ids of the application (comma separated for multiple)
    
</dd>
</dl>

<dl>
<dd>

**cluster_id:** `typing.Optional[str]` — Filter by Cluster ids of the application (comma separated for multiple)
    
</dd>
</dl>

<dl>
<dd>

**application_set_id:** `typing.Optional[str]` — Filter by Application Set id of the application
    
</dd>
</dl>

<dl>
<dd>

**paused:** `typing.Optional[bool]` — Filter by Application Paused status
    
</dd>
</dl>

<dl>
<dd>

**device_type_filter:** `typing.Optional[ApplicationsListRequestDeviceTypeFilter]` — Filter by device type of the application. Allowed values: cpu, nvidia_gpu, aws_inferentia, nvidia_mig_gpu, nvidia_timeslicing_gpu, gcp_tpu
    
</dd>
</dl>

<dl>
<dd>

**last_deployed_by_subjects:** `typing.Optional[str]` — Filter by last deployed by specific users
    
</dd>
</dl>

<dl>
<dd>

**lifecycle_stage:** `typing.Optional[ApplicationsListRequestLifecycleStage]` — Filter by application lifecycle state
    
</dd>
</dl>

<dl>
<dd>

**is_recommendation_present:** `typing.Optional[bool]` — Filter out applications with recommendations
    
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

<details><summary><code>client.v1.applications.<a href="src/truefoundry_sdk/v1/applications/client.py">create_or_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new Application Deployment based on the provided manifest.
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
client.v1.applications.create_or_update(
    manifest={"key": "value"},
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

**manifest:** `typing.Dict[str, typing.Optional[typing.Any]]` — Manifest of application
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` — Dry run
    
</dd>
</dl>

<dl>
<dd>

**force_deploy:** `typing.Optional[bool]` — Cancels any ongoing deployments
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `typing.Optional[str]` — workspace id of the workspace
    
</dd>
</dl>

<dl>
<dd>

**application_id:** `typing.Optional[str]` — Id of the application
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of application
    
</dd>
</dl>

<dl>
<dd>

**application_set_id:** `typing.Optional[str]` — Application Set Id
    
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

<details><summary><code>client.v1.applications.<a href="src/truefoundry_sdk/v1/applications/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Application associated with the provided application ID.
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
client.v1.applications.get(
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

**id:** `str` — Id of the application
    
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

<details><summary><code>client.v1.applications.<a href="src/truefoundry_sdk/v1/applications/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Application associated with the provided application ID.
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
client.v1.applications.delete(
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

**id:** `str` — Id of the application
    
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

<details><summary><code>client.v1.applications.<a href="src/truefoundry_sdk/v1/applications/client.py">scale_to_zero</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Pause a running application by scaling to 0 replicas
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
client.v1.applications.scale_to_zero(
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

**id:** `str` — Id of the application
    
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

<details><summary><code>client.v1.applications.<a href="src/truefoundry_sdk/v1/applications/client.py">scale_to_original</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resume a paused application by scaling back to the original number of replicas
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
client.v1.applications.scale_to_original(
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

**id:** `str` — Id of the application
    
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

<details><summary><code>client.v1.applications.<a href="src/truefoundry_sdk/v1/applications/client.py">cancel_deployment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel an ongoing deployment associated with the provided application ID and deployment ID.
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
client.v1.applications.cancel_deployment(
    id="id",
    deployment_id="deploymentId",
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

**id:** `str` — Application id of the application
    
</dd>
</dl>

<dl>
<dd>

**deployment_id:** `str` — Deployment id of the deployment
    
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

## V1 ApplicationVersions
<details><summary><code>client.v1.application_versions.<a href="src/truefoundry_sdk/v1/application_versions/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch all deployments for a given application ID with optional filters such as deployment ID or version. Supports pagination.
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
response = client.v1.application_versions.list(
    id="id",
    limit=10,
    offset=0,
    version="1",
    deployment_id="deployment123",
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

**id:** `str` — Id of the application
    
</dd>
</dl>

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

**version:** `typing.Optional[str]` — Deployment version. Filter deployments by version.
    
</dd>
</dl>

<dl>
<dd>

**deployment_id:** `typing.Optional[str]` — Deployment ID. Filter deployments by a specific ID.
    
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

<details><summary><code>client.v1.application_versions.<a href="src/truefoundry_sdk/v1/application_versions/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Deployment associated with the provided application ID and deployment ID.
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
client.v1.application_versions.get(
    id="id",
    deployment_id="deploymentId",
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

**id:** `str` — Application id of the application
    
</dd>
</dl>

<dl>
<dd>

**deployment_id:** `str` — Deployment id of the deployment
    
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

## V1 Jobs
<details><summary><code>client.v1.jobs.<a href="src/truefoundry_sdk/v1/jobs/client.py">list_runs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Job Runs for provided Job Id. Filter the data based on parameters passed in the query
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
response = client.v1.jobs.list_runs(
    job_id="jobId",
    limit=1,
    offset=1,
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

**job_id:** `str` — Job id of the application
    
</dd>
</dl>

<dl>
<dd>

**limit:** `int` — Number of items per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `int` — Number of items to skip
    
</dd>
</dl>

<dl>
<dd>

**search_prefix:** `typing.Optional[str]` — Prefix used to search for job runs by name or identifier
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[JobRunsSortBy]` — Attribute to sort by
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[JobRunsSortDirection]` — Sorting order
    
</dd>
</dl>

<dl>
<dd>

**triggered_by:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Array of subject slugs
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[JobRunStatus, typing.Sequence[JobRunStatus]]]` — Status of the job run
    
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

<details><summary><code>client.v1.jobs.<a href="src/truefoundry_sdk/v1/jobs/client.py">get_run</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Job Run for provided jobRunName and jobId
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
client.v1.jobs.get_run(
    job_id="jobId",
    job_run_name="jobRunName",
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

**job_id:** `str` — Application Id of JOB
    
</dd>
</dl>

<dl>
<dd>

**job_run_name:** `str` — Job run name of the application
    
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

<details><summary><code>client.v1.jobs.<a href="src/truefoundry_sdk/v1/jobs/client.py">delete_run</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Job Run for provided jobRunName and jobId
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
client.v1.jobs.delete_run(
    job_id="jobId",
    job_run_name="jobRunName",
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

**job_id:** `str` — Application Id of JOB
    
</dd>
</dl>

<dl>
<dd>

**job_run_name:** `str` — Job run name of the application
    
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

<details><summary><code>client.v1.jobs.<a href="src/truefoundry_sdk/v1/jobs/client.py">trigger</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Trigger Job for provided deploymentId or applicationId
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
client.v1.jobs.trigger()

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

**deployment_id:** `typing.Optional[str]` — Deployment Id of the job
    
</dd>
</dl>

<dl>
<dd>

**application_id:** `typing.Optional[str]` — Application Id of the job
    
</dd>
</dl>

<dl>
<dd>

**input:** `typing.Optional[JobTriggerInput]` — Job trigger input
    
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

<details><summary><code>client.v1.jobs.<a href="src/truefoundry_sdk/v1/jobs/client.py">terminate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Terminate Job for provided deploymentId and jobRunName
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
client.v1.jobs.terminate(
    deployment_id="deploymentId",
    job_run_name="jobRunName",
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

**deployment_id:** `str` — Deployment Id of the Deployment
    
</dd>
</dl>

<dl>
<dd>

**job_run_name:** `str` — Job Run name
    
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

## V1 Events
<details><summary><code>client.v1.events.<a href="src/truefoundry_sdk/v1/events/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Events for Pod, Job Run, Application. The events are sourced from Kubernetes as well as events captured by truefoundry. Optional query parameters include startTs, endTs for filtering.
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
client.v1.events.get()

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

**start_ts:** `typing.Optional[str]` — Start timestamp (ISO format) for querying events
    
</dd>
</dl>

<dl>
<dd>

**end_ts:** `typing.Optional[str]` — End timestamp (ISO format) for querying events
    
</dd>
</dl>

<dl>
<dd>

**application_id:** `typing.Optional[str]` — Application ID
    
</dd>
</dl>

<dl>
<dd>

**application_fqn:** `typing.Optional[str]` — Application FQN
    
</dd>
</dl>

<dl>
<dd>

**pod_names:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Name of the pods
    
</dd>
</dl>

<dl>
<dd>

**job_run_name:** `typing.Optional[str]` — Job run name
    
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

## V1 Alerts
<details><summary><code>client.v1.alerts.<a href="src/truefoundry_sdk/v1/alerts/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get alerts for a given application or cluster filtered by start and end timestamp
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
client.v1.alerts.list()

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

**start_ts:** `typing.Optional[str]` — Start timestamp (ISO format) for querying events
    
</dd>
</dl>

<dl>
<dd>

**end_ts:** `typing.Optional[str]` — End timestamp (ISO format) for querying events
    
</dd>
</dl>

<dl>
<dd>

**cluster_id:** `typing.Optional[str]` — Cluster id
    
</dd>
</dl>

<dl>
<dd>

**application_id:** `typing.Optional[str]` — Application id
    
</dd>
</dl>

<dl>
<dd>

**alert_status:** `typing.Optional[AlertStatus]` — Alert status
    
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

## V1 Logs
<details><summary><code>client.v1.logs.<a href="src/truefoundry_sdk/v1/logs/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch logs for various workload components, including Services, Jobs, Workflows, Job Runs, and Pods. Logs are filtered based on the provided query parameters.
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
client.v1.logs.get()

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

**start_ts:** `typing.Optional[int]` — Start timestamp for querying logs, in nanoseconds from the Unix epoch.
    
</dd>
</dl>

<dl>
<dd>

**end_ts:** `typing.Optional[int]` — End timestamp for querying logs, in nanoseconds from the Unix epoch.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max number of log lines to fetch
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[LogsSortingDirection]` — Direction of sorting logs. Can be `asc` or `desc`
    
</dd>
</dl>

<dl>
<dd>

**num_logs_to_ignore:** `typing.Optional[int]` — Number of logs corresponding to the starting timestamp to be ignored.
    
</dd>
</dl>

<dl>
<dd>

**application_id:** `typing.Optional[str]` — Application ID
    
</dd>
</dl>

<dl>
<dd>

**application_fqn:** `typing.Optional[str]` — Application FQN
    
</dd>
</dl>

<dl>
<dd>

**deployment_id:** `typing.Optional[str]` — Deployment ID
    
</dd>
</dl>

<dl>
<dd>

**job_run_name:** `typing.Optional[str]` — Name of the Job Run for which to fetch logs.
    
</dd>
</dl>

<dl>
<dd>

**pod_name:** `typing.Optional[str]` — Name of Pod for which to fetch logs.
    
</dd>
</dl>

<dl>
<dd>

**container_name:** `typing.Optional[str]` — Name of the Container for which to fetch logs.
    
</dd>
</dl>

<dl>
<dd>

**pod_names:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — List of pod names for which to fetch logs.
    
</dd>
</dl>

<dl>
<dd>

**pod_names_regex:** `typing.Optional[str]` — Regex pattern for pod names to fetch logs.
    
</dd>
</dl>

<dl>
<dd>

**search_string:** `typing.Optional[str]` — String that needs to be matched
    
</dd>
</dl>

<dl>
<dd>

**search_type:** `typing.Optional[LogsSearchFilterType]` — Query filter type, `regex` or `substring`
    
</dd>
</dl>

<dl>
<dd>

**search_operator:** `typing.Optional[LogsSearchOperatorType]` — Comparison operator for filter. `equal` or `not_equal`
    
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
<details><summary><code>client.v1.ml_repos.<a href="src/truefoundry_sdk/v1/ml_repos/client.py">create_or_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates or updates an MLRepo entity based on the provided manifest.
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
client.v1.ml_repos.create_or_update(
    manifest={"key": "value"},
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

**manifest:** `typing.Dict[str, typing.Optional[typing.Any]]` — MLRepo manifest
    
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
from truefoundry_sdk import Operation, TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.artifact_versions.get_signed_urls(
    id="id",
    paths=["paths"],
    operation=Operation.READ,
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

<details><summary><code>client.v1.artifact_versions.<a href="src/truefoundry_sdk/v1/artifact_versions/client.py">mark_stage_failure</a>(...)</code></summary>
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
client.v1.artifact_versions.mark_stage_failure(
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
from truefoundry_sdk import Operation, TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.data_directories.get_signed_urls(
    id="id",
    paths=["paths"],
    operation=Operation.READ,
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

## V1 TracingProjects
<details><summary><code>client.v1.tracing_projects.<a href="src/truefoundry_sdk/v1/tracing_projects/client.py">list</a>(...)</code></summary>
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
response = client.v1.tracing_projects.list()
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

**ml_repo_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**fqn:** `typing.Optional[str]` 
    
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

<details><summary><code>client.v1.tracing_projects.<a href="src/truefoundry_sdk/v1/tracing_projects/client.py">create_or_update</a>(...)</code></summary>
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
client.v1.tracing_projects.create_or_update(
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

<details><summary><code>client.v1.tracing_projects.<a href="src/truefoundry_sdk/v1/tracing_projects/client.py">get</a>(...)</code></summary>
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
client.v1.tracing_projects.get(
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

<details><summary><code>client.v1.tracing_projects.<a href="src/truefoundry_sdk/v1/tracing_projects/client.py">delete</a>(...)</code></summary>
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
client.v1.tracing_projects.delete(
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

## V1 Internal Users
<details><summary><code>client.v1.internal.users.<a href="src/truefoundry_sdk/v1/internal/users/client.py">get_info</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the user session details for the currently authenticated user
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
client.v1.internal.users.get_info()

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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V1 Internal Clusters
<details><summary><code>client.v1.internal.clusters.<a href="src/truefoundry_sdk/v1/internal/clusters/client.py">get_autoprovisioning_state</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the auto provisioning status for the provided cluster
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
client.v1.internal.clusters.get_autoprovisioning_state(
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

## V1 Internal Deployments
<details><summary><code>client.v1.internal.deployments.<a href="src/truefoundry_sdk/v1/internal/deployments/client.py">get_builds</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint returns all build details associated with a specific deployment in a given application.
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
client.v1.internal.deployments.get_builds(
    id="id",
    deployment_id="deploymentId",
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

**id:** `str` — Application id of the application
    
</dd>
</dl>

<dl>
<dd>

**deployment_id:** `str` — Deployment id of the deployment
    
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

<details><summary><code>client.v1.internal.deployments.<a href="src/truefoundry_sdk/v1/internal/deployments/client.py">get_code_upload_url</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate presigned URL to upload code for given serviceName and workspaceFqn
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
client.v1.internal.deployments.get_code_upload_url(
    service_name="serviceName",
    workspace_fqn="workspaceFqn",
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

**service_name:** `str` — ServiceName of the deployment
    
</dd>
</dl>

<dl>
<dd>

**workspace_fqn:** `str` — WorkSpaceFQN of the workspace
    
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

<details><summary><code>client.v1.internal.deployments.<a href="src/truefoundry_sdk/v1/internal/deployments/client.py">get_suggested_endpoint</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate deployment endpoint based on the provided query parameters.
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
from truefoundry_sdk import ApplicationType, TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.internal.deployments.get_suggested_endpoint(
    application_type=ApplicationType.ASYNC_SERVICE,
    application_name="applicationName",
    workspace_id="workspaceId",
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

**application_type:** `ApplicationType` — Application Type
    
</dd>
</dl>

<dl>
<dd>

**application_name:** `str` — Application name
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `str` — Workspace id
    
</dd>
</dl>

<dl>
<dd>

**base_domain:** `typing.Optional[str]` — Base domain
    
</dd>
</dl>

<dl>
<dd>

**port:** `typing.Optional[str]` — Port
    
</dd>
</dl>

<dl>
<dd>

**prefer_wildcard:** `typing.Optional[bool]` — Prefer wildcard
    
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

## V1 Internal Applications
<details><summary><code>client.v1.internal.applications.<a href="src/truefoundry_sdk/v1/internal/applications/client.py">get_pod_template_hash_to_deployment_version</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint fetches the pod template hash to deployment version map for a specific application.
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
client.v1.internal.applications.get_pod_template_hash_to_deployment_version(
    id="id",
    pod_template_hashes="podTemplateHashes",
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

**id:** `str` — Id of the application
    
</dd>
</dl>

<dl>
<dd>

**pod_template_hashes:** `str` — Pod Template Hashes (comma separated for multiple)
    
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

## V1 Internal Vcs
<details><summary><code>client.v1.internal.vcs.<a href="src/truefoundry_sdk/v1/internal/vcs/client.py">get_repository_details</a>(...)</code></summary>
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
client.v1.internal.vcs.get_repository_details(
    repo_url="repoURL",
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

**repo_url:** `str` — The URL of the repository
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — The integration id of the repository
    
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

<details><summary><code>client.v1.internal.vcs.<a href="src/truefoundry_sdk/v1/internal/vcs/client.py">get_authenticated_url</a>(...)</code></summary>
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
client.v1.internal.vcs.get_authenticated_url(
    repo_url="repoURL",
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

**repo_url:** `str` — Repository URL (e.g., https://github.com/user/repo, https://bitbucket.org/user/repo)
    
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

## V1 Internal Metrics
<details><summary><code>client.v1.internal.metrics.<a href="src/truefoundry_sdk/v1/internal/metrics/client.py">get_charts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List charts for a given Application based on parameters passed in the query.
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
from truefoundry_sdk.v1.internal.metrics import (
    MetricsGetChartsRequestFilterEntity,
)

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.internal.metrics.get_charts(
    workspace_id="workspaceId",
    application_id="applicationId",
    filter_entity=MetricsGetChartsRequestFilterEntity.APPLICATION,
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

**workspace_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**application_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter_entity:** `MetricsGetChartsRequestFilterEntity` 
    
</dd>
</dl>

<dl>
<dd>

**start_ts:** `typing.Optional[str]` — Start Timestamp
    
</dd>
</dl>

<dl>
<dd>

**end_ts:** `typing.Optional[str]` — End Timestamp
    
</dd>
</dl>

<dl>
<dd>

**filter_query:** `typing.Optional[str]` — Query params to filter metrics
    
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

