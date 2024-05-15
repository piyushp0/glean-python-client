# GetPinResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pin** | [**PinDocument**](PinDocument.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_pin_response import GetPinResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPinResponse from a JSON string
get_pin_response_instance = GetPinResponse.from_json(json)
# print the JSON string representation of the object
print(GetPinResponse.to_json())

# convert the object into a dict
get_pin_response_dict = get_pin_response_instance.to_dict()
# create an instance of GetPinResponse from a dict
get_pin_response_from_dict = GetPinResponse.from_dict(get_pin_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


