# CountInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The counter value | 
**period** | [**Period**](Period.md) |  | [optional] 
**org** | **str** | The unit of organization over which we did the count aggregation, e.g. org (department) or company | [optional] 

## Example

```python
from openapi_client.models.count_info import CountInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CountInfo from a JSON string
count_info_instance = CountInfo.from_json(json)
# print the JSON string representation of the object
print(CountInfo.to_json())

# convert the object into a dict
count_info_dict = count_info_instance.to_dict()
# create an instance of CountInfo from a dict
count_info_from_dict = CountInfo.from_dict(count_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


