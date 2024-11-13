# SearchClientConfig

Configuration settings related to Search

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** | Whether search is available or not. | [optional] 
**placeholder** | **str** | Custom autocomplete box placeholder to replace rotating prompts | [optional] 

## Example

```python
from openapi_client.models.search_client_config import SearchClientConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SearchClientConfig from a JSON string
search_client_config_instance = SearchClientConfig.from_json(json)
# print the JSON string representation of the object
print(SearchClientConfig.to_json())

# convert the object into a dict
search_client_config_dict = search_client_config_instance.to_dict()
# create an instance of SearchClientConfig from a dict
search_client_config_from_dict = SearchClientConfig.from_dict(search_client_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


