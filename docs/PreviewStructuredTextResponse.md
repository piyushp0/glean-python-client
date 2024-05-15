# PreviewStructuredTextResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**structured_text** | [**StructuredText**](StructuredText.md) |  | 
**docs_inaccessible_to_user** | **List[str]** | A list of links the user doesn&#39;t have access to. | [optional] 
**combined_answer_text** | [**StructuredText**](StructuredText.md) |  | 

## Example

```python
from openapi_client.models.preview_structured_text_response import PreviewStructuredTextResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewStructuredTextResponse from a JSON string
preview_structured_text_response_instance = PreviewStructuredTextResponse.from_json(json)
# print the JSON string representation of the object
print(PreviewStructuredTextResponse.to_json())

# convert the object into a dict
preview_structured_text_response_dict = preview_structured_text_response_instance.to_dict()
# create an instance of PreviewStructuredTextResponse from a dict
preview_structured_text_response_from_dict = PreviewStructuredTextResponse.from_dict(preview_structured_text_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


