# DatasourceProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasource** | **str** | The datasource the profile is of. | 
**handle** | **str** | The display name of the entity in the given datasource. | 
**url** | **str** | URL to view the entity&#39;s profile. | [optional] 
**native_app_url** | **str** | A deep link, if available, into the datasource&#39;s native application for the entity&#39;s platform (i.e. slack://...). | [optional] 
**is_user_generated** | **bool** | For internal use only. True iff the data source profile was manually added by a user from within Glean (aka not from the original data source) | [optional] 

## Example

```python
from openapi_client.models.datasource_profile import DatasourceProfile

# TODO update the JSON string below
json = "{}"
# create an instance of DatasourceProfile from a JSON string
datasource_profile_instance = DatasourceProfile.from_json(json)
# print the JSON string representation of the object
print(DatasourceProfile.to_json())

# convert the object into a dict
datasource_profile_dict = datasource_profile_instance.to_dict()
# create an instance of DatasourceProfile from a dict
datasource_profile_from_dict = DatasourceProfile.from_dict(datasource_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


