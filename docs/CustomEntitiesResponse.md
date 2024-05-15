# CustomEntitiesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[CustomEntity]**](CustomEntity.md) | A custom entity object | [optional] 
**errors** | **List[str]** | A list of IDs that could not be found. | [optional] 

## Example

```python
from openapi_client.models.custom_entities_response import CustomEntitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEntitiesResponse from a JSON string
custom_entities_response_instance = CustomEntitiesResponse.from_json(json)
# print the JSON string representation of the object
print(CustomEntitiesResponse.to_json())

# convert the object into a dict
custom_entities_response_dict = custom_entities_response_instance.to_dict()
# create an instance of CustomEntitiesResponse from a dict
custom_entities_response_from_dict = CustomEntitiesResponse.from_dict(custom_entities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


