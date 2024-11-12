# PinCollectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Whether to pin or unpin | [default to 'PIN']
**data** | [**CollectionPinMetadata**](CollectionPinMetadata.md) |  | [optional] 

## Example

```python
from openapi_client.models.pin_collection_request import PinCollectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PinCollectionRequest from a JSON string
pin_collection_request_instance = PinCollectionRequest.from_json(json)
# print the JSON string representation of the object
print(PinCollectionRequest.to_json())

# convert the object into a dict
pin_collection_request_dict = pin_collection_request_instance.to_dict()
# create an instance of PinCollectionRequest from a dict
pin_collection_request_from_dict = PinCollectionRequest.from_dict(pin_collection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


