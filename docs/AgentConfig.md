# AgentConfig

Describes the agent that executes the request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent** | **str** | Name of the agent. DEFAULT - Integrates with your company&#39;s knowledge. GPT - Communicates directly with the LLM. | [optional] 
**mode** | **str** | Top level modes to run GleanChat in. DEFAULT - Used if no mode supplied. QUICK - Trades accuracy and precision for speed. | [optional] 

## Example

```python
from openapi_client.models.agent_config import AgentConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AgentConfig from a JSON string
agent_config_instance = AgentConfig.from_json(json)
# print the JSON string representation of the object
print(AgentConfig.to_json())

# convert the object into a dict
agent_config_dict = agent_config_instance.to_dict()
# create an instance of AgentConfig from a dict
agent_config_from_dict = AgentConfig.from_dict(agent_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


