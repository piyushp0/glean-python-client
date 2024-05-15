# StructuredText


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**structured_list** | [**List[StructuredTextItem]**](StructuredTextItem.md) | An array of objects each of which contains either a string or a link which optionally corresponds to a document. | [optional] 

## Example

```python
from openapi_client.models.structured_text import StructuredText

# TODO update the JSON string below
json = "{}"
# create an instance of StructuredText from a JSON string
structured_text_instance = StructuredText.from_json(json)
# print the JSON string representation of the object
print(StructuredText.to_json())

# convert the object into a dict
structured_text_dict = structured_text_instance.to_dict()
# create an instance of StructuredText from a dict
structured_text_from_dict = StructuredText.from_dict(structured_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


