# AskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detect_only** | **bool** | Whether to apply only question detection and not answering. | [optional] 
**ask_experimental_metadata** | [**AskExperimentalMetadata**](AskExperimentalMetadata.md) |  | [optional] 
**search_request** | [**SearchRequest**](SearchRequest.md) |  | 
**excluded_document_specs** | [**List[DocumentSpec]**](DocumentSpec.md) | A list of Glean Document IDs to be excluded when retrieving documents. Note that, currently, it only supports exclusion of one Glean Documnet ID based spec. If multiple specifications are provided only the first Glean Document ID based spec is excluded and the remaining specs are ignored. | [optional] 
**operators** | **str** | Search operators to append to the query | [optional] 
**backend** | **str** | Which backend to use to fulfill the requests. | [optional] 
**chat_application_id** | **str** | The ID of the application this request originates from, used to determine the configuration of underlying chat processes when invoking the CHAT backend. This should correspond to the ID set during admin setup. If not specified, the default chat experience will be used. | [optional] 

## Example

```python
from openapi_client.models.ask_request import AskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AskRequest from a JSON string
ask_request_instance = AskRequest.from_json(json)
# print the JSON string representation of the object
print(AskRequest.to_json())

# convert the object into a dict
ask_request_dict = ask_request_instance.to_dict()
# create an instance of AskRequest from a dict
ask_request_from_dict = AskRequest.from_dict(ask_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


