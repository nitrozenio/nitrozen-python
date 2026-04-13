# UserPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**plan_type** | **str** |  | [optional] 
**max_projects** | **int** |  | [optional] 
**max_entries_per_month** | **int** |  | [optional] 
**custom_domain_allowed** | **bool** |  | [optional] 
**analytics_enabled** | **bool** |  | [optional] 
**api_access_enabled** | **bool** |  | [optional] 
**api_rate_limit** | **int** | Maximum API requests per minute for this plan | [optional] 

## Example

```python
from openapi_client.models.user_plan import UserPlan

# TODO update the JSON string below
json = "{}"
# create an instance of UserPlan from a JSON string
user_plan_instance = UserPlan.from_json(json)
# print the JSON string representation of the object
print(UserPlan.to_json())

# convert the object into a dict
user_plan_dict = user_plan_instance.to_dict()
# create an instance of UserPlan from a dict
user_plan_from_dict = UserPlan.from_dict(user_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


