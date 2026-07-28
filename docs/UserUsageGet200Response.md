# UserUsageGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Usage**](Usage.md) |  | [optional] 

## Example

```python
from nitrozenio.models.user_usage_get200_response import UserUsageGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserUsageGet200Response from a JSON string
user_usage_get200_response_instance = UserUsageGet200Response.from_json(json)
# print the JSON string representation of the object
print(UserUsageGet200Response.to_json())

# convert the object into a dict
user_usage_get200_response_dict = user_usage_get200_response_instance.to_dict()
# create an instance of UserUsageGet200Response from a dict
user_usage_get200_response_from_dict = UserUsageGet200Response.from_dict(user_usage_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


