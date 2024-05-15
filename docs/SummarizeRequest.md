# SummarizeRequest

Summary of the document

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | The ISO 8601 timestamp associated with the client request. | [optional] 
**query** | **str** | Optional query that the summary should be about | [optional] 
**preferred_summary_length** | **int** | Optional length of summary output. If not given, defaults to 500 chars. | [optional] 
**document_specs** | [**List[DocumentSpec]**](DocumentSpec.md) | Specifications of documents to summarize | 
**tracking_token** | **str** | An opaque token that represents this particular result. To be used for /feedback reporting. | [optional] 

## Example

```python
from openapi_client.models.summarize_request import SummarizeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SummarizeRequest from a JSON string
summarize_request_instance = SummarizeRequest.from_json(json)
# print the JSON string representation of the object
print(SummarizeRequest.to_json())

# convert the object into a dict
summarize_request_dict = summarize_request_instance.to_dict()
# create an instance of SummarizeRequest from a dict
summarize_request_from_dict = SummarizeRequest.from_dict(summarize_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


