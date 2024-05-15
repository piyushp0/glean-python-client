# MessagesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_type** | **str** | Type of the id in the incoming request. | 
**id** | **str** | ID corresponding to the requested idType. Note that channel and threads are represented by the underlying datasource&#39;s ID and conversations are represented by their document&#39;s ID. | 
**workspace_id** | **str** | Id for the for the workspace in case of multiple workspaces. | [optional] 
**direction** | **str** | The direction of the results asked with respect to the reference timestamp. Missing field defaults to OLDER. | [optional] 
**timestamp_millis** | **int** | Timestamp in millis of the reference message. | 
**include_root_message** | **bool** | Whether to include root message in response. | [optional] 
**datasource** | **str** | The type of the data source. Missing field defaults to SLACK. | [optional] 
**datasource_instance_display_name** | **str** | The datasource instance display name from which the document was extracted. This is used for appinstance facet filter for datasources that support multiple instances. | [optional] 

## Example

```python
from openapi_client.models.messages_request import MessagesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MessagesRequest from a JSON string
messages_request_instance = MessagesRequest.from_json(json)
# print the JSON string representation of the object
print(MessagesRequest.to_json())

# convert the object into a dict
messages_request_dict = messages_request_instance.to_dict()
# create an instance of MessagesRequest from a dict
messages_request_from_dict = MessagesRequest.from_dict(messages_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


