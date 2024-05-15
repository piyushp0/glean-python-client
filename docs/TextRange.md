# TextRange

A subsection of a given string to which some special formatting should be applied.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_index** | **int** | The inclusive start index of the range. | 
**end_index** | **int** | The exclusive end index of the range. | [optional] 
**type** | **str** |  | [optional] 
**url** | **str** | The URL associated with the range, if applicable. For example, the linked URL for a LINK range. | [optional] 
**document** | [**Document**](Document.md) |  | [optional] 

## Example

```python
from openapi_client.models.text_range import TextRange

# TODO update the JSON string below
json = "{}"
# create an instance of TextRange from a JSON string
text_range_instance = TextRange.from_json(json)
# print the JSON string representation of the object
print(TextRange.to_json())

# convert the object into a dict
text_range_dict = text_range_instance.to_dict()
# create an instance of TextRange from a dict
text_range_from_dict = TextRange.from_dict(text_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


