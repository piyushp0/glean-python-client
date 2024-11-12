# PreviewUgcRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**draft** | [**UgcDraft**](UgcDraft.md) |  | [optional] 
**draft_spec** | [**DocumentSpec**](DocumentSpec.md) |  | [optional] 
**type** | [**UgcType**](UgcType.md) |  | [optional] 

## Example

```python
from openapi_client.models.preview_ugc_request import PreviewUgcRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewUgcRequest from a JSON string
preview_ugc_request_instance = PreviewUgcRequest.from_json(json)
# print the JSON string representation of the object
print(PreviewUgcRequest.to_json())

# convert the object into a dict
preview_ugc_request_dict = preview_ugc_request_instance.to_dict()
# create an instance of PreviewUgcRequest from a dict
preview_ugc_request_from_dict = PreviewUgcRequest.from_dict(preview_ugc_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


