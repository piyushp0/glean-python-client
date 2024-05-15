# openapi_client.EntitiesApi

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createteams**](EntitiesApi.md#createteams) | **POST** /createteams | Create teams
[**customentities**](EntitiesApi.md#customentities) | **POST** /customentities | Read custom entities
[**deleteteams**](EntitiesApi.md#deleteteams) | **POST** /deleteteams | Delete teams
[**downloadentities**](EntitiesApi.md#downloadentities) | **GET** /downloadentities | Download entities
[**listentities**](EntitiesApi.md#listentities) | **POST** /listentities | List entities
[**people**](EntitiesApi.md#people) | **POST** /people | Read people
[**teams**](EntitiesApi.md#teams) | **POST** /teams | Read teams


# **createteams**
> CreateTeamsResponse createteams(payload, x_scio_actas=x_scio_actas)

Create teams

Create the given teams.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.create_teams_request import CreateTeamsRequest
from openapi_client.models.create_teams_response import CreateTeamsResponse
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
    api_instance = openapi_client.EntitiesApi(api_client)
    payload = openapi_client.CreateTeamsRequest() # CreateTeamsRequest | Teams to be created
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

    try:
        # Create teams
        api_response = api_instance.createteams(payload, x_scio_actas=x_scio_actas)
        print("The response of EntitiesApi->createteams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->createteams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**CreateTeamsRequest**](CreateTeamsRequest.md)| Teams to be created | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**CreateTeamsResponse**](CreateTeamsResponse.md)

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

# **customentities**
> CustomEntitiesResponse customentities(payload, x_scio_actas=x_scio_actas)

Read custom entities

Read the details of the custom entities with the given IDs.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.custom_entities_request import CustomEntitiesRequest
from openapi_client.models.custom_entities_response import CustomEntitiesResponse
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
    api_instance = openapi_client.EntitiesApi(api_client)
    payload = openapi_client.CustomEntitiesRequest() # CustomEntitiesRequest | Custom entities request
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

    try:
        # Read custom entities
        api_response = api_instance.customentities(payload, x_scio_actas=x_scio_actas)
        print("The response of EntitiesApi->customentities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->customentities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**CustomEntitiesRequest**](CustomEntitiesRequest.md)| Custom entities request | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**CustomEntitiesResponse**](CustomEntitiesResponse.md)

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

# **deleteteams**
> DeleteTeamsResponse deleteteams(payload, x_scio_actas=x_scio_actas)

Delete teams

Delete the given teams.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.delete_teams_request import DeleteTeamsRequest
from openapi_client.models.delete_teams_response import DeleteTeamsResponse
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
    api_instance = openapi_client.EntitiesApi(api_client)
    payload = openapi_client.DeleteTeamsRequest() # DeleteTeamsRequest | Teams to be deleted
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

    try:
        # Delete teams
        api_response = api_instance.deleteteams(payload, x_scio_actas=x_scio_actas)
        print("The response of EntitiesApi->deleteteams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->deleteteams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**DeleteTeamsRequest**](DeleteTeamsRequest.md)| Teams to be deleted | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**DeleteTeamsResponse**](DeleteTeamsResponse.md)

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

# **downloadentities**
> str downloadentities(entity_type, x_scio_actas=x_scio_actas)

Download entities

Download a list of all entities of the specified type. Currently only supports people.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.entities_type_enum import EntitiesTypeEnum
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
    api_instance = openapi_client.EntitiesApi(api_client)
    entity_type = openapi_client.EntitiesTypeEnum() # EntitiesTypeEnum | Entity type the requested CSV should be populated with
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

    try:
        # Download entities
        api_response = api_instance.downloadentities(entity_type, x_scio_actas=x_scio_actas)
        print("The response of EntitiesApi->downloadentities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->downloadentities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | [**EntitiesTypeEnum**](.md)| Entity type the requested CSV should be populated with | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

**str**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listentities**
> ListEntitiesResponse listentities(payload, x_scio_actas=x_scio_actas)

List entities

List some set of details for all entities that fit the given criteria and return in the requested order. Does not support negation in filters, assumes relation type EQUALS.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.list_entities_request import ListEntitiesRequest
from openapi_client.models.list_entities_response import ListEntitiesResponse
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
    api_instance = openapi_client.EntitiesApi(api_client)
    payload = openapi_client.ListEntitiesRequest() # ListEntitiesRequest | List people request
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

    try:
        # List entities
        api_response = api_instance.listentities(payload, x_scio_actas=x_scio_actas)
        print("The response of EntitiesApi->listentities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->listentities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**ListEntitiesRequest**](ListEntitiesRequest.md)| List people request | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**ListEntitiesResponse**](ListEntitiesResponse.md)

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

# **people**
> PeopleResponse people(payload, x_scio_actas=x_scio_actas)

Read people

Read people details for the given IDs.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.people_request import PeopleRequest
from openapi_client.models.people_response import PeopleResponse
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
    api_instance = openapi_client.EntitiesApi(api_client)
    payload = openapi_client.PeopleRequest() # PeopleRequest | People request
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

    try:
        # Read people
        api_response = api_instance.people(payload, x_scio_actas=x_scio_actas)
        print("The response of EntitiesApi->people:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->people: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**PeopleRequest**](PeopleRequest.md)| People request | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**PeopleResponse**](PeopleResponse.md)

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

# **teams**
> TeamsResponse teams(payload, x_scio_actas=x_scio_actas)

Read teams

Read the details of the teams with the given IDs.

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.teams_request import TeamsRequest
from openapi_client.models.teams_response import TeamsResponse
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
    api_instance = openapi_client.EntitiesApi(api_client)
    payload = openapi_client.TeamsRequest() # TeamsRequest | Teams request
    x_scio_actas = 'x_scio_actas_example' # str | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). (optional)

    try:
        # Read teams
        api_response = api_instance.teams(payload, x_scio_actas=x_scio_actas)
        print("The response of EntitiesApi->teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**TeamsRequest**](TeamsRequest.md)| Teams request | 
 **x_scio_actas** | **str**| Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). | [optional] 

### Return type

[**TeamsResponse**](TeamsResponse.md)

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

