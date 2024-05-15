# SearchWarning


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warning_type** | **str** | The type of the warning. | 
**last_used_term** | **str** | The last term we considered in the user&#39;s long query. | [optional] 
**quotes_ignored_query** | **str** | The query after ignoring/removing quotes. | [optional] 
**ignored_terms** | **List[str]** | A list of query terms that were ignored when generating search results, if any. For example, terms containing invalid filters such as \&quot;updated:invalid_date\&quot; will be ignored. | [optional] 

## Example

```python
from openapi_client.models.search_warning import SearchWarning

# TODO update the JSON string below
json = "{}"
# create an instance of SearchWarning from a JSON string
search_warning_instance = SearchWarning.from_json(json)
# print the JSON string representation of the object
print(SearchWarning.to_json())

# convert the object into a dict
search_warning_dict = search_warning_instance.to_dict()
# create an instance of SearchWarning from a dict
search_warning_from_dict = SearchWarning.from_dict(search_warning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


