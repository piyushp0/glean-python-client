# ChatMessageFragment

One fragment of a message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**structured_results** | [**List[StructuredResult]**](StructuredResult.md) | An array of entities in the work graph retrieved via a data request. | [optional] 
**tracking_token** | **str** | An opaque token that represents this particular result in this particular query. To be used for /feedback reporting. | [optional] 
**text** | **str** |  | [optional] 
**query_suggestion** | [**QuerySuggestion**](QuerySuggestion.md) |  | [optional] 
**write_action** | [**WriteAction**](WriteAction.md) |  | [optional] 

## Example

```python
from openapi_client.models.chat_message_fragment import ChatMessageFragment

# TODO update the JSON string below
json = "{}"
# create an instance of ChatMessageFragment from a JSON string
chat_message_fragment_instance = ChatMessageFragment.from_json(json)
# print the JSON string representation of the object
print(ChatMessageFragment.to_json())

# convert the object into a dict
chat_message_fragment_dict = chat_message_fragment_instance.to_dict()
# create an instance of ChatMessageFragment from a dict
chat_message_fragment_from_dict = ChatMessageFragment.from_dict(chat_message_fragment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


