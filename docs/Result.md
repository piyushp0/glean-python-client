# Result


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**structured_results** | [**List[StructuredResult]**](StructuredResult.md) | An array of entities in the work graph retrieved via a data request. | [optional] 
**tracking_token** | **str** | An opaque token that represents this particular result in this particular query. To be used for /feedback reporting. | [optional] 

## Example

```python
from openapi_client.models.result import Result

# TODO update the JSON string below
json = "{}"
# create an instance of Result from a JSON string
result_instance = Result.from_json(json)
# print the JSON string representation of the object
print(Result.to_json())

# convert the object into a dict
result_dict = result_instance.to_dict()
# create an instance of Result from a dict
result_from_dict = Result.from_dict(result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


