# NewToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**token** | **str** | The plain-text token. Only shown once. | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from nitrozenio.models.new_token import NewToken

# TODO update the JSON string below
json = "{}"
# create an instance of NewToken from a JSON string
new_token_instance = NewToken.from_json(json)
# print the JSON string representation of the object
print(NewToken.to_json())

# convert the object into a dict
new_token_dict = new_token_instance.to_dict()
# create an instance of NewToken from a dict
new_token_from_dict = NewToken.from_dict(new_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


