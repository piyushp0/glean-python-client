# Badge

Displays a user's accomplishment or milestone

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | An auto generated unique identifier. | [optional] 
**display_name** | **str** | The badge name displayed to users | [optional] 
**icon_config** | [**IconConfig**](IconConfig.md) |  | [optional] 
**pinned** | **bool** | The badge should be shown on the PersonAttribution | [optional] 

## Example

```python
from openapi_client.models.badge import Badge

# TODO update the JSON string below
json = "{}"
# create an instance of Badge from a JSON string
badge_instance = Badge.from_json(json)
# print the JSON string representation of the object
print(Badge.to_json())

# convert the object into a dict
badge_dict = badge_instance.to_dict()
# create an instance of Badge from a dict
badge_from_dict = Badge.from_dict(badge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


