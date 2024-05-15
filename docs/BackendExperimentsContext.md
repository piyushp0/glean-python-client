# BackendExperimentsContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**experiment_ids** | **List[int]** | List of experiment ids for the corresponding request. | [optional] 

## Example

```python
from openapi_client.models.backend_experiments_context import BackendExperimentsContext

# TODO update the JSON string below
json = "{}"
# create an instance of BackendExperimentsContext from a JSON string
backend_experiments_context_instance = BackendExperimentsContext.from_json(json)
# print the JSON string representation of the object
print(BackendExperimentsContext.to_json())

# convert the object into a dict
backend_experiments_context_dict = backend_experiments_context_instance.to_dict()
# create an instance of BackendExperimentsContext from a dict
backend_experiments_context_from_dict = BackendExperimentsContext.from_dict(backend_experiments_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


