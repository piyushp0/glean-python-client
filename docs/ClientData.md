# ClientData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_refresh_timestamp** | **int** | Server unix timestamp of the last refresh/request (in seconds since epoch UTC). | [optional] 

## Example

```python
from openapi_client.models.client_data import ClientData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientData from a JSON string
client_data_instance = ClientData.from_json(json)
# print the JSON string representation of the object
print(ClientData.to_json())

# convert the object into a dict
client_data_dict = client_data_instance.to_dict()
# create an instance of ClientData from a dict
client_data_from_dict = ClientData.from_dict(client_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


