# ChatMessageFragment

Represents a part of a ChatMessage that originates from a single action/tool. It is designed to support rich data formats beyond simple text, allowing for a more dynamic and interactive chat experience. Each fragment can include various types of content, such as text, search queries, action information, and more. Also, each ChatMessageFragment should only have one of structuredResults, querySuggestion, writeAction, or file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**structured_results** | [**List[StructuredResult]**](StructuredResult.md) | An array of entities in the work graph retrieved via a data request. | [optional] 
**tracking_token** | **str** | An opaque token that represents this particular result in this particular query. To be used for /feedback reporting. | [optional] 
**text** | **str** |  | [optional] 
**query_suggestion** | [**QuerySuggestion**](QuerySuggestion.md) |  | [optional] 
**write_action** | [**WriteAction**](WriteAction.md) |  | [optional] 
**file** | [**ChatFile**](ChatFile.md) |  | [optional] 
**action** | [**ToolInfo**](ToolInfo.md) |  | [optional] 

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


