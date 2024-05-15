# PersonToTeamRelationship

Metadata about the relationship of a person to a team.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**person** | [**Person**](Person.md) |  | 
**relationship** | **str** | The team member&#39;s relationship to the team. This defaults to MEMBER if not set. | [optional] [default to 'MEMBER']
**custom_relationship_str** | **str** | Displayed name for the relationship if relationship is set to &#x60;OTHER&#x60;. | [optional] 
**join_date** | **datetime** | The team member&#39;s start date | [optional] 

## Example

```python
from openapi_client.models.person_to_team_relationship import PersonToTeamRelationship

# TODO update the JSON string below
json = "{}"
# create an instance of PersonToTeamRelationship from a JSON string
person_to_team_relationship_instance = PersonToTeamRelationship.from_json(json)
# print the JSON string representation of the object
print(PersonToTeamRelationship.to_json())

# convert the object into a dict
person_to_team_relationship_dict = person_to_team_relationship_instance.to_dict()
# create an instance of PersonToTeamRelationship from a dict
person_to_team_relationship_from_dict = PersonToTeamRelationship.from_dict(person_to_team_relationship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


