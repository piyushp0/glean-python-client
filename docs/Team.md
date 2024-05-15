# Team


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**related_objects** | [**Dict[str, RelatedObjectEdge]**](RelatedObjectEdge.md) | A list of objects related to a source object. | [optional] 
**permissions** | [**ObjectPermissions**](ObjectPermissions.md) |  | [optional] 
**id** | **str** | Unique identifier | 
**name** | **str** | Team name | 
**description** | **str** | A description of the team | [optional] 
**business_unit** | **str** | Typically the highest level organizational unit; generally applies to bigger companies with multiple distinct businesses. | [optional] 
**department** | **str** | An organizational unit where everyone has a similar task, e.g. &#x60;Engineering&#x60;. | [optional] 
**photo_url** | **str** | A link to the team&#39;s photo. | [optional] 
**banner_url** | **str** | A link to the team&#39;s banner photo. | [optional] 
**external_link** | **str** | Link to a team page on the internet or your company&#39;s intranet | [optional] 
**members** | [**List[PersonToTeamRelationship]**](PersonToTeamRelationship.md) | The members on this team | [optional] 
**member_count** | **int** | Number of members on this team (recursive; includes all individuals that belong to this team, and all individuals that belong to a subteam within this team) | [optional] 
**emails** | [**List[TeamEmail]**](TeamEmail.md) | The emails for this team | [optional] 
**datasource_profiles** | [**List[DatasourceProfile]**](DatasourceProfile.md) | The datasource profiles of the team | [optional] 
**datasource** | **str** | the data source of the team, e.g. GDRIVE | [optional] 
**created_from** | **str** | For teams created from docs, the doc title. Otherwise empty. | [optional] 
**last_updated_at** | **datetime** | when this team was last updated. | [optional] 
**status** | **str** | whether this team is fully processed or there are still unprocessed operations that&#39;ll affect it | [optional] [default to 'PROCESSED']
**can_be_deleted** | **bool** | can this team be deleted. Some manually ingested teams like GCS_CSV or PUSH_API cannot | [optional] [default to True]
**logging_id** | **str** | The logging id of the team used in scrubbed logs, client analytics, and metrics. | [optional] 

## Example

```python
from openapi_client.models.team import Team

# TODO update the JSON string below
json = "{}"
# create an instance of Team from a JSON string
team_instance = Team.from_json(json)
# print the JSON string representation of the object
print(Team.to_json())

# convert the object into a dict
team_dict = team_instance.to_dict()
# create an instance of Team from a dict
team_from_dict = Team.from_dict(team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


