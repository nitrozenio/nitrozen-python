# Entry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**category** | **str** | The entry&#39;s category slug. Every project has the built-in categories &#x60;new&#x60;, &#x60;improvement&#x60;, &#x60;fix&#x60;, and &#x60;announcement&#x60;; projects on plans with custom categories enabled may also define additional project-specific slugs.  | [optional] 
**is_published** | **bool** |  | [optional] 
**published_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from nitrozenio.models.entry import Entry

# TODO update the JSON string below
json = "{}"
# create an instance of Entry from a JSON string
entry_instance = Entry.from_json(json)
# print the JSON string representation of the object
print(Entry.to_json())

# convert the object into a dict
entry_dict = entry_instance.to_dict()
# create an instance of Entry from a dict
entry_from_dict = Entry.from_dict(entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


