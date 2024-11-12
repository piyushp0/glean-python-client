# PreviewUgcResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement** | [**Announcement**](Announcement.md) |  | [optional] 
**answer** | [**Answer**](Answer.md) |  | [optional] 

## Example

```python
from openapi_client.models.preview_ugc_response import PreviewUgcResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewUgcResponse from a JSON string
preview_ugc_response_instance = PreviewUgcResponse.from_json(json)
# print the JSON string representation of the object
print(PreviewUgcResponse.to_json())

# convert the object into a dict
preview_ugc_response_dict = preview_ugc_response_instance.to_dict()
# create an instance of PreviewUgcResponse from a dict
preview_ugc_response_from_dict = PreviewUgcResponse.from_dict(preview_ugc_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


