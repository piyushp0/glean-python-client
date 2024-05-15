# TeamsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | The IDs of the teams to retrieve. | [optional] 
**include_fields** | **List[str]** | List of teams fields to return that aren&#39;t returned by default | [optional] 

## Example

```python
from openapi_client.models.teams_request import TeamsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TeamsRequest from a JSON string
teams_request_instance = TeamsRequest.from_json(json)
# print the JSON string representation of the object
print(TeamsRequest.to_json())

# convert the object into a dict
teams_request_dict = teams_request_instance.to_dict()
# create an instance of TeamsRequest from a dict
teams_request_from_dict = TeamsRequest.from_dict(teams_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


