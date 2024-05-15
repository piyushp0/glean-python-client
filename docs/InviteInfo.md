# InviteInfo

Information regarding the invite status of a person.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sign_up_time** | **datetime** | The time this person signed up in ISO format (ISO 8601). | [optional] 
**invites** | [**List[ChannelInviteInfo]**](ChannelInviteInfo.md) | Latest invites received by the user for each channel | [optional] 
**inviter** | [**Person**](Person.md) |  | [optional] 
**invite_time** | **datetime** | The time this person was invited in ISO format (ISO 8601). | [optional] 
**reminder_time** | **datetime** | The time this person was reminded in ISO format (ISO 8601) if a reminder was sent. | [optional] 

## Example

```python
from openapi_client.models.invite_info import InviteInfo

# TODO update the JSON string below
json = "{}"
# create an instance of InviteInfo from a JSON string
invite_info_instance = InviteInfo.from_json(json)
# print the JSON string representation of the object
print(InviteInfo.to_json())

# convert the object into a dict
invite_info_dict = invite_info_instance.to_dict()
# create an instance of InviteInfo from a dict
invite_info_from_dict = InviteInfo.from_dict(invite_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


