# AgentClientConfig

Describes the configurations that GleanChat has based on an AgentConfig.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_config** | [**AgentConfig**](AgentConfig.md) |  | [optional] 
**input_char_limit** | **int** | The character limit of an input to GleanChat under the specified AgentConfig. | [optional] 

## Example

```python
from openapi_client.models.agent_client_config import AgentClientConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AgentClientConfig from a JSON string
agent_client_config_instance = AgentClientConfig.from_json(json)
# print the JSON string representation of the object
print(AgentClientConfig.to_json())

# convert the object into a dict
agent_client_config_dict = agent_client_config_instance.to_dict()
# create an instance of AgentClientConfig from a dict
agent_client_config_from_dict = AgentClientConfig.from_dict(agent_client_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


