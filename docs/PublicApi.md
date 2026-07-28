# nitrozenio.PublicApi

All URIs are relative to *https://nitrozen.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**public_projects_slug_entries_get**](PublicApi.md#public_projects_slug_entries_get) | **GET** /public/projects/{slug}/entries | List published entries (public)


# **public_projects_slug_entries_get**
> PublicProjectsSlugEntriesGet200Response public_projects_slug_entries_get(slug)

List published entries (public)

Returns all published entries for a project. No authentication required.

### Example


```python
import nitrozenio
from nitrozenio.models.public_projects_slug_entries_get200_response import PublicProjectsSlugEntriesGet200Response
from nitrozenio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://nitrozen.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nitrozenio.Configuration(
    host = "https://nitrozen.io/api/v1"
)


# Enter a context with an instance of the API client
with nitrozenio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nitrozenio.PublicApi(api_client)
    slug = 'slug_example' # str | Project slug

    try:
        # List published entries (public)
        api_response = api_instance.public_projects_slug_entries_get(slug)
        print("The response of PublicApi->public_projects_slug_entries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->public_projects_slug_entries_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| Project slug | 

### Return type

[**PublicProjectsSlugEntriesGet200Response**](PublicProjectsSlugEntriesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of published entries |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

