# ResultsDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Textual description of the results. Can be shown at the top of SERP, e.g. &#39;People who write about this topic&#39; for experts in people tab. | [optional] 
**icon_config** | [**IconConfig**](IconConfig.md) |  | [optional] 

## Example

```python
from openapi_client.models.results_description import ResultsDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ResultsDescription from a JSON string
results_description_instance = ResultsDescription.from_json(json)
# print the JSON string representation of the object
print(ResultsDescription.to_json())

# convert the object into a dict
results_description_dict = results_description_instance.to_dict()
# create an instance of ResultsDescription from a dict
results_description_from_dict = ResultsDescription.from_dict(results_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


