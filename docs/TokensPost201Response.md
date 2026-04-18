# TokensPost201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**NewToken**](NewToken.md) |  | [optional] 

## Example

```python
from openapi_client.models.tokens_post201_response import TokensPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of TokensPost201Response from a JSON string
tokens_post201_response_instance = TokensPost201Response.from_json(json)
# print the JSON string representation of the object
print(TokensPost201Response.to_json())

# convert the object into a dict
tokens_post201_response_dict = tokens_post201_response_instance.to_dict()
# create an instance of TokensPost201Response from a dict
tokens_post201_response_from_dict = TokensPost201Response.from_dict(tokens_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


