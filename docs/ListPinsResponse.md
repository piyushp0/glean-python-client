# ListPinsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pins** | [**List[PinDocument]**](PinDocument.md) | List of pinned documents. | 

## Example

```python
from openapi_client.models.list_pins_response import ListPinsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListPinsResponse from a JSON string
list_pins_response_instance = ListPinsResponse.from_json(json)
# print the JSON string representation of the object
print(ListPinsResponse.to_json())

# convert the object into a dict
list_pins_response_dict = list_pins_response_instance.to_dict()
# create an instance of ListPinsResponse from a dict
list_pins_response_from_dict = ListPinsResponse.from_dict(list_pins_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


