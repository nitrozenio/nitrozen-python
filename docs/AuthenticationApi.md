# nitrozenio.AuthenticationApi

All URIs are relative to *https://nitrozen.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tokens_get**](AuthenticationApi.md#tokens_get) | **GET** /tokens | List API tokens
[**tokens_post**](AuthenticationApi.md#tokens_post) | **POST** /tokens | Create an API token
[**tokens_token_delete**](AuthenticationApi.md#tokens_token_delete) | **DELETE** /tokens/{token} | Revoke an API token


# **tokens_get**
> TokensGet200Response tokens_get()

List API tokens

Returns all API tokens for the authenticated user. Token values are not included.

### Example

* Bearer Authentication (BearerAuth):

```python
import nitrozenio
from nitrozenio.models.tokens_get200_response import TokensGet200Response
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
    api_instance = nitrozenio.AuthenticationApi(api_client)

    try:
        # List API tokens
        api_response = api_instance.tokens_get()
        print("The response of AuthenticationApi->tokens_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->tokens_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TokensGet200Response**](TokensGet200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of tokens |  -  |
**401** | Not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tokens_post**
> TokensPost201Response tokens_post(tokens_post_request)

Create an API token

Creates a new API token. The plain-text token is only returned in this response
and cannot be retrieved later.


### Example

* Bearer Authentication (BearerAuth):

```python
import nitrozenio
from nitrozenio.models.tokens_post201_response import TokensPost201Response
from nitrozenio.models.tokens_post_request import TokensPostRequest
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
    api_instance = nitrozenio.AuthenticationApi(api_client)
    tokens_post_request = {"name":"CI/CD Pipeline"} # TokensPostRequest | 

    try:
        # Create an API token
        api_response = api_instance.tokens_post(tokens_post_request)
        print("The response of AuthenticationApi->tokens_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->tokens_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tokens_post_request** | [**TokensPostRequest**](TokensPostRequest.md)|  | 

### Return type

[**TokensPost201Response**](TokensPost201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Token created |  -  |
**422** | Validation failed |  -  |
**401** | Not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tokens_token_delete**
> tokens_token_delete(token)

Revoke an API token

Permanently revokes an API token. Any requests using this token will be rejected.

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
    api_instance = nitrozenio.AuthenticationApi(api_client)
    token = 56 # int | Token ID

    try:
        # Revoke an API token
        api_instance.tokens_token_delete(token)
    except Exception as e:
        print("Exception when calling AuthenticationApi->tokens_token_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **int**| Token ID | 

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
**204** | Token revoked |  -  |
**404** | Resource not found |  -  |
**401** | Not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

