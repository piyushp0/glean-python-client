# Group


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**GroupType**](GroupType.md) |  | 
**id** | **str** | A unique identifier for the group. May be the same as name. | 
**name** | **str** | Name of the group. | [optional] 

## Example

```python
from openapi_client.models.group import Group

# TODO update the JSON string below
json = "{}"
# create an instance of Group from a JSON string
group_instance = Group.from_json(json)
# print the JSON string representation of the object
print(Group.to_json())

# convert the object into a dict
group_dict = group_instance.to_dict()
# create an instance of Group from a dict
group_from_dict = Group.from_dict(group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


