# ExtractedQnA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**heading** | **str** | Heading text that was matched to produce this result. | [optional] 
**question** | **str** | Question text that was matched to produce this result. | [optional] 
**question_result** | [**SearchResult**](SearchResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.extracted_qn_a import ExtractedQnA

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractedQnA from a JSON string
extracted_qn_a_instance = ExtractedQnA.from_json(json)
# print the JSON string representation of the object
print(ExtractedQnA.to_json())

# convert the object into a dict
extracted_qn_a_dict = extracted_qn_a_instance.to_dict()
# create an instance of ExtractedQnA from a dict
extracted_qn_a_from_dict = ExtractedQnA.from_dict(extracted_qn_a_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


