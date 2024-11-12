# openapi_client.VerificationApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addverificationreminder**](VerificationApi.md#addverificationreminder) | **POST** /addverificationreminder | Create verification
[**listverifications**](VerificationApi.md#listverifications) | **POST** /listverifications | List verifications
[**verify**](VerificationApi.md#verify) | **POST** /verify | Update verification


# **addverificationreminder**
> Verification addverificationreminder(payload, x_scio_actas=x_scio_actas)

Create verification

Creates a verification reminder for the document. Users can create verification reminders from different product surfaces.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.reminder_request import ReminderRequest
from openapi_client.models.verification import Verification
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
    api_instance = openapi_client.VerificationApi(api_client)
    payload = openapi_client.ReminderRequest() # ReminderRequest | Details about the reminder.
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

    try:
        # Create verification
        api_response = api_instance.addverificationreminder(payload, x_scio_actas=x_scio_actas)
        print("The response of VerificationApi->addverificationreminder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerificationApi->addverificationreminder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**ReminderRequest**](ReminderRequest.md)| Details about the reminder. | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**Verification**](Verification.md)

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
**403** | Document does not exist, does not support verification or user cannot access document |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listverifications**
> VerificationFeed listverifications(x_scio_actas=x_scio_actas, count=count)

List verifications

Returns the information to be rendered in verification dashboard. Includes information for each document owned by user regarding their verifications.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.verification_feed import VerificationFeed
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
    api_instance = openapi_client.VerificationApi(api_client)
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
    count = 56 # int | Maximum number of documents to return (optional)

    try:
        # List verifications
        api_response = api_instance.listverifications(x_scio_actas=x_scio_actas, count=count)
        print("The response of VerificationApi->listverifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerificationApi->listverifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **count** | **int**| Maximum number of documents to return | [optional] 

### Return type

[**VerificationFeed**](VerificationFeed.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request |  -  |
**401** | Not Authorized |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify**
> Verification verify(payload, x_scio_actas=x_scio_actas)

Update verification

Verify documents to keep the knowledge up to date within customer corpus.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.verification import Verification
from openapi_client.models.verify_request import VerifyRequest
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
    api_instance = openapi_client.VerificationApi(api_client)
    payload = openapi_client.VerifyRequest() # VerifyRequest | Details about the verification request.
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

    try:
        # Update verification
        api_response = api_instance.verify(payload, x_scio_actas=x_scio_actas)
        print("The response of VerificationApi->verify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerificationApi->verify: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**VerifyRequest**](VerifyRequest.md)| Details about the verification request. | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**Verification**](Verification.md)

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
**403** | Document does not exist, does not support verification or user cannot access document |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

