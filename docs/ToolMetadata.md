# ToolMetadata

The manifest for a tool that can be used to augment Glean Assistant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of tool. | 
**name** | **str** | Unique identifier for the tool. Name should be understandable by the LLM, and will be used to invoke a tool. | 
**display_name** | **str** | Human understandable name of the tool. Max 50 characters. | 
**tool_id** | **str** | An opaque id which is unique identifier for the tool. | [optional] 
**display_description** | **str** | Description of the tool meant for a human. | 
**logo_url** | **str** | URL used to fetch the logo. | [optional] 
**object_name** | **str** | Name of the generated object. This will be used to indicate to the end user what the generated object contains. | [optional] 
**created_by** | [**PersonObject**](PersonObject.md) |  | [optional] 
**last_updated_by** | [**PersonObject**](PersonObject.md) |  | [optional] 
**created_at** | **datetime** | The time the tool was created in ISO format (ISO 8601) | [optional] 
**last_updated_at** | **datetime** | The time the tool was last updated in ISO format (ISO 8601) | [optional] 
**auth** | [**AuthConfig**](AuthConfig.md) |  | [optional] 

## Example

```python
from openapi_client.models.tool_metadata import ToolMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ToolMetadata from a JSON string
tool_metadata_instance = ToolMetadata.from_json(json)
# print the JSON string representation of the object
print(ToolMetadata.to_json())

# convert the object into a dict
tool_metadata_dict = tool_metadata_instance.to_dict()
# create an instance of ToolMetadata from a dict
tool_metadata_from_dict = ToolMetadata.from_dict(tool_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


