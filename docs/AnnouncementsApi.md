# openapi_client.AnnouncementsApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createannouncement**](AnnouncementsApi.md#createannouncement) | **POST** /createannouncement | Create Announcement
[**deleteannouncement**](AnnouncementsApi.md#deleteannouncement) | **POST** /deleteannouncement | Delete Announcement
[**updateannouncement**](AnnouncementsApi.md#updateannouncement) | **POST** /updateannouncement | Update Announcement


# **createannouncement**
> Announcement createannouncement(payload, x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)

Create Announcement

Create a textual announcement visible to some set of users based on department and location.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.announcement import Announcement
from openapi_client.models.create_announcement_request import CreateAnnouncementRequest
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
    api_instance = openapi_client.AnnouncementsApi(api_client)
    payload = openapi_client.CreateAnnouncementRequest() # CreateAnnouncementRequest | Announcement content
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
    x_glean_auth_type = 'x_glean_auth_type_example' # str | Auth type being used to access the endpoint (should be non-empty only for global tokens). (optional)

    try:
        # Create Announcement
        api_response = api_instance.createannouncement(payload, x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)
        print("The response of AnnouncementsApi->createannouncement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnouncementsApi->createannouncement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**CreateAnnouncementRequest**](CreateAnnouncementRequest.md)| Announcement content | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **x_glean_auth_type** | **str**| Auth type being used to access the endpoint (should be non-empty only for global tokens). | [optional] 

### Return type

[**Announcement**](Announcement.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request |  -  |
**401** | Not Authorized |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deleteannouncement**
> deleteannouncement(payload, x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)

Delete Announcement

Delete an existing user-generated announcement.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.delete_announcement_request import DeleteAnnouncementRequest
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
    api_instance = openapi_client.AnnouncementsApi(api_client)
    payload = openapi_client.DeleteAnnouncementRequest() # DeleteAnnouncementRequest | Delete announcement request
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
    x_glean_auth_type = 'x_glean_auth_type_example' # str | Auth type being used to access the endpoint (should be non-empty only for global tokens). (optional)

    try:
        # Delete Announcement
        api_instance.deleteannouncement(payload, x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)
    except Exception as e:
        print("Exception when calling AnnouncementsApi->deleteannouncement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**DeleteAnnouncementRequest**](DeleteAnnouncementRequest.md)| Delete announcement request | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **x_glean_auth_type** | **str**| Auth type being used to access the endpoint (should be non-empty only for global tokens). | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request |  -  |
**401** | Not Authorized |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updateannouncement**
> Announcement updateannouncement(payload, x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)

Update Announcement

Update a textual announcement visible to some set of users based on department and location.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.announcement import Announcement
from openapi_client.models.update_announcement_request import UpdateAnnouncementRequest
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
    api_instance = openapi_client.AnnouncementsApi(api_client)
    payload = openapi_client.UpdateAnnouncementRequest() # UpdateAnnouncementRequest | Announcement content. Id need to be specified for the announcement.
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
    x_glean_auth_type = 'x_glean_auth_type_example' # str | Auth type being used to access the endpoint (should be non-empty only for global tokens). (optional)

    try:
        # Update Announcement
        api_response = api_instance.updateannouncement(payload, x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)
        print("The response of AnnouncementsApi->updateannouncement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnouncementsApi->updateannouncement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**UpdateAnnouncementRequest**](UpdateAnnouncementRequest.md)| Announcement content. Id need to be specified for the announcement. | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **x_glean_auth_type** | **str**| Auth type being used to access the endpoint (should be non-empty only for global tokens). | [optional] 

### Return type

[**Announcement**](Announcement.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request |  -  |
**401** | Not Authorized |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

