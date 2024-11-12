# Branding

A map of visual aspects of the app such as the company background image, logos, logo background colors, and wide company logos.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_background_image_name** | **str** | User facing company background image to be displayed to users on the home page. | [optional] 
**company_logo_url** | **str** | An image URL pointing to a custom logo that should be displayed to users. Must be square and recognizable down to 40x40px. SVG images with transparent background are preferred. | [optional] 
**company_wide_logo_url** | **str** | An image URL pointing to a wide format custom logo that should be displayed to users. Should be rectangular and recognizable at 40px height, and aspect ratio should be between 2:1 and 4:1. SVG images with transparent background are preferred. | [optional] 
**company_logo_background_color** | **str** | A hex RGB color to display behind custom logo (e.g. &#39;#ff4080&#39;). | [optional] 

## Example

```python
from openapi_client.models.branding import Branding

# TODO update the JSON string below
json = "{}"
# create an instance of Branding from a JSON string
branding_instance = Branding.from_json(json)
# print the JSON string representation of the object
print(Branding.to_json())

# convert the object into a dict
branding_dict = branding_instance.to_dict()
# create an instance of Branding from a dict
branding_from_dict = Branding.from_dict(branding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


