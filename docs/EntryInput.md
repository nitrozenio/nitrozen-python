# EntryInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**content** | **str** |  | 
**category** | **str** |  | 
**is_published** | **bool** |  | [optional] [default to False]
**published_at** | **datetime** | Defaults to current time if is_published is true and this is not set. | [optional] 

## Example

```python
from openapi_client.models.entry_input import EntryInput

# TODO update the JSON string below
json = "{}"
# create an instance of EntryInput from a JSON string
entry_input_instance = EntryInput.from_json(json)
# print the JSON string representation of the object
print(EntryInput.to_json())

# convert the object into a dict
entry_input_dict = entry_input_instance.to_dict()
# create an instance of EntryInput from a dict
entry_input_from_dict = EntryInput.from_dict(entry_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


