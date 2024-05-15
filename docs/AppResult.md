# AppResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasource** | **str** | The app or other repository type this represents | 
**doc_type** | **str** | The datasource-specific type of the document (e.g. for Jira issues, this is the issue type such as Bug or Feature Request). | [optional] 
**mime_type** | **str** | Mimetype is used to differentiate between sub applications from a datasource (e.g. Sheets, Docs from Gdrive) | [optional] 
**icon_url** | **str** | If there is available icon URL. | [optional] 

## Example

```python
from openapi_client.models.app_result import AppResult

# TODO update the JSON string below
json = "{}"
# create an instance of AppResult from a JSON string
app_result_instance = AppResult.from_json(json)
# print the JSON string representation of the object
print(AppResult.to_json())

# convert the object into a dict
app_result_dict = app_result_instance.to_dict()
# create an instance of AppResult from a dict
app_result_from_dict = AppResult.from_dict(app_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


