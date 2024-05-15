# DeleteTeamsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_errors** | **int** | Number of teams that failed to be deleted | [optional] 

## Example

```python
from openapi_client.models.delete_teams_response import DeleteTeamsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteTeamsResponse from a JSON string
delete_teams_response_instance = DeleteTeamsResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteTeamsResponse.to_json())

# convert the object into a dict
delete_teams_response_dict = delete_teams_response_instance.to_dict()
# create an instance of DeleteTeamsResponse from a dict
delete_teams_response_from_dict = DeleteTeamsResponse.from_dict(delete_teams_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


