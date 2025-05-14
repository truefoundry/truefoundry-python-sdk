# Reference
## Users
<details><summary><code>client.users.<a href="src/truefoundry_sdk/users/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all users of tenant filtered by query and showInvalidUsers. Pagination is available based on query parameters.
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
response = client.users.list(limit=10, offset=0, )
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

**query:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**show_invalid_users:** `typing.Optional[bool]` — Show Deactivated users
    
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

<details><summary><code>client.users.<a href="src/truefoundry_sdk/users/client.py">update_roles</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint allows tenant administrators to update the roles of a user within their tenant.
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.users.update_roles(email='email', roles=['roles'], )

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

**email:** `str` — Email of the user
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.Sequence[str]` — Roles for the user
    
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

<details><summary><code>client.users.<a href="src/truefoundry_sdk/users/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get User associated with provided User id
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.users.get(id='id', )

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

**id:** `str` — User Id
    
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

<details><summary><code>client.users.<a href="src/truefoundry_sdk/users/client.py">invite_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Invite a user to the tenant
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.users.invite_user(accept_invite_client_url='<control plane url>/invite-accept', email='email', )

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

**accept_invite_client_url:** `str` — Url to redirect when invite is accepted
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — Email of user
    
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

<details><summary><code>client.users.<a href="src/truefoundry_sdk/users/client.py">deactivate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deactivate user associated with the provided email within the tenant.
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.users.deactivate(email='email', )

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

**email:** `str` — Email of the user
    
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

<details><summary><code>client.users.<a href="src/truefoundry_sdk/users/client.py">activate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Activate user associated with the provided email within the tenant.
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.users.activate(email='email', )

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

**email:** `str` — Email of the user
    
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

## Teams
<details><summary><code>client.teams.<a href="src/truefoundry_sdk/teams/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all teams associated with the authenticated user. If the user is a tenant admin, returns all teams for the tenant. Pagination is available based on query parameters
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
response = client.teams.list(limit=10, offset=0, )
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

<details><summary><code>client.teams.<a href="src/truefoundry_sdk/teams/client.py">create_or_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new team or updates an existing team. It ensures that the team name is unique, valid, and that the team has at least one member. The members of the team are added or updated based on the provided emails.
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
from truefoundry_sdk import TeamManifest
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.teams.create_or_update(manifest=TeamManifest(name='name', members=['members'], ), )

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

**manifest:** `TeamManifest` — Team manifest
    
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

<details><summary><code>client.teams.<a href="src/truefoundry_sdk/teams/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Team associated with provided team id
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.teams.get(id='id', )

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

**id:** `str` — Team Id
    
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

<details><summary><code>client.teams.<a href="src/truefoundry_sdk/teams/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the Team associated with the provided Id.
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.teams.delete(id='id', )

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

**id:** `str` — Team Id
    
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

## PersonalAccessTokens
<details><summary><code>client.personal_access_tokens.<a href="src/truefoundry_sdk/personal_access_tokens/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Personal Access Tokens created by the user in the current tenant.
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
response = client.personal_access_tokens.list(limit=10, offset=0, )
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

<details><summary><code>client.personal_access_tokens.<a href="src/truefoundry_sdk/personal_access_tokens/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Personal Access Token
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.personal_access_tokens.create(name='name', )

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

**name:** `str` — serviceaccount name
    
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

<details><summary><code>client.personal_access_tokens.<a href="src/truefoundry_sdk/personal_access_tokens/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Personal Access Token associated with the provided serviceAccountId
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.personal_access_tokens.delete(id='id', )

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

**id:** `str` — serviceaccount id
    
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

## VirtualAccounts
<details><summary><code>client.virtual_accounts.<a href="src/truefoundry_sdk/virtual_accounts/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List virtual accounts for the tenant.
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
response = client.virtual_accounts.list(limit=10, offset=0, )
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

<details><summary><code>client.virtual_accounts.<a href="src/truefoundry_sdk/virtual_accounts/client.py">create_or_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new virtual account or updates an existing one based on the provided manifest.
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
from truefoundry_sdk import VirtualAccountManifest
from truefoundry_sdk import Permissions
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.virtual_accounts.create_or_update(manifest=VirtualAccountManifest(name='name', permissions=[Permissions(resource_fqn='resource_fqn', resource_type='resource_type', role_id='role_id', )], ), )

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

**manifest:** `VirtualAccountManifest` — Virtual account manifest
    
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

<details><summary><code>client.virtual_accounts.<a href="src/truefoundry_sdk/virtual_accounts/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get virtual account by id
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.virtual_accounts.get(id='id', )

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

**id:** `str` — serviceaccount id
    
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

<details><summary><code>client.virtual_accounts.<a href="src/truefoundry_sdk/virtual_accounts/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a virtual account associated with the provided virtual account id.
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.virtual_accounts.delete(id='id', )

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

**id:** `str` — serviceaccount id
    
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

## Secrets
<details><summary><code>client.secrets.<a href="src/truefoundry_sdk/secrets/client.py">list</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
response = client.secrets.list()
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

<details><summary><code>client.secrets.<a href="src/truefoundry_sdk/secrets/client.py">get</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.secrets.get(id='id', )

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

<details><summary><code>client.secrets.<a href="src/truefoundry_sdk/secrets/client.py">delete</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.secrets.delete(id='id', )

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

## SecretGroups
<details><summary><code>client.secret_groups.<a href="src/truefoundry_sdk/secret_groups/client.py">list</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
response = client.secret_groups.list(limit=10, offset=0, )
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

<details><summary><code>client.secret_groups.<a href="src/truefoundry_sdk/secret_groups/client.py">create</a>(...)</code></summary>
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
from truefoundry_sdk import TrueFoundry
from truefoundry_sdk import SecretInput
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.secret_groups.create(name='name', integration_id='integrationId', secrets=[SecretInput(key='key', value='value', )], )

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

<details><summary><code>client.secret_groups.<a href="src/truefoundry_sdk/secret_groups/client.py">get</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.secret_groups.get(id='id', )

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

<details><summary><code>client.secret_groups.<a href="src/truefoundry_sdk/secret_groups/client.py">update</a>(...)</code></summary>
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
from truefoundry_sdk import TrueFoundry
from truefoundry_sdk import UpdateSecretInput
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.secret_groups.update(id='id', secrets=[UpdateSecretInput(key='key', value='value', )], )

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

**secrets:** `typing.Sequence[UpdateSecretInput]` 
    
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

<details><summary><code>client.secret_groups.<a href="src/truefoundry_sdk/secret_groups/client.py">delete</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.secret_groups.delete(id='id', )

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

<details><summary><code>client.secret_groups.<a href="src/truefoundry_sdk/secret_groups/client.py">list_secrets</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.secret_groups.list_secrets(id='id', )

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

## Clusters
<details><summary><code>client.clusters.<a href="src/truefoundry_sdk/clusters/client.py">list</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
response = client.clusters.list(limit=10, offset=0, )
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

<details><summary><code>client.clusters.<a href="src/truefoundry_sdk/clusters/client.py">create_or_update</a>(...)</code></summary>
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
from truefoundry_sdk import TrueFoundry
from truefoundry_sdk import ClusterManifest
from truefoundry_sdk import ClusterManifestClusterType
from truefoundry_sdk import Collaborator
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.clusters.create_or_update(manifest=ClusterManifest(name='name', cluster_type=ClusterManifestClusterType.AWS_EKS, environment_names=['environment_names'], collaborators=[Collaborator(subject='subject', role_id='role_id', )], ), )

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

<details><summary><code>client.clusters.<a href="src/truefoundry_sdk/clusters/client.py">get</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.clusters.get(id='id', )

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

<details><summary><code>client.clusters.<a href="src/truefoundry_sdk/clusters/client.py">delete</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.clusters.delete(id='id', )

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

<details><summary><code>client.clusters.<a href="src/truefoundry_sdk/clusters/client.py">get_addons</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.clusters.get_addons(id='id', limit=10, offset=0, )

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

<details><summary><code>client.clusters.<a href="src/truefoundry_sdk/clusters/client.py">is_connected</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.clusters.is_connected(id='id', )

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

## Environments
<details><summary><code>client.environments.<a href="src/truefoundry_sdk/environments/client.py">list</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
response = client.environments.list(limit=10, offset=0, )
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

<details><summary><code>client.environments.<a href="src/truefoundry_sdk/environments/client.py">create_or_update</a>(...)</code></summary>
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
from truefoundry_sdk import TrueFoundry
from truefoundry_sdk import EnvironmentManifest
from truefoundry_sdk import EnvironmentColor
from truefoundry_sdk import EnvironmentOptimizeFor
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.environments.create_or_update(manifest=EnvironmentManifest(name='name', color=EnvironmentColor(), is_production=True, optimize_for=EnvironmentOptimizeFor.COST, ), )

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

<details><summary><code>client.environments.<a href="src/truefoundry_sdk/environments/client.py">get</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.environments.get(id='id', )

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

<details><summary><code>client.environments.<a href="src/truefoundry_sdk/environments/client.py">delete</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.environments.delete(id='id', )

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

## Applications
<details><summary><code>client.applications.<a href="src/truefoundry_sdk/applications/client.py">list</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
response = client.applications.list(limit=10, offset=0, )
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

**fqn:** `typing.Optional[str]` — Fully qualified name (FQN) of the application
    
</dd>
</dl>

<dl>
<dd>

**workspace_fqn:** `typing.Optional[str]` — Fully qualified name (FQN) of the workspace
    
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

<details><summary><code>client.applications.<a href="src/truefoundry_sdk/applications/client.py">create_or_update</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.applications.create_or_update(manifest={'key': 'value'
}, )

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

<details><summary><code>client.applications.<a href="src/truefoundry_sdk/applications/client.py">get</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.applications.get(id='id', )

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

<details><summary><code>client.applications.<a href="src/truefoundry_sdk/applications/client.py">delete</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.applications.delete(id='id', )

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

<details><summary><code>client.applications.<a href="src/truefoundry_sdk/applications/client.py">scale_to_zero</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.applications.scale_to_zero(id='id', )

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

<details><summary><code>client.applications.<a href="src/truefoundry_sdk/applications/client.py">scale_to_original</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.applications.scale_to_original(id='id', )

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

<details><summary><code>client.applications.<a href="src/truefoundry_sdk/applications/client.py">cancel_deployment</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.applications.cancel_deployment(id='id', deployment_id='deploymentId', )

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

## ApplicationVersions
<details><summary><code>client.application_versions.<a href="src/truefoundry_sdk/application_versions/client.py">list</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
response = client.application_versions.list(id='id', limit=10, offset=0, version='1', deployment_id='deployment123', )
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

<details><summary><code>client.application_versions.<a href="src/truefoundry_sdk/application_versions/client.py">get</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.application_versions.get(id='id', deployment_id='deploymentId', )

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

## Jobs
<details><summary><code>client.jobs.<a href="src/truefoundry_sdk/jobs/client.py">list_runs</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
response = client.jobs.list_runs(job_id='jobId', limit=10, offset=0, )
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

<details><summary><code>client.jobs.<a href="src/truefoundry_sdk/jobs/client.py">get_run</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.jobs.get_run(job_id='jobId', job_run_name='jobRunName', )

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

<details><summary><code>client.jobs.<a href="src/truefoundry_sdk/jobs/client.py">delete_run</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.jobs.delete_run(job_id='jobId', job_run_name='jobRunName', )

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

<details><summary><code>client.jobs.<a href="src/truefoundry_sdk/jobs/client.py">trigger</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.jobs.trigger()

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

**input:** `typing.Optional[TriggerJobRequestInput]` — Job trigger input
    
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

<details><summary><code>client.jobs.<a href="src/truefoundry_sdk/jobs/client.py">terminate</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.jobs.terminate(deployment_id='deploymentId', job_run_name='jobRunName', )

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

## Workspaces
<details><summary><code>client.workspaces.<a href="src/truefoundry_sdk/workspaces/client.py">list</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
response = client.workspaces.list(limit=10, offset=0, )
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

<details><summary><code>client.workspaces.<a href="src/truefoundry_sdk/workspaces/client.py">create_or_update</a>(...)</code></summary>
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
from truefoundry_sdk import TrueFoundry
from truefoundry_sdk import WorkspaceManifest
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.workspaces.create_or_update(manifest=WorkspaceManifest(cluster_fqn='cluster_fqn', name='name', ), )

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

<details><summary><code>client.workspaces.<a href="src/truefoundry_sdk/workspaces/client.py">get</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.workspaces.get(id='id', )

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

<details><summary><code>client.workspaces.<a href="src/truefoundry_sdk/workspaces/client.py">delete</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.workspaces.delete(id='id', )

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

## Events
<details><summary><code>client.events.<a href="src/truefoundry_sdk/events/client.py">get</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.events.get()

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

## Alerts
<details><summary><code>client.alerts.<a href="src/truefoundry_sdk/alerts/client.py">list</a>(...)</code></summary>
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
client = TrueFoundry(api_key="YOUR_API_KEY", base_url="https://yourhost.com/path/to/api", )
client.alerts.list()

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

## Logs
<details><summary><code>client.logs.<a href="src/truefoundry_sdk/logs/client.py">get</a>(...)</code></summary>
