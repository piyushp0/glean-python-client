# StructuredLocation

Detailed location with information about country, state, city etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**desk_location** | **str** | Desk number. | [optional] 
**timezone** | **str** | Location&#39;s timezone, e.g. UTC, PST. | [optional] 
**address** | **str** | Office address or name. | [optional] 
**city** | **str** | Name of the city. | [optional] 
**state** | **str** | State code. | [optional] 
**region** | **str** | Region information, e.g. NORAM, APAC. | [optional] 
**zip_code** | **str** | ZIP Code for the address. | [optional] 
**country** | **str** | Country name. | [optional] 
**country_code** | **str** | Alpha-2 or Alpha-3 ISO 3166 country code, e.g. US or USA. | [optional] 

## Example

```python
from openapi_client.models.structured_location import StructuredLocation

# TODO update the JSON string below
json = "{}"
# create an instance of StructuredLocation from a JSON string
structured_location_instance = StructuredLocation.from_json(json)
# print the JSON string representation of the object
print(StructuredLocation.to_json())

# convert the object into a dict
structured_location_dict = structured_location_instance.to_dict()
# create an instance of StructuredLocation from a dict
structured_location_from_dict = StructuredLocation.from_dict(structured_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


