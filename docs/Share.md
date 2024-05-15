# Share

Search endpoint will only fill out numDays ago since that's all we need to display shared badge; docmetadata endpoint will fill out all the fields so that we can display shared badge tooltip

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_days_ago** | **int** | The number of days that has passed since the share happened | 
**sharer** | [**Person**](Person.md) |  | [optional] 
**sharing_document** | [**Document**](Document.md) |  | [optional] 

## Example

```python
from openapi_client.models.share import Share

# TODO update the JSON string below
json = "{}"
# create an instance of Share from a JSON string
share_instance = Share.from_json(json)
# print the JSON string representation of the object
print(Share.to_json())

# convert the object into a dict
share_dict = share_instance.to_dict()
# create an instance of Share from a dict
share_from_dict = Share.from_dict(share_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


