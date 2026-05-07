# Nitrozen Python SDK

Official Python client for the [Nitrozen.io](https://nitrozen.io) changelog API.

[![PyPI](https://img.shields.io/badge/pypi-v1.0.0-blue?logo=pypi&logoColor=white)](https://pypi.org/project/nitrozenio/)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue?logo=python&logoColor=white)](https://pypi.org/project/nitrozenio/)
[![GitHub](https://img.shields.io/badge/github-nitrozenio%2Fnitrozen--python-blue?logo=github)](https://github.com/nitrozenio/nitrozen-python)

## Requirements

Python 3.9+

## Installation

```sh
pip install nitrozenio
```

## Quick Start

```python
import nitrozenio
from nitrozenio.api.projects_api import ProjectsApi
from nitrozenio.api.entries_api import EntriesApi

# Configure with your API token
configuration = nitrozenio.Configuration(
    host="https://nitrozen.io/api/v1",
    access_token="YOUR_API_TOKEN",
)

with nitrozenio.ApiClient(configuration) as client:
    # List your projects
    projects_api = ProjectsApi(client)
    response = projects_api.projects_get()
    for project in response.data:
        print(f"{project.id}  {project.name}  ({project.slug})")

    # Create a changelog entry
    entries_api = EntriesApi(client)
    entry = entries_api.projects_project_entries_post(
        project=response.data[0].id,
        entry_input=nitrozenio.EntryInput(
            title="New feature",
            content="We shipped something great.",
            category="new",
        ),
    )
    print(entry.data.title)
```

## Authentication

Create an API token on the [API Tokens](https://nitrozen.io/api-tokens) page, then pass it via `access_token` in the configuration:

```python
configuration = nitrozenio.Configuration(
    host="https://nitrozen.io/api/v1",
    access_token="YOUR_API_TOKEN",
)
```

## Error Handling

API errors raise `ApiException`, which carries the HTTP status code and response body:

```python
from nitrozenio.exceptions import ApiException

try:
    response = projects_api.projects_project_get(project=999)
except ApiException as e:
    print(e.status)   # e.g. 404
    print(e.reason)   # e.g. "Not Found"
    print(e.body)     # raw JSON error body
```

## Pagination

List endpoints accept `page` and `per_page` parameters and return a `meta` object:

```python
response = entries_api.projects_project_entries_get(
    project=project_id,
    page=2,
    per_page=20,
)
print(f"page {response.meta.current_page} of {response.meta.last_page} ({response.meta.total} total)")
for entry in response.data:
    print(f"{entry.id}  {entry.title}")
```

## API Reference

All URIs are relative to `https://nitrozen.io/api/v1`.

### Authentication

| Method | HTTP | Description |
|--------|------|-------------|
| `AuthenticationApi.tokens_get()` | GET /tokens | List API tokens |
| `AuthenticationApi.tokens_post(body)` | POST /tokens | Create an API token |
| `AuthenticationApi.tokens_token_delete(id)` | DELETE /tokens/{token} | Revoke an API token |

### Projects

| Method | HTTP | Description |
|--------|------|-------------|
| `ProjectsApi.projects_get()` | GET /projects | List projects |
| `ProjectsApi.projects_post(body)` | POST /projects | Create a project |
| `ProjectsApi.projects_project_get(id)` | GET /projects/{project} | Get a project |
| `ProjectsApi.projects_project_put(id, body)` | PUT /projects/{project} | Update a project |
| `ProjectsApi.projects_project_delete(id)` | DELETE /projects/{project} | Delete a project |

### Entries

| Method | HTTP | Description |
|--------|------|-------------|
| `EntriesApi.projects_project_entries_get(id, page?, per_page?)` | GET /projects/{project}/entries | List entries |
| `EntriesApi.projects_project_entries_post(id, body)` | POST /projects/{project}/entries | Create an entry |
| `EntriesApi.projects_project_entries_entry_get(pid, eid)` | GET …/entries/{entry} | Get an entry |
| `EntriesApi.projects_project_entries_entry_put(pid, eid, body)` | PUT …/entries/{entry} | Update an entry |
| `EntriesApi.projects_project_entries_entry_delete(pid, eid)` | DELETE …/entries/{entry} | Delete an entry |

### Users

| Method | HTTP | Description |
|--------|------|-------------|
| `UsersApi.user_get()` | GET /user | Get current user |
| `UsersApi.user_usage_get()` | GET /user/usage | Get usage statistics |

### Public

| Method | HTTP | Description |
|--------|------|-------------|
| `PublicApi.public_projects_slug_entries_get(slug)` | GET /public/projects/{slug}/entries | List published entries (no auth) |

Valid values for the `category` field: `new`, `improvement`, `fix`, `announcement`

## Links

- [Documentation](https://nitrozen.io/docs)
- [API Reference](https://nitrozen.io/docs/api)
- [GitHub](https://github.com/nitrozenio/nitrozen-python)
- [PyPI](https://pypi.org/project/nitrozenio/)
