# ChatZeroStateSuggestionOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | The Chat Application ID this feed request should be scoped to. Empty means there is no Chat Application ID.. | [optional] 

## Example

```python
from openapi_client.models.chat_zero_state_suggestion_options import ChatZeroStateSuggestionOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ChatZeroStateSuggestionOptions from a JSON string
chat_zero_state_suggestion_options_instance = ChatZeroStateSuggestionOptions.from_json(json)
# print the JSON string representation of the object
print(ChatZeroStateSuggestionOptions.to_json())

# convert the object into a dict
chat_zero_state_suggestion_options_dict = chat_zero_state_suggestion_options_instance.to_dict()
# create an instance of ChatZeroStateSuggestionOptions from a dict
chat_zero_state_suggestion_options_from_dict = ChatZeroStateSuggestionOptions.from_dict(chat_zero_state_suggestion_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


