# IconConfig

Defines how to render an icon

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generated_background_color_key** | **str** |  | [optional] 
**background_color** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**icon_type** | **str** |  | [optional] 
**masked** | **bool** | Whether the icon should be masked based on current theme. | [optional] 
**name** | **str** | The name of the icon if applicable, e.g. the glyph name for &#x60;IconType.GLYPH&#x60; icons. | [optional] 
**url** | **str** | The URL to an image to be displayed if applicable, e.g. the URL for &#x60;iconType.URL&#x60; icons. | [optional] 

## Example

```python
from openapi_client.models.icon_config import IconConfig

# TODO update the JSON string below
json = "{}"
# create an instance of IconConfig from a JSON string
icon_config_instance = IconConfig.from_json(json)
# print the JSON string representation of the object
print(IconConfig.to_json())

# convert the object into a dict
icon_config_dict = icon_config_instance.to_dict()
# create an instance of IconConfig from a dict
icon_config_from_dict = IconConfig.from_dict(icon_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


