# CreateTeamsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**teams** | [**List[TeamCreationData]**](TeamCreationData.md) | List of all teams from data sources to create | [optional] 

## Example

```python
from openapi_client.models.create_teams_request import CreateTeamsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTeamsRequest from a JSON string
create_teams_request_instance = CreateTeamsRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTeamsRequest.to_json())

# convert the object into a dict
create_teams_request_dict = create_teams_request_instance.to_dict()
# create an instance of CreateTeamsRequest from a dict
create_teams_request_from_dict = CreateTeamsRequest.from_dict(create_teams_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


