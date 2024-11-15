# openapi_client.DocumentsApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getdocpermissions**](DocumentsApi.md#getdocpermissions) | **POST** /getdocpermissions | Read document permissions
[**getdocumentanalytics**](DocumentsApi.md#getdocumentanalytics) | **POST** /getdocumentanalytics | Read document analytics
[**getdocuments**](DocumentsApi.md#getdocuments) | **POST** /getdocuments | Read documents
[**getdocumentsbyfacets**](DocumentsApi.md#getdocumentsbyfacets) | **POST** /getdocumentsbyfacets | Read documents by facets


# **getdocpermissions**
> GetDocPermissionsResponse getdocpermissions(payload, x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)

Read document permissions

Read the emails of all users who have access to the given document.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.get_doc_permissions_request import GetDocPermissionsRequest
from openapi_client.models.get_doc_permissions_response import GetDocPermissionsResponse
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
    api_instance = openapi_client.DocumentsApi(api_client)
    payload = openapi_client.GetDocPermissionsRequest() # GetDocPermissionsRequest | Document permissions request
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
    x_glean_auth_type = 'x_glean_auth_type_example' # str | Auth type being used to access the endpoint (should be non-empty only for global tokens). (optional)

    try:
        # Read document permissions
        api_response = api_instance.getdocpermissions(payload, x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)
        print("The response of DocumentsApi->getdocpermissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->getdocpermissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**GetDocPermissionsRequest**](GetDocPermissionsRequest.md)| Document permissions request | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **x_glean_auth_type** | **str**| Auth type being used to access the endpoint (should be non-empty only for global tokens). | [optional] 

### Return type

[**GetDocPermissionsResponse**](GetDocPermissionsResponse.md)

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getdocumentanalytics**
> GetDocumentAnalyticsResponse getdocumentanalytics(x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type, payload=payload)

Read document analytics

Read the document analytics information for the given list of Glean Document IDs or URLs specified in the request

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.get_document_analytics_request import GetDocumentAnalyticsRequest
from openapi_client.models.get_document_analytics_response import GetDocumentAnalyticsResponse
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
    api_instance = openapi_client.DocumentsApi(api_client)
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
    x_glean_auth_type = 'x_glean_auth_type_example' # str | Auth type being used to access the endpoint (should be non-empty only for global tokens). (optional)
    payload = openapi_client.GetDocumentAnalyticsRequest() # GetDocumentAnalyticsRequest | Information about analytics requested. (optional)

    try:
        # Read document analytics
        api_response = api_instance.getdocumentanalytics(x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type, payload=payload)
        print("The response of DocumentsApi->getdocumentanalytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->getdocumentanalytics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **x_glean_auth_type** | **str**| Auth type being used to access the endpoint (should be non-empty only for global tokens). | [optional] 
 **payload** | [**GetDocumentAnalyticsRequest**](GetDocumentAnalyticsRequest.md)| Information about analytics requested. | [optional] 

### Return type

[**GetDocumentAnalyticsResponse**](GetDocumentAnalyticsResponse.md)

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

# **getdocuments**
> GetDocumentsResponse getdocuments(x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type, payload=payload)

Read documents

Read the documents including metadata (does not include enhanced metadata via `/documentmetadata`) for the given list of Glean Document IDs or URLs specified in the request.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.get_documents_request import GetDocumentsRequest
from openapi_client.models.get_documents_response import GetDocumentsResponse
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
    api_instance = openapi_client.DocumentsApi(api_client)
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
    x_glean_auth_type = 'x_glean_auth_type_example' # str | Auth type being used to access the endpoint (should be non-empty only for global tokens). (optional)
    payload = openapi_client.GetDocumentsRequest() # GetDocumentsRequest | Information about documents requested. (optional)

    try:
        # Read documents
        api_response = api_instance.getdocuments(x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type, payload=payload)
        print("The response of DocumentsApi->getdocuments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->getdocuments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **x_glean_auth_type** | **str**| Auth type being used to access the endpoint (should be non-empty only for global tokens). | [optional] 
 **payload** | [**GetDocumentsRequest**](GetDocumentsRequest.md)| Information about documents requested. | [optional] 

### Return type

[**GetDocumentsResponse**](GetDocumentsResponse.md)

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
**403** | Documents does not exist, or user cannot access documents. |  -  |
**404** | All documents requested are not found. |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getdocumentsbyfacets**
> GetDocumentsByFacetsResponse getdocumentsbyfacets(x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type, payload=payload)

Read documents by facets

Read the documents including metadata (does not include enhanced metadata via `/documentmetadata`) macthing the given facet conditions.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.get_documents_by_facets_request import GetDocumentsByFacetsRequest
from openapi_client.models.get_documents_by_facets_response import GetDocumentsByFacetsResponse
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
    api_instance = openapi_client.DocumentsApi(api_client)
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
    x_glean_auth_type = 'x_glean_auth_type_example' # str | Auth type being used to access the endpoint (should be non-empty only for global tokens). (optional)
    payload = openapi_client.GetDocumentsByFacetsRequest() # GetDocumentsByFacetsRequest | Information about facet conditions for documents to be retrieved. (optional)

    try:
        # Read documents by facets
        api_response = api_instance.getdocumentsbyfacets(x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type, payload=payload)
        print("The response of DocumentsApi->getdocumentsbyfacets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->getdocumentsbyfacets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **x_glean_auth_type** | **str**| Auth type being used to access the endpoint (should be non-empty only for global tokens). | [optional] 
 **payload** | [**GetDocumentsByFacetsRequest**](GetDocumentsByFacetsRequest.md)| Information about facet conditions for documents to be retrieved. | [optional] 

### Return type

[**GetDocumentsByFacetsResponse**](GetDocumentsByFacetsResponse.md)

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
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

