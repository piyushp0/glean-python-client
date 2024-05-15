# UgcDraft


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement** | [**AnnouncementMutableProperties**](AnnouncementMutableProperties.md) |  | [optional] 
**answer** | [**AnswerMutableProperties**](AnswerMutableProperties.md) |  | [optional] 

## Example

```python
from openapi_client.models.ugc_draft import UgcDraft

# TODO update the JSON string below
json = "{}"
# create an instance of UgcDraft from a JSON string
ugc_draft_instance = UgcDraft.from_json(json)
# print the JSON string representation of the object
print(UgcDraft.to_json())

# convert the object into a dict
ugc_draft_dict = ugc_draft_instance.to_dict()
# create an instance of UgcDraft from a dict
ugc_draft_from_dict = UgcDraft.from_dict(ugc_draft_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


