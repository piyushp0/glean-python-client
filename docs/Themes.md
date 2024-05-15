# Themes

A set of Theme objects to make available to the user based on their chosen preference. If a theme variant is not supplied, the default theme will be used.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**light** | **Dict[str, str]** | A map of {string, string} pairs where the key represents a known theme option and the value is the CSS color to apply. Supported options are documented in https://dev.glean.com/meta/browser_api/interfaces/Theme.html. | [optional] 
**dark** | **Dict[str, str]** | A map of {string, string} pairs where the key represents a known theme option and the value is the CSS color to apply. Supported options are documented in https://dev.glean.com/meta/browser_api/interfaces/Theme.html. | [optional] 

## Example

```python
from openapi_client.models.themes import Themes

# TODO update the JSON string below
json = "{}"
# create an instance of Themes from a JSON string
themes_instance = Themes.from_json(json)
# print the JSON string representation of the object
print(Themes.to_json())

# convert the object into a dict
themes_dict = themes_instance.to_dict()
# create an instance of Themes from a dict
themes_from_dict = Themes.from_dict(themes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


