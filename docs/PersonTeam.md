# PersonTeam

Use `id` if you index teams via Glean, and use `name` and `externalLink` if you want to use your own team pages

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier | [optional] 
**name** | **str** | Team name | [optional] 
**external_link** | **str** | Link to a team page on the internet or your company&#39;s intranet | [optional] 
**relationship** | **str** | The team member&#39;s relationship to the team. This defaults to MEMBER if not set. | [optional] [default to 'MEMBER']
**join_date** | **datetime** | The team member&#39;s start date | [optional] 

## Example

```python
from openapi_client.models.person_team import PersonTeam

# TODO update the JSON string below
json = "{}"
# create an instance of PersonTeam from a JSON string
person_team_instance = PersonTeam.from_json(json)
# print the JSON string representation of the object
print(PersonTeam.to_json())

# convert the object into a dict
person_team_dict = person_team_instance.to_dict()
# create an instance of PersonTeam from a dict
person_team_from_dict = PersonTeam.from_dict(person_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


