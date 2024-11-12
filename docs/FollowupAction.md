# FollowupAction

A follow-up action that can be invoked by the user after a response. The action parameters are not included and need to be predicted/filled separately.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_instance_id** | **str** | The ID of the action instance that will be invoked. | [optional] 

## Example

```python
from openapi_client.models.followup_action import FollowupAction

# TODO update the JSON string below
json = "{}"
# create an instance of FollowupAction from a JSON string
followup_action_instance = FollowupAction.from_json(json)
# print the JSON string representation of the object
print(FollowupAction.to_json())

# convert the object into a dict
followup_action_dict = followup_action_instance.to_dict()
# create an instance of FollowupAction from a dict
followup_action_from_dict = FollowupAction.from_dict(followup_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


