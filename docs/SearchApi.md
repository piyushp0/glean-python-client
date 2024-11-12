# openapi_client.SearchApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminsearch**](SearchApi.md#adminsearch) | **POST** /adminsearch | Search the index (admin)
[**autocomplete**](SearchApi.md#autocomplete) | **POST** /autocomplete | Autocomplete
[**feed**](SearchApi.md#feed) | **POST** /feed | Suggest a feed of documents and events
[**peoplesuggest**](SearchApi.md#peoplesuggest) | **POST** /peoplesuggest | Suggest people
[**peoplesuggestadmin**](SearchApi.md#peoplesuggestadmin) | **POST** /peoplesuggestadmin | Suggest people (admin)
[**recommendations**](SearchApi.md#recommendations) | **POST** /recommendations | Recommend documents
[**search**](SearchApi.md#search) | **POST** /search | Search


# **adminsearch**
> SearchResponse adminsearch(x_scio_actas=x_scio_actas, payload=payload)

Search the index (admin)

Retrieves results for search query without respect for permissions. This is available only to privileged users.

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
    payload = openapi_client.SearchRequest() # SearchRequest | Admin search request (optional)

    try:
        # Search the index (admin)
        api_response = api_instance.adminsearch(x_scio_actas=x_scio_actas, payload=payload)
        print("The response of SearchApi->adminsearch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->adminsearch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **payload** | [**SearchRequest**](SearchRequest.md)| Admin search request | [optional] 

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
**422** | Invalid Query |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **autocomplete**
> AutocompleteResponse autocomplete(payload, x_scio_actas=x_scio_actas)

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

    try:
        # Autocomplete
        api_response = api_instance.autocomplete(payload, x_scio_actas=x_scio_actas)
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
> FeedResponse feed(payload, x_scio_actas=x_scio_actas)

Suggest a feed of documents and events

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

    try:
        # Suggest a feed of documents and events
        api_response = api_instance.feed(payload, x_scio_actas=x_scio_actas)
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

# **peoplesuggest**
> PeopleSuggestResponse peoplesuggest(payload, x_scio_actas=x_scio_actas)

Suggest people

Retrieves a list of suggested people for given type. Includes information about the persons.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.people_suggest_request import PeopleSuggestRequest
from openapi_client.models.people_suggest_response import PeopleSuggestResponse
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
    payload = openapi_client.PeopleSuggestRequest() # PeopleSuggestRequest | Includes request params for type of suggestions.
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

    try:
        # Suggest people
        api_response = api_instance.peoplesuggest(payload, x_scio_actas=x_scio_actas)
        print("The response of SearchApi->peoplesuggest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->peoplesuggest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**PeopleSuggestRequest**](PeopleSuggestRequest.md)| Includes request params for type of suggestions. | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**PeopleSuggestResponse**](PeopleSuggestResponse.md)

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

# **peoplesuggestadmin**
> PeopleSuggestResponse peoplesuggestadmin(payload, x_scio_actas=x_scio_actas)

Suggest people (admin)

Returns a list of suggested people for given type for admin's view. Includes information about the persons.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.people_suggest_request import PeopleSuggestRequest
from openapi_client.models.people_suggest_response import PeopleSuggestResponse
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
    payload = openapi_client.PeopleSuggestRequest() # PeopleSuggestRequest | Includes request params for type of suggestions.
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

    try:
        # Suggest people (admin)
        api_response = api_instance.peoplesuggestadmin(payload, x_scio_actas=x_scio_actas)
        print("The response of SearchApi->peoplesuggestadmin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->peoplesuggestadmin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**PeopleSuggestRequest**](PeopleSuggestRequest.md)| Includes request params for type of suggestions. | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**PeopleSuggestResponse**](PeopleSuggestResponse.md)

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

# **recommendations**
> RecommendationsResponse recommendations(x_scio_actas=x_scio_actas, payload=payload)

Recommend documents

Retrieve recommended documents for the given URL or Glean Document ID.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.recommendations_request import RecommendationsRequest
from openapi_client.models.recommendations_response import RecommendationsResponse
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
    payload = openapi_client.RecommendationsRequest() # RecommendationsRequest | Recommendations request (optional)

    try:
        # Recommend documents
        api_response = api_instance.recommendations(x_scio_actas=x_scio_actas, payload=payload)
        print("The response of SearchApi->recommendations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->recommendations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **payload** | [**RecommendationsRequest**](RecommendationsRequest.md)| Recommendations request | [optional] 

### Return type

[**RecommendationsResponse**](RecommendationsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**202** | Accepted. The Retry-After header has a hint about when the response will be available |  -  |
**204** | There are no recommendations for this URL |  -  |
**400** | Invalid request |  -  |
**401** | Not Authorized |  -  |
**403** | Document does not exist or user cannot access document |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> SearchResponse search(x_scio_actas=x_scio_actas, payload=payload)

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
    payload = openapi_client.SearchRequest() # SearchRequest | Search request (optional)

    try:
        # Search
        api_response = api_instance.search(x_scio_actas=x_scio_actas, payload=payload)
        print("The response of SearchApi->search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
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

