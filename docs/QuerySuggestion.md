# QuerySuggestion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**missing_term** | **str** | A query term missing from the original query on which this suggestion is based. | [optional] 
**query** | **str** | The query being suggested (e.g. enforcing the missing term from the original query). | 
**label** | **str** | A user-facing description to display for the suggestion. | [optional] 
**datasource** | **str** | The datasource associated with the suggestion. | [optional] 
**request_options** | [**SearchRequestOptions**](SearchRequestOptions.md) |  | [optional] 
**ranges** | [**List[TextRange]**](TextRange.md) | The bolded ranges within the query of the QuerySuggestion. | [optional] 

## Example

```python
from openapi_client.models.query_suggestion import QuerySuggestion

# TODO update the JSON string below
json = "{}"
# create an instance of QuerySuggestion from a JSON string
query_suggestion_instance = QuerySuggestion.from_json(json)
# print the JSON string representation of the object
print(QuerySuggestion.to_json())

# convert the object into a dict
query_suggestion_dict = query_suggestion_instance.to_dict()
# create an instance of QuerySuggestion from a dict
query_suggestion_from_dict = QuerySuggestion.from_dict(query_suggestion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


