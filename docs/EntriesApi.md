# nitrozenio.EntriesApi

All URIs are relative to *https://nitrozen.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_project_entries_entry_delete**](EntriesApi.md#projects_project_entries_entry_delete) | **DELETE** /projects/{project}/entries/{entry} | Delete an entry
[**projects_project_entries_entry_get**](EntriesApi.md#projects_project_entries_entry_get) | **GET** /projects/{project}/entries/{entry} | Get an entry
[**projects_project_entries_entry_put**](EntriesApi.md#projects_project_entries_entry_put) | **PUT** /projects/{project}/entries/{entry} | Update an entry
[**projects_project_entries_get**](EntriesApi.md#projects_project_entries_get) | **GET** /projects/{project}/entries | List entries
[**projects_project_entries_post**](EntriesApi.md#projects_project_entries_post) | **POST** /projects/{project}/entries | Create an entry


# **projects_project_entries_entry_delete**
> projects_project_entries_entry_delete(project, entry)

Delete an entry

Permanently deletes a changelog entry.

### Example

* Bearer Authentication (BearerAuth):

```python
import nitrozenio
from nitrozenio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://nitrozen.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nitrozenio.Configuration(
    host = "https://nitrozen.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = nitrozenio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with nitrozenio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nitrozenio.EntriesApi(api_client)
    project = 56 # int | Project ID
    entry = 56 # int | Entry ID

    try:
        # Delete an entry
        api_instance.projects_project_entries_entry_delete(project, entry)
    except Exception as e:
        print("Exception when calling EntriesApi->projects_project_entries_entry_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| Project ID | 
 **entry** | **int**| Entry ID | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Entry deleted |  -  |
**403** | Access denied |  -  |
**404** | Resource not found |  -  |
**401** | Not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_entries_entry_get**
> ProjectsProjectEntriesPost201Response projects_project_entries_entry_get(project, entry)

Get an entry

Returns a single entry by ID.

### Example

* Bearer Authentication (BearerAuth):

```python
import nitrozenio
from nitrozenio.models.projects_project_entries_post201_response import ProjectsProjectEntriesPost201Response
from nitrozenio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://nitrozen.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nitrozenio.Configuration(
    host = "https://nitrozen.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = nitrozenio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with nitrozenio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nitrozenio.EntriesApi(api_client)
    project = 56 # int | Project ID
    entry = 56 # int | Entry ID

    try:
        # Get an entry
        api_response = api_instance.projects_project_entries_entry_get(project, entry)
        print("The response of EntriesApi->projects_project_entries_entry_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntriesApi->projects_project_entries_entry_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| Project ID | 
 **entry** | **int**| Entry ID | 

### Return type

[**ProjectsProjectEntriesPost201Response**](ProjectsProjectEntriesPost201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Entry details |  -  |
**403** | Access denied |  -  |
**404** | Resource not found |  -  |
**401** | Not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_entries_entry_put**
> ProjectsProjectEntriesPost201Response projects_project_entries_entry_put(project, entry, entry_input)

Update an entry

Updates an existing changelog entry.

### Example

* Bearer Authentication (BearerAuth):

```python
import nitrozenio
from nitrozenio.models.entry_input import EntryInput
from nitrozenio.models.projects_project_entries_post201_response import ProjectsProjectEntriesPost201Response
from nitrozenio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://nitrozen.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nitrozenio.Configuration(
    host = "https://nitrozen.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = nitrozenio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with nitrozenio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nitrozenio.EntriesApi(api_client)
    project = 56 # int | Project ID
    entry = 56 # int | Entry ID
    entry_input = nitrozenio.EntryInput() # EntryInput | 

    try:
        # Update an entry
        api_response = api_instance.projects_project_entries_entry_put(project, entry, entry_input)
        print("The response of EntriesApi->projects_project_entries_entry_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntriesApi->projects_project_entries_entry_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| Project ID | 
 **entry** | **int**| Entry ID | 
 **entry_input** | [**EntryInput**](EntryInput.md)|  | 

### Return type

[**ProjectsProjectEntriesPost201Response**](ProjectsProjectEntriesPost201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Entry updated |  -  |
**403** | Access denied |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed |  -  |
**401** | Not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_entries_get**
> ProjectsProjectEntriesGet200Response projects_project_entries_get(project, category=category, status=status, page=page, per_page=per_page)

List entries

Returns entries for a project with optional filtering and pagination.

### Example

* Bearer Authentication (BearerAuth):

```python
import nitrozenio
from nitrozenio.models.projects_project_entries_get200_response import ProjectsProjectEntriesGet200Response
from nitrozenio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://nitrozen.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nitrozenio.Configuration(
    host = "https://nitrozen.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = nitrozenio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with nitrozenio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nitrozenio.EntriesApi(api_client)
    project = 56 # int | Project ID
    category = 'category_example' # str | Filter by category slug. Every project has the built-in categories `new`, `improvement`, `fix`, and `announcement`; projects on plans with custom categories enabled may also have additional project-specific slugs.  (optional)
    status = 'status_example' # str | Filter by publish status (optional)
    page = 1 # int | Page number (optional) (default to 1)
    per_page = 15 # int | Items per page (optional) (default to 15)

    try:
        # List entries
        api_response = api_instance.projects_project_entries_get(project, category=category, status=status, page=page, per_page=per_page)
        print("The response of EntriesApi->projects_project_entries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntriesApi->projects_project_entries_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| Project ID | 
 **category** | **str**| Filter by category slug. Every project has the built-in categories &#x60;new&#x60;, &#x60;improvement&#x60;, &#x60;fix&#x60;, and &#x60;announcement&#x60;; projects on plans with custom categories enabled may also have additional project-specific slugs.  | [optional] 
 **status** | **str**| Filter by publish status | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 15]

### Return type

[**ProjectsProjectEntriesGet200Response**](ProjectsProjectEntriesGet200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of entries |  -  |
**403** | Access denied |  -  |
**401** | Not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_entries_post**
> ProjectsProjectEntriesPost201Response projects_project_entries_post(project, entry_input)

Create an entry

Creates a new changelog entry. Set `is_published` to `true` to publish immediately.
If `published_at` is not provided for a published entry, it defaults to the current time.


### Example

* Bearer Authentication (BearerAuth):

```python
import nitrozenio
from nitrozenio.models.entry_input import EntryInput
from nitrozenio.models.projects_project_entries_post201_response import ProjectsProjectEntriesPost201Response
from nitrozenio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://nitrozen.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nitrozenio.Configuration(
    host = "https://nitrozen.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = nitrozenio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with nitrozenio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nitrozenio.EntriesApi(api_client)
    project = 56 # int | Project ID
    entry_input = {"title":"Dark mode support","content":"We've added dark mode across the entire application.","category":"new","is_published":true} # EntryInput | 

    try:
        # Create an entry
        api_response = api_instance.projects_project_entries_post(project, entry_input)
        print("The response of EntriesApi->projects_project_entries_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntriesApi->projects_project_entries_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| Project ID | 
 **entry_input** | [**EntryInput**](EntryInput.md)|  | 

### Return type

[**ProjectsProjectEntriesPost201Response**](ProjectsProjectEntriesPost201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Entry created |  -  |
**403** | Plan limit reached or forbidden |  -  |
**422** | Validation failed |  -  |
**401** | Not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

