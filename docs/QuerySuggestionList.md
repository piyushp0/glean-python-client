# QuerySuggestionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suggestions** | [**List[QuerySuggestion]**](QuerySuggestion.md) |  | 
**person** | [**Person**](Person.md) |  | [optional] 

## Example

```python
from openapi_client.models.query_suggestion_list import QuerySuggestionList

# TODO update the JSON string below
json = "{}"
# create an instance of QuerySuggestionList from a JSON string
query_suggestion_list_instance = QuerySuggestionList.from_json(json)
# print the JSON string representation of the object
print(QuerySuggestionList.to_json())

# convert the object into a dict
query_suggestion_list_dict = query_suggestion_list_instance.to_dict()
# create an instance of QuerySuggestionList from a dict
query_suggestion_list_from_dict = QuerySuggestionList.from_dict(query_suggestion_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


