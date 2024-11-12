# openapi_client.ShortcutsApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createshortcut**](ShortcutsApi.md#createshortcut) | **POST** /createshortcut | Create shortcut
[**deleteshortcut**](ShortcutsApi.md#deleteshortcut) | **POST** /deleteshortcut | Delete shortcut
[**getshortcut**](ShortcutsApi.md#getshortcut) | **POST** /getshortcut | Read shortcut
[**listshortcuts**](ShortcutsApi.md#listshortcuts) | **POST** /listshortcuts | List shortcuts


# **createshortcut**
> CreateShortcutResponse createshortcut(payload, x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)

Create shortcut

Create a user-generated shortcut that contains an alias and destination URL.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.create_shortcut_request import CreateShortcutRequest
from openapi_client.models.create_shortcut_response import CreateShortcutResponse
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
    api_instance = openapi_client.ShortcutsApi(api_client)
    payload = openapi_client.CreateShortcutRequest() # CreateShortcutRequest | CreateShortcut request
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
    x_glean_auth_type = 'x_glean_auth_type_example' # str | Auth type being used to access the endpoint (should be non-empty only for global tokens). (optional)

    try:
        # Create shortcut
        api_response = api_instance.createshortcut(payload, x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)
        print("The response of ShortcutsApi->createshortcut:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShortcutsApi->createshortcut: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**CreateShortcutRequest**](CreateShortcutRequest.md)| CreateShortcut request | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **x_glean_auth_type** | **str**| Auth type being used to access the endpoint (should be non-empty only for global tokens). | [optional] 

### Return type

[**CreateShortcutResponse**](CreateShortcutResponse.md)

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

# **deleteshortcut**
> deleteshortcut(payload, x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)

Delete shortcut

Delete an existing user-generated shortcut.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.delete_shortcut_request import DeleteShortcutRequest
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
    api_instance = openapi_client.ShortcutsApi(api_client)
    payload = openapi_client.DeleteShortcutRequest() # DeleteShortcutRequest | DeleteShortcut request
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
    x_glean_auth_type = 'x_glean_auth_type_example' # str | Auth type being used to access the endpoint (should be non-empty only for global tokens). (optional)

    try:
        # Delete shortcut
        api_instance.deleteshortcut(payload, x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)
    except Exception as e:
        print("Exception when calling ShortcutsApi->deleteshortcut: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**DeleteShortcutRequest**](DeleteShortcutRequest.md)| DeleteShortcut request | 
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

# **getshortcut**
> GetShortcutResponse getshortcut(payload, x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)

Read shortcut

Read a particular shortcut's details given its ID.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.get_shortcut_request import GetShortcutRequest
from openapi_client.models.get_shortcut_response import GetShortcutResponse
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
    api_instance = openapi_client.ShortcutsApi(api_client)
    payload = openapi_client.GetShortcutRequest() # GetShortcutRequest | GetShortcut request
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
    x_glean_auth_type = 'x_glean_auth_type_example' # str | Auth type being used to access the endpoint (should be non-empty only for global tokens). (optional)

    try:
        # Read shortcut
        api_response = api_instance.getshortcut(payload, x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)
        print("The response of ShortcutsApi->getshortcut:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShortcutsApi->getshortcut: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**GetShortcutRequest**](GetShortcutRequest.md)| GetShortcut request | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **x_glean_auth_type** | **str**| Auth type being used to access the endpoint (should be non-empty only for global tokens). | [optional] 

### Return type

[**GetShortcutResponse**](GetShortcutResponse.md)

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

# **listshortcuts**
> ListShortcutsPaginatedResponse listshortcuts(payload, x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)

List shortcuts

List shortcuts editable/owned by the currently authenticated user.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.list_shortcuts_paginated_request import ListShortcutsPaginatedRequest
from openapi_client.models.list_shortcuts_paginated_response import ListShortcutsPaginatedResponse
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
    api_instance = openapi_client.ShortcutsApi(api_client)
    payload = openapi_client.ListShortcutsPaginatedRequest() # ListShortcutsPaginatedRequest | Filters, sorters, paging params required for pagination
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
    x_glean_auth_type = 'x_glean_auth_type_example' # str | Auth type being used to access the endpoint (should be non-empty only for global tokens). (optional)

    try:
        # List shortcuts
        api_response = api_instance.listshortcuts(payload, x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)
        print("The response of ShortcutsApi->listshortcuts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShortcutsApi->listshortcuts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**ListShortcutsPaginatedRequest**](ListShortcutsPaginatedRequest.md)| Filters, sorters, paging params required for pagination | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **x_glean_auth_type** | **str**| Auth type being used to access the endpoint (should be non-empty only for global tokens). | [optional] 

### Return type

[**ListShortcutsPaginatedResponse**](ListShortcutsPaginatedResponse.md)

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

