# ChannelInviteInfo

Information regarding the invite status of a person for a particular channel.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | [**CommunicationChannel**](CommunicationChannel.md) |  | [optional] 
**is_auto_invite** | **bool** | Bit that tracks if this invite was automatically sent or user-sent | [optional] 
**inviter** | [**Person**](Person.md) |  | [optional] 
**invite_time** | **datetime** | The time this person was invited in ISO format (ISO 8601). | [optional] 
**reminder_time** | **datetime** | The time this person was reminded in ISO format (ISO 8601) if a reminder was sent. | [optional] 

## Example

```python
from openapi_client.models.channel_invite_info import ChannelInviteInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelInviteInfo from a JSON string
channel_invite_info_instance = ChannelInviteInfo.from_json(json)
# print the JSON string representation of the object
print(ChannelInviteInfo.to_json())

# convert the object into a dict
channel_invite_info_dict = channel_invite_info_instance.to_dict()
# create an instance of ChannelInviteInfo from a dict
channel_invite_info_from_dict = ChannelInviteInfo.from_dict(channel_invite_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


