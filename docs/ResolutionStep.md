# ResolutionStep

A step to take to resolve an alert

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_text** | **str** | text for what step to take | [optional] 
**link** | **str** | optional link url for instructions | [optional] 
**metadata** | **List[str]** | optional metadata for the step | [optional] 

## Example

```python
from openapi_client.models.resolution_step import ResolutionStep

# TODO update the JSON string below
json = "{}"
# create an instance of ResolutionStep from a JSON string
resolution_step_instance = ResolutionStep.from_json(json)
# print the JSON string representation of the object
print(ResolutionStep.to_json())

# convert the object into a dict
resolution_step_dict = resolution_step_instance.to_dict()
# create an instance of ResolutionStep from a dict
resolution_step_from_dict = ResolutionStep.from_dict(resolution_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


