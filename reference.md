# Reference
<details><summary><code>client.<a href="src/truefoundry_sdk/base_client.py">apply</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Applies a given manifest to create or update resources of specific types, such as provider-account, cluster, workspace, or ml-repo.
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
from truefoundry_sdk import Collaborator, MlRepoManifest, TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.apply(
    manifest=MlRepoManifest(
        name="name",
        storage_integration_fqn="storage_integration_fqn",
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

**manifest:** `TrueFoundryApplyRequestManifest` — manifest of the resource to be created or updated
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` — Dry run the apply operation without actually applying
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/truefoundry_sdk/base_client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes resources of specific types, such as provider-account, cluster, workspace, or application.
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
from truefoundry_sdk import Collaborator, MlRepoManifest, TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.delete(
    manifest=MlRepoManifest(
        name="name",
        storage_integration_fqn="storage_integration_fqn",
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

**manifest:** `TrueFoundryDeleteRequestManifest` — manifest of the resource to be deleted
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Internal
<details><summary><code>client.internal.<a href="src/truefoundry_sdk/internal/client.py">get_id_from_fqn</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get IDs associated with the FQN for various entity types, such as deployment, application, workspace, or cluster.
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
client.internal.get_id_from_fqn(
    type="type",
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

**type:** `str` — Entity Type
    
</dd>
</dl>

<dl>
<dd>

**fqn:** `str` — Entity FQN
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
response = client.users.list(
    limit=10,
    offset=0,
    query="query",
    show_invalid_users=True,
    include_virtual_accounts="includeVirtualAccounts",
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

**include_virtual_accounts:** `typing.Optional[str]` — Include virtual accounts
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/truefoundry_sdk/users/client.py">pre_register_users</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint allows tenant administrators to register users within their tenant.
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
client.users.pre_register_users(
    email="email",
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

**email:** `str` — Email of the user
    
</dd>
</dl>

<dl>
<dd>

**send_invite_email:** `typing.Optional[bool]` — Send invite email if user does not exist
    
</dd>
</dl>

<dl>
<dd>

**skip_if_user_exists:** `typing.Optional[bool]` — Fail if user exists
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` — Dry run
    
</dd>
</dl>

<dl>
<dd>

**accept_invite_client_url:** `typing.Optional[str]` — Url to redirect when invite is accepted
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `typing.Optional[str]` — Account ID to add the user to
    
</dd>
</dl>

<dl>
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.users.update_roles(
    email="email",
    roles=["roles"],
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.users.get(
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

<details><summary><code>client.users.<a href="src/truefoundry_sdk/users/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete user if they are not a collaborator in any resource and not part of any team other than everyone.
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
client.users.delete(
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.users.invite_user(
    accept_invite_client_url="<control plane url>/invite-accept",
    email="email",
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

**account_id:** `typing.Optional[str]` — Account ID to add the user to
    
</dd>
</dl>

<dl>
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.users.deactivate(
    email="email",
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.users.activate(
    email="email",
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

<details><summary><code>client.users.<a href="src/truefoundry_sdk/users/client.py">change_password</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Change password for the authenticated user. Requires clientId and loginId in the request body.
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
client.users.change_password(
    login_id="loginId",
    new_password="newPassword",
    old_password="oldPassword",
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

**login_id:** `str` — login id of the user(email)
    
</dd>
</dl>

<dl>
<dd>

**new_password:** `str` — New password
    
</dd>
</dl>

<dl>
<dd>

**old_password:** `str` — Old password
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/truefoundry_sdk/users/client.py">get_resources</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all resources associated with a user.
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
client.users.get_resources(
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

<details><summary><code>client.users.<a href="src/truefoundry_sdk/users/client.py">get_teams</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all manual teams associated with a user.
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
client.users.get_teams(
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
from truefoundry_sdk.teams import TeamsListRequestType

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
response = client.teams.list(
    limit=10,
    offset=0,
    type=TeamsListRequestType.TEAM,
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

**type:** `typing.Optional[TeamsListRequestType]` — Filter teams by type
    
</dd>
</dl>

<dl>
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
from truefoundry_sdk import TeamManifest, TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.teams.create_or_update(
    manifest=TeamManifest(
        name="name",
        members=["members"],
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

**manifest:** `ApplyTeamRequestManifest` — Team manifest
    
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.teams.get(
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.teams.delete(
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
response = client.personal_access_tokens.list(
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.personal_access_tokens.create(
    name="name",
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

**name:** `str` — serviceaccount name
    
</dd>
</dl>

<dl>
<dd>

**expiration_date:** `typing.Optional[str]` — Expiration date in ISO format (e.g. 2025-08-01T12:00)
    
</dd>
</dl>

<dl>
<dd>

**account_name:** `typing.Optional[str]` — Account name that owns this PAT
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.personal_access_tokens.<a href="src/truefoundry_sdk/personal_access_tokens/client.py">revoke_all</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke All Personal Access Tokens for the user with the given email
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
client.personal_access_tokens.revoke_all(
    email="email",
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

**email:** `str` — Email of the user to revoke all Personal Access Tokens for
    
</dd>
</dl>

<dl>
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.personal_access_tokens.delete(
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

<details><summary><code>client.personal_access_tokens.<a href="src/truefoundry_sdk/personal_access_tokens/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an existing Personal Access Token by name, if it doesn't exist, it will create a new one and return the PAT data along with a fresh token.
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
client.personal_access_tokens.get(
    name="name",
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

**name:** `str` 
    
</dd>
</dl>

<dl>
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
response = client.virtual_accounts.list(
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
from truefoundry_sdk import Permissions, TrueFoundry, VirtualAccountManifest

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.virtual_accounts.create_or_update(
    manifest=VirtualAccountManifest(
        name="name",
        permissions=[
            Permissions(
                resource_fqn="resource_fqn",
                resource_type="resource_type",
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.virtual_accounts.get(
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.virtual_accounts.delete(
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

<details><summary><code>client.virtual_accounts.<a href="src/truefoundry_sdk/virtual_accounts/client.py">get_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get token for a virtual account by id
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
client.virtual_accounts.get_token(
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

<details><summary><code>client.virtual_accounts.<a href="src/truefoundry_sdk/virtual_accounts/client.py">sync_to_secret_store</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Syncs the virtual account token to the configured secret store. Returns the updated JWT with sync metadata including timestamp and error (if any).
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
client.virtual_accounts.sync_to_secret_store(
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

<details><summary><code>client.virtual_accounts.<a href="src/truefoundry_sdk/virtual_accounts/client.py">regenerate_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Regenerate token for a virtual account by id. The old token will remain valid for the specified grace period.
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
client.virtual_accounts.regenerate_token(
    id="id",
    grace_period_in_days=30.0,
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

**id:** `str` — serviceaccount id
    
</dd>
</dl>

<dl>
<dd>

**grace_period_in_days:** `float` — Grace period in days for which the old token will remain valid after regeneration
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.virtual_accounts.<a href="src/truefoundry_sdk/virtual_accounts/client.py">delete_jwt</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a JWT for a virtual account by id
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
client.virtual_accounts.delete_jwt(
    id="id",
    jwt_id="jwtId",
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

**id:** `str` — virtual account id
    
</dd>
</dl>

<dl>
<dd>

**jwt_id:** `str` — JWT id
    
</dd>
</dl>

<dl>
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
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

**with_value:** `typing.Optional[bool]` — Whether to include the secret values in the response. Defaults to false.
    
</dd>
</dl>

<dl>
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

Get Secret associated with provided id. The secret value is not returned if the control plane has `DISABLE_SECRET_VALUE_VIEW` set
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
client.secrets.get(
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.secrets.delete(
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

## SecretGroups
<details><summary><code>client.secret_groups.<a href="src/truefoundry_sdk/secret_groups/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the secret groups associated with a user along with the associated secrets for each group. Filtered with the options passed in the query fields. Note: This method does not return the secret values of the <em>associatedSecrets</em> in the response. A separate API call to `/v1/secrets/{id}` should be made to fetch the associated secret value.
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
response = client.secret_groups.list(
    limit=10,
    offset=0,
    fqn="fqn",
    search="search",
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

**fqn:** `typing.Optional[str]` — Fqn of secret group.
    
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

Creates a secret group with secrets in it. A secret version for each of the created secret is created with version number as 1. The returned secret group does not have any secret values in the <em>associatedSecrets</em> field. A separate API call to `/v1/secrets/{id}` should be made to fetch the associated secret value.
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
client.secret_groups.create(
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

<details><summary><code>client.secret_groups.<a href="src/truefoundry_sdk/secret_groups/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Secret Group by id. This method does not return the secret values of the <em>associatedSecrets</em> in the response. A separate API call to `/v1/secrets/{id}` should be made to fetch the associated secret value.
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
client.secret_groups.get(
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

<details><summary><code>client.secret_groups.<a href="src/truefoundry_sdk/secret_groups/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the secrets in a secret group with new values. A new secret version is created for every secret that has a modified value and any omitted secrets are deleted. The returned updated secret group does not have any secret values in the <em>associatedSecrets</em> field. A separate API call to `/v1/secrets/{id}` should be made to fetch the associated secret value.
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
from truefoundry_sdk import TrueFoundry, UpdateSecretInput

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.secret_groups.update(
    id="id",
    secrets=[
        UpdateSecretInput(
            key="key",
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.secret_groups.delete(
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
response = client.clusters.list(
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
client.clusters.create_or_update(
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.clusters.get(
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.clusters.delete(
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

<details><summary><code>client.clusters.<a href="src/truefoundry_sdk/clusters/client.py">get_addons</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List addons for the provided cluster. Pagination is available based on query parameters.
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
client.clusters.get_addons(
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.clusters.is_connected(
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
response = client.environments.list(
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
client.environments.create_or_update(
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.environments.get(
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.environments.delete(
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
from truefoundry_sdk.applications import (
    ApplicationsListRequestDeviceTypeFilter,
    ApplicationsListRequestLifecycleStage,
)

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
response = client.applications.list(
    limit=10,
    offset=0,
    application_id="applicationId",
    workspace_id="workspaceId",
    application_name="applicationName",
    fqn="fqn",
    workspace_fqn="workspaceFqn",
    application_type="applicationType",
    name_search_query="nameSearchQuery",
    environment_id="environmentId",
    cluster_id="clusterId",
    application_set_id="applicationSetId",
    paused=True,
    device_type_filter=ApplicationsListRequestDeviceTypeFilter.CPU,
    last_deployed_by_subjects="lastDeployedBySubjects",
    lifecycle_stage=ApplicationsListRequestLifecycleStage.ACTIVE,
    is_recommendation_present_and_visible=True,
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

**is_recommendation_present_and_visible:** `typing.Optional[bool]` — Filter out applications with recommendations that are allowed to be shown
    
</dd>
</dl>

<dl>
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.applications.create_or_update(
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

**trigger_on_deploy:** `typing.Optional[bool]` — Trigger on deploy
    
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.applications.get(
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.applications.delete(
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.applications.scale_to_zero(
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.applications.scale_to_original(
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.applications.cancel_deployment(
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
response = client.application_versions.list(
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.application_versions.get(
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
from truefoundry_sdk import JobRunsSortBy, SortDirection, TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
response = client.jobs.list_runs(
    job_id="jobId",
    limit=10,
    offset=0,
    search_prefix="searchPrefix",
    sort_by=JobRunsSortBy.START_TIME,
    order=SortDirection.ASC,
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

**order:** `typing.Optional[SortDirection]` — Sorting order
    
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

**version_numbers:** `typing.Optional[typing.Union[float, typing.Sequence[float]]]` — Version number of the deployment
    
</dd>
</dl>

<dl>
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.jobs.get_run(
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.jobs.delete_run(
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
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

**metadata:** `typing.Optional[Metadata]` — Metadata for the job run including job_alias_name
    
</dd>
</dl>

<dl>
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.jobs.terminate(
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
response = client.workspaces.list(
    limit=10,
    offset=0,
    cluster_id="clusterId",
    name="name",
    fqn="fqn",
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
from truefoundry_sdk import TrueFoundry, WorkspaceManifest

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.workspaces.create_or_update(
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.workspaces.get(
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.workspaces.delete(
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

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.events.get(
    start_ts="startTs",
    end_ts="endTs",
    application_id="applicationId",
    application_fqn="applicationFqn",
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
from truefoundry_sdk import AlertStatus, TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.alerts.list(
    start_ts="startTs",
    end_ts="endTs",
    cluster_id="clusterId",
    application_id="applicationId",
    alert_status=AlertStatus.FIRING,
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
from truefoundry_sdk import (
    LogsSearchFilterType,
    LogsSearchOperatorType,
    LogsSortingDirection,
    TrueFoundry,
)

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.logs.get(
    start_ts=1000000,
    end_ts=1000000,
    limit=1,
    direction=LogsSortingDirection.ASC,
    num_logs_to_ignore=1,
    application_id="applicationId",
    application_fqn="applicationFqn",
    deployment_id="deploymentId",
    job_run_name="jobRunName",
    pod_name="podName",
    container_name="containerName",
    pod_names_regex="podNamesRegex",
    search_filters="searchFilters",
    search_string="searchString",
    search_type=LogsSearchFilterType.REGEX,
    search_operator=LogsSearchOperatorType.EQUAL,
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

**search_filters:** `typing.Optional[str]` — JSON string containing array of search filters with string, type and operator
    
</dd>
</dl>

<dl>
<dd>

**search_string:** `typing.Optional[str]` — String that needs to be matched
    
</dd>
</dl>

<dl>
<dd>

**search_type:** `typing.Optional[LogsSearchFilterType]` — Query filter type, `regex` `substring` `ignore_case_substring`
    
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

## MlRepos
<details><summary><code>client.ml_repos.<a href="src/truefoundry_sdk/ml_repos/client.py">create_or_update</a>(...)</code></summary>
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
from truefoundry_sdk import Collaborator, MlRepoManifest, TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.ml_repos.create_or_update(
    manifest=MlRepoManifest(
        name="name",
        storage_integration_fqn="storage_integration_fqn",
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

**manifest:** `MlRepoManifest` — MLRepo manifest
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ml_repos.<a href="src/truefoundry_sdk/ml_repos/client.py">get</a>(...)</code></summary>
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
client.ml_repos.get(
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

<details><summary><code>client.ml_repos.<a href="src/truefoundry_sdk/ml_repos/client.py">delete</a>(...)</code></summary>
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
client.ml_repos.delete(
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

<details><summary><code>client.ml_repos.<a href="src/truefoundry_sdk/ml_repos/client.py">list</a>(...)</code></summary>
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
response = client.ml_repos.list(
    name="name",
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

## Traces
<details><summary><code>client.traces.<a href="src/truefoundry_sdk/traces/client.py">query_spans</a>(...)</code></summary>
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
response = client.traces.query_spans(
    start_time="startTime",
    tracing_project_fqn="tracingProjectFqn",
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

**start_time:** `str` — Start time in ISO 8601 format (e.g., 2025-03-12T00:00:09.872Z)
    
</dd>
</dl>

<dl>
<dd>

**tracing_project_fqn:** `str` — Tracing project FQN (e.g., truefoundry:tracing-project:tfy-default)
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` — End time in ISO 8601 format (e.g., 2025-03-12T00:10:00.000Z). Defaults to current time if not provided.
    
</dd>
</dl>

<dl>
<dd>

**trace_ids:** `typing.Optional[typing.Sequence[str]]` — Array of trace IDs to filter by
    
</dd>
</dl>

<dl>
<dd>

**span_ids:** `typing.Optional[typing.Sequence[str]]` — Array of span IDs to filter by
    
</dd>
</dl>

<dl>
<dd>

**parent_span_ids:** `typing.Optional[typing.Sequence[str]]` — Array of parent span IDs to filter by
    
</dd>
</dl>

<dl>
<dd>

**created_by_subject_types:** `typing.Optional[typing.Sequence[SubjectType]]` — Array of subject types to filter by
    
</dd>
</dl>

<dl>
<dd>

**created_by_subject_slugs:** `typing.Optional[typing.Sequence[str]]` — Array of subject slugs to filter by
    
</dd>
</dl>

<dl>
<dd>

**application_names:** `typing.Optional[typing.Sequence[str]]` — Array of application names to filter by
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of spans to return per page. Defaults to 200 if not provided.
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Sort direction for results based on time. Defaults to descending (latest first)
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — An opaque string that should be passed as-is from previous response for fetching the next page. Pass `$response.pagination.nextPageToken` from previous response for fetching the next page.
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[typing.Sequence[QuerySpansRequestFiltersItem]]` — Array of filters
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Artifacts
<details><summary><code>client.artifacts.<a href="src/truefoundry_sdk/artifacts/client.py">get</a>(...)</code></summary>
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
client.artifacts.get(
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

<details><summary><code>client.artifacts.<a href="src/truefoundry_sdk/artifacts/client.py">delete</a>(...)</code></summary>
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
client.artifacts.delete(
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

<details><summary><code>client.artifacts.<a href="src/truefoundry_sdk/artifacts/client.py">list</a>(...)</code></summary>
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
response = client.artifacts.list(
    fqn="fqn",
    ml_repo_id="ml_repo_id",
    name="name",
    offset=1,
    limit=1,
    run_id="run_id",
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

**fqn:** `typing.Optional[str]` 
    
</dd>
</dl>

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

<details><summary><code>client.artifacts.<a href="src/truefoundry_sdk/artifacts/client.py">create_or_update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import (
    ArtifactManifest,
    TrueFoundry,
    TrueFoundryManagedSource,
)

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.artifacts.create_or_update(
    manifest=ArtifactManifest(
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

**manifest:** `ArtifactManifest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Prompts
<details><summary><code>client.prompts.<a href="src/truefoundry_sdk/prompts/client.py">get</a>(...)</code></summary>
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
client.prompts.get(
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

<details><summary><code>client.prompts.<a href="src/truefoundry_sdk/prompts/client.py">delete</a>(...)</code></summary>
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
client.prompts.delete(
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

<details><summary><code>client.prompts.<a href="src/truefoundry_sdk/prompts/client.py">list</a>(...)</code></summary>
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
response = client.prompts.list(
    fqn="fqn",
    ml_repo_id="ml_repo_id",
    name="name",
    offset=1,
    limit=1,
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

**fqn:** `typing.Optional[str]` 
    
</dd>
</dl>

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

<details><summary><code>client.prompts.<a href="src/truefoundry_sdk/prompts/client.py">create_or_update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import ChatPromptManifest, SystemMessage, TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.prompts.create_or_update(
    manifest=ChatPromptManifest(
        name="name",
        metadata={"key": "value"},
        ml_repo="ml_repo",
        messages=[
            SystemMessage(
                content="content",
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

**manifest:** `ChatPromptManifest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Models
<details><summary><code>client.models.<a href="src/truefoundry_sdk/models/client.py">get</a>(...)</code></summary>
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
client.models.get(
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

<details><summary><code>client.models.<a href="src/truefoundry_sdk/models/client.py">delete</a>(...)</code></summary>
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
client.models.delete(
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

<details><summary><code>client.models.<a href="src/truefoundry_sdk/models/client.py">list</a>(...)</code></summary>
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
response = client.models.list(
    fqn="fqn",
    ml_repo_id="ml_repo_id",
    name="name",
    offset=1,
    limit=1,
    run_id="run_id",
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

**fqn:** `typing.Optional[str]` 
    
</dd>
</dl>

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

<details><summary><code>client.models.<a href="src/truefoundry_sdk/models/client.py">create_or_update</a>(...)</code></summary>
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
client.models.create_or_update(
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

**manifest:** `ModelManifest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ArtifactVersions
<details><summary><code>client.artifact_versions.<a href="src/truefoundry_sdk/artifact_versions/client.py">apply_tags</a>(...)</code></summary>
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
client.artifact_versions.apply_tags(
    artifact_version_id="artifact_version_id",
    tags=["tags"],
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

**artifact_version_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**force:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artifact_versions.<a href="src/truefoundry_sdk/artifact_versions/client.py">get</a>(...)</code></summary>
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
client.artifact_versions.get(
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

<details><summary><code>client.artifact_versions.<a href="src/truefoundry_sdk/artifact_versions/client.py">delete</a>(...)</code></summary>
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
client.artifact_versions.delete(
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

<details><summary><code>client.artifact_versions.<a href="src/truefoundry_sdk/artifact_versions/client.py">list</a>(...)</code></summary>
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
response = client.artifact_versions.list(
    tag="tag",
    fqn="fqn",
    artifact_id="artifact_id",
    ml_repo_id="ml_repo_id",
    name="name",
    version=1,
    offset=1,
    limit=1,
    include_internal_metadata=True,
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

**tag:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**fqn:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**artifact_id:** `typing.Optional[str]` 
    
</dd>
</dl>

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

**version:** `typing.Optional[int]` 
    
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

<details><summary><code>client.artifact_versions.<a href="src/truefoundry_sdk/artifact_versions/client.py">get_signed_urls</a>(...)</code></summary>
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
client.artifact_versions.get_signed_urls(
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

<details><summary><code>client.artifact_versions.<a href="src/truefoundry_sdk/artifact_versions/client.py">create_multi_part_upload</a>(...)</code></summary>
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
client.artifact_versions.create_multi_part_upload(
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

<details><summary><code>client.artifact_versions.<a href="src/truefoundry_sdk/artifact_versions/client.py">stage</a>(...)</code></summary>
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
client.artifact_versions.stage(
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

**manifest:** `StageArtifactRequestManifest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artifact_versions.<a href="src/truefoundry_sdk/artifact_versions/client.py">list_files</a>(...)</code></summary>
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
response = client.artifact_versions.list_files(
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

<details><summary><code>client.artifact_versions.<a href="src/truefoundry_sdk/artifact_versions/client.py">mark_stage_failure</a>(...)</code></summary>
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
client.artifact_versions.mark_stage_failure(
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

## ModelVersions
<details><summary><code>client.model_versions.<a href="src/truefoundry_sdk/model_versions/client.py">apply_tags</a>(...)</code></summary>
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
client.model_versions.apply_tags(
    model_version_id="model_version_id",
    tags=["tags"],
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

**model_version_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**force:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.model_versions.<a href="src/truefoundry_sdk/model_versions/client.py">get</a>(...)</code></summary>
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
client.model_versions.get(
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

<details><summary><code>client.model_versions.<a href="src/truefoundry_sdk/model_versions/client.py">delete</a>(...)</code></summary>
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
client.model_versions.delete(
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

<details><summary><code>client.model_versions.<a href="src/truefoundry_sdk/model_versions/client.py">list</a>(...)</code></summary>
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
response = client.model_versions.list(
    tag="tag",
    fqn="fqn",
    model_id="model_id",
    ml_repo_id="ml_repo_id",
    name="name",
    version=1,
    offset=1,
    limit=1,
    include_internal_metadata=True,
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

**tag:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**fqn:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**model_id:** `typing.Optional[str]` 
    
</dd>
</dl>

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

**version:** `typing.Optional[int]` 
    
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

## PromptVersions
<details><summary><code>client.prompt_versions.<a href="src/truefoundry_sdk/prompt_versions/client.py">apply_tags</a>(...)</code></summary>
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
client.prompt_versions.apply_tags(
    prompt_version_id="prompt_version_id",
    tags=["tags"],
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

**prompt_version_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**force:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prompt_versions.<a href="src/truefoundry_sdk/prompt_versions/client.py">get</a>(...)</code></summary>
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
client.prompt_versions.get(
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

<details><summary><code>client.prompt_versions.<a href="src/truefoundry_sdk/prompt_versions/client.py">delete</a>(...)</code></summary>
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
client.prompt_versions.delete(
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

<details><summary><code>client.prompt_versions.<a href="src/truefoundry_sdk/prompt_versions/client.py">list</a>(...)</code></summary>
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
response = client.prompt_versions.list(
    tag="tag",
    fqn="fqn",
    prompt_id="prompt_id",
    ml_repo_id="ml_repo_id",
    name="name",
    version=1,
    offset=1,
    limit=1,
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

**tag:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**fqn:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**prompt_id:** `typing.Optional[str]` 
    
</dd>
</dl>

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

**version:** `typing.Optional[int]` 
    
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

## DataDirectories
<details><summary><code>client.data_directories.<a href="src/truefoundry_sdk/data_directories/client.py">get</a>(...)</code></summary>
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
client.data_directories.get(
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

<details><summary><code>client.data_directories.<a href="src/truefoundry_sdk/data_directories/client.py">delete</a>(...)</code></summary>
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
client.data_directories.delete(
    id="id",
    delete_contents=True,
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

<details><summary><code>client.data_directories.<a href="src/truefoundry_sdk/data_directories/client.py">list</a>(...)</code></summary>
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
response = client.data_directories.list(
    fqn="fqn",
    ml_repo_id="ml_repo_id",
    name="name",
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

**fqn:** `typing.Optional[str]` 
    
</dd>
</dl>

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

<details><summary><code>client.data_directories.<a href="src/truefoundry_sdk/data_directories/client.py">create_or_update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import (
    DataDirectoryManifest,
    TrueFoundry,
    TrueFoundryManagedSource,
)

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.data_directories.create_or_update(
    manifest=DataDirectoryManifest(
        name="name",
        ml_repo="ml_repo",
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

**manifest:** `DataDirectoryManifest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_directories.<a href="src/truefoundry_sdk/data_directories/client.py">list_files</a>(...)</code></summary>
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
response = client.data_directories.list_files(
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

<details><summary><code>client.data_directories.<a href="src/truefoundry_sdk/data_directories/client.py">delete_files</a>(...)</code></summary>
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
client.data_directories.delete_files(
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

<details><summary><code>client.data_directories.<a href="src/truefoundry_sdk/data_directories/client.py">get_signed_urls</a>(...)</code></summary>
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
client.data_directories.get_signed_urls(
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

<details><summary><code>client.data_directories.<a href="src/truefoundry_sdk/data_directories/client.py">create_multipart_upload</a>(...)</code></summary>
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
client.data_directories.create_multipart_upload(
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

## Internal Users
<details><summary><code>client.internal.users.<a href="src/truefoundry_sdk/internal/users/client.py">get_info</a>()</code></summary>
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
client.internal.users.get_info()

```
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

## Internal AiGateway
<details><summary><code>client.internal.ai_gateway.<a href="src/truefoundry_sdk/internal/ai_gateway/client.py">get_gateway_config</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Gateway configuration based on type for the tenant.
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
from truefoundry_sdk.internal.ai_gateway import (
    AiGatewayGetGatewayConfigRequestType,
)

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.internal.ai_gateway.get_gateway_config(
    type=AiGatewayGetGatewayConfigRequestType.GATEWAY_RATE_LIMITING_CONFIG,
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

**type:** `AiGatewayGetGatewayConfigRequestType` — Type of Config
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Internal Clusters
<details><summary><code>client.internal.clusters.<a href="src/truefoundry_sdk/internal/clusters/client.py">get_autoprovisioning_state</a>(...)</code></summary>
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
client.internal.clusters.get_autoprovisioning_state(
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

## Internal Deployments
<details><summary><code>client.internal.deployments.<a href="src/truefoundry_sdk/internal/deployments/client.py">get_deployment_statuses</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint returns all statuses for a specific deployment in a given application.
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
client.internal.deployments.get_deployment_statuses(
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

<details><summary><code>client.internal.deployments.<a href="src/truefoundry_sdk/internal/deployments/client.py">get_builds</a>(...)</code></summary>
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
client.internal.deployments.get_builds(
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

<details><summary><code>client.internal.deployments.<a href="src/truefoundry_sdk/internal/deployments/client.py">get_code_upload_url</a>(...)</code></summary>
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
client.internal.deployments.get_code_upload_url(
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

<details><summary><code>client.internal.deployments.<a href="src/truefoundry_sdk/internal/deployments/client.py">get_suggested_endpoint</a>(...)</code></summary>
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
client.internal.deployments.get_suggested_endpoint(
    application_type=ApplicationType.ASYNC_SERVICE,
    application_name="applicationName",
    workspace_id="workspaceId",
    base_domain="baseDomain",
    port="port",
    prefer_wildcard=True,
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

## Internal Applications
<details><summary><code>client.internal.applications.<a href="src/truefoundry_sdk/internal/applications/client.py">promote_rollout</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Promote an application rollout for canary and blue-green.
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
client.internal.applications.promote_rollout(
    id="id",
    full=True,
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

**full:** `typing.Optional[bool]` — Whether to promote a rollout to full
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.internal.applications.<a href="src/truefoundry_sdk/internal/applications/client.py">get_pod_template_hash_to_deployment_version</a>(...)</code></summary>
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
client.internal.applications.get_pod_template_hash_to_deployment_version(
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

**pod_template_hashes:** `typing.Optional[str]` — Pod Template Hashes (comma separated for multiple)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Internal Metrics
<details><summary><code>client.internal.metrics.<a href="src/truefoundry_sdk/internal/metrics/client.py">get_charts</a>(...)</code></summary>
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
from truefoundry_sdk.internal.metrics import MetricsGetChartsRequestFilterEntity

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
client.internal.metrics.get_charts(
    workspace_id="workspaceId",
    application_id="applicationId",
    start_ts="startTs",
    end_ts="endTs",
    filter_entity=MetricsGetChartsRequestFilterEntity.APPLICATION,
    filter_query="filterQuery",
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

## Internal Vcs
<details><summary><code>client.internal.vcs.<a href="src/truefoundry_sdk/internal/vcs/client.py">get_repository_details</a>(...)</code></summary>
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
client.internal.vcs.get_repository_details(
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

<details><summary><code>client.internal.vcs.<a href="src/truefoundry_sdk/internal/vcs/client.py">get_authenticated_url</a>(...)</code></summary>
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
client.internal.vcs.get_authenticated_url(
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

## Internal DockerRegistries
<details><summary><code>client.internal.docker_registries.<a href="src/truefoundry_sdk/internal/docker_registries/client.py">create_repository</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a docker repository in the provided workspace.
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
client.internal.docker_registries.create_repository(
    fqn="fqn",
    application_name="applicationName",
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

**fqn:** `str` — Docker registry FQN
    
</dd>
</dl>

<dl>
<dd>

**application_name:** `str` — Application Name for the image being built
    
</dd>
</dl>

<dl>
<dd>

**workspace_fqn:** `str` — FQN for the workspace of application
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.internal.docker_registries.<a href="src/truefoundry_sdk/internal/docker_registries/client.py">get_credentials</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get docker registry credentials for building and pushing an image.
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
client.internal.docker_registries.get_credentials(
    fqn="fqn",
    cluster_id="clusterId",
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

**fqn:** `typing.Optional[str]` — Docker registry FQN
    
</dd>
</dl>

<dl>
<dd>

**cluster_id:** `typing.Optional[str]` — Cluster Id if provided will fetch the default docker registry for the cluster
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Internal Workflows
<details><summary><code>client.internal.workflows.<a href="src/truefoundry_sdk/internal/workflows/client.py">execute_workflow</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute a workflow for the specified application
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
client.internal.workflows.execute_workflow(
    application_id="applicationId",
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

**application_id:** `str` — Id of the application
    
</dd>
</dl>

<dl>
<dd>

**inputs:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Workflow inputs
    
</dd>
</dl>

<dl>
<dd>

**inputs_literal_map:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Workflow inputs literal map
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Internal ArtifactVersions
<details><summary><code>client.internal.artifact_versions.<a href="src/truefoundry_sdk/internal/artifact_versions/client.py">list</a>(...)</code></summary>
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
response = client.internal.artifact_versions.list(
    tag="tag",
    fqn="fqn",
    artifact_id="artifact_id",
    ml_repo_id="ml_repo_id",
    name="name",
    version=1,
    offset=1,
    limit=1,
    include_internal_metadata=True,
    include_model_versions=True,
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

**tag:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**fqn:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**artifact_id:** `typing.Optional[str]` 
    
</dd>
</dl>

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

**version:** `typing.Optional[int]` 
    
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

## Internal Ml
<details><summary><code>client.internal.ml.<a href="src/truefoundry_sdk/internal/ml/client.py">apply</a>(...)</code></summary>
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
client.internal.ml.apply(
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

**manifest:** `ApplyMlEntityRequestManifest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.internal.ml.<a href="src/truefoundry_sdk/internal/ml/client.py">delete</a>(...)</code></summary>
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
client.internal.ml.delete(
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

**manifest:** `DeleteMlEntityRequestManifest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

