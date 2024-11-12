# openapi_client.ImagesApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**images**](ImagesApi.md#images) | **GET** /images | Get image
[**uploadimage**](ImagesApi.md#uploadimage) | **POST** /uploadimage | Upload images


# **images**
> bytearray images(x_scio_actas=x_scio_actas, key=key, type=type, id=id, ds=ds, cid=cid)

Get image

Serves images of various types (profile pic, background, UGC thumnail/content, etc).

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.image_type import ImageType
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://domain-be.glean.com/rest/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://domain-be.glean.com/rest/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ImagesApi(api_client)
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
    key = 'key_example' # str | Primary key for the image being asked. The key is returned by the API when an image is uploaded. If key is used, other parameters should not be used. (optional)
    type = openapi_client.ImageType() # ImageType | The type of image requested. Supported values are listed in ImageMetadata.type enum. (optional)
    id = 'id_example' # str | ID, if a specific entity/type is requested. The id may have different meaning for each type. for user, it is user id, for UGC, it is the id of the content, and so on. (optional)
    ds = 'ds_example' # str | A specific datasource for which an image is requested for. The ds may have different meaning for each type and can also be empty for some. (optional)
    cid = 'cid_example' # str | Content id to differentitate multiple images that can have the same type and datasource e.g. thumnail or image from content of UGC. It can also be empty. (optional)

    try:
        # Get image
        api_response = api_instance.images(x_scio_actas=x_scio_actas, key=key, type=type, id=id, ds=ds, cid=cid)
        print("The response of ImagesApi->images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **key** | **str**| Primary key for the image being asked. The key is returned by the API when an image is uploaded. If key is used, other parameters should not be used. | [optional] 
 **type** | [**ImageType**](.md)| The type of image requested. Supported values are listed in ImageMetadata.type enum. | [optional] 
 **id** | **str**| ID, if a specific entity/type is requested. The id may have different meaning for each type. for user, it is user id, for UGC, it is the id of the content, and so on. | [optional] 
 **ds** | **str**| A specific datasource for which an image is requested for. The ds may have different meaning for each type and can also be empty for some. | [optional] 
 **cid** | **str**| Content id to differentitate multiple images that can have the same type and datasource e.g. thumnail or image from content of UGC. It can also be empty. | [optional] 

### Return type

**bytearray**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request |  -  |
**401** | Not Authorized |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uploadimage**
> UploadImageResponse uploadimage(payload, x_scio_actas=x_scio_actas, type=type, id=id, ds=ds, cid=cid)

Upload images

Upload images for various types (profile pic, background, UGC thumnail/content, etc) with additional metadata.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.image_type import ImageType
from openapi_client.models.upload_image_response import UploadImageResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://domain-be.glean.com/rest/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://domain-be.glean.com/rest/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ImagesApi(api_client)
    payload = None # bytearray | Content and metadata for the image. Content is in the POST body, metadata is in the URL.
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
    type = openapi_client.ImageType() # ImageType | The type of image requested. Supported values are listed in ImageMetadata.type enum. (optional)
    id = 'id_example' # str | ID, if a specific entity/type is requested. The id may have different meaning for each type. For USER, it is user id For UGC, it is the id of the content For ICON, the doctype. (optional)
    ds = 'ds_example' # str | A specific datasource for which an image is requested for. The ds may have different meaning for each type and can also be empty for some. For USER, it is empty or datasource the icon is asked for. For UGC, it is the UGC datasource. For ICON, it is datasource instance the icon is asked for. (optional)
    cid = 'cid_example' # str | Content id to differentitate multiple images that can have the same type and datasource e.g. thumnail or image from content of UGC. It can also be empty. (optional)

    try:
        # Upload images
        api_response = api_instance.uploadimage(payload, x_scio_actas=x_scio_actas, type=type, id=id, ds=ds, cid=cid)
        print("The response of ImagesApi->uploadimage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->uploadimage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | **bytearray**| Content and metadata for the image. Content is in the POST body, metadata is in the URL. | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **type** | [**ImageType**](.md)| The type of image requested. Supported values are listed in ImageMetadata.type enum. | [optional] 
 **id** | **str**| ID, if a specific entity/type is requested. The id may have different meaning for each type. For USER, it is user id For UGC, it is the id of the content For ICON, the doctype. | [optional] 
 **ds** | **str**| A specific datasource for which an image is requested for. The ds may have different meaning for each type and can also be empty for some. For USER, it is empty or datasource the icon is asked for. For UGC, it is the UGC datasource. For ICON, it is datasource instance the icon is asked for. | [optional] 
 **cid** | **str**| Content id to differentitate multiple images that can have the same type and datasource e.g. thumnail or image from content of UGC. It can also be empty. | [optional] 

### Return type

[**UploadImageResponse**](UploadImageResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: image/*
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request |  -  |
**401** | Not Authorized |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

