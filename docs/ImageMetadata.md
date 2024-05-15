# ImageMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ImageType**](ImageType.md) |  | 
**id** | **str** | ID, if a specific entity/type is requested. The id may have different meaning for each type. For USER, it is user id For UGC, it is the id of the content For ICON, the doctype. | [optional] 
**ds** | **str** | A specific datasource for which an image is requested for. The ds may have different meaning for each type and can also be empty for some. For USER, it is empty or datasource the icon is asked for. For UGC, it is the UGC datasource. For ICON, it is datasource instance the icon is asked for. | [optional] 
**cid** | **str** | Content id to differentitate multiple images that can have the same type and datasource e.g. thumnail or image from content of UGC. It can also be empty. | [optional] 
**ext** | **str** | Extension the image is saved with. The extension data is deduced from content type for image uploads. | [optional] 

## Example

```python
from openapi_client.models.image_metadata import ImageMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ImageMetadata from a JSON string
image_metadata_instance = ImageMetadata.from_json(json)
# print the JSON string representation of the object
print(ImageMetadata.to_json())

# convert the object into a dict
image_metadata_dict = image_metadata_instance.to_dict()
# create an instance of ImageMetadata from a dict
image_metadata_from_dict = ImageMetadata.from_dict(image_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


