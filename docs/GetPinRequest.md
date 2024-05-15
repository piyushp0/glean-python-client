# GetPinRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The opaque id of the pin to be fetched. | [optional] 

## Example

```python
from openapi_client.models.get_pin_request import GetPinRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetPinRequest from a JSON string
get_pin_request_instance = GetPinRequest.from_json(json)
# print the JSON string representation of the object
print(GetPinRequest.to_json())

# convert the object into a dict
get_pin_request_dict = get_pin_request_instance.to_dict()
# create an instance of GetPinRequest from a dict
get_pin_request_from_dict = GetPinRequest.from_dict(get_pin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


