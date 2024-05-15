# Period


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_days_from_now** | **int** | DEPRECATED - The number of days from now in the past to define upper boundary of time period. | [optional] 
**max_days_from_now** | **int** | DEPRECATED - The number of days from now in the past to define lower boundary of time period. | [optional] 
**start** | [**TimePoint**](TimePoint.md) |  | [optional] 
**end** | [**TimePoint**](TimePoint.md) |  | [optional] 

## Example

```python
from openapi_client.models.period import Period

# TODO update the JSON string below
json = "{}"
# create an instance of Period from a JSON string
period_instance = Period.from_json(json)
# print the JSON string representation of the object
print(Period.to_json())

# convert the object into a dict
period_dict = period_instance.to_dict()
# create an instance of Period from a dict
period_from_dict = Period.from_dict(period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


