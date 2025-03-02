# Reference
## V1
<details><summary><code>client.v1.<a href="src/truefoundry/v1/client.py">apply</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry import (
    ModelVersionManifest,
    TrueFoundry,
    TrueFoundryManagedSource,
)

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.apply(
    manifest=ModelVersionManifest(
        metadata={"key": "value"},
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

## Health
<details><summary><code>client.health.<a href="src/truefoundry/health/client.py">serve_get</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.health.serve_get()

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

<details><summary><code>client.health.<a href="src/truefoundry/health/client.py">get</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.health.get()

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

## V1 Artifacts
<details><summary><code>client.v1.artifacts.<a href="src/truefoundry/v1/artifacts/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.artifacts.<a href="src/truefoundry/v1/artifacts/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.artifacts.<a href="src/truefoundry/v1/artifacts/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.artifacts.<a href="src/truefoundry/v1/artifacts/client.py">create_or_update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry import (
    ModelVersionManifest,
    TrueFoundry,
    TrueFoundryManagedSource,
)

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.artifacts.create_or_update(
    manifest=ModelVersionManifest(
        metadata={"key": "value"},
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
<details><summary><code>client.v1.agents.<a href="src/truefoundry/v1/agents/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.agents.<a href="src/truefoundry/v1/agents/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.agents.<a href="src/truefoundry/v1/agents/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.agents.<a href="src/truefoundry/v1/agents/client.py">create_or_update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry import (
    ModelVersionManifest,
    TrueFoundry,
    TrueFoundryManagedSource,
)

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.agents.create_or_update(
    manifest=ModelVersionManifest(
        metadata={"key": "value"},
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
<details><summary><code>client.v1.prompts.<a href="src/truefoundry/v1/prompts/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.prompts.<a href="src/truefoundry/v1/prompts/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.prompts.<a href="src/truefoundry/v1/prompts/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.prompts.<a href="src/truefoundry/v1/prompts/client.py">create_or_update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry import (
    ModelVersionManifest,
    TrueFoundry,
    TrueFoundryManagedSource,
)

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.prompts.create_or_update(
    manifest=ModelVersionManifest(
        metadata={"key": "value"},
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
<details><summary><code>client.v1.tools.<a href="src/truefoundry/v1/tools/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.tools.<a href="src/truefoundry/v1/tools/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.tools.<a href="src/truefoundry/v1/tools/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.tools.<a href="src/truefoundry/v1/tools/client.py">create_or_update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry import (
    ModelVersionManifest,
    TrueFoundry,
    TrueFoundryManagedSource,
)

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.tools.create_or_update(
    manifest=ModelVersionManifest(
        metadata={"key": "value"},
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
<details><summary><code>client.v1.models.<a href="src/truefoundry/v1/models/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.models.<a href="src/truefoundry/v1/models/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.models.<a href="src/truefoundry/v1/models/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.models.<a href="src/truefoundry/v1/models/client.py">create_or_update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry import (
    ModelVersionManifest,
    TrueFoundry,
    TrueFoundryManagedSource,
)

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.models.create_or_update(
    manifest=ModelVersionManifest(
        metadata={"key": "value"},
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
<details><summary><code>client.v1.artifact_versions.<a href="src/truefoundry/v1/artifact_versions/client.py">get</a>(...)</code></summary>
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
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.artifact_versions.<a href="src/truefoundry/v1/artifact_versions/client.py">delete</a>(...)</code></summary>
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
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.artifact_versions.<a href="src/truefoundry/v1/artifact_versions/client.py">list</a>(...)</code></summary>
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
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.artifact_versions.<a href="src/truefoundry/v1/artifact_versions/client.py">get_signed_urls</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.artifact_versions.<a href="src/truefoundry/v1/artifact_versions/client.py">create_multi_part_upload</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.artifact_versions.<a href="src/truefoundry/v1/artifact_versions/client.py">stage</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry import (
    ModelVersionManifest,
    TrueFoundry,
    TrueFoundryManagedSource,
)

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.artifact_versions.stage(
    manifest=ModelVersionManifest(
        metadata={"key": "value"},
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

<details><summary><code>client.v1.artifact_versions.<a href="src/truefoundry/v1/artifact_versions/client.py">list_files</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry import TrueFoundry

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
<details><summary><code>client.v1.model_versions.<a href="src/truefoundry/v1/model_versions/client.py">get</a>(...)</code></summary>
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
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.model_versions.<a href="src/truefoundry/v1/model_versions/client.py">delete</a>(...)</code></summary>
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
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.model_versions.<a href="src/truefoundry/v1/model_versions/client.py">list</a>(...)</code></summary>
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
from truefoundry import TrueFoundry

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

## V1 PromptVersions
<details><summary><code>client.v1.prompt_versions.<a href="src/truefoundry/v1/prompt_versions/client.py">get</a>(...)</code></summary>
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
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.prompt_versions.<a href="src/truefoundry/v1/prompt_versions/client.py">delete</a>(...)</code></summary>
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
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.prompt_versions.<a href="src/truefoundry/v1/prompt_versions/client.py">list</a>(...)</code></summary>
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
from truefoundry import TrueFoundry

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
<details><summary><code>client.v1.tool_versions.<a href="src/truefoundry/v1/tool_versions/client.py">get</a>(...)</code></summary>
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
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.tool_versions.<a href="src/truefoundry/v1/tool_versions/client.py">delete</a>(...)</code></summary>
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
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.tool_versions.<a href="src/truefoundry/v1/tool_versions/client.py">list</a>(...)</code></summary>
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
from truefoundry import TrueFoundry

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
<details><summary><code>client.v1.agent_versions.<a href="src/truefoundry/v1/agent_versions/client.py">get</a>(...)</code></summary>
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
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.agent_versions.<a href="src/truefoundry/v1/agent_versions/client.py">delete</a>(...)</code></summary>
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
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.agent_versions.<a href="src/truefoundry/v1/agent_versions/client.py">list</a>(...)</code></summary>
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
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.agent_versions.<a href="src/truefoundry/v1/agent_versions/client.py">resolve</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry import TrueFoundry

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
<details><summary><code>client.v1.data_directories.<a href="src/truefoundry/v1/data_directories/client.py">get</a>(...)</code></summary>
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
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.data_directories.<a href="src/truefoundry/v1/data_directories/client.py">delete</a>(...)</code></summary>
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
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.data_directories.<a href="src/truefoundry/v1/data_directories/client.py">list</a>(...)</code></summary>
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
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.data_directories.<a href="src/truefoundry/v1/data_directories/client.py">create_or_update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry import (
    ModelVersionManifest,
    TrueFoundry,
    TrueFoundryManagedSource,
)

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.v1.data_directories.create_or_update(
    manifest=ModelVersionManifest(
        metadata={"key": "value"},
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

<details><summary><code>client.v1.data_directories.<a href="src/truefoundry/v1/data_directories/client.py">get_signed_urls</a>(...)</code></summary>
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
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.data_directories.<a href="src/truefoundry/v1/data_directories/client.py">list_files</a>(...)</code></summary>
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
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.data_directories.<a href="src/truefoundry/v1/data_directories/client.py">delete_files</a>(...)</code></summary>
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
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.data_directories.<a href="src/truefoundry/v1/data_directories/client.py">create_multipart_upload</a>(...)</code></summary>
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
from truefoundry import TrueFoundry

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
<details><summary><code>client.v1.ml_repos.<a href="src/truefoundry/v1/ml_repos/client.py">get</a>(...)</code></summary>
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
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.ml_repos.<a href="src/truefoundry/v1/ml_repos/client.py">delete</a>(...)</code></summary>
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
from truefoundry import TrueFoundry

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

<details><summary><code>client.v1.ml_repos.<a href="src/truefoundry/v1/ml_repos/client.py">list</a>(...)</code></summary>
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
from truefoundry import TrueFoundry

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

