# openapi_client.AnswersApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createanswer**](AnswersApi.md#createanswer) | **POST** /createanswer | Create Answer
[**deleteanswer**](AnswersApi.md#deleteanswer) | **POST** /deleteanswer | Delete Answer
[**editanswer**](AnswersApi.md#editanswer) | **POST** /editanswer | Update Answer
[**getanswer**](AnswersApi.md#getanswer) | **POST** /getanswer | Read Answer
[**listanswers**](AnswersApi.md#listanswers) | **POST** /listanswers | List Answers


# **createanswer**
> Answer createanswer(payload, x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)

Create Answer

Create a user-generated Answer that contains a question and answer.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.answer import Answer
from openapi_client.models.create_answer_request import CreateAnswerRequest
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
    api_instance = openapi_client.AnswersApi(api_client)
    payload = openapi_client.CreateAnswerRequest() # CreateAnswerRequest | CreateAnswer request
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
    x_glean_auth_type = 'x_glean_auth_type_example' # str | Auth type being used to access the endpoint (should be non-empty only for global tokens). (optional)

    try:
        # Create Answer
        api_response = api_instance.createanswer(payload, x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)
        print("The response of AnswersApi->createanswer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnswersApi->createanswer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**CreateAnswerRequest**](CreateAnswerRequest.md)| CreateAnswer request | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **x_glean_auth_type** | **str**| Auth type being used to access the endpoint (should be non-empty only for global tokens). | [optional] 

### Return type

[**Answer**](Answer.md)

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

# **deleteanswer**
> deleteanswer(payload, x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)

Delete Answer

Delete an existing user-generated Answer.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.delete_answer_request import DeleteAnswerRequest
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
    api_instance = openapi_client.AnswersApi(api_client)
    payload = openapi_client.DeleteAnswerRequest() # DeleteAnswerRequest | DeleteAnswer request
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
    x_glean_auth_type = 'x_glean_auth_type_example' # str | Auth type being used to access the endpoint (should be non-empty only for global tokens). (optional)

    try:
        # Delete Answer
        api_instance.deleteanswer(payload, x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)
    except Exception as e:
        print("Exception when calling AnswersApi->deleteanswer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**DeleteAnswerRequest**](DeleteAnswerRequest.md)| DeleteAnswer request | 
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

# **editanswer**
> Answer editanswer(payload, x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)

Update Answer

Update an existing user-generated Answer.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.answer import Answer
from openapi_client.models.edit_answer_request import EditAnswerRequest
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
    api_instance = openapi_client.AnswersApi(api_client)
    payload = openapi_client.EditAnswerRequest() # EditAnswerRequest | EditAnswer request
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
    x_glean_auth_type = 'x_glean_auth_type_example' # str | Auth type being used to access the endpoint (should be non-empty only for global tokens). (optional)

    try:
        # Update Answer
        api_response = api_instance.editanswer(payload, x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)
        print("The response of AnswersApi->editanswer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnswersApi->editanswer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**EditAnswerRequest**](EditAnswerRequest.md)| EditAnswer request | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **x_glean_auth_type** | **str**| Auth type being used to access the endpoint (should be non-empty only for global tokens). | [optional] 

### Return type

[**Answer**](Answer.md)

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

# **getanswer**
> GetAnswerResponse getanswer(payload, x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)

Read Answer

Read the details of a particular Answer given its ID.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.get_answer_request import GetAnswerRequest
from openapi_client.models.get_answer_response import GetAnswerResponse
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
    api_instance = openapi_client.AnswersApi(api_client)
    payload = openapi_client.GetAnswerRequest() # GetAnswerRequest | GetAnswer request
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
    x_glean_auth_type = 'x_glean_auth_type_example' # str | Auth type being used to access the endpoint (should be non-empty only for global tokens). (optional)

    try:
        # Read Answer
        api_response = api_instance.getanswer(payload, x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)
        print("The response of AnswersApi->getanswer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnswersApi->getanswer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**GetAnswerRequest**](GetAnswerRequest.md)| GetAnswer request | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **x_glean_auth_type** | **str**| Auth type being used to access the endpoint (should be non-empty only for global tokens). | [optional] 

### Return type

[**GetAnswerResponse**](GetAnswerResponse.md)

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

# **listanswers**
> ListAnswersResponse listanswers(payload, x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)

List Answers

List Answers created by the current user.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.list_answers_request import ListAnswersRequest
from openapi_client.models.list_answers_response import ListAnswersResponse
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
    api_instance = openapi_client.AnswersApi(api_client)
    payload = openapi_client.ListAnswersRequest() # ListAnswersRequest | ListAnswers request
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
    x_glean_auth_type = 'x_glean_auth_type_example' # str | Auth type being used to access the endpoint (should be non-empty only for global tokens). (optional)

    try:
        # List Answers
        api_response = api_instance.listanswers(payload, x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)
        print("The response of AnswersApi->listanswers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnswersApi->listanswers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**ListAnswersRequest**](ListAnswersRequest.md)| ListAnswers request | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **x_glean_auth_type** | **str**| Auth type being used to access the endpoint (should be non-empty only for global tokens). | [optional] 

### Return type

[**ListAnswersResponse**](ListAnswersResponse.md)

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

