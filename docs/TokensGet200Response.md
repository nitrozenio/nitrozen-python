# TokensGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TokenInfo]**](TokenInfo.md) |  | [optional] 

## Example

```python
from openapi_client.models.tokens_get200_response import TokensGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TokensGet200Response from a JSON string
tokens_get200_response_instance = TokensGet200Response.from_json(json)
# print the JSON string representation of the object
print(TokensGet200Response.to_json())

# convert the object into a dict
tokens_get200_response_dict = tokens_get200_response_instance.to_dict()
# create an instance of TokensGet200Response from a dict
tokens_get200_response_from_dict = TokensGet200Response.from_dict(tokens_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


