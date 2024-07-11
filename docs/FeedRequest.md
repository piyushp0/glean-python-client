# FeedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **List[str]** | Categories of content requested. An allowlist gives flexibility to request content separately or together. | [optional] 
**request_options** | [**FeedRequestOptions**](FeedRequestOptions.md) |  | [optional] 
**timeout_millis** | **int** | Timeout in milliseconds for the request. A &#x60;408&#x60; error will be returned if handling the request takes longer. | [optional] 
**session_info** | [**SessionInfo**](SessionInfo.md) |  | [optional] 

## Example

```python
from openapi_client.models.feed_request import FeedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FeedRequest from a JSON string
feed_request_instance = FeedRequest.from_json(json)
# print the JSON string representation of the object
print(FeedRequest.to_json())

# convert the object into a dict
feed_request_dict = feed_request_instance.to_dict()
# create an instance of FeedRequest from a dict
feed_request_from_dict = FeedRequest.from_dict(feed_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


