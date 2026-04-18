# openapi_client.ProjectsApi

All URIs are relative to *https://nitrozen.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_get**](ProjectsApi.md#projects_get) | **GET** /projects | List projects
[**projects_post**](ProjectsApi.md#projects_post) | **POST** /projects | Create a project
[**projects_project_delete**](ProjectsApi.md#projects_project_delete) | **DELETE** /projects/{project} | Delete a project
[**projects_project_get**](ProjectsApi.md#projects_project_get) | **GET** /projects/{project} | Get a project
[**projects_project_put**](ProjectsApi.md#projects_project_put) | **PUT** /projects/{project} | Update a project


# **projects_get**
> ProjectsGet200Response projects_get()

List projects

Returns all projects owned by the authenticated user.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.projects_get200_response import ProjectsGet200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://nitrozen.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://nitrozen.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectsApi(api_client)

    try:
        # List projects
        api_response = api_instance.projects_get()
        print("The response of ProjectsApi->projects_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ProjectsGet200Response**](ProjectsGet200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of projects |  -  |
**401** | Not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_post**
> ProjectsPost201Response projects_post(project_input)

Create a project

Creates a new changelog project. The slug is auto-generated from the name.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.project_input import ProjectInput
from openapi_client.models.projects_post201_response import ProjectsPost201Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://nitrozen.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://nitrozen.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectsApi(api_client)
    project_input = {"name":"My Product","description":"Changelog for My Product"} # ProjectInput | 

    try:
        # Create a project
        api_response = api_instance.projects_post(project_input)
        print("The response of ProjectsApi->projects_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_input** | [**ProjectInput**](ProjectInput.md)|  | 

### Return type

[**ProjectsPost201Response**](ProjectsPost201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Project created |  -  |
**403** | Plan limit reached |  -  |
**422** | Validation failed |  -  |
**401** | Not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_delete**
> projects_project_delete(project)

Delete a project

Permanently deletes a project and all its entries.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://nitrozen.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://nitrozen.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectsApi(api_client)
    project = 56 # int | Project ID

    try:
        # Delete a project
        api_instance.projects_project_delete(project)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_project_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| Project ID | 

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
**204** | Project deleted |  -  |
**403** | Access denied |  -  |
**404** | Resource not found |  -  |
**401** | Not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_get**
> ProjectsPost201Response projects_project_get(project)

Get a project

Returns a single project by ID.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.projects_post201_response import ProjectsPost201Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://nitrozen.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://nitrozen.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectsApi(api_client)
    project = 56 # int | Project ID

    try:
        # Get a project
        api_response = api_instance.projects_project_get(project)
        print("The response of ProjectsApi->projects_project_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_project_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| Project ID | 

### Return type

[**ProjectsPost201Response**](ProjectsPost201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project details |  -  |
**403** | Access denied |  -  |
**404** | Resource not found |  -  |
**401** | Not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_put**
> ProjectsPost201Response projects_project_put(project, project_input)

Update a project

Updates an existing project's name and description.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.project_input import ProjectInput
from openapi_client.models.projects_post201_response import ProjectsPost201Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://nitrozen.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://nitrozen.io/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ProjectsApi(api_client)
    project = 56 # int | Project ID
    project_input = openapi_client.ProjectInput() # ProjectInput | 

    try:
        # Update a project
        api_response = api_instance.projects_project_put(project, project_input)
        print("The response of ProjectsApi->projects_project_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_project_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **int**| Project ID | 
 **project_input** | [**ProjectInput**](ProjectInput.md)|  | 

### Return type

[**ProjectsPost201Response**](ProjectsPost201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project updated |  -  |
**403** | Access denied |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed |  -  |
**401** | Not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

