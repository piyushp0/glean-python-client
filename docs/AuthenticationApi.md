# openapi_client.AuthenticationApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createauthtoken**](AuthenticationApi.md#createauthtoken) | **POST** /createauthtoken | Create authentication token


# **createauthtoken**
> CreateAuthTokenResponse createauthtoken(x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)

Create authentication token

Creates an authentication token for the authenticated user.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.create_auth_token_response import CreateAuthTokenResponse
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
    api_instance = openapi_client.AuthenticationApi(api_client)
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)
    x_glean_auth_type = 'x_glean_auth_type_example' # str | Auth type being used to access the endpoint (should be non-empty only for global tokens). (optional)

    try:
        # Create authentication token
        api_response = api_instance.createauthtoken(x_scio_actas=x_scio_actas, x_glean_auth_type=x_glean_auth_type)
        print("The response of AuthenticationApi->createauthtoken:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->createauthtoken: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 
 **x_glean_auth_type** | **str**| Auth type being used to access the endpoint (should be non-empty only for global tokens). | [optional] 

### Return type

[**CreateAuthTokenResponse**](CreateAuthTokenResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid Request |  -  |
**401** | Not Authorized |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

