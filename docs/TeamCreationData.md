# TeamCreationData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | For people field teams, the field value, e.g. ENGINEERING. Otherwise, a Glean Document ID used to identify the team. | [optional] 
**people_field** | **str** | if the data source is people fields, then this is the field name (otherwise it&#39;s ignored) | [optional] 
**datasource** | **str** | what data source this team comes from, e.g. GDRIVE | [optional] 
**created_from** | **str** | If the team is from a doc (i.e. not from a people field), this is the doc title, e.g. for Slack channels, the channel name. Otherwise, it&#39;s ignored. | [optional] 

## Example

```python
from openapi_client.models.team_creation_data import TeamCreationData

# TODO update the JSON string below
json = "{}"
# create an instance of TeamCreationData from a JSON string
team_creation_data_instance = TeamCreationData.from_json(json)
# print the JSON string representation of the object
print(TeamCreationData.to_json())

# convert the object into a dict
team_creation_data_dict = team_creation_data_instance.to_dict()
# create an instance of TeamCreationData from a dict
team_creation_data_from_dict = TeamCreationData.from_dict(team_creation_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


