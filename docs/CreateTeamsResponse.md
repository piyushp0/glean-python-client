# CreateTeamsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_errors** | **int** | Number of teams that failed to be created | [optional] 

## Example

```python
from openapi_client.models.create_teams_response import CreateTeamsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTeamsResponse from a JSON string
create_teams_response_instance = CreateTeamsResponse.from_json(json)
# print the JSON string representation of the object
print(CreateTeamsResponse.to_json())

# convert the object into a dict
create_teams_response_dict = create_teams_response_instance.to_dict()
# create an instance of CreateTeamsResponse from a dict
create_teams_response_from_dict = CreateTeamsResponse.from_dict(create_teams_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


