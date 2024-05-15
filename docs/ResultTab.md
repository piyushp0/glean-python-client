# ResultTab


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the tab. Can be passed in a search request to get results for that tab. | [optional] 
**count** | **int** | The number of results in this tab for the current query. | [optional] 
**datasource** | **str** | The datasource associated with the tab, if any. | [optional] 
**datasource_instance** | **str** | The datasource instance associated with the tab, if any. | [optional] 

## Example

```python
from openapi_client.models.result_tab import ResultTab

# TODO update the JSON string below
json = "{}"
# create an instance of ResultTab from a JSON string
result_tab_instance = ResultTab.from_json(json)
# print the JSON string representation of the object
print(ResultTab.to_json())

# convert the object into a dict
result_tab_dict = result_tab_instance.to_dict()
# create an instance of ResultTab from a dict
result_tab_from_dict = ResultTab.from_dict(result_tab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


