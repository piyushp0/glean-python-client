# openapi_client.SearchApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autocomplete**](SearchApi.md#autocomplete) | **POST** /autocomplete | Autocomplete
[**feed**](SearchApi.md#feed) | **POST** /feed | Feed of documents and events
[**search**](SearchApi.md#search) | **POST** /search | Search


# **autocomplete**
> AutocompleteResponse autocomplete(payload, x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)

Autocomplete

Retrieve query suggestions, operators and documents for the given partially typed query.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.autocomplete_request import AutocompleteRequest
from openapi_client.models.autocomplete_response import AutocompleteResponse
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
    api_instance = openapi_client.SearchApi(api_client)
    payload = openapi_client.AutocompleteRequest() # AutocompleteRequest | Autocomplete request
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
    x_glean_auth_type = 'x_glean_auth_type_example' # str | Auth type being used to access the endpoint (should be non-empty only for global tokens). (optional)

    try:
        # Autocomplete
        api_response = api_instance.autocomplete(payload, x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)
        print("The response of SearchApi->autocomplete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->autocomplete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**AutocompleteRequest**](AutocompleteRequest.md)| Autocomplete request | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **x_glean_auth_type** | **str**| Auth type being used to access the endpoint (should be non-empty only for global tokens). | [optional] 

### Return type

[**AutocompleteResponse**](AutocompleteResponse.md)

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

# **feed**
> FeedResponse feed(payload, x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)

Feed of documents and events

The personalized feed/home includes different types of contents including suggestions, recents, calendar events and many more.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.feed_request import FeedRequest
from openapi_client.models.feed_response import FeedResponse
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
    api_instance = openapi_client.SearchApi(api_client)
    payload = openapi_client.FeedRequest() # FeedRequest | Includes request params, client data and more for making user's feed.
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
    x_glean_auth_type = 'x_glean_auth_type_example' # str | Auth type being used to access the endpoint (should be non-empty only for global tokens). (optional)

    try:
        # Feed of documents and events
        api_response = api_instance.feed(payload, x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)
        print("The response of SearchApi->feed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->feed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**FeedRequest**](FeedRequest.md)| Includes request params, client data and more for making user&#39;s feed. | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **x_glean_auth_type** | **str**| Auth type being used to access the endpoint (should be non-empty only for global tokens). | [optional] 

### Return type

[**FeedResponse**](FeedResponse.md)

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
**408** | Request Timeout |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> SearchResponse search(x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type, payload=payload)

Search

Retrieve results from the index for the given query and filters.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.search_request import SearchRequest
from openapi_client.models.search_response import SearchResponse
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
    api_instance = openapi_client.SearchApi(api_client)
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
    x_glean_auth_type = 'x_glean_auth_type_example' # str | Auth type being used to access the endpoint (should be non-empty only for global tokens). (optional)
    payload = openapi_client.SearchRequest() # SearchRequest | Search request (optional)

    try:
        # Search
        api_response = api_instance.search(x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type, payload=payload)
        print("The response of SearchApi->search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **x_glean_auth_type** | **str**| Auth type being used to access the endpoint (should be non-empty only for global tokens). | [optional] 
 **payload** | [**SearchRequest**](SearchRequest.md)| Search request | [optional] 

### Return type

[**SearchResponse**](SearchResponse.md)

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
**403** | Forbidden |  -  |
**408** | Request Timeout |  -  |
**422** | Invalid Query |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

