# QueryInsight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | The query string the information is about. | 
**search_count** | [**CountInfo**](CountInfo.md) |  | [optional] 
**searchor_count** | [**CountInfo**](CountInfo.md) |  | [optional] 
**search_with_click_count** | [**CountInfo**](CountInfo.md) |  | [optional] 
**click_count** | [**CountInfo**](CountInfo.md) |  | [optional] 
**similar_queries** | [**List[QueryInsight]**](QueryInsight.md) | list of similar queries to current one. | [optional] 

## Example

```python
from openapi_client.models.query_insight import QueryInsight

# TODO update the JSON string below
json = "{}"
# create an instance of QueryInsight from a JSON string
query_insight_instance = QueryInsight.from_json(json)
# print the JSON string representation of the object
print(QueryInsight.to_json())

# convert the object into a dict
query_insight_dict = query_insight_instance.to_dict()
# create an instance of QueryInsight from a dict
query_insight_from_dict = QueryInsight.from_dict(query_insight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


