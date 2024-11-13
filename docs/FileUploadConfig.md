# FileUploadConfig

Configuration settings for the chat file upload feature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether file upload for Chat is enabled for the deployment | [optional] 
**max_file_count** | **int** | Maximum number of files that can be uploaded in a single turn | [optional] 
**max_file_size** | **int** | Maximum file size, in bytes, that is allowed for upload | [optional] 

## Example

```python
from openapi_client.models.file_upload_config import FileUploadConfig

# TODO update the JSON string below
json = "{}"
# create an instance of FileUploadConfig from a JSON string
file_upload_config_instance = FileUploadConfig.from_json(json)
# print the JSON string representation of the object
print(FileUploadConfig.to_json())

# convert the object into a dict
file_upload_config_dict = file_upload_config_instance.to_dict()
# create an instance of FileUploadConfig from a dict
file_upload_config_from_dict = FileUploadConfig.from_dict(file_upload_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


