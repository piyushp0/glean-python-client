# SummarizeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**SummarizeResponseError**](SummarizeResponseError.md) |  | [optional] 
**summary** | [**Summary**](Summary.md) |  | [optional] 
**tracking_token** | **str** | An opaque token that represents this summary in this particular query. To be used for /feedback reporting. | [optional] 

## Example

```python
from openapi_client.models.summarize_response import SummarizeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SummarizeResponse from a JSON string
summarize_response_instance = SummarizeResponse.from_json(json)
# print the JSON string representation of the object
print(SummarizeResponse.to_json())

# convert the object into a dict
summarize_response_dict = summarize_response_instance.to_dict()
# create an instance of SummarizeResponse from a dict
summarize_response_from_dict = SummarizeResponse.from_dict(summarize_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


