# WorkflowMetadata

Metadata of a workflow.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**Person**](Person.md) |  | [optional] 
**create_timestamp** | **int** | Server Unix timestamp of the creation time. | [optional] 
**last_update_timestamp** | **int** | Server Unix timestamp of the last update time. | [optional] 
**last_updated_by** | [**Person**](Person.md) |  | [optional] 
**roles** | [**List[UserRoleSpecification]**](UserRoleSpecification.md) | A list of roles for this prompt template explicitly granted. | [optional] 

## Example

```python
from openapi_client.models.workflow_metadata import WorkflowMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowMetadata from a JSON string
workflow_metadata_instance = WorkflowMetadata.from_json(json)
# print the JSON string representation of the object
print(WorkflowMetadata.to_json())

# convert the object into a dict
workflow_metadata_dict = workflow_metadata_instance.to_dict()
# create an instance of WorkflowMetadata from a dict
workflow_metadata_from_dict = WorkflowMetadata.from_dict(workflow_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


