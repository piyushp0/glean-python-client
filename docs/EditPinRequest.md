# EditPinRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queries** | **List[str]** | The query strings for which the pinned result will show. | [optional] 
**audience_filters** | [**List[FacetFilter]**](FacetFilter.md) | Filters which restrict who should see the pinned document. Values are taken from the corresponding filters in people search. | [optional] 
**id** | **str** | The opaque id of the pin to be edited. | [optional] 

## Example

```python
from openapi_client.models.edit_pin_request import EditPinRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditPinRequest from a JSON string
edit_pin_request_instance = EditPinRequest.from_json(json)
# print the JSON string representation of the object
print(EditPinRequest.to_json())

# convert the object into a dict
edit_pin_request_dict = edit_pin_request_instance.to_dict()
# create an instance of EditPinRequest from a dict
edit_pin_request_from_dict = EditPinRequest.from_dict(edit_pin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


