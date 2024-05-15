# AutocompleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**experiment_ids** | **List[int]** | List of experiment ids for the corresponding request. | [optional] 
**tracking_token** | **str** | An opaque token that represents this particular set of autocomplete results. To be used for /feedback reporting. | [optional] 
**session_info** | [**SessionInfo**](SessionInfo.md) |  | [optional] 
**results** | [**List[AutocompleteResult]**](AutocompleteResult.md) |  | [optional] 
**groups** | [**List[AutocompleteResultGroup]**](AutocompleteResultGroup.md) | Subsections of the results list from which distinct sections should be created. | [optional] 
**error_info** | [**ErrorInfo**](ErrorInfo.md) |  | [optional] 
**backend_time_millis** | **int** | Time in milliseconds the backend took to respond to the request. | [optional] 

## Example

```python
from openapi_client.models.autocomplete_response import AutocompleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AutocompleteResponse from a JSON string
autocomplete_response_instance = AutocompleteResponse.from_json(json)
# print the JSON string representation of the object
print(AutocompleteResponse.to_json())

# convert the object into a dict
autocomplete_response_dict = autocomplete_response_instance.to_dict()
# create an instance of AutocompleteResponse from a dict
autocomplete_response_from_dict = AutocompleteResponse.from_dict(autocomplete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


