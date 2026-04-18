# TokensPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name for the token | 

## Example

```python
from openapi_client.models.tokens_post_request import TokensPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokensPostRequest from a JSON string
tokens_post_request_instance = TokensPostRequest.from_json(json)
# print the JSON string representation of the object
print(TokensPostRequest.to_json())

# convert the object into a dict
tokens_post_request_dict = tokens_post_request_instance.to_dict()
# create an instance of TokensPostRequest from a dict
tokens_post_request_from_dict = TokensPostRequest.from_dict(tokens_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


