# StructuredLink

The display configuration for a link.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The display name for the link | [optional] 
**url** | **str** | The URL for the link. | [optional] 
**icon_config** | [**IconConfig**](IconConfig.md) |  | [optional] 

## Example

```python
from openapi_client.models.structured_link import StructuredLink

# TODO update the JSON string below
json = "{}"
# create an instance of StructuredLink from a JSON string
structured_link_instance = StructuredLink.from_json(json)
# print the JSON string representation of the object
print(StructuredLink.to_json())

# convert the object into a dict
structured_link_dict = structured_link_instance.to_dict()
# create an instance of StructuredLink from a dict
structured_link_from_dict = StructuredLink.from_dict(structured_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


