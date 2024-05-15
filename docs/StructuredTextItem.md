# StructuredTextItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**document** | [**Document**](Document.md) |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.structured_text_item import StructuredTextItem

# TODO update the JSON string below
json = "{}"
# create an instance of StructuredTextItem from a JSON string
structured_text_item_instance = StructuredTextItem.from_json(json)
# print the JSON string representation of the object
print(StructuredTextItem.to_json())

# convert the object into a dict
structured_text_item_dict = structured_text_item_instance.to_dict()
# create an instance of StructuredTextItem from a dict
structured_text_item_from_dict = StructuredTextItem.from_dict(structured_text_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


