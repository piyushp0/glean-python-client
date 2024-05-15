# TeamEmail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | An email address | [optional] 
**type** | **str** |  | [optional] [default to 'OTHER']
**is_user_generated** | **bool** | true iff the email was manually added by a user from within Glean (aka not from the original data source) | [optional] 

## Example

```python
from openapi_client.models.team_email import TeamEmail

# TODO update the JSON string below
json = "{}"
# create an instance of TeamEmail from a JSON string
team_email_instance = TeamEmail.from_json(json)
# print the JSON string representation of the object
print(TeamEmail.to_json())

# convert the object into a dict
team_email_dict = team_email_instance.to_dict()
# create an instance of TeamEmail from a dict
team_email_from_dict = TeamEmail.from_dict(team_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


