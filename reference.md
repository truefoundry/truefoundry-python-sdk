# Reference
<details><summary><code>client.<a href="src/truefoundry_sdk/client.py">apply</a>(...) -> TrueFoundryApplyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Apply a manifest to create or update a resource.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry, MlRepoManifest, Collaborator

client = TrueFoundry(
    api_key="<token>",
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

**manifest:** `TrueFoundryApplyRequestManifest` — Manifest of the resource to be created or updated
    
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

<details><summary><code>client.<a href="src/truefoundry_sdk/client.py">delete</a>(...) -> TrueFoundryDeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a resource identified by the provided manifest.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry, MlRepoManifest, Collaborator

client = TrueFoundry(
    api_key="<token>",
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

**manifest:** `TrueFoundryDeleteRequestManifest` — Manifest of the resource to be deleted
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.internal.<a href="src/truefoundry_sdk/internal/client.py">get_id_from_fqn</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
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
    api_key="<token>",
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
<details><summary><code>client.users.<a href="src/truefoundry_sdk/users/client.py">list</a>(...) -> ListUsersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List users in the current tenant.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.users.list(
    limit=10,
    offset=0,
    query="john@example.com",
    show_invalid_users=True,
)

```
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

**query:** `typing.Optional[str]` — Filter users by email substring match.
    
</dd>
</dl>

<dl>
<dd>

**show_invalid_users:** `typing.Optional[bool]` — When true, includes deactivated users in the response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/truefoundry_sdk/users/client.py">pre_register_users</a>(...) -> RegisterUsersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Pre-register a user in the current tenant. Optionally sends an invite email if the auth provider is managed by TrueFoundry.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.users.pre_register_users(
    email="user@example.com",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` — Email address of the user to register.
    
</dd>
</dl>

<dl>
<dd>

**send_invite_email:** `typing.Optional[bool]` — When true, sends an invite email to the user after registration.
    
</dd>
</dl>

<dl>
<dd>

**skip_if_user_exists:** `typing.Optional[bool]` — When true, silently skips registration if the user already exists instead of returning an error.
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` — When true, validates the request without persisting changes.
    
</dd>
</dl>

<dl>
<dd>

**accept_invite_client_url:** `typing.Optional[str]` — URL the user is redirected to when they accept the invite. Required when sendInviteEmail is true.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/truefoundry_sdk/users/client.py">update_roles</a>(...) -> UpdateUserRolesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the role assigned to a user in the current tenant.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.users.update_roles(
    email="user@example.com",
    roles=[
        "tenant-admin"
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

**email:** `str` — Email of the user whose roles are being updated.
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.List[str]` — Role names to assign to the user.
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `typing.Optional[UpdateUserRolesRequestResourceType]` — Resource type scope for the role assignment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/truefoundry_sdk/users/client.py">get</a>(...) -> GetUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single user by their ID.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.users.get(
    id="jqfwg345gi25n5ju2yz5iz6m",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — System-generated user ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/truefoundry_sdk/users/client.py">delete</a>(...) -> DeleteUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete a user by ID. The user must not be a collaborator on any resource and must not belong to any team other than "everyone".
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.users.delete(
    id="jqfwg345gi25n5ju2yz5iz6m",
    tenant_name="tenantName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — System-generated user ID.
    
</dd>
</dl>

<dl>
<dd>

**tenant_name:** `typing.Optional[str]` — Tenant name override. Defaults to the caller's tenant when omitted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/truefoundry_sdk/users/client.py">invite_user</a>(...) -> InviteUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Invite a new user to the current tenant by email. Only available when the auth provider is managed by TrueFoundry.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.users.invite_user(
    accept_invite_client_url="https://app.example.com/invite-accept",
    email="user@example.com",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**accept_invite_client_url:** `str` — URL the user is redirected to when they accept the invite.
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — Email address of the user to invite.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/truefoundry_sdk/users/client.py">deactivate</a>(...) -> DeactivateUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deactivate a user by email in the current tenant. The user will no longer be able to log in.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.users.deactivate(
    email="user@example.com",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` — Email of the user to deactivate.
    
</dd>
</dl>

<dl>
<dd>

**tenant_name:** `typing.Optional[str]` — Tenant name override. Defaults to the caller's tenant when omitted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/truefoundry_sdk/users/client.py">activate</a>(...) -> ActivateUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Re-activate a previously deactivated user by email in the current tenant.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.users.activate(
    email="user@example.com",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` — Email of the user to activate.
    
</dd>
</dl>

<dl>
<dd>

**tenant_name:** `typing.Optional[str]` — Tenant name override. Defaults to the caller's tenant when omitted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/truefoundry_sdk/users/client.py">change_password</a>(...) -> ChangePasswordResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Change the password for the authenticated user.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.users.change_password(
    login_id="user@example.com",
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

**login_id:** `str` — Email address of the user changing their password.
    
</dd>
</dl>

<dl>
<dd>

**new_password:** `str` — New password (minimum 8 characters).
    
</dd>
</dl>

<dl>
<dd>

**old_password:** `str` — Current password of the user for verification.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.teams.<a href="src/truefoundry_sdk/teams/client.py">list</a>(...) -> ListTeamsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List teams accessible to the current user.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.teams.list(
    limit=10,
    offset=0,
    type=TeamsListRequestType.TEAM,
    role="manager",
    attributes=[
        "attributes"
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

**type:** `typing.Optional[TeamsListRequestType]` — Filter teams by type.
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[typing.Literal]` — Filter to teams where the caller holds this role. `manager` returns teams the caller can manage (team managers and admins).
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma-separated list of attributes to return (e.g. `id,teamName`). When provided, only the specified fields are fetched. `id` is always included.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/truefoundry_sdk/teams/client.py">create_or_update</a>(...) -> GetTeamResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new team or update an existing one using the provided TeamManifest. Matching is by name — if the name matches an existing team it is updated, otherwise a new one is created.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry, TeamManifest

client = TrueFoundry(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.teams.create_or_update(
    manifest=TeamManifest(
        name="name",
        members=[
            "members"
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

**manifest:** `TeamManifest` — The team manifest describing the team to create or update.
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` — When true, validate the request without persisting any changes.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/truefoundry_sdk/teams/client.py">list_members</a>(...) -> ListTeamMembersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List users who are members of a team.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.teams.list_members(
    id="jqfwg345gi25n5ju2yz5iz6m",
    limit=10,
    offset=0,
    filter="{\"type\":\"AND\",\"children\":[{\"column\":\"email\",\"op\":\"STRING_CONTAINS\",\"value\":\"@example.com\"}]}",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — System-generated team ID.
    
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

**filter:** `typing.Optional[str]` — JSON string: structured filter tree (AND/OR groups, column leaves on `email` and `userId`).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/truefoundry_sdk/teams/client.py">list_managers</a>(...) -> ListTeamManagersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List users who hold the team-manager role on a team.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.teams.list_managers(
    id="jqfwg345gi25n5ju2yz5iz6m",
    limit=10,
    offset=0,
    filter="{\"type\":\"AND\",\"children\":[{\"column\":\"email\",\"op\":\"STRING_CONTAINS\",\"value\":\"@example.com\"}]}",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — System-generated team ID.
    
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

**filter:** `typing.Optional[str]` — JSON string: structured filter tree (AND/OR groups, column leaves on `email` and `userId`).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/truefoundry_sdk/teams/client.py">get</a>(...) -> GetTeamResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single team by its ID.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.teams.get(
    id="jqfwg345gi25n5ju2yz5iz6m",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — System-generated team ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/truefoundry_sdk/teams/client.py">delete</a>(...) -> DeleteTeamResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete the team with the given ID. This action is irreversible.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.teams.delete(
    id="jqfwg345gi25n5ju2yz5iz6m",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — System-generated team ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/truefoundry_sdk/teams/client.py">get_permissions</a>(...) -> GetTeamPermissionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all role bindings associated with a team.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.teams.get_permissions(
    id="jqfwg345gi25n5ju2yz5iz6m",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — System-generated team ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## GatewayConfigs
<details><summary><code>client.gateway_configs.<a href="src/truefoundry_sdk/gateway_configs/client.py">get</a>(...) -> GatewayConfiguration</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the AI Gateway configuration for the given type.
</dd>
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
from truefoundry_sdk.gateway_configs import GatewayConfigsGetRequestType

client = TrueFoundry(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.gateway_configs.get(
    type=GatewayConfigsGetRequestType.GATEWAY_RATE_LIMITING_CONFIG,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `GatewayConfigsGetRequestType` — The type of gateway configuration to retrieve or delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.gateway_configs.<a href="src/truefoundry_sdk/gateway_configs/client.py">get_budget_usage</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the current budget usage for every budget rule configured in the tenant.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.gateway_configs.get_budget_usage()

```
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

## PersonalAccessTokens
<details><summary><code>client.personal_access_tokens.<a href="src/truefoundry_sdk/personal_access_tokens/client.py">list</a>(...) -> ListPersonalAccessTokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List personal access tokens created by the current user.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.personal_access_tokens.list(
    limit=10,
    offset=0,
    name_search_query="ci-token",
)

```
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

**name_search_query:** `typing.Optional[str]` — Return personal access tokens whose name contains this substring.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.personal_access_tokens.<a href="src/truefoundry_sdk/personal_access_tokens/client.py">create</a>(...) -> CreatePersonalAccessTokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new personal access token for the current user.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.personal_access_tokens.create(
    name="my-ci-token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name for the personal access token. Must be 3-36 characters, start with a lowercase letter, end with a lowercase alphanumeric character, and contain only lowercase letters, numbers, and hyphens.
    
</dd>
</dl>

<dl>
<dd>

**expiration_date:** `typing.Optional[str]` — Expiration date in ISO format. The token becomes invalid after this date.
    
</dd>
</dl>

<dl>
<dd>

**account_name:** `typing.Optional[str]` — Account name that owns this personal access token.
    
</dd>
</dl>

<dl>
<dd>

**team_name:** `typing.Optional[str]` — Team name that owns this personal access token.
    
</dd>
</dl>

<dl>
<dd>

**token_type:** `typing.Optional[CreatePersonalAccessTokenRequestTokenType]` — Format of the issued token. Leave empty to use the tenant override or platform default.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.personal_access_tokens.<a href="src/truefoundry_sdk/personal_access_tokens/client.py">revoke_all</a>(...) -> RevokeAllPersonalAccessTokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke all personal access tokens belonging to the user with the given email. Requires tenant admin.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.personal_access_tokens.revoke_all(
    email="alice@example.com",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` — Email of the user whose personal access tokens should be revoked.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.personal_access_tokens.<a href="src/truefoundry_sdk/personal_access_tokens/client.py">delete</a>(...) -> DeletePersonalAccessTokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete the personal access token with the given ID. This action is irreversible.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.personal_access_tokens.delete(
    id="jqfwg345gi25n5ju2yz5iz6m",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — System-generated service account ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.personal_access_tokens.<a href="src/truefoundry_sdk/personal_access_tokens/client.py">get</a>(...) -> GetOrCreatePersonalAccessTokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an existing personal access token by name. If none exists, a new one is created and returned with a fresh token.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.personal_access_tokens.get(
    name="name",
    team_name="teamName",
)

```
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

**team_name:** `typing.Optional[str]` — Team name that owns this PAT when a new PAT is created
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.virtual_accounts.<a href="src/truefoundry_sdk/virtual_accounts/client.py">list</a>(...) -> ListVirtualAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List virtual accounts accessible to the current user.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.virtual_accounts.list(
    limit=10,
    offset=0,
    name_search_query="staging-bot",
    owned_by_teams=[
        "ownedByTeams"
    ],
    is_expired=True,
    filter="{\"type\":\"AND\",\"children\":[{\"column\":\"name\",\"op\":\"STRING_CONTAINS\",\"value\":\"bot\"}]}",
)

```
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

**name_search_query:** `typing.Optional[str]` — Return virtual accounts with names that contain this string.
    
</dd>
</dl>

<dl>
<dd>

**owned_by_teams:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma-separated team names. Return virtual accounts owned by these teams.
    
</dd>
</dl>

<dl>
<dd>

**is_expired:** `typing.Optional[bool]` — Filter by expiration status. `true` = expired only, `false` = not expired only.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` — JSON string: structured filter tree (AND/OR groups, column leaves on `name`, json_map leaves on `manifest.tags`).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.virtual_accounts.<a href="src/truefoundry_sdk/virtual_accounts/client.py">create_or_update</a>(...) -> GetVirtualAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new virtual account or update an existing one using the provided VirtualAccountManifest. Matching is by name — if the name matches an existing virtual account it is updated, otherwise a new one is created.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry, VirtualAccountManifest, Permissions

client = TrueFoundry(
    api_key="<token>",
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

**manifest:** `VirtualAccountManifest` — The virtual account manifest describing the virtual account to create or update.
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` — When true, validate the request without persisting any changes.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.virtual_accounts.<a href="src/truefoundry_sdk/virtual_accounts/client.py">get</a>(...) -> GetVirtualAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single virtual account by its ID.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.virtual_accounts.get(
    id="jqfwg345gi25n5ju2yz5iz6m",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — System-generated service account ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.virtual_accounts.<a href="src/truefoundry_sdk/virtual_accounts/client.py">delete</a>(...) -> DeleteVirtualAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete the virtual account with the given ID. This action is irreversible.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.virtual_accounts.delete(
    id="jqfwg345gi25n5ju2yz5iz6m",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — System-generated service account ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.virtual_accounts.<a href="src/truefoundry_sdk/virtual_accounts/client.py">get_token</a>(...) -> GetTokenForVirtualAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the current authentication token for a virtual account by its ID.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.virtual_accounts.get_token(
    id="jqfwg345gi25n5ju2yz5iz6m",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — System-generated service account ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.virtual_accounts.<a href="src/truefoundry_sdk/virtual_accounts/client.py">sync_to_secret_store</a>(...) -> SyncVirtualAccountTokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sync the virtual account token to the configured secret store. Returns the sync metadata including timestamp and error (if any).
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.virtual_accounts.sync_to_secret_store(
    id="jqfwg345gi25n5ju2yz5iz6m",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — System-generated service account ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.virtual_accounts.<a href="src/truefoundry_sdk/virtual_accounts/client.py">regenerate_token</a>(...) -> GetTokenForVirtualAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Regenerate the authentication token for a virtual account. The old token remains valid for the specified grace period.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.virtual_accounts.regenerate_token(
    id="jqfwg345gi25n5ju2yz5iz6m",
    grace_period_in_days=30,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — System-generated service account ID.
    
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

Delete a specific JWT token belonging to a virtual account. The virtual account itself is not affected.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.virtual_accounts.delete_jwt(
    id="jqfwg345gi25n5ju2yz5iz6m",
    jwt_id="jwt_abc123def456",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — System-generated virtual account ID that owns the JWT.
    
</dd>
</dl>

<dl>
<dd>

**jwt_id:** `str` — System-generated JWT ID to delete.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.clusters.<a href="src/truefoundry_sdk/clusters/client.py">list</a>(...) -> ListClustersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List clusters the caller can read.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.clusters.list(
    limit=10,
    offset=0,
    attributes=[
        "attributes"
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

**attributes:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma-separated list of attributes to return (e.g. id,name). When provided, only the specified fields are fetched. `id` is always included.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clusters.<a href="src/truefoundry_sdk/clusters/client.py">create_or_update</a>(...) -> GetClusterResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new cluster or update an existing one using the provided `ClusterManifest`. Matching is by `name` — if a cluster with the same name exists it is updated, otherwise a new one is created.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry, ClusterManifest, ClusterManifestClusterType, Collaborator

client = TrueFoundry(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.clusters.create_or_update(
    manifest=ClusterManifest(
        name="name",
        cluster_type=ClusterManifestClusterType.AWS_EKS,
        environment_names=[
            "environment_names"
        ],
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

**manifest:** `ClusterManifest` — Full cluster manifest.
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` — When true, validates the request without persisting changes.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clusters.<a href="src/truefoundry_sdk/clusters/client.py">get</a>(...) -> GetClusterResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single cluster by its ID.
</dd>
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
    api_key="<token>",
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

**id:** `str` — Unique identifier of the cluster.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clusters.<a href="src/truefoundry_sdk/clusters/client.py">delete</a>(...) -> DeleteClusterResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete the cluster with the given ID. This action is irreversible.
</dd>
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
    api_key="<token>",
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

**id:** `str` — Unique identifier of the cluster.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clusters.<a href="src/truefoundry_sdk/clusters/client.py">get_addons</a>(...) -> ListClusterAddonsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List addons installed on the cluster.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.clusters.get_addons(
    id="id",
    limit=10,
    offset=0,
    attributes=[
        "attributes"
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

**id:** `str` — Unique identifier of the cluster.
    
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

**attributes:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma-separated list of attributes to return (e.g. id,name). When provided, only the specified fields are fetched. `id` is always included.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clusters.<a href="src/truefoundry_sdk/clusters/client.py">is_connected</a>(...) -> IsClusterConnectedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the connection status of the cluster agent to the control plane.
</dd>
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
    api_key="<token>",
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

**id:** `str` — Unique identifier of the cluster.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.applications.<a href="src/truefoundry_sdk/applications/client.py">list</a>(...) -> ListApplicationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List applications the caller can read.
</dd>
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
from truefoundry_sdk.applications import ApplicationsListRequestApplicationType, ApplicationsListRequestDeviceTypeFilter, ApplicationsListRequestLifecycleStage

client = TrueFoundry(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.applications.list(
    limit=10,
    offset=0,
    application_id="applicationId",
    workspace_id="workspaceId",
    application_name="applicationName",
    fqn="fqn",
    workspace_fqn="workspaceFqn",
    application_type=ApplicationsListRequestApplicationType.ASYNC_SERVICE,
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

```
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

**application_id:** `typing.Optional[str]` — Unique identifier of the application to filter by
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `typing.Optional[str]` — Workspace IDs to filter by (comma-separated)
    
</dd>
</dl>

<dl>
<dd>

**application_name:** `typing.Optional[str]` — Exact application name to filter by. Takes precedence over nameSearchQuery if both are provided.
    
</dd>
</dl>

<dl>
<dd>

**fqn:** `typing.Optional[str]` — FQN of the application to filter by.
    
</dd>
</dl>

<dl>
<dd>

**workspace_fqn:** `typing.Optional[str]` — FQN of the workspace to filter by.
    
</dd>
</dl>

<dl>
<dd>

**application_type:** `typing.Optional[ApplicationsListRequestApplicationType]` — Application type to filter by (comma-separated).
    
</dd>
</dl>

<dl>
<dd>

**name_search_query:** `typing.Optional[str]` — Substring search query for application name. Ignored if applicationName is also provided.
    
</dd>
</dl>

<dl>
<dd>

**environment_id:** `typing.Optional[str]` — Environment IDs to filter by (comma-separated)
    
</dd>
</dl>

<dl>
<dd>

**cluster_id:** `typing.Optional[str]` — Cluster IDs to filter by (comma-separated)
    
</dd>
</dl>

<dl>
<dd>

**application_set_id:** `typing.Optional[str]` — Application set ID to filter by
    
</dd>
</dl>

<dl>
<dd>

**paused:** `typing.Optional[bool]` — Filter by explicit pause state (true = paused, false = not paused). Does not account for autoshutdown.
    
</dd>
</dl>

<dl>
<dd>

**device_type_filter:** `typing.Optional[ApplicationsListRequestDeviceTypeFilter]` — Device type to filter by (comma-separated).
    
</dd>
</dl>

<dl>
<dd>

**last_deployed_by_subjects:** `typing.Optional[str]` — Subject slugs of last deployers to filter by (comma-separated). Email for users (e.g. user@example.com), name for virtual accounts.
    
</dd>
</dl>

<dl>
<dd>

**lifecycle_stage:** `typing.Optional[ApplicationsListRequestLifecycleStage]` — Application lifecycle stage to filter by
    
</dd>
</dl>

<dl>
<dd>

**is_recommendation_present_and_visible:** `typing.Optional[bool]` — Whether the application has visible recommendations
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.applications.<a href="src/truefoundry_sdk/applications/client.py">create_or_update</a>(...) -> GetApplicationDeploymentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deploy an application from a manifest. Create the application if it does not exist, otherwise create a new deployment version. Return the resulting deployment.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.applications.create_or_update(
    manifest={
        "key": "value"
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**manifest:** `typing.Dict[str, typing.Any]` — Manifest of application
    
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

<details><summary><code>client.applications.<a href="src/truefoundry_sdk/applications/client.py">get</a>(...) -> GetApplicationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single application by its ID.
</dd>
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
    api_key="<token>",
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

**id:** `str` — Unique identifier of the application
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.applications.<a href="src/truefoundry_sdk/applications/client.py">delete</a>(...) -> DeleteApplicationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete an application. This action cannot be undone.
</dd>
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
    api_key="<token>",
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

**id:** `str` — Unique identifier of the application
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.applications.<a href="src/truefoundry_sdk/applications/client.py">redeploy</a>(...) -> GetApplicationDeploymentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Redeploy an application by creating a new deployment version using the same manifest as the specified deployment.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.applications.redeploy(
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

**id:** `str` — Unique identifier of the application
    
</dd>
</dl>

<dl>
<dd>

**deployment_id:** `str` — Unique identifier of the deployment
    
</dd>
</dl>

<dl>
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

Pause a running application.
</dd>
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
    api_key="<token>",
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

**id:** `str` — Unique identifier of the application
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.applications.<a href="src/truefoundry_sdk/applications/client.py">scale_to_original</a>(...) -> Deployment</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resume a paused application.
</dd>
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
    api_key="<token>",
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

**id:** `str` — Unique identifier of the application
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.applications.<a href="src/truefoundry_sdk/applications/client.py">cancel_deployment</a>(...) -> ApplicationsCancelDeploymentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel an in-progress deployment.
</dd>
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
    api_key="<token>",
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

**id:** `str` — Unique identifier of the application
    
</dd>
</dl>

<dl>
<dd>

**deployment_id:** `str` — Unique identifier of the deployment
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.application_versions.<a href="src/truefoundry_sdk/application_versions/client.py">list</a>(...) -> ListApplicationDeploymentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List deployments for a given application. Each deployment is a new version of the application.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.application_versions.list(
    id="id",
    limit=10,
    offset=0,
    version="1",
    deployment_id="deployment123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the application
    
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

**version:** `typing.Optional[str]` — Deployment version to filter by
    
</dd>
</dl>

<dl>
<dd>

**deployment_id:** `typing.Optional[str]` — Deployment ID to filter by
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.application_versions.<a href="src/truefoundry_sdk/application_versions/client.py">get</a>(...) -> GetApplicationDeploymentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single deployment by application ID and deployment ID.
</dd>
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
    api_key="<token>",
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

**id:** `str` — Unique identifier of the application
    
</dd>
</dl>

<dl>
<dd>

**deployment_id:** `str` — Unique identifier of the deployment
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.jobs.<a href="src/truefoundry_sdk/jobs/client.py">list_runs</a>(...) -> ListJobRunResponse</code></summary>
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
from truefoundry_sdk import TrueFoundry, JobRunsSortBy, SortDirection, JobRunStatus

client = TrueFoundry(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.jobs.list_runs(
    job_id="jobId",
    limit=10,
    offset=0,
    search_prefix="searchPrefix",
    sort_by=JobRunsSortBy.START_TIME,
    order=SortDirection.ASC,
    triggered_by=[
        "triggeredBy"
    ],
    status=[
        JobRunStatus.CREATED
    ],
    version_numbers=[
        1.1
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

<details><summary><code>client.jobs.<a href="src/truefoundry_sdk/jobs/client.py">get_run</a>(...) -> GetJobRunResponse</code></summary>
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
    api_key="<token>",
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

<details><summary><code>client.jobs.<a href="src/truefoundry_sdk/jobs/client.py">delete_run</a>(...) -> DeleteJobRunResponse</code></summary>
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
    api_key="<token>",
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

<details><summary><code>client.jobs.<a href="src/truefoundry_sdk/jobs/client.py">trigger</a>(...) -> TriggerJobRunResponse</code></summary>
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
    api_key="<token>",
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

<details><summary><code>client.jobs.<a href="src/truefoundry_sdk/jobs/client.py">terminate</a>(...) -> TerminateJobResponse</code></summary>
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
    api_key="<token>",
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
<details><summary><code>client.workspaces.<a href="src/truefoundry_sdk/workspaces/client.py">list</a>(...) -> ListWorkspacesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List workspaces the caller can read.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.workspaces.list(
    limit=10,
    offset=0,
    cluster_id="jqfwg345gi25n5ju2yz5iz6m",
    name="name",
    fqn="fqn",
    include_cluster=True,
    attributes=[
        "attributes"
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

**cluster_id:** `typing.Optional[str]` — System-generated cluster ID to filter by.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter workspaces by exact name match.
    
</dd>
</dl>

<dl>
<dd>

**fqn:** `typing.Optional[str]` — Human-readable Fully Qualified Name to filter by.
    
</dd>
</dl>

<dl>
<dd>

**include_cluster:** `typing.Optional[bool]` — When true, each workspace in the response includes summary information about its cluster.
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma-separated list of attributes to return (e.g. id,name). When provided, only the specified fields are fetched. `id` is always included.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workspaces.<a href="src/truefoundry_sdk/workspaces/client.py">create_or_update</a>(...) -> GetWorkspaceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new workspace or update an existing one using the provided WorkspaceManifest. Matching is by name and cluster — if both match an existing workspace it is updated, otherwise a new one is created.
</dd>
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
    api_key="<token>",
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

**dry_run:** `typing.Optional[bool]` — When true, validates the request without persisting changes.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workspaces.<a href="src/truefoundry_sdk/workspaces/client.py">search</a>(...) -> ListWorkspacesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search workspaces using a structured filter expression. Return a paginated list of workspaces matching the filter criteria.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.workspaces.search(
    limit=10,
    offset=0,
    filter="[{\"type\":\"name\",\"operator\":\"STRING_CONTAINS\",\"value\":\"prod\"}]",
    include_cluster=True,
)

```
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

**filter:** `typing.Optional[str]` — JSON-encoded filter string for structured search. Supported fields: name, id, environmentId, cluster_fqn. Supported operators: STRING_CONTAINS, STRING_STARTS_WITH, STRING_ENDS_WITH, EQUAL, IN, NOT_IN, IS_NULL.
    
</dd>
</dl>

<dl>
<dd>

**include_cluster:** `typing.Optional[bool]` — When true, each workspace in the response includes summary information about its cluster.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workspaces.<a href="src/truefoundry_sdk/workspaces/client.py">get</a>(...) -> GetWorkspaceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single workspace by its ID.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.workspaces.get(
    id="jqfwg345gi25n5ju2yz5iz6m",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — System-generated workspace ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workspaces.<a href="src/truefoundry_sdk/workspaces/client.py">delete</a>(...) -> DeleteWorkspaceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete the workspace with the given ID. This action is irreversible.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.workspaces.delete(
    id="jqfwg345gi25n5ju2yz5iz6m",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — System-generated workspace ID.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.environments.<a href="src/truefoundry_sdk/environments/client.py">list</a>(...) -> ListEnvironmentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List environments the caller can read within the tenant.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.environments.list(
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

<details><summary><code>client.environments.<a href="src/truefoundry_sdk/environments/client.py">create_or_update</a>(...) -> GetEnvironmentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new environment or update an existing one using the provided `EnvironmentManifest`. Matching is by `name` — if an environment with the same name exists it is updated, otherwise a new one is created.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry, EnvironmentManifest, EnvironmentColor, EnvironmentOptimizeFor

client = TrueFoundry(
    api_key="<token>",
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

**manifest:** `EnvironmentManifest` — Environment manifest. The environment is matched by `name` for upsert.
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` — When true, validates the manifest without persisting changes.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/truefoundry_sdk/environments/client.py">get</a>(...) -> GetEnvironmentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single environment by its ID.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.environments.get(
    id="jqfwg345gi25n5ju2yz5iz6m",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — System-generated environment ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/truefoundry_sdk/environments/client.py">delete</a>(...) -> bool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete the environment with the given ID.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.environments.delete(
    id="jqfwg345gi25n5ju2yz5iz6m",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — System-generated environment ID.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.secrets.<a href="src/truefoundry_sdk/secrets/client.py">list</a>(...) -> ListSecretsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List secrets the caller has access to.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.secrets.list()

```
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

**secret_fqns:** `typing.Optional[typing.List[str]]` — Filter by secret FQNs.
    
</dd>
</dl>

<dl>
<dd>

**secret_group_id:** `typing.Optional[str]` — Filter by secret group ID.
    
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

<details><summary><code>client.secrets.<a href="src/truefoundry_sdk/secrets/client.py">get</a>(...) -> GetSecretResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the secret with the specified ID. The secret value is omitted if value viewing is disabled on the control plane.
</dd>
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
    api_key="<token>",
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

**id:** `str` — Unique identifier of the secret.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.secrets.<a href="src/truefoundry_sdk/secrets/client.py">delete</a>(...) -> float</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the secret and all its versions permanently.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.secrets.delete(
    id="id",
    force_delete=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the secret.
    
</dd>
</dl>

<dl>
<dd>

**force_delete:** `typing.Optional[bool]` — Whether to force delete the secret.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.secret_groups.<a href="src/truefoundry_sdk/secret_groups/client.py">list</a>(...) -> ListSecretGroupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List secret groups the caller has access to, along with associated secrets for each group. Secret values are not included in the response.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.secret_groups.list(
    limit=10,
    offset=0,
    fqn="fqn",
    search="search",
    attributes=[
        "attributes"
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

**attributes:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma-separated list of attributes to return (e.g. id,name). When provided, only the specified fields are fetched. `id` is always included.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.secret_groups.<a href="src/truefoundry_sdk/secret_groups/client.py">create</a>(...) -> GetSecretGroupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a secret group with initial secrets.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry, SecretInput

client = TrueFoundry(
    api_key="<token>",
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

**secrets:** `typing.List[SecretInput]` — The secrets to be associated with the secret group
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.secret_groups.<a href="src/truefoundry_sdk/secret_groups/client.py">create_or_update</a>(...) -> GetSecretGroupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new secret group or update an existing one using the provided manifest. Matching is by name.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry, SecretGroupManifest, Collaborator

client = TrueFoundry(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.secret_groups.create_or_update(
    manifest=SecretGroupManifest(
        name="name",
        integration_fqn="integration_fqn",
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

**manifest:** `SecretGroupManifest` — Secret Group Manifest
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` — Validate the manifest and collaborators without persisting or updating authorizations and secret groups
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.secret_groups.<a href="src/truefoundry_sdk/secret_groups/client.py">get</a>(...) -> GetSecretGroupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a secret group by ID.
</dd>
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
    api_key="<token>",
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

**id:** `str` — Unique identifier of the secret group.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.secret_groups.<a href="src/truefoundry_sdk/secret_groups/client.py">update</a>(...) -> GetSecretGroupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update secrets in a secret group. A new version is created for each secret with a modified value. Omitted secrets are deleted. Secret values are not returned in the response.
</dd>
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
    api_key="<token>",
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

**id:** `str` — Unique identifier of the secret group.
    
</dd>
</dl>

<dl>
<dd>

**secrets:** `typing.List[UpdateSecretInput]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.secret_groups.<a href="src/truefoundry_sdk/secret_groups/client.py">delete</a>(...) -> DeleteSecretGroupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the secret group and all its associated secrets and secret versions permanently.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.secret_groups.delete(
    id="id",
    force_delete=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the secret group.
    
</dd>
</dl>

<dl>
<dd>

**force_delete:** `typing.Optional[bool]` — Whether to force delete the secret group even when the associated secret integration is faulty or unavailable.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.events.<a href="src/truefoundry_sdk/events/client.py">get</a>(...) -> GetEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get events for an application, filtered by pod names, job run, or time range.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.events.get(
    start_ts="startTs",
    end_ts="endTs",
    application_id="applicationId",
    application_fqn="applicationFqn",
    pod_names=[
        "podNames"
    ],
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

**start_ts:** `typing.Optional[str]` — Start timestamp for filtering events (ISO 8601 format, UTC). Defaults to 24 hours before endTs. Must be less than or equal to endTs.
    
</dd>
</dl>

<dl>
<dd>

**end_ts:** `typing.Optional[str]` — End timestamp for filtering events (ISO 8601 format, UTC). Defaults to current time. Must be greater than or equal to startTs.
    
</dd>
</dl>

<dl>
<dd>

**application_id:** `typing.Optional[str]` — Unique identifier of the application. Either applicationId or applicationFqn must be provided.
    
</dd>
</dl>

<dl>
<dd>

**application_fqn:** `typing.Optional[str]` — Fully qualified name of the application. Either applicationId or applicationFqn must be provided.
    
</dd>
</dl>

<dl>
<dd>

**pod_names:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — List of Kubernetes pod names to filter events. Cannot be provided together with jobRunName.
    
</dd>
</dl>

<dl>
<dd>

**job_run_name:** `typing.Optional[str]` — Name of the TrueFoundry job run. Cannot be provided together with podNames.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.alerts.<a href="src/truefoundry_sdk/alerts/client.py">list</a>(...) -> GetAlertsResponse</code></summary>
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
from truefoundry_sdk import TrueFoundry, AlertStatus

client = TrueFoundry(
    api_key="<token>",
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

**start_ts:** `typing.Optional[str]` — Start timestamp for filtering alerts (ISO 8601 format, UTC). Must be before endTs.
    
</dd>
</dl>

<dl>
<dd>

**end_ts:** `typing.Optional[str]` — End timestamp for filtering alerts (ISO 8601 format, UTC). Must be after startTs.
    
</dd>
</dl>

<dl>
<dd>

**cluster_id:** `typing.Optional[str]` — Unique identifier of the cluster.
    
</dd>
</dl>

<dl>
<dd>

**application_id:** `typing.Optional[str]` — Unique identifier of the application.
    
</dd>
</dl>

<dl>
<dd>

**alert_status:** `typing.Optional[AlertStatus]` — Filter by alert status.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.prompts.<a href="src/truefoundry_sdk/prompts/client.py">get</a>(...) -> GetPromptResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a prompt by its ID.
</dd>
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
    api_key="<token>",
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

<details><summary><code>client.prompts.<a href="src/truefoundry_sdk/prompts/client.py">delete</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a prompt by its ID.
</dd>
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
    api_key="<token>",
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

<details><summary><code>client.prompts.<a href="src/truefoundry_sdk/prompts/client.py">list</a>(...) -> ListPromptsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List prompts with optional filtering by FQN, ML Repo, or name.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.prompts.list(
    limit=10,
    offset=0,
    fqn="fqn",
    ml_repo_id="ml_repo_id",
    name="name",
    include_empty_prompts=True,
)

```
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

**include_empty_prompts:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prompts.<a href="src/truefoundry_sdk/prompts/client.py">create_or_update</a>(...) -> GetPromptVersionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or update a prompt version.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry, ChatPromptManifest, SystemMessage

client = TrueFoundry(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.prompts.create_or_update(
    manifest=ChatPromptManifest(
        metadata={
            "key": "value"
        },
        messages=[
            SystemMessage(
                role="system",
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

**manifest:** `ChatPromptManifest` — Manifest containing metadata for the prompt version to apply
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.prompt_versions.<a href="src/truefoundry_sdk/prompt_versions/client.py">list</a>(...) -> ListPromptVersionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List prompt versions with optional filtering by tag, FQN, prompt ID, ML Repo, name, or version.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.prompt_versions.list(
    limit=10,
    offset=0,
    tag="tag",
    fqn="fqn",
    prompt_id="prompt_id",
    ml_repo_id="ml_repo_id",
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

**version:** `typing.Optional[Object]` — Version number (positive integer) or `latest`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prompt_versions.<a href="src/truefoundry_sdk/prompt_versions/client.py">apply_tags</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Apply tags to a prompt version.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.prompt_versions.apply_tags(
    prompt_version_id="prompt_version_id",
    tags=[
        "tags"
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

**prompt_version_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.List[str]` 
    
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

<details><summary><code>client.prompt_versions.<a href="src/truefoundry_sdk/prompt_versions/client.py">get</a>(...) -> GetPromptVersionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a prompt version by its ID.
</dd>
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
    api_key="<token>",
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

**id:** `str` — Prompt version ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prompt_versions.<a href="src/truefoundry_sdk/prompt_versions/client.py">delete</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a prompt version by its ID.
</dd>
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
    api_key="<token>",
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

**id:** `str` — Prompt version ID
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.artifacts.<a href="src/truefoundry_sdk/artifacts/client.py">get</a>(...) -> GetArtifactResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an artifact by its ID.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.artifacts.get(
    id="jqfwg345gi25n5ju2yz5iz6m",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — System-generated artifact ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artifacts.<a href="src/truefoundry_sdk/artifacts/client.py">delete</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an artifact by its ID.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.artifacts.delete(
    id="jqfwg345gi25n5ju2yz5iz6m",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — System-generated artifact ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artifacts.<a href="src/truefoundry_sdk/artifacts/client.py">list</a>(...) -> ListArtifactsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List artifacts with optional filtering by FQN, ML Repo, name, or run ID.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.artifacts.list(
    limit=10,
    offset=0,
    fqn="fqn",
    ml_repo_id="ml_repo_id",
    name="name",
    run_id="run_id",
    include_empty_artifacts=True,
)

```
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

**fqn:** `typing.Optional[str]` — Human-readable Fully Qualified Name of the artifact.
    
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

**run_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**include_empty_artifacts:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artifacts.<a href="src/truefoundry_sdk/artifacts/client.py">create_or_update</a>(...) -> GetArtifactVersionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or update an artifact version from a manifest.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry, ArtifactManifest, TrueFoundryManagedSource

client = TrueFoundry(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.artifacts.create_or_update(
    manifest=ArtifactManifest(
        metadata={
            "key": "value"
        },
        source=TrueFoundryManagedSource(),
        step=1,
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

**manifest:** `ApplyArtifactRequestManifest` — Manifest containing metadata for the artifact version to create or update
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.artifact_versions.<a href="src/truefoundry_sdk/artifact_versions/client.py">list</a>(...) -> ListArtifactVersionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List artifact versions with optional filtering by tag, FQN, artifact ID, ML Repo, name, version, run IDs, or run steps.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.artifact_versions.list(
    limit=10,
    offset=0,
    tag="tag",
    fqn="fqn",
    artifact_id="artifact_id",
    ml_repo_id="ml_repo_id",
    name="name",
    run_ids=[
        "run_ids"
    ],
    run_steps=[
        1.1
    ],
    include_internal_metadata=True,
)

```
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

**version:** `typing.Optional[Object]` 
    
</dd>
</dl>

<dl>
<dd>

**run_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**run_steps:** `typing.Optional[typing.Union[float, typing.Sequence[float]]]` 
    
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

<details><summary><code>client.artifact_versions.<a href="src/truefoundry_sdk/artifact_versions/client.py">apply_tags</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Apply tags to an artifact version.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.artifact_versions.apply_tags(
    artifact_version_id="artifact_version_id",
    tags=[
        "tags"
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

**artifact_version_id:** `str` — ID of the artifact version to apply tags to
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.List[str]` — List of tags to apply to the artifact version
    
</dd>
</dl>

<dl>
<dd>

**force:** `typing.Optional[bool]` — Whether to overwrite existing tags if they conflict
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artifact_versions.<a href="src/truefoundry_sdk/artifact_versions/client.py">get_signed_urls</a>(...) -> GetSignedUrLsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get pre-signed URLs for reading or writing files in an artifact version.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry, GetSignedUrLsRequestOperation

client = TrueFoundry(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.artifact_versions.get_signed_urls(
    id="id",
    paths=[
        "paths"
    ],
    operation=GetSignedUrLsRequestOperation.READ,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `GetSignedUrLsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artifact_versions.<a href="src/truefoundry_sdk/artifact_versions/client.py">create_multi_part_upload</a>(...) -> MultiPartUploadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a multipart upload for large files in an artifact version.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.artifact_versions.create_multi_part_upload(
    id="id",
    path="path",
    num_parts=1.1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateMultiPartUploadRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artifact_versions.<a href="src/truefoundry_sdk/artifact_versions/client.py">list_files</a>(...) -> ListFilesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List files and directories in an artifact version.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.artifact_versions.list_files(
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

**request:** `ListFilesRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artifact_versions.<a href="src/truefoundry_sdk/artifact_versions/client.py">stage</a>(...) -> StageArtifactResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stage an artifact version for upload, returning storage location and version ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry, ArtifactManifest, TrueFoundryManagedSource

client = TrueFoundry(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.artifact_versions.stage(
    manifest=ArtifactManifest(
        metadata={
            "key": "value"
        },
        source=TrueFoundryManagedSource(),
        step=1,
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

**manifest:** `StageArtifactRequestManifest` — Manifest containing metadata for the artifact to be staged (model or generic artifact)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artifact_versions.<a href="src/truefoundry_sdk/artifact_versions/client.py">mark_stage_failure</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mark a staged artifact version as failed.
</dd>
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
    api_key="<token>",
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

<details><summary><code>client.artifact_versions.<a href="src/truefoundry_sdk/artifact_versions/client.py">get</a>(...) -> GetArtifactVersionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an artifact version by its ID.
</dd>
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
    api_key="<token>",
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

**id:** `str` — Artifact version ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artifact_versions.<a href="src/truefoundry_sdk/artifact_versions/client.py">delete</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an artifact version by its ID.
</dd>
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
    api_key="<token>",
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

**id:** `str` — Artifact version ID
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.ml_repos.<a href="src/truefoundry_sdk/ml_repos/client.py">get</a>(...) -> GetMlRepoResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an ML Repo by its ID.
</dd>
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
    api_key="<token>",
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

**id:** `str` — ML Repo Id
    
</dd>
</dl>

<dl>
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

Delete an ML Repo by its ID.
</dd>
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
    api_key="<token>",
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

**id:** `str` — ML Repo Id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ml_repos.<a href="src/truefoundry_sdk/ml_repos/client.py">list</a>(...) -> ListMlReposResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List ML Repos with optional filtering by name.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.ml_repos.list(
    limit=10,
    offset=0,
    name="name",
    attributes=[
        "attributes"
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

**name:** `typing.Optional[str]` — ML Repo Name
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma-separated list of attributes to return (e.g. id,name). When provided, only the specified fields are fetched. `id` is always included.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ml_repos.<a href="src/truefoundry_sdk/ml_repos/client.py">create_or_update</a>(...) -> GetMlRepoResponse</code></summary>
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
from truefoundry_sdk import TrueFoundry, MlRepoManifest, Collaborator

client = TrueFoundry(
    api_key="<token>",
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

**dry_run:** `typing.Optional[bool]` — Validate the manifest and collaborators without persisting changes or updating artifact location in the database
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.data_directories.<a href="src/truefoundry_sdk/data_directories/client.py">list</a>(...) -> ListDataDirectoriesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List data directories with optional filtering by FQN, ML Repo, or name.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.data_directories.list(
    limit=10,
    offset=0,
    fqn="fqn",
    ml_repo_id="ml_repo_id",
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

**fqn:** `typing.Optional[str]` — Fully qualified name to filter by
    
</dd>
</dl>

<dl>
<dd>

**ml_repo_id:** `typing.Optional[str]` — ID of the ML Repo to filter by
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the data directory to filter by
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_directories.<a href="src/truefoundry_sdk/data_directories/client.py">create_or_update</a>(...) -> GetDataDirectoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or update a data directory.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry, DataDirectoryManifest, TrueFoundryManagedSource

client = TrueFoundry(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.data_directories.create_or_update(
    manifest=DataDirectoryManifest(
        name="name",
        ml_repo="ml_repo",
        metadata={
            "key": "value"
        },
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

**manifest:** `DataDirectoryManifest` — Manifest containing metadata for the data directory to apply
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_directories.<a href="src/truefoundry_sdk/data_directories/client.py">list_files</a>(...) -> ListFilesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List files and directories in a data directory.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.data_directories.list_files(
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

**request:** `ListFilesRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_directories.<a href="src/truefoundry_sdk/data_directories/client.py">delete_files</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete files from a data directory.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.data_directories.delete_files(
    id="id",
    paths=[
        "paths"
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

**id:** `str` — ID of the data directory
    
</dd>
</dl>

<dl>
<dd>

**paths:** `typing.List[str]` — Paths of files to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_directories.<a href="src/truefoundry_sdk/data_directories/client.py">create_multipart_upload</a>(...) -> MultiPartUploadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a multipart upload for large files in a data directory.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.data_directories.create_multipart_upload(
    id="id",
    path="path",
    num_parts=1.1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateMultiPartUploadRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_directories.<a href="src/truefoundry_sdk/data_directories/client.py">get_signed_urls</a>(...) -> GetSignedUrLsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get pre-signed URLs for reading or writing files in a data directory.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry, GetSignedUrLsRequestOperation

client = TrueFoundry(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.data_directories.get_signed_urls(
    id="id",
    paths=[
        "paths"
    ],
    operation=GetSignedUrLsRequestOperation.READ,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `GetSignedUrLsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_directories.<a href="src/truefoundry_sdk/data_directories/client.py">get</a>(...) -> GetDataDirectoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a data directory by its ID.
</dd>
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
    api_key="<token>",
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

**id:** `str` — Data directory ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_directories.<a href="src/truefoundry_sdk/data_directories/client.py">delete</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a data directory, optionally including its contents.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.data_directories.delete(
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

**id:** `str` — Data directory ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Runs
<details><summary><code>client.runs.<a href="src/truefoundry_sdk/runs/client.py">create</a>(...) -> CreateRunResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new run within an ML Repo.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.runs.create(
    experiment_id="experiment_id",
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

**experiment_id:** `str` — System-generated unique identifier for the ML Repo.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable name of the run.
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[float]` — Unix timestamp in milliseconds when the run started. Defaults to the current time.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[RunTagInput]]` — Initial tags to set on the run.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the run.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.runs.<a href="src/truefoundry_sdk/runs/client.py">get_columns</a>(...) -> GetRunColumnsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List distinct metric, parameter, and tag keys for runs in an ML Repo.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.runs.get_columns(
    experiment_id="experiment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**experiment_id:** `str` — System-generated unique identifier for the ML Repo.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.runs.<a href="src/truefoundry_sdk/runs/client.py">get</a>(...) -> GetRunResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get metadata, metrics, params, and tags for a run.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.runs.get(
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

**id:** `str` — System-generated unique identifier for the run.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.runs.<a href="src/truefoundry_sdk/runs/client.py">update</a>(...) -> UpdateRunResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update run status, end time, or description.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.runs.update(
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

**id:** `str` — System-generated unique identifier for the run.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — Updated status of the run (e.g. RUNNING, FINISHED, FAILED).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[float]` — Unix timestamp in milliseconds when the run ended.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Updated description of the run.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.runs.<a href="src/truefoundry_sdk/runs/client.py">delete</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete a run and its metadata.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.runs.delete(
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

**id:** `str` — System-generated unique identifier for the run.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.runs.<a href="src/truefoundry_sdk/runs/client.py">search</a>(...) -> SearchRunsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search runs across ML Repos with optional filters.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.runs.search()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**experiment_ids:** `typing.Optional[typing.List[str]]` — List of ML Repo experiment IDs to search over.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` — Filter expression over params, metrics, and tags. Supports SQL-like comparisons (e.g. metrics.rmse < 1 and params.model_class = "LogisticRegression").
    
</dd>
</dl>

<dl>
<dd>

**run_view_type:** `typing.Optional[str]` — Whether to return active only, deleted only, or all runs.
    
</dd>
</dl>

<dl>
<dd>

**max_results:** `typing.Optional[float]` — Maximum number of runs to return.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[typing.List[str]]` — Sort order for results (e.g. metrics.accuracy DESC, params.lr ASC).
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Token for fetching the next page of results.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[float]` — Zero-based offset for pagination.
    
</dd>
</dl>

<dl>
<dd>

**fqn:** `typing.Optional[str]` — Exact FQN lookup.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Run name lookup within experiment.
    
</dd>
</dl>

<dl>
<dd>

**experiment_id:** `typing.Optional[str]` — System-generated unique identifier for the ML Repo.
    
</dd>
</dl>

<dl>
<dd>

**ml_repo_name:** `typing.Optional[str]` — ML Repo name when resolving by run name.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.runs.<a href="src/truefoundry_sdk/runs/client.py">archive</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Soft-delete a run.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.runs.archive(
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

**id:** `str` — System-generated unique identifier for the run.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.runs.<a href="src/truefoundry_sdk/runs/client.py">restore</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restore an archived run.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.runs.restore(
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

**id:** `str` — System-generated unique identifier for the run.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.runs.<a href="src/truefoundry_sdk/runs/client.py">get_metric_history</a>(...) -> GetMetricHistoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get full time-series history for a metric key on a run.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.runs.get_metric_history(
    id="id",
    metric_key="metric_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — System-generated unique identifier for the run.
    
</dd>
</dl>

<dl>
<dd>

**metric_key:** `str` — Metric key (may contain slashes).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.runs.<a href="src/truefoundry_sdk/runs/client.py">list_metric_history</a>(...) -> ListMetricHistoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List metric histories for a run, optionally filtered by keys and step.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.runs.list_metric_history(
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

**id:** `str` — System-generated unique identifier for the run.
    
</dd>
</dl>

<dl>
<dd>

**metric_keys:** `typing.Optional[typing.List[str]]` — Metric keys to filter by. When omitted, returns all metric keys for the run.
    
</dd>
</dl>

<dl>
<dd>

**step:** `typing.Optional[float]` — Training step to filter metric history by.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.runs.<a href="src/truefoundry_sdk/runs/client.py">log_metric</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Log a metric for a run.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.runs.log_metric(
    id="id",
    key="key",
    value=1.1,
    timestamp=1.1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — System-generated unique identifier for the run.
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Name of the metric.
    
</dd>
</dl>

<dl>
<dd>

**value:** `float` — Numeric value of the metric.
    
</dd>
</dl>

<dl>
<dd>

**timestamp:** `float` — Unix timestamp in milliseconds when the metric was logged.
    
</dd>
</dl>

<dl>
<dd>

**step:** `typing.Optional[float]` — Training step at which to log the metric.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.runs.<a href="src/truefoundry_sdk/runs/client.py">log_parameter</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Log a parameter for a run.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.runs.log_parameter(
    id="id",
    key="key",
    value="value",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — System-generated unique identifier for the run.
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Name of the parameter.
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` — String value of the parameter.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.runs.<a href="src/truefoundry_sdk/runs/client.py">set_tag</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set a tag on a run.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.runs.set_tag(
    id="id",
    key="key",
    value="value",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — System-generated unique identifier for the run.
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Name of the tag.
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` — String value of the tag.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.runs.<a href="src/truefoundry_sdk/runs/client.py">delete_tag</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a tag from a run.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.runs.delete_tag(
    id="id",
    key="key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — System-generated unique identifier for the run.
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Name of the tag to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.runs.<a href="src/truefoundry_sdk/runs/client.py">log_batch</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Log a batch of metrics, params, and tags for a run.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.runs.log_batch(
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

**id:** `str` — System-generated unique identifier for the run.
    
</dd>
</dl>

<dl>
<dd>

**metrics:** `typing.Optional[typing.List[Metric]]` — Metrics to log for the run.
    
</dd>
</dl>

<dl>
<dd>

**params:** `typing.Optional[typing.List[RunParam]]` — Parameters to log for the run.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[RunTag]]` — Tags to set on the run.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.models.<a href="src/truefoundry_sdk/models/client.py">get</a>(...) -> GetModelResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a model by its ID.
</dd>
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
    api_key="<token>",
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

<details><summary><code>client.models.<a href="src/truefoundry_sdk/models/client.py">delete</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a model by its ID.
</dd>
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
    api_key="<token>",
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

<details><summary><code>client.models.<a href="src/truefoundry_sdk/models/client.py">list</a>(...) -> ListModelsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List models with optional filtering by FQN, ML Repo, name, or run ID.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.models.list(
    limit=10,
    offset=0,
    fqn="fqn",
    ml_repo_id="ml_repo_id",
    name="name",
    run_id="run_id",
    include_empty_models=True,
)

```
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

**run_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**include_empty_models:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.models.<a href="src/truefoundry_sdk/models/client.py">create_or_update</a>(...) -> GetModelVersionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or update a model version.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry, ModelManifest, TrueFoundryManagedSource

client = TrueFoundry(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.models.create_or_update(
    manifest=ModelManifest(
        metadata={
            "key": "value"
        },
        source=TrueFoundryManagedSource(),
        step=1,
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

**manifest:** `ModelManifest` — Manifest containing metadata for the model to apply
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.model_versions.<a href="src/truefoundry_sdk/model_versions/client.py">list</a>(...) -> ListModelVersionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List model versions with optional filtering by tag, FQN, model ID, ML Repo, name, version, run IDs, or run steps.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.model_versions.list(
    limit=10,
    offset=0,
    tag="tag",
    fqn="fqn",
    model_id="model_id",
    ml_repo_id="ml_repo_id",
    name="name",
    run_ids=[
        "run_ids"
    ],
    run_steps=[
        1.1
    ],
    include_internal_metadata=True,
)

```
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

**version:** `typing.Optional[Object]` — Version number (positive integer) or `latest`
    
</dd>
</dl>

<dl>
<dd>

**run_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**run_steps:** `typing.Optional[typing.Union[float, typing.Sequence[float]]]` 
    
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

<details><summary><code>client.model_versions.<a href="src/truefoundry_sdk/model_versions/client.py">apply_tags</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Apply tags to a model version.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.model_versions.apply_tags(
    model_version_id="model_version_id",
    tags=[
        "tags"
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

**model_version_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.List[str]` 
    
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

<details><summary><code>client.model_versions.<a href="src/truefoundry_sdk/model_versions/client.py">get</a>(...) -> GetModelVersionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a model version by its ID.
</dd>
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
    api_key="<token>",
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

**id:** `str` — Model version ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.model_versions.<a href="src/truefoundry_sdk/model_versions/client.py">delete</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a model version by its ID.
</dd>
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
    api_key="<token>",
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

**id:** `str` — Model version ID
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.logs.<a href="src/truefoundry_sdk/logs/client.py">get</a>(...) -> GetLogsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get runtime logs (stdout/stderr) emitted by the pods of a deployed application.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry, LogsSortingDirection, LogsSearchFilterType, LogsSearchOperatorType

client = TrueFoundry(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.logs.get(
    start_ts="1779262323000000000",
    end_ts="1779348723000000000",
    limit=1,
    direction=LogsSortingDirection.ASC,
    num_logs_to_ignore=1,
    application_id="applicationId",
    application_fqn="applicationFqn",
    deployment_id="deploymentId",
    job_run_name="jobRunName",
    pod_name="podName",
    container_name="containerName",
    pod_names=[
        "podNames"
    ],
    pod_names_regex="podNamesRegex",
    search_filters="[{\"string\":\"error\",\"type\":\"substring\",\"operator\":\"equal\"}]",
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

**start_ts:** `typing.Optional[str]` — Start timestamp for querying logs, in nanoseconds from the Unix epoch.
    
</dd>
</dl>

<dl>
<dd>

**end_ts:** `typing.Optional[str]` — End timestamp for querying logs, in nanoseconds from the Unix epoch.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of log lines to fetch.
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[LogsSortingDirection]` — Direction of sorting logs by timestamp.
    
</dd>
</dl>

<dl>
<dd>

**num_logs_to_ignore:** `typing.Optional[int]` — Number of log lines at the start timestamp to skip.
    
</dd>
</dl>

<dl>
<dd>

**application_id:** `typing.Optional[str]` — Unique identifier of the application. Either applicationId or applicationFqn must be provided.
    
</dd>
</dl>

<dl>
<dd>

**application_fqn:** `typing.Optional[str]` — FQN of the application. Either applicationId or applicationFqn must be provided.
    
</dd>
</dl>

<dl>
<dd>

**deployment_id:** `typing.Optional[str]` — Unique identifier of the deployment.
    
</dd>
</dl>

<dl>
<dd>

**job_run_name:** `typing.Optional[str]` — Name of the job run whose logs to fetch.
    
</dd>
</dl>

<dl>
<dd>

**pod_name:** `typing.Optional[str]` — Name of a single pod whose logs to fetch. Cannot be used together with podNames or podNamesRegex.
    
</dd>
</dl>

<dl>
<dd>

**container_name:** `typing.Optional[str]` — Name of the container whose logs to fetch.
    
</dd>
</dl>

<dl>
<dd>

**pod_names:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — List of pod names whose logs to fetch. Cannot be used together with podName or podNamesRegex.
    
</dd>
</dl>

<dl>
<dd>

**pod_names_regex:** `typing.Optional[str]` — Regex pattern matching pod names whose logs to fetch. Cannot be used together with podName or podNames.
    
</dd>
</dl>

<dl>
<dd>

**search_filters:** `typing.Optional[str]` — JSON-encoded array of search filters; each item is `{ string, type, operator }`. Takes precedence over `searchString` when provided.
    
</dd>
</dl>

<dl>
<dd>

**search_string:** `typing.Optional[str]` — Substring or regex to match against log content. Used when `searchFilters` is not provided.
    
</dd>
</dl>

<dl>
<dd>

**search_type:** `typing.Optional[LogsSearchFilterType]` — How `searchString` should be matched against log content.
    
</dd>
</dl>

<dl>
<dd>

**search_operator:** `typing.Optional[LogsSearchOperatorType]` — Comparison operator applied to the `searchString` match.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AgentSkills
<details><summary><code>client.agent_skills.<a href="src/truefoundry_sdk/agent_skills/client.py">get</a>(...) -> GetAgentSkillResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an agent skill by its ID.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.agent_skills.get(
    agent_skill_id="agent_skill_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_skill_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent_skills.<a href="src/truefoundry_sdk/agent_skills/client.py">delete</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an agent skill by its ID.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.agent_skills.delete(
    agent_skill_id="agent_skill_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_skill_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent_skills.<a href="src/truefoundry_sdk/agent_skills/client.py">list</a>(...) -> ListAgentSkillsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List agent skills with optional filtering by FQN, ML Repo, or name.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.agent_skills.list(
    limit=10,
    offset=0,
    fqn="fqn",
    ml_repo_id="ml_repo_id",
    name="name",
    include_empty_agent_skills=True,
)

```
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

**include_empty_agent_skills:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent_skills.<a href="src/truefoundry_sdk/agent_skills/client.py">create_or_update</a>(...) -> GetAgentSkillVersionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or update an agent skill version.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry, AgentSkillManifest, AgentSkillSourceInline

client = TrueFoundry(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.agent_skills.create_or_update(
    manifest=AgentSkillManifest(
        name="name",
        metadata={
            "key": "value"
        },
        ml_repo="ml_repo",
        source=AgentSkillSourceInline(
            skill_md="skill_md",
        ),
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

**manifest:** `AgentSkillManifest` — Manifest containing metadata for the agent skill to apply
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AgentSkillVersions
<details><summary><code>client.agent_skill_versions.<a href="src/truefoundry_sdk/agent_skill_versions/client.py">list</a>(...) -> ListAgentSkillVersionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List agent skill versions with optional filtering by FQN, agent skill ID, ML Repo, name, or version.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.agent_skill_versions.list(
    limit=10,
    offset=0,
    fqn="fqn",
    agent_skill_id="agent_skill_id",
    ml_repo_id="ml_repo_id",
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

**fqn:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**agent_skill_id:** `typing.Optional[str]` 
    
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

**version:** `typing.Optional[Object]` — Version number (positive integer) or `latest`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent_skill_versions.<a href="src/truefoundry_sdk/agent_skill_versions/client.py">get</a>(...) -> GetAgentSkillVersionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an agent skill version by its ID.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.agent_skill_versions.get(
    agent_skill_version_id="agent_skill_version_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_skill_version_id:** `str` — Agent skill version ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent_skill_versions.<a href="src/truefoundry_sdk/agent_skill_versions/client.py">delete</a>(...) -> EmptyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an agent skill version by its ID.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.agent_skill_versions.delete(
    agent_skill_version_id="agent_skill_version_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_skill_version_id:** `str` — Agent skill version ID
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.traces.<a href="src/truefoundry_sdk/traces/client.py">query_spans</a>(...) -> QuerySpansResponse</code></summary>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.traces.query_spans(
    start_time="startTime",
)

```
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

**end_time:** `typing.Optional[str]` — End time in ISO 8601 format (e.g., 2025-03-12T00:10:00.000Z). Defaults to current time if not provided.
    
</dd>
</dl>

<dl>
<dd>

**trace_ids:** `typing.Optional[typing.List[str]]` — Array of trace IDs to filter by
    
</dd>
</dl>

<dl>
<dd>

**span_ids:** `typing.Optional[typing.List[str]]` — Array of span IDs to filter by
    
</dd>
</dl>

<dl>
<dd>

**parent_span_ids:** `typing.Optional[typing.List[str]]` — Array of parent span IDs to filter by
    
</dd>
</dl>

<dl>
<dd>

**created_by_subject_types:** `typing.Optional[typing.List[SubjectType]]` — Array of subject types to filter by
    
</dd>
</dl>

<dl>
<dd>

**created_by_subject_slugs:** `typing.Optional[typing.List[str]]` — Array of subject slugs to filter by
    
</dd>
</dl>

<dl>
<dd>

**application_names:** `typing.Optional[typing.List[str]]` — Array of application names to filter by
    
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

**tracing_project_fqn:** `typing.Optional[str]` — Tracing project FQN (e.g., truefoundry:tracing-project:tfy-default)
    
</dd>
</dl>

<dl>
<dd>

**data_routing_destination:** `typing.Optional[str]` — Data Routing Destination. One of tracingProjectFqn or dataRoutingDestination is required.
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[typing.List[QuerySpansRequestFiltersItem]]` — Array of filters
    
</dd>
</dl>

<dl>
<dd>

**include_feedbacks:** `typing.Optional[bool]` — When true, feedback data is included in the response. When false, feedback data is excluded (returns empty array).
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.internal.clusters.<a href="src/truefoundry_sdk/internal/clusters/client.py">get_autoprovisioning_state</a>(...) -> GetAutoProvisioningStateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the auto-provisioning status for the specified cluster.
</dd>
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
    api_key="<token>",
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

**id:** `str` — Unique identifier of the cluster.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.internal.deployments.<a href="src/truefoundry_sdk/internal/deployments/client.py">get_deployment_statuses</a>(...) -> typing.List[DeploymentStatus]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all statuses for a specific deployment of an application.
</dd>
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
    api_key="<token>",
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

**id:** `str` — Unique identifier of the application
    
</dd>
</dl>

<dl>
<dd>

**deployment_id:** `str` — Unique identifier of the deployment
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.internal.deployments.<a href="src/truefoundry_sdk/internal/deployments/client.py">get_builds</a>(...) -> typing.List[DeploymentBuild]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all builds associated with a specific deployment of an application.
</dd>
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
    api_key="<token>",
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

**id:** `str` — Unique identifier of the application
    
</dd>
</dl>

<dl>
<dd>

**deployment_id:** `str` — Unique identifier of the deployment
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.internal.deployments.<a href="src/truefoundry_sdk/internal/deployments/client.py">get_code_upload_url</a>(...) -> PresignedUrlObject</code></summary>
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
    api_key="<token>",
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

<details><summary><code>client.internal.deployments.<a href="src/truefoundry_sdk/internal/deployments/client.py">get_suggested_endpoint</a>(...) -> GetSuggestedDeploymentEndpointResponse</code></summary>
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
from truefoundry_sdk import TrueFoundry, ApplicationType

client = TrueFoundry(
    api_key="<token>",
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
    api_key="<token>",
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

**id:** `str` — Unique identifier of the application
    
</dd>
</dl>

<dl>
<dd>

**full:** `typing.Optional[bool]` — Whether to promote the rollout to full traffic
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.internal.applications.<a href="src/truefoundry_sdk/internal/applications/client.py">get_pod_template_hash_to_deployment_version</a>(...) -> typing.Dict[str, float]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the pod template hash to deployment version map for a specific application.
</dd>
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
    api_key="<token>",
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

**id:** `str` — Unique identifier of the application
    
</dd>
</dl>

<dl>
<dd>

**pod_template_hashes:** `typing.Optional[str]` — Pod template hashes to filter by (comma-separated)
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.internal.metrics.<a href="src/truefoundry_sdk/internal/metrics/client.py">get_charts</a>(...) -> GetChartsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List metric charts available for an application.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.internal.metrics.get_charts(
    workspace_id="workspaceId",
    application_id="applicationId",
    start_ts="startTs",
    end_ts="endTs",
    filter_entity=MetricsGetChartsRequestFilterEntity.APPLICATION,
    filter_query="{\"pod\":\"my-app-abc123-xyz\"}",
)

```
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

**application_id:** `str` — Unique identifier of the application.
    
</dd>
</dl>

<dl>
<dd>

**filter_entity:** `MetricsGetChartsRequestFilterEntity` — Scope of the chart bundle to return.
    
</dd>
</dl>

<dl>
<dd>

**start_ts:** `typing.Optional[str]` — Start timestamp in milliseconds since epoch. Defaults to the application's last deployment creation time.
    
</dd>
</dl>

<dl>
<dd>

**end_ts:** `typing.Optional[str]` — End timestamp in milliseconds since epoch. Defaults to the current time.
    
</dd>
</dl>

<dl>
<dd>

**filter_query:** `typing.Optional[str]` — JSON-encoded filter required by certain scopes.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.internal.vcs.<a href="src/truefoundry_sdk/internal/vcs/client.py">get_repository_details</a>(...) -> GitRepositoryExistsResponse</code></summary>
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
    api_key="<token>",
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

<details><summary><code>client.internal.vcs.<a href="src/truefoundry_sdk/internal/vcs/client.py">get_authenticated_url</a>(...) -> GetAuthenticatedVcsurlResponse</code></summary>
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
    api_key="<token>",
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

## Internal ArtifactVersions
<details><summary><code>client.internal.artifact_versions.<a href="src/truefoundry_sdk/internal/artifact_versions/client.py">list</a>(...) -> InternalListArtifactVersionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List artifact versions with internal metadata, optionally including model versions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from truefoundry_sdk import TrueFoundry, ArtifactType

client = TrueFoundry(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.internal.artifact_versions.list(
    limit=10,
    offset=0,
    tag="tag",
    fqn="fqn",
    artifact_id="artifact_id",
    ml_repo_id="ml_repo_id",
    name="name",
    run_ids=[
        "run_ids"
    ],
    run_steps=[
        1.1
    ],
    include_internal_metadata=True,
    include_model_versions=True,
    artifact_types=[
        ArtifactType.ARTIFACT
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

**version:** `typing.Optional[Object]` 
    
</dd>
</dl>

<dl>
<dd>

**run_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**run_steps:** `typing.Optional[typing.Union[float, typing.Sequence[float]]]` 
    
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

**artifact_types:** `typing.Optional[typing.Union[ArtifactType, typing.Sequence[ArtifactType]]]` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.internal.docker_registries.<a href="src/truefoundry_sdk/internal/docker_registries/client.py">create_repository</a>(...) -> CreateDockerRepositoryResponse</code></summary>
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
    api_key="<token>",
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

<details><summary><code>client.internal.docker_registries.<a href="src/truefoundry_sdk/internal/docker_registries/client.py">get_credentials</a>(...) -> GetDockerRegistryCredentialsResponse</code></summary>
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
    api_key="<token>",
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
<details><summary><code>client.internal.workflows.<a href="src/truefoundry_sdk/internal/workflows/client.py">execute_workflow</a>(...) -> WorkflowsExecuteWorkflowResponse</code></summary>
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
    api_key="<token>",
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

**inputs:** `typing.Optional[typing.Dict[str, typing.Any]]` — Workflow inputs
    
</dd>
</dl>

<dl>
<dd>

**inputs_literal_map:** `typing.Optional[typing.Dict[str, typing.Any]]` — Workflow inputs literal map
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Internal BuildLogs
<details><summary><code>client.internal.build_logs.<a href="src/truefoundry_sdk/internal/build_logs/client.py">get</a>(...) -> LogsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get logs emitted by the image build and deploy pipeline for a specific build of an application.
</dd>
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
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.internal.build_logs.get(
    pipeline_run_name="pipelineRunName",
    start_ts="1635467890123456789",
    end_ts="1635467891123456789",
    limit="limit",
    direction="direction",
    filter_query="{\"matchString\":\"error\",\"type\":\"substring\",\"operator\":\"equal\"}",
    num_logs_to_ignore=1.1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pipeline_run_name:** `str` — PipelineRun Name
    
</dd>
</dl>

<dl>
<dd>

**start_ts:** `typing.Optional[str]` — Start timestamp for querying logs, in nanoseconds from the Unix epoch.
    
</dd>
</dl>

<dl>
<dd>

**end_ts:** `typing.Optional[str]` — End timestamp for querying logs, in nanoseconds from the Unix epoch.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[str]` — Max number of log lines to fetch
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[str]` — Direction of sorting logs. Can be `asc` or `desc`
    
</dd>
</dl>

<dl>
<dd>

**filter_query:** `typing.Optional[str]` — JSON-encoded filter object with shape `{ matchString, type, operator }`. `type` is `regex` or `substring`; `operator` is `equal` or `not_equal`.
    
</dd>
</dl>

<dl>
<dd>

**num_logs_to_ignore:** `typing.Optional[float]` — Number of logs corresponding to the starting timestamp to be ignored.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

