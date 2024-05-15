# openapi_client.DisplayableListsApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createdisplayablelists**](DisplayableListsApi.md#createdisplayablelists) | **POST** /createdisplayablelists | Create displayable lists
[**deletedisplayablelists**](DisplayableListsApi.md#deletedisplayablelists) | **POST** /deletedisplayablelists | Delete displayable lists
[**getdisplayablelists**](DisplayableListsApi.md#getdisplayablelists) | **POST** /getdisplayablelists | Read displayable lists
[**updatedisplayablelists**](DisplayableListsApi.md#updatedisplayablelists) | **POST** /updatedisplayablelists | Update displayable lists


# **createdisplayablelists**
> CreateDisplayableListsResponse createdisplayablelists(payload, x_scio_actas=x_scio_actas)

Create displayable lists

Create one or more lists that can be display on the home page.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.create_displayable_lists_request import CreateDisplayableListsRequest
from openapi_client.models.create_displayable_lists_response import CreateDisplayableListsResponse
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
    api_instance = openapi_client.DisplayableListsApi(api_client)
    payload = openapi_client.CreateDisplayableListsRequest() # CreateDisplayableListsRequest | Create new displayable lists
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

    try:
        # Create displayable lists
        api_response = api_instance.createdisplayablelists(payload, x_scio_actas=x_scio_actas)
        print("The response of DisplayableListsApi->createdisplayablelists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisplayableListsApi->createdisplayablelists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**CreateDisplayableListsRequest**](CreateDisplayableListsRequest.md)| Create new displayable lists | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**CreateDisplayableListsResponse**](CreateDisplayableListsResponse.md)

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
**403** | Forbidden from creating displayable list configs |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletedisplayablelists**
> deletedisplayablelists(payload, x_scio_actas=x_scio_actas)

Delete displayable lists

Delete one or more displayable lists.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.delete_displayable_lists_request import DeleteDisplayableListsRequest
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
    api_instance = openapi_client.DisplayableListsApi(api_client)
    payload = openapi_client.DeleteDisplayableListsRequest() # DeleteDisplayableListsRequest | Updated version of the displayable list configs.
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

    try:
        # Delete displayable lists
        api_instance.deletedisplayablelists(payload, x_scio_actas=x_scio_actas)
    except Exception as e:
        print("Exception when calling DisplayableListsApi->deletedisplayablelists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**DeleteDisplayableListsRequest**](DeleteDisplayableListsRequest.md)| Updated version of the displayable list configs. | 
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
**403** | Forbidden from deleting displayable list configs |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getdisplayablelists**
> GetDisplayableListsResponse getdisplayablelists(payload, x_scio_actas=x_scio_actas)

Read displayable lists

Read the details of the displayable lists with the given IDs.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.get_displayable_lists_request import GetDisplayableListsRequest
from openapi_client.models.get_displayable_lists_response import GetDisplayableListsResponse
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
    api_instance = openapi_client.DisplayableListsApi(api_client)
    payload = openapi_client.GetDisplayableListsRequest() # GetDisplayableListsRequest | 
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

    try:
        # Read displayable lists
        api_response = api_instance.getdisplayablelists(payload, x_scio_actas=x_scio_actas)
        print("The response of DisplayableListsApi->getdisplayablelists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisplayableListsApi->getdisplayablelists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**GetDisplayableListsRequest**](GetDisplayableListsRequest.md)|  | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**GetDisplayableListsResponse**](GetDisplayableListsResponse.md)

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
**403** | Forbidden from seeing configs |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updatedisplayablelists**
> UpdateDisplayableListsResponse updatedisplayablelists(payload, x_scio_actas=x_scio_actas)

Update displayable lists

Update one or more displayable lists with all fields from request fields.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.update_displayable_lists_request import UpdateDisplayableListsRequest
from openapi_client.models.update_displayable_lists_response import UpdateDisplayableListsResponse
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
    api_instance = openapi_client.DisplayableListsApi(api_client)
    payload = openapi_client.UpdateDisplayableListsRequest() # UpdateDisplayableListsRequest | Updated version of the displayable list configs.
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

    try:
        # Update displayable lists
        api_response = api_instance.updatedisplayablelists(payload, x_scio_actas=x_scio_actas)
        print("The response of DisplayableListsApi->updatedisplayablelists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisplayableListsApi->updatedisplayablelists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**UpdateDisplayableListsRequest**](UpdateDisplayableListsRequest.md)| Updated version of the displayable list configs. | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**UpdateDisplayableListsResponse**](UpdateDisplayableListsResponse.md)

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
**403** | Forbidden from updating displayable list configs |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

