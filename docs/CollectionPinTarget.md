# CollectionPinTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**CollectionPinnableCategories**](CollectionPinnableCategories.md) |  | 
**value** | **str** | Optional. If category supports values, then the additional value for the category e.g. department name for DEPARTMENT_RESOURCE, team name/id for TEAM_RESOURCE and so on. | [optional] 
**target** | [**CollectionPinnableTargets**](CollectionPinnableTargets.md) |  | [optional] 

## Example

```python
from openapi_client.models.collection_pin_target import CollectionPinTarget

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionPinTarget from a JSON string
collection_pin_target_instance = CollectionPinTarget.from_json(json)
# print the JSON string representation of the object
print(CollectionPinTarget.to_json())

# convert the object into a dict
collection_pin_target_dict = collection_pin_target_instance.to_dict()
# create an instance of CollectionPinTarget from a dict
collection_pin_target_from_dict = CollectionPinTarget.from_dict(collection_pin_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


