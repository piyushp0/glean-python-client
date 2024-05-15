# LabeledCountInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Label for the included count information. | 
**count_info** | [**List[CountInfo]**](CountInfo.md) | List of data points for counts for a given date period. | [optional] 

## Example

```python
from openapi_client.models.labeled_count_info import LabeledCountInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LabeledCountInfo from a JSON string
labeled_count_info_instance = LabeledCountInfo.from_json(json)
# print the JSON string representation of the object
print(LabeledCountInfo.to_json())

# convert the object into a dict
labeled_count_info_dict = labeled_count_info_instance.to_dict()
# create an instance of LabeledCountInfo from a dict
labeled_count_info_from_dict = LabeledCountInfo.from_dict(labeled_count_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


