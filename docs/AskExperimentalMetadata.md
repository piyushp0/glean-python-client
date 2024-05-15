# AskExperimentalMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_has_mentions** | **bool** | Whether or not the query (i.e. the slack message) has a mention. | [optional] 
**query_is_length_appropriate** | **bool** | Whether or not the query (i.e. the slack message) is length appropriate. | [optional] 
**query_is_answerable** | **bool** | Whether or not the query (i.e. the slack message) has a question term. | [optional] 

## Example

```python
from openapi_client.models.ask_experimental_metadata import AskExperimentalMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AskExperimentalMetadata from a JSON string
ask_experimental_metadata_instance = AskExperimentalMetadata.from_json(json)
# print the JSON string representation of the object
print(AskExperimentalMetadata.to_json())

# convert the object into a dict
ask_experimental_metadata_dict = ask_experimental_metadata_instance.to_dict()
# create an instance of AskExperimentalMetadata from a dict
ask_experimental_metadata_from_dict = AskExperimentalMetadata.from_dict(ask_experimental_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


