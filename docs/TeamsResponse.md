# TeamsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Team]**](Team.md) | A Team and a deep copy of all its members for each ID in the request | [optional] 
**errors** | **List[str]** | A list of IDs that could not be found. | [optional] 

## Example

```python
from openapi_client.models.teams_response import TeamsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TeamsResponse from a JSON string
teams_response_instance = TeamsResponse.from_json(json)
# print the JSON string representation of the object
print(TeamsResponse.to_json())

# convert the object into a dict
teams_response_dict = teams_response_instance.to_dict()
# create an instance of TeamsResponse from a dict
teams_response_from_dict = TeamsResponse.from_dict(teams_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


