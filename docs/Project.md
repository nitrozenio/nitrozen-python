# Project


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**public_url** | **str** | Public changelog page URL. &#x60;https://&lt;custom_domain&gt;&#x60; when the project&#39;s custom domain is verified, otherwise &#x60;https://nitrozen.io/c/&lt;slug&gt;&#x60;. Read-only; ignored on create and update. | [optional] [readonly] 
**description** | **str** |  | [optional] 
**custom_domain** | **str** |  | [optional] 
**domain_verification_status** | **str** |  | [optional] 
**entries_count** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from nitrozenio.models.project import Project

# TODO update the JSON string below
json = "{}"
# create an instance of Project from a JSON string
project_instance = Project.from_json(json)
# print the JSON string representation of the object
print(Project.to_json())

# convert the object into a dict
project_dict = project_instance.to_dict()
# create an instance of Project from a dict
project_from_dict = Project.from_dict(project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


