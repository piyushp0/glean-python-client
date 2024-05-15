# PinRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queries** | **List[str]** | The query strings for which the pinned result will show. | [optional] 
**audience_filters** | [**List[FacetFilter]**](FacetFilter.md) | Filters which restrict who should see the pinned document. Values are taken from the corresponding filters in people search. | [optional] 
**document_id** | **str** | The document to be pinned. | [optional] 

## Example

```python
from openapi_client.models.pin_request import PinRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PinRequest from a JSON string
pin_request_instance = PinRequest.from_json(json)
# print the JSON string representation of the object
print(PinRequest.to_json())

# convert the object into a dict
pin_request_dict = pin_request_instance.to_dict()
# create an instance of PinRequest from a dict
pin_request_from_dict = PinRequest.from_dict(pin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


