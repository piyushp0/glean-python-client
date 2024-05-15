# DeleteTeamsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | List of all team IDs to be deleted | [optional] 

## Example

```python
from openapi_client.models.delete_teams_request import DeleteTeamsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteTeamsRequest from a JSON string
delete_teams_request_instance = DeleteTeamsRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteTeamsRequest.to_json())

# convert the object into a dict
delete_teams_request_dict = delete_teams_request_instance.to_dict()
# create an instance of DeleteTeamsRequest from a dict
delete_teams_request_from_dict = DeleteTeamsRequest.from_dict(delete_teams_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


