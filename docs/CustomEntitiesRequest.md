# CustomEntitiesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | The IDs of the custom entities to retrieve. | [optional] 

## Example

```python
from openapi_client.models.custom_entities_request import CustomEntitiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEntitiesRequest from a JSON string
custom_entities_request_instance = CustomEntitiesRequest.from_json(json)
# print the JSON string representation of the object
print(CustomEntitiesRequest.to_json())

# convert the object into a dict
custom_entities_request_dict = custom_entities_request_instance.to_dict()
# create an instance of CustomEntitiesRequest from a dict
custom_entities_request_from_dict = CustomEntitiesRequest.from_dict(custom_entities_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


