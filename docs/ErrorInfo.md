# ErrorInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bad_gmail_token** | **bool** | Indicates the gmail results could not be fetched due to bad token. | [optional] 
**bad_outlook_token** | **bool** | Indicates the outlook results could not be fetched due to bad token. | [optional] 
**invalid_operators** | [**List[InvalidOperatorValueError]**](InvalidOperatorValueError.md) | Indicates results could not be fetched due to invalid operators in the query. | [optional] 
**error_messages** | [**List[ErrorMessage]**](ErrorMessage.md) |  | [optional] 

## Example

```python
from openapi_client.models.error_info import ErrorInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorInfo from a JSON string
error_info_instance = ErrorInfo.from_json(json)
# print the JSON string representation of the object
print(ErrorInfo.to_json())

# convert the object into a dict
error_info_dict = error_info_instance.to_dict()
# create an instance of ErrorInfo from a dict
error_info_from_dict = ErrorInfo.from_dict(error_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


