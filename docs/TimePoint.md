# TimePoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**epoch_seconds** | **int** | Epoch seconds. Has precedence over daysFromNow. | [optional] 
**days_from_now** | **int** | The number of days from now. Specification relative to current time. Can be negative. | [optional] 

## Example

```python
from openapi_client.models.time_point import TimePoint

# TODO update the JSON string below
json = "{}"
# create an instance of TimePoint from a JSON string
time_point_instance = TimePoint.from_json(json)
# print the JSON string representation of the object
print(TimePoint.to_json())

# convert the object into a dict
time_point_dict = time_point_instance.to_dict()
# create an instance of TimePoint from a dict
time_point_from_dict = TimePoint.from_dict(time_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


