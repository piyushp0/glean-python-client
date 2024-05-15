# ClientAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the client action. | 
**quicklink** | [**Quicklink**](Quicklink.md) |  | [optional] 
**destination_url** | **str** | Specific URL if action requires a destination URL to complete. Has precedence over action context. | [optional] 

## Example

```python
from openapi_client.models.client_action import ClientAction

# TODO update the JSON string below
json = "{}"
# create an instance of ClientAction from a JSON string
client_action_instance = ClientAction.from_json(json)
# print the JSON string representation of the object
print(ClientAction.to_json())

# convert the object into a dict
client_action_dict = client_action_instance.to_dict()
# create an instance of ClientAction from a dict
client_action_from_dict = ClientAction.from_dict(client_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


