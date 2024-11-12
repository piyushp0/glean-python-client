# PublicConfigRequest

Will only send back publicly available config and will ignore other keys

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**theme_keys** | **List[str]** | A list of theme keys to include in the response. | [optional] 
**bool_keys** | **List[str]** | A list of boolean flag keys to include in the response. | [optional] 

## Example

```python
from openapi_client.models.public_config_request import PublicConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PublicConfigRequest from a JSON string
public_config_request_instance = PublicConfigRequest.from_json(json)
# print the JSON string representation of the object
print(PublicConfigRequest.to_json())

# convert the object into a dict
public_config_request_dict = public_config_request_instance.to_dict()
# create an instance of PublicConfigRequest from a dict
public_config_request_from_dict = PublicConfigRequest.from_dict(public_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


