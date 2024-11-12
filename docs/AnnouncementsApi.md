# openapi_client.AnnouncementsApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createannouncement**](AnnouncementsApi.md#createannouncement) | **POST** /createannouncement | Create Announcement
[**createdraftannouncement**](AnnouncementsApi.md#createdraftannouncement) | **POST** /createdraftannouncement | Create draft Announcement
[**deleteannouncement**](AnnouncementsApi.md#deleteannouncement) | **POST** /deleteannouncement | Delete Announcement
[**deletedraftannouncement**](AnnouncementsApi.md#deletedraftannouncement) | **POST** /deletedraftannouncement | Delete draft Announcement
[**getannouncement**](AnnouncementsApi.md#getannouncement) | **POST** /getannouncement | Read Announcement
[**getdraftannouncement**](AnnouncementsApi.md#getdraftannouncement) | **POST** /getdraftannouncement | Read draft Announcement
[**listannouncements**](AnnouncementsApi.md#listannouncements) | **POST** /listannouncements | List Announcements
[**previewannouncement**](AnnouncementsApi.md#previewannouncement) | **POST** /previewannouncement | Preview Announcement
[**previewannouncementdraft**](AnnouncementsApi.md#previewannouncementdraft) | **POST** /previewannouncementdraft | Preview draft Announcement
[**publishdraftannouncement**](AnnouncementsApi.md#publishdraftannouncement) | **POST** /publishdraftannouncement | Publish draft Announcement
[**unpublishannouncement**](AnnouncementsApi.md#unpublishannouncement) | **POST** /unpublishannouncement | Unpublish Announcement
[**updateannouncement**](AnnouncementsApi.md#updateannouncement) | **POST** /updateannouncement | Update Announcement
[**updatedraftannouncement**](AnnouncementsApi.md#updatedraftannouncement) | **POST** /updatedraftannouncement | Update draft Announcement


# **createannouncement**
> Announcement createannouncement(payload, x_scio_actas=x_scio_actas)

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

    try:
        # Create Announcement
        api_response = api_instance.createannouncement(payload, x_scio_actas=x_scio_actas)
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

# **createdraftannouncement**
> Announcement createdraftannouncement(payload, x_scio_actas=x_scio_actas)

Create draft Announcement

Create a draft of a textual announcement visible to some set of users based on department and location.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.announcement import Announcement
from openapi_client.models.create_draft_announcement_request import CreateDraftAnnouncementRequest
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
    payload = openapi_client.CreateDraftAnnouncementRequest() # CreateDraftAnnouncementRequest | Draft announcement content
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

    try:
        # Create draft Announcement
        api_response = api_instance.createdraftannouncement(payload, x_scio_actas=x_scio_actas)
        print("The response of AnnouncementsApi->createdraftannouncement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnouncementsApi->createdraftannouncement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**CreateDraftAnnouncementRequest**](CreateDraftAnnouncementRequest.md)| Draft announcement content | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

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
> deleteannouncement(payload, x_scio_actas=x_scio_actas)

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

    try:
        # Delete Announcement
        api_instance.deleteannouncement(payload, x_scio_actas=x_scio_actas)
    except Exception as e:
        print("Exception when calling AnnouncementsApi->deleteannouncement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**DeleteAnnouncementRequest**](DeleteAnnouncementRequest.md)| Delete announcement request | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

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

# **deletedraftannouncement**
> deletedraftannouncement(payload, x_scio_actas=x_scio_actas)

Delete draft Announcement

Delete an existing user-generated draft Announcement.

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
    payload = openapi_client.DeleteAnnouncementRequest() # DeleteAnnouncementRequest | Delete draft announcement request
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

    try:
        # Delete draft Announcement
        api_instance.deletedraftannouncement(payload, x_scio_actas=x_scio_actas)
    except Exception as e:
        print("Exception when calling AnnouncementsApi->deletedraftannouncement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**DeleteAnnouncementRequest**](DeleteAnnouncementRequest.md)| Delete draft announcement request | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

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

# **getannouncement**
> GetAnnouncementResponse getannouncement(payload, x_scio_actas=x_scio_actas)

Read Announcement

Read the details of an Announcement given its ID.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.get_announcement_request import GetAnnouncementRequest
from openapi_client.models.get_announcement_response import GetAnnouncementResponse
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
    payload = openapi_client.GetAnnouncementRequest() # GetAnnouncementRequest | GetAnnouncement request
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

    try:
        # Read Announcement
        api_response = api_instance.getannouncement(payload, x_scio_actas=x_scio_actas)
        print("The response of AnnouncementsApi->getannouncement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnouncementsApi->getannouncement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**GetAnnouncementRequest**](GetAnnouncementRequest.md)| GetAnnouncement request | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**GetAnnouncementResponse**](GetAnnouncementResponse.md)

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

# **getdraftannouncement**
> GetDraftAnnouncementResponse getdraftannouncement(payload, x_scio_actas=x_scio_actas)

Read draft Announcement

Read the details of an existing user-generated draft Announcement.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.get_announcement_request import GetAnnouncementRequest
from openapi_client.models.get_draft_announcement_response import GetDraftAnnouncementResponse
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
    payload = openapi_client.GetAnnouncementRequest() # GetAnnouncementRequest | Get draft announcement request
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

    try:
        # Read draft Announcement
        api_response = api_instance.getdraftannouncement(payload, x_scio_actas=x_scio_actas)
        print("The response of AnnouncementsApi->getdraftannouncement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnouncementsApi->getdraftannouncement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**GetAnnouncementRequest**](GetAnnouncementRequest.md)| Get draft announcement request | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**GetDraftAnnouncementResponse**](GetDraftAnnouncementResponse.md)

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

# **listannouncements**
> ListAnnouncementsResponse listannouncements(payload, x_scio_actas=x_scio_actas)

List Announcements

List Announcement details for all Announcements matching the given criteria.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.list_announcements_request import ListAnnouncementsRequest
from openapi_client.models.list_announcements_response import ListAnnouncementsResponse
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
    payload = openapi_client.ListAnnouncementsRequest() # ListAnnouncementsRequest | Includes request params for querying announcements.
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

    try:
        # List Announcements
        api_response = api_instance.listannouncements(payload, x_scio_actas=x_scio_actas)
        print("The response of AnnouncementsApi->listannouncements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnouncementsApi->listannouncements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**ListAnnouncementsRequest**](ListAnnouncementsRequest.md)| Includes request params for querying announcements. | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**ListAnnouncementsResponse**](ListAnnouncementsResponse.md)

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

# **previewannouncement**
> PreviewStructuredTextResponse previewannouncement(payload, x_scio_actas=x_scio_actas)

Preview Announcement

Generate a preview for a user-generated Announcement from structured text.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.preview_structured_text_request import PreviewStructuredTextRequest
from openapi_client.models.preview_structured_text_response import PreviewStructuredTextResponse
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
    payload = openapi_client.PreviewStructuredTextRequest() # PreviewStructuredTextRequest | preview structured text request
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

    try:
        # Preview Announcement
        api_response = api_instance.previewannouncement(payload, x_scio_actas=x_scio_actas)
        print("The response of AnnouncementsApi->previewannouncement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnouncementsApi->previewannouncement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**PreviewStructuredTextRequest**](PreviewStructuredTextRequest.md)| preview structured text request | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**PreviewStructuredTextResponse**](PreviewStructuredTextResponse.md)

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

# **previewannouncementdraft**
> PreviewUgcResponse previewannouncementdraft(payload, x_scio_actas=x_scio_actas)

Preview draft Announcement

Generates a preview for a user-generated Announcement from a draft.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.preview_ugc_request import PreviewUgcRequest
from openapi_client.models.preview_ugc_response import PreviewUgcResponse
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
    payload = openapi_client.PreviewUgcRequest() # PreviewUgcRequest | preview announcement request
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

    try:
        # Preview draft Announcement
        api_response = api_instance.previewannouncementdraft(payload, x_scio_actas=x_scio_actas)
        print("The response of AnnouncementsApi->previewannouncementdraft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnouncementsApi->previewannouncementdraft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**PreviewUgcRequest**](PreviewUgcRequest.md)| preview announcement request | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**PreviewUgcResponse**](PreviewUgcResponse.md)

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

# **publishdraftannouncement**
> publishdraftannouncement(payload, x_scio_actas=x_scio_actas)

Publish draft Announcement

Promote a draft Announcement to be visible to others.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.publish_draft_announcement_request import PublishDraftAnnouncementRequest
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
    payload = openapi_client.PublishDraftAnnouncementRequest() # PublishDraftAnnouncementRequest | Publish draft announcement content.
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

    try:
        # Publish draft Announcement
        api_instance.publishdraftannouncement(payload, x_scio_actas=x_scio_actas)
    except Exception as e:
        print("Exception when calling AnnouncementsApi->publishdraftannouncement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**PublishDraftAnnouncementRequest**](PublishDraftAnnouncementRequest.md)| Publish draft announcement content. | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

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

# **unpublishannouncement**
> Announcement unpublishannouncement(payload, x_scio_actas=x_scio_actas)

Unpublish Announcement

Unpublish an Announcement to hide it from users.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.announcement import Announcement
from openapi_client.models.unpublish_announcement_request import UnpublishAnnouncementRequest
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
    payload = openapi_client.UnpublishAnnouncementRequest() # UnpublishAnnouncementRequest | Unpublish announcement content.
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

    try:
        # Unpublish Announcement
        api_response = api_instance.unpublishannouncement(payload, x_scio_actas=x_scio_actas)
        print("The response of AnnouncementsApi->unpublishannouncement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnouncementsApi->unpublishannouncement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**UnpublishAnnouncementRequest**](UnpublishAnnouncementRequest.md)| Unpublish announcement content. | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

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

# **updateannouncement**
> Announcement updateannouncement(payload, x_scio_actas=x_scio_actas)

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

    try:
        # Update Announcement
        api_response = api_instance.updateannouncement(payload, x_scio_actas=x_scio_actas)
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

# **updatedraftannouncement**
> Announcement updatedraftannouncement(payload, x_scio_actas=x_scio_actas)

Update draft Announcement

Update a textual Announcement visible to some set of users based on department and location.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.announcement import Announcement
from openapi_client.models.update_draft_announcement_request import UpdateDraftAnnouncementRequest
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
    payload = openapi_client.UpdateDraftAnnouncementRequest() # UpdateDraftAnnouncementRequest | Draft announcement content. DraftId needs to be specified.
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

    try:
        # Update draft Announcement
        api_response = api_instance.updatedraftannouncement(payload, x_scio_actas=x_scio_actas)
        print("The response of AnnouncementsApi->updatedraftannouncement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnouncementsApi->updatedraftannouncement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**UpdateDraftAnnouncementRequest**](UpdateDraftAnnouncementRequest.md)| Draft announcement content. DraftId needs to be specified. | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

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

