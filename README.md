# openapi-client
# Introduction
These are the public APIs to enable implementing a custom client interface to the Glean system.

# Usage guidelines
This API is evolving fast. Glean will provide advance notice of any planned backwards incompatible changes along
with a 6-month sunset period for anything that requires developers to adopt the new versions.

# SDK
Client bindings for the API can be generated for most popular languages (Python, Java, NodeJS, etc). To do so:

Download the OpenAPI specification for the API, by clicking on one of the following options:
1. [Download JSON specification](https://api.redocly.com/registry/bundle/glean/Glean%20Client%20API%20SDK%20source/v1/openapi.json?branch=main&download=true)
2. [Download YAML specification](https://api.redocly.com/registry/bundle/glean/Glean%20Client%20API%20SDK%20source/v1/openapi.yaml?branch=main&download=true)

Use [openapi-generator-cli](https://github.com/OpenAPITools/openapi-generator-cli) to generate bindings for your language of choice, for example:
```bash shell
$ npx @openapitools/openapi-generator-cli@latest generate -i client_api.yaml -g go
```

To see available languages:
```bash shell
$ npx @openapitools/openapi-generator-cli@latest list
```

Determine the host you need to connect to. This will be the URL of the backend for your Glean deployment, for example, customer-be.glean.com


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.9.0
- Package version: 1.0.0
- Generator version: 7.7.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import openapi_client
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
    api_instance = openapi_client.ActivityApi(api_client)
    payload = openapi_client.Activity() # Activity | 

    try:
        # Report document activity
        api_instance.activity(payload)
    except ApiException as e:
        print("Exception when calling ActivityApi->activity: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://domain-be.glean.com/rest/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ActivityApi* | [**activity**](docs/ActivityApi.md#activity) | **POST** /activity | Report document activity
*ActivityApi* | [**feedback**](docs/ActivityApi.md#feedback) | **POST** /feedback | Report client activity
*AnnouncementsApi* | [**createannouncement**](docs/AnnouncementsApi.md#createannouncement) | **POST** /createannouncement | Create Announcement
*AnnouncementsApi* | [**createdraftannouncement**](docs/AnnouncementsApi.md#createdraftannouncement) | **POST** /createdraftannouncement | Create draft Announcement
*AnnouncementsApi* | [**deleteannouncement**](docs/AnnouncementsApi.md#deleteannouncement) | **POST** /deleteannouncement | Delete Announcement
*AnnouncementsApi* | [**deletedraftannouncement**](docs/AnnouncementsApi.md#deletedraftannouncement) | **POST** /deletedraftannouncement | Delete draft Announcement
*AnnouncementsApi* | [**getannouncement**](docs/AnnouncementsApi.md#getannouncement) | **POST** /getannouncement | Read Announcement
*AnnouncementsApi* | [**getdraftannouncement**](docs/AnnouncementsApi.md#getdraftannouncement) | **POST** /getdraftannouncement | Read draft Announcement
*AnnouncementsApi* | [**listannouncements**](docs/AnnouncementsApi.md#listannouncements) | **POST** /listannouncements | List Announcements
*AnnouncementsApi* | [**previewannouncement**](docs/AnnouncementsApi.md#previewannouncement) | **POST** /previewannouncement | Preview Announcement
*AnnouncementsApi* | [**previewannouncementdraft**](docs/AnnouncementsApi.md#previewannouncementdraft) | **POST** /previewannouncementdraft | Preview draft Announcement
*AnnouncementsApi* | [**publishdraftannouncement**](docs/AnnouncementsApi.md#publishdraftannouncement) | **POST** /publishdraftannouncement | Publish draft Announcement
*AnnouncementsApi* | [**unpublishannouncement**](docs/AnnouncementsApi.md#unpublishannouncement) | **POST** /unpublishannouncement | Unpublish Announcement
*AnnouncementsApi* | [**updateannouncement**](docs/AnnouncementsApi.md#updateannouncement) | **POST** /updateannouncement | Update Announcement
*AnnouncementsApi* | [**updatedraftannouncement**](docs/AnnouncementsApi.md#updatedraftannouncement) | **POST** /updatedraftannouncement | Update draft Announcement
*AnswersApi* | [**createanswer**](docs/AnswersApi.md#createanswer) | **POST** /createanswer | Create Answer
*AnswersApi* | [**createanswerboard**](docs/AnswersApi.md#createanswerboard) | **POST** /createanswerboard | Create Answer Board
*AnswersApi* | [**deleteanswer**](docs/AnswersApi.md#deleteanswer) | **POST** /deleteanswer | Delete Answer
*AnswersApi* | [**deleteanswerboards**](docs/AnswersApi.md#deleteanswerboards) | **POST** /deleteanswerboards | Delete Answer Board
*AnswersApi* | [**editanswer**](docs/AnswersApi.md#editanswer) | **POST** /editanswer | Update Answer
*AnswersApi* | [**editanswerboard**](docs/AnswersApi.md#editanswerboard) | **POST** /editanswerboard | Update Answer Board
*AnswersApi* | [**getanswer**](docs/AnswersApi.md#getanswer) | **POST** /getanswer | Read Answer
*AnswersApi* | [**getanswerboard**](docs/AnswersApi.md#getanswerboard) | **POST** /getanswerboard | Read Answer Board
*AnswersApi* | [**listanswerboards**](docs/AnswersApi.md#listanswerboards) | **POST** /listanswerboards | List Answer Boards
*AnswersApi* | [**listanswers**](docs/AnswersApi.md#listanswers) | **POST** /listanswers | List Answers
*AnswersApi* | [**previewanswer**](docs/AnswersApi.md#previewanswer) | **POST** /previewanswer | Preview Answer
*AnswersApi* | [**previewanswerdraft**](docs/AnswersApi.md#previewanswerdraft) | **POST** /previewanswerdraft | Preview draft Answer
*AnswersApi* | [**updateanswerlikes**](docs/AnswersApi.md#updateanswerlikes) | **POST** /updateanswerlikes | Update Answer likes
*AuthenticationApi* | [**createanonymoustoken**](docs/AuthenticationApi.md#createanonymoustoken) | **POST** /createanonymoustoken | Create anonymous token
*AuthenticationApi* | [**createauthtoken**](docs/AuthenticationApi.md#createauthtoken) | **POST** /createauthtoken | Create authentication token
*CalendarApi* | [**getevents**](docs/CalendarApi.md#getevents) | **POST** /getevents | Read events
*ChatApi* | [**ask**](docs/ChatApi.md#ask) | **POST** /ask | Detect and answer questions
*ChatApi* | [**chat**](docs/ChatApi.md#chat) | **POST** /chat | Chat
*ChatApi* | [**deleteallchats**](docs/ChatApi.md#deleteallchats) | **POST** /deleteallchats | Deletes all saved Chats owned by a user
*ChatApi* | [**deletechats**](docs/ChatApi.md#deletechats) | **POST** /deletechats | Deletes saved Chats
*ChatApi* | [**getchat**](docs/ChatApi.md#getchat) | **POST** /getchat | Retrieves a Chat
*ChatApi* | [**getchatapplication**](docs/ChatApi.md#getchatapplication) | **POST** /getchatapplication | Gets the metadata for a custom Chat application
*ChatApi* | [**listchats**](docs/ChatApi.md#listchats) | **POST** /listchats | Retrieves all saved Chats
*CollectionsApi* | [**addcollectionitems**](docs/CollectionsApi.md#addcollectionitems) | **POST** /addcollectionitems | Add Collection item
*CollectionsApi* | [**createcollection**](docs/CollectionsApi.md#createcollection) | **POST** /createcollection | Create Collection
*CollectionsApi* | [**deletecollection**](docs/CollectionsApi.md#deletecollection) | **POST** /deletecollection | Delete Collection
*CollectionsApi* | [**deletecollectionitem**](docs/CollectionsApi.md#deletecollectionitem) | **POST** /deletecollectionitem | Delete Collection item
*CollectionsApi* | [**editcollection**](docs/CollectionsApi.md#editcollection) | **POST** /editcollection | Update Collection
*CollectionsApi* | [**editcollectionitem**](docs/CollectionsApi.md#editcollectionitem) | **POST** /editcollectionitem | Update Collection item
*CollectionsApi* | [**editdocumentcollections**](docs/CollectionsApi.md#editdocumentcollections) | **POST** /editdocumentcollections | Update document Collections
*CollectionsApi* | [**getcollection**](docs/CollectionsApi.md#getcollection) | **POST** /getcollection | Read Collection
*CollectionsApi* | [**listcollections**](docs/CollectionsApi.md#listcollections) | **POST** /listcollections | List Collections
*CollectionsApi* | [**movecollectionitem**](docs/CollectionsApi.md#movecollectionitem) | **POST** /movecollectionitem | Move Collection item
*CollectionsApi* | [**pincollection**](docs/CollectionsApi.md#pincollection) | **POST** /pincollection | Pin Collection
*DisplayableListsApi* | [**createdisplayablelists**](docs/DisplayableListsApi.md#createdisplayablelists) | **POST** /createdisplayablelists | Create displayable lists
*DisplayableListsApi* | [**deletedisplayablelists**](docs/DisplayableListsApi.md#deletedisplayablelists) | **POST** /deletedisplayablelists | Delete displayable lists
*DisplayableListsApi* | [**getdisplayablelists**](docs/DisplayableListsApi.md#getdisplayablelists) | **POST** /getdisplayablelists | Read displayable lists
*DisplayableListsApi* | [**updatedisplayablelists**](docs/DisplayableListsApi.md#updatedisplayablelists) | **POST** /updatedisplayablelists | Update displayable lists
*DocumentsApi* | [**getdocpermissions**](docs/DocumentsApi.md#getdocpermissions) | **POST** /getdocpermissions | Read document permissions
*DocumentsApi* | [**getdocumentanalytics**](docs/DocumentsApi.md#getdocumentanalytics) | **POST** /getdocumentanalytics | Read document analytics
*DocumentsApi* | [**getdocuments**](docs/DocumentsApi.md#getdocuments) | **POST** /getdocuments | Read documents
*DocumentsApi* | [**getdocumentsbyfacets**](docs/DocumentsApi.md#getdocumentsbyfacets) | **POST** /getdocumentsbyfacets | Read documents by facets
*EntitiesApi* | [**listentities**](docs/EntitiesApi.md#listentities) | **POST** /listentities | List entities
*EntitiesApi* | [**people**](docs/EntitiesApi.md#people) | **POST** /people | Read people
*EntitiesApi* | [**teams**](docs/EntitiesApi.md#teams) | **POST** /teams | Read teams
*ImagesApi* | [**images**](docs/ImagesApi.md#images) | **GET** /images | Get image
*ImagesApi* | [**uploadimage**](docs/ImagesApi.md#uploadimage) | **POST** /uploadimage | Upload images
*InsightsApi* | [**insights**](docs/InsightsApi.md#insights) | **POST** /insights | Read insights
*MessagesApi* | [**messages**](docs/MessagesApi.md#messages) | **POST** /messages | Read messages
*PinsApi* | [**editpin**](docs/PinsApi.md#editpin) | **POST** /editpin | Update pin
*PinsApi* | [**getpin**](docs/PinsApi.md#getpin) | **POST** /getpin | Read pin
*PinsApi* | [**listpins**](docs/PinsApi.md#listpins) | **POST** /listpins | List pins
*PinsApi* | [**pin**](docs/PinsApi.md#pin) | **POST** /pin | Create pin
*PinsApi* | [**unpin**](docs/PinsApi.md#unpin) | **POST** /unpin | Delete pin
*SearchApi* | [**adminsearch**](docs/SearchApi.md#adminsearch) | **POST** /adminsearch | Search the index (admin)
*SearchApi* | [**autocomplete**](docs/SearchApi.md#autocomplete) | **POST** /autocomplete | Autocomplete
*SearchApi* | [**feed**](docs/SearchApi.md#feed) | **POST** /feed | Suggest a feed of documents and events
*SearchApi* | [**peoplesuggest**](docs/SearchApi.md#peoplesuggest) | **POST** /peoplesuggest | Suggest people
*SearchApi* | [**peoplesuggestadmin**](docs/SearchApi.md#peoplesuggestadmin) | **POST** /peoplesuggestadmin | Suggest people (admin)
*SearchApi* | [**recommendations**](docs/SearchApi.md#recommendations) | **POST** /recommendations | Recommend documents
*SearchApi* | [**search**](docs/SearchApi.md#search) | **POST** /search | Search
*ShortcutsApi* | [**createshortcut**](docs/ShortcutsApi.md#createshortcut) | **POST** /createshortcut | Create shortcut
*ShortcutsApi* | [**deleteshortcut**](docs/ShortcutsApi.md#deleteshortcut) | **POST** /deleteshortcut | Delete shortcut
*ShortcutsApi* | [**getshortcut**](docs/ShortcutsApi.md#getshortcut) | **POST** /getshortcut | Read shortcut
*ShortcutsApi* | [**getsimilarshortcuts**](docs/ShortcutsApi.md#getsimilarshortcuts) | **POST** /getsimilarshortcuts | Get similar shortcuts
*ShortcutsApi* | [**listshortcuts**](docs/ShortcutsApi.md#listshortcuts) | **POST** /listshortcuts | List shortcuts
*ShortcutsApi* | [**previewshortcut**](docs/ShortcutsApi.md#previewshortcut) | **POST** /previewshortcut | Preview shortcut
*ShortcutsApi* | [**updateshortcut**](docs/ShortcutsApi.md#updateshortcut) | **POST** /updateshortcut | Update shortcut
*SummarizeApi* | [**summarize**](docs/SummarizeApi.md#summarize) | **POST** /summarize | Summarize documents
*ToolsApi* | [**executeactiontool**](docs/ToolsApi.md#executeactiontool) | **POST** /executeactiontool | Execute Action Tool
*UserApi* | [**addcredential**](docs/UserApi.md#addcredential) | **POST** /addcredential | Create credentials
*UserApi* | [**deletequeryhistory**](docs/UserApi.md#deletequeryhistory) | **POST** /deletequeryhistory | Delete query history
*UserApi* | [**editpermissions**](docs/UserApi.md#editpermissions) | **POST** /editpermissions | Update permissions
*UserApi* | [**invite**](docs/UserApi.md#invite) | **POST** /invite | Send invitation
*UserApi* | [**publicconfig**](docs/UserApi.md#publicconfig) | **POST** /publicclientconfig | Read public client configuration
*UserApi* | [**removecredential**](docs/UserApi.md#removecredential) | **POST** /removecredential | Delete credentials
*UserApi* | [**support_email**](docs/UserApi.md#support_email) | **POST** /support | Send support email
*VerificationApi* | [**addverificationreminder**](docs/VerificationApi.md#addverificationreminder) | **POST** /addverificationreminder | Create verification
*VerificationApi* | [**listverifications**](docs/VerificationApi.md#listverifications) | **POST** /listverifications | List verifications
*VerificationApi* | [**verify**](docs/VerificationApi.md#verify) | **POST** /verify | Update verification


## Documentation For Models

 - [Activity](docs/Activity.md)
 - [ActivityEvent](docs/ActivityEvent.md)
 - [ActivityEventParams](docs/ActivityEventParams.md)
 - [AddCollectionItemsError](docs/AddCollectionItemsError.md)
 - [AddCollectionItemsRequest](docs/AddCollectionItemsRequest.md)
 - [AddCollectionItemsResponse](docs/AddCollectionItemsResponse.md)
 - [AddCredentialRequest](docs/AddCredentialRequest.md)
 - [AddedCollections](docs/AddedCollections.md)
 - [AgentClientConfig](docs/AgentClientConfig.md)
 - [AgentConfig](docs/AgentConfig.md)
 - [AiAppActionCounts](docs/AiAppActionCounts.md)
 - [AiAppsInsightsResponse](docs/AiAppsInsightsResponse.md)
 - [AiInsightsResponse](docs/AiInsightsResponse.md)
 - [AlertData](docs/AlertData.md)
 - [Announcement](docs/Announcement.md)
 - [AnnouncementAllOfViewerInfo](docs/AnnouncementAllOfViewerInfo.md)
 - [AnnouncementChannel](docs/AnnouncementChannel.md)
 - [AnnouncementError](docs/AnnouncementError.md)
 - [AnnouncementMutableProperties](docs/AnnouncementMutableProperties.md)
 - [AnonymousEvent](docs/AnonymousEvent.md)
 - [Answer](docs/Answer.md)
 - [AnswerBoard](docs/AnswerBoard.md)
 - [AnswerBoardError](docs/AnswerBoardError.md)
 - [AnswerBoardMutableProperties](docs/AnswerBoardMutableProperties.md)
 - [AnswerBoardResult](docs/AnswerBoardResult.md)
 - [AnswerCreationData](docs/AnswerCreationData.md)
 - [AnswerDocId](docs/AnswerDocId.md)
 - [AnswerId](docs/AnswerId.md)
 - [AnswerLike](docs/AnswerLike.md)
 - [AnswerLikes](docs/AnswerLikes.md)
 - [AnswerMutableProperties](docs/AnswerMutableProperties.md)
 - [AnswerResult](docs/AnswerResult.md)
 - [AppResult](docs/AppResult.md)
 - [AskExperimentalMetadata](docs/AskExperimentalMetadata.md)
 - [AskRequest](docs/AskRequest.md)
 - [AskResponse](docs/AskResponse.md)
 - [AssistantConfig](docs/AssistantConfig.md)
 - [AuthConfig](docs/AuthConfig.md)
 - [AuthToken](docs/AuthToken.md)
 - [AutocompleteRequest](docs/AutocompleteRequest.md)
 - [AutocompleteResponse](docs/AutocompleteResponse.md)
 - [AutocompleteResult](docs/AutocompleteResult.md)
 - [AutocompleteResultGroup](docs/AutocompleteResultGroup.md)
 - [BackendExperimentsContext](docs/BackendExperimentsContext.md)
 - [Badge](docs/Badge.md)
 - [Branding](docs/Branding.md)
 - [CalendarAttendee](docs/CalendarAttendee.md)
 - [CalendarAttendees](docs/CalendarAttendees.md)
 - [CalendarEvent](docs/CalendarEvent.md)
 - [ChannelInviteInfo](docs/ChannelInviteInfo.md)
 - [Chat](docs/Chat.md)
 - [ChatFile](docs/ChatFile.md)
 - [ChatFileFailureReason](docs/ChatFileFailureReason.md)
 - [ChatFileMetadata](docs/ChatFileMetadata.md)
 - [ChatFileStatus](docs/ChatFileStatus.md)
 - [ChatMessage](docs/ChatMessage.md)
 - [ChatMessageCitation](docs/ChatMessageCitation.md)
 - [ChatMessageFragment](docs/ChatMessageFragment.md)
 - [ChatMetadata](docs/ChatMetadata.md)
 - [ChatMetadataResult](docs/ChatMetadataResult.md)
 - [ChatRequest](docs/ChatRequest.md)
 - [ChatResponse](docs/ChatResponse.md)
 - [ChatResult](docs/ChatResult.md)
 - [ClientConfig](docs/ClientConfig.md)
 - [ClientConfigBrandings](docs/ClientConfigBrandings.md)
 - [ClusterGroup](docs/ClusterGroup.md)
 - [ClusterTypeEnum](docs/ClusterTypeEnum.md)
 - [Code](docs/Code.md)
 - [CodeLine](docs/CodeLine.md)
 - [Collection](docs/Collection.md)
 - [CollectionBaseMutableProperties](docs/CollectionBaseMutableProperties.md)
 - [CollectionError](docs/CollectionError.md)
 - [CollectionItem](docs/CollectionItem.md)
 - [CollectionItemDescriptor](docs/CollectionItemDescriptor.md)
 - [CollectionItemMutableProperties](docs/CollectionItemMutableProperties.md)
 - [CollectionMutableProperties](docs/CollectionMutableProperties.md)
 - [CollectionPinMetadata](docs/CollectionPinMetadata.md)
 - [CollectionPinTarget](docs/CollectionPinTarget.md)
 - [CollectionPinnableCategories](docs/CollectionPinnableCategories.md)
 - [CollectionPinnableTargets](docs/CollectionPinnableTargets.md)
 - [CollectionPinnedMetadata](docs/CollectionPinnedMetadata.md)
 - [CommunicationChannel](docs/CommunicationChannel.md)
 - [CommunicationTemplate](docs/CommunicationTemplate.md)
 - [Company](docs/Company.md)
 - [ConferenceData](docs/ConferenceData.md)
 - [ConnectorType](docs/ConnectorType.md)
 - [ContentInsightsResponse](docs/ContentInsightsResponse.md)
 - [CountInfo](docs/CountInfo.md)
 - [CreateAnnouncementRequest](docs/CreateAnnouncementRequest.md)
 - [CreateAnswerBoardRequest](docs/CreateAnswerBoardRequest.md)
 - [CreateAnswerBoardResponse](docs/CreateAnswerBoardResponse.md)
 - [CreateAnswerRequest](docs/CreateAnswerRequest.md)
 - [CreateAuthTokenResponse](docs/CreateAuthTokenResponse.md)
 - [CreateCollectionRequest](docs/CreateCollectionRequest.md)
 - [CreateCollectionResponse](docs/CreateCollectionResponse.md)
 - [CreateDisplayableListsRequest](docs/CreateDisplayableListsRequest.md)
 - [CreateDisplayableListsResponse](docs/CreateDisplayableListsResponse.md)
 - [CreateDraftAnnouncementRequest](docs/CreateDraftAnnouncementRequest.md)
 - [CreateShortcutRequest](docs/CreateShortcutRequest.md)
 - [CreateShortcutResponse](docs/CreateShortcutResponse.md)
 - [CustomDataValue](docs/CustomDataValue.md)
 - [CustomEntity](docs/CustomEntity.md)
 - [CustomEntityMetadata](docs/CustomEntityMetadata.md)
 - [CustomFieldData](docs/CustomFieldData.md)
 - [CustomFieldValue](docs/CustomFieldValue.md)
 - [CustomFieldValueHyperlink](docs/CustomFieldValueHyperlink.md)
 - [CustomFieldValuePerson](docs/CustomFieldValuePerson.md)
 - [CustomFieldValueStr](docs/CustomFieldValueStr.md)
 - [Customer](docs/Customer.md)
 - [CustomerMetadata](docs/CustomerMetadata.md)
 - [DatasourceProfile](docs/DatasourceProfile.md)
 - [DeleteAnnouncementRequest](docs/DeleteAnnouncementRequest.md)
 - [DeleteAnswerBoardsRequest](docs/DeleteAnswerBoardsRequest.md)
 - [DeleteAnswerBoardsResponse](docs/DeleteAnswerBoardsResponse.md)
 - [DeleteAnswerRequest](docs/DeleteAnswerRequest.md)
 - [DeleteChatsRequest](docs/DeleteChatsRequest.md)
 - [DeleteCollectionItemRequest](docs/DeleteCollectionItemRequest.md)
 - [DeleteCollectionItemResponse](docs/DeleteCollectionItemResponse.md)
 - [DeleteCollectionRequest](docs/DeleteCollectionRequest.md)
 - [DeleteDisplayableListsRequest](docs/DeleteDisplayableListsRequest.md)
 - [DeleteQueryHistoryError](docs/DeleteQueryHistoryError.md)
 - [DeleteQueryHistoryRequest](docs/DeleteQueryHistoryRequest.md)
 - [DeleteQueryHistoryResponse](docs/DeleteQueryHistoryResponse.md)
 - [DeleteShortcutRequest](docs/DeleteShortcutRequest.md)
 - [DisplayableList](docs/DisplayableList.md)
 - [DisplayableListConfig](docs/DisplayableListConfig.md)
 - [DisplayableListFormat](docs/DisplayableListFormat.md)
 - [DisplayableListItemUIConfig](docs/DisplayableListItemUIConfig.md)
 - [DisplayableListSource](docs/DisplayableListSource.md)
 - [Document](docs/Document.md)
 - [DocumentAnalytics](docs/DocumentAnalytics.md)
 - [DocumentContent](docs/DocumentContent.md)
 - [DocumentFacetAnalytics](docs/DocumentFacetAnalytics.md)
 - [DocumentInsight](docs/DocumentInsight.md)
 - [DocumentInteractions](docs/DocumentInteractions.md)
 - [DocumentMetadata](docs/DocumentMetadata.md)
 - [DocumentOrError](docs/DocumentOrError.md)
 - [DocumentOrErrorOneOf](docs/DocumentOrErrorOneOf.md)
 - [DocumentSection](docs/DocumentSection.md)
 - [DocumentSpec](docs/DocumentSpec.md)
 - [DocumentSpecOneOf](docs/DocumentSpecOneOf.md)
 - [DocumentSpecOneOf1](docs/DocumentSpecOneOf1.md)
 - [DocumentSpecOneOf2](docs/DocumentSpecOneOf2.md)
 - [DocumentVisibility](docs/DocumentVisibility.md)
 - [DraftProperties](docs/DraftProperties.md)
 - [EditAnswerBoardRequest](docs/EditAnswerBoardRequest.md)
 - [EditAnswerBoardResponse](docs/EditAnswerBoardResponse.md)
 - [EditAnswerRequest](docs/EditAnswerRequest.md)
 - [EditCollectionItemRequest](docs/EditCollectionItemRequest.md)
 - [EditCollectionItemResponse](docs/EditCollectionItemResponse.md)
 - [EditCollectionRequest](docs/EditCollectionRequest.md)
 - [EditCollectionResponse](docs/EditCollectionResponse.md)
 - [EditDocumentCollectionsRequest](docs/EditDocumentCollectionsRequest.md)
 - [EditDocumentCollectionsResponse](docs/EditDocumentCollectionsResponse.md)
 - [EditPermissionsRequest](docs/EditPermissionsRequest.md)
 - [EditPermissionsResponse](docs/EditPermissionsResponse.md)
 - [EditPinRequest](docs/EditPinRequest.md)
 - [EmailRequest](docs/EmailRequest.md)
 - [EmailRequestChatFeedbackPayload](docs/EmailRequestChatFeedbackPayload.md)
 - [EmailRequestFeedbackPayload](docs/EmailRequestFeedbackPayload.md)
 - [EntitiesSortOrder](docs/EntitiesSortOrder.md)
 - [ErrorInfo](docs/ErrorInfo.md)
 - [ErrorMessage](docs/ErrorMessage.md)
 - [EventClassification](docs/EventClassification.md)
 - [EventClassificationName](docs/EventClassificationName.md)
 - [EventStrategyName](docs/EventStrategyName.md)
 - [ExecuteActionToolRequest](docs/ExecuteActionToolRequest.md)
 - [ExecuteActionToolResponse](docs/ExecuteActionToolResponse.md)
 - [ExtractedQnA](docs/ExtractedQnA.md)
 - [FacetBucket](docs/FacetBucket.md)
 - [FacetBucketFilter](docs/FacetBucketFilter.md)
 - [FacetFilter](docs/FacetFilter.md)
 - [FacetFilterSet](docs/FacetFilterSet.md)
 - [FacetFilterValue](docs/FacetFilterValue.md)
 - [FacetResult](docs/FacetResult.md)
 - [FacetValue](docs/FacetValue.md)
 - [FeedEntry](docs/FeedEntry.md)
 - [FeedEntryUiConfig](docs/FeedEntryUiConfig.md)
 - [FeedRequest](docs/FeedRequest.md)
 - [FeedRequestOptions](docs/FeedRequestOptions.md)
 - [FeedRequestOptionsCategoryToResultSizeValue](docs/FeedRequestOptionsCategoryToResultSizeValue.md)
 - [FeedResponse](docs/FeedResponse.md)
 - [FeedResult](docs/FeedResult.md)
 - [Feedback](docs/Feedback.md)
 - [FeedbackChannel](docs/FeedbackChannel.md)
 - [FeedbackCustomizations](docs/FeedbackCustomizations.md)
 - [FeedbackDebugInfo](docs/FeedbackDebugInfo.md)
 - [GeneratedAttachment](docs/GeneratedAttachment.md)
 - [GeneratedAttachmentContent](docs/GeneratedAttachmentContent.md)
 - [GeneratedQna](docs/GeneratedQna.md)
 - [GetAnnouncementRequest](docs/GetAnnouncementRequest.md)
 - [GetAnnouncementResponse](docs/GetAnnouncementResponse.md)
 - [GetAnswerBoardRequest](docs/GetAnswerBoardRequest.md)
 - [GetAnswerBoardResponse](docs/GetAnswerBoardResponse.md)
 - [GetAnswerError](docs/GetAnswerError.md)
 - [GetAnswerRequest](docs/GetAnswerRequest.md)
 - [GetAnswerResponse](docs/GetAnswerResponse.md)
 - [GetChatApplicationRequest](docs/GetChatApplicationRequest.md)
 - [GetChatApplicationResponse](docs/GetChatApplicationResponse.md)
 - [GetChatRequest](docs/GetChatRequest.md)
 - [GetChatResponse](docs/GetChatResponse.md)
 - [GetCollectionRequest](docs/GetCollectionRequest.md)
 - [GetCollectionResponse](docs/GetCollectionResponse.md)
 - [GetDisplayableListsRequest](docs/GetDisplayableListsRequest.md)
 - [GetDisplayableListsResponse](docs/GetDisplayableListsResponse.md)
 - [GetDocPermissionsRequest](docs/GetDocPermissionsRequest.md)
 - [GetDocPermissionsResponse](docs/GetDocPermissionsResponse.md)
 - [GetDocumentAnalyticsRequest](docs/GetDocumentAnalyticsRequest.md)
 - [GetDocumentAnalyticsResponse](docs/GetDocumentAnalyticsResponse.md)
 - [GetDocumentsByFacetsRequest](docs/GetDocumentsByFacetsRequest.md)
 - [GetDocumentsByFacetsResponse](docs/GetDocumentsByFacetsResponse.md)
 - [GetDocumentsRequest](docs/GetDocumentsRequest.md)
 - [GetDocumentsResponse](docs/GetDocumentsResponse.md)
 - [GetDraftAnnouncementResponse](docs/GetDraftAnnouncementResponse.md)
 - [GetEventsRequest](docs/GetEventsRequest.md)
 - [GetEventsResponse](docs/GetEventsResponse.md)
 - [GetPinRequest](docs/GetPinRequest.md)
 - [GetPinResponse](docs/GetPinResponse.md)
 - [GetShortcutRequest](docs/GetShortcutRequest.md)
 - [GetShortcutRequestOneOf](docs/GetShortcutRequestOneOf.md)
 - [GetShortcutResponse](docs/GetShortcutResponse.md)
 - [GetSimilarShortcutsRequest](docs/GetSimilarShortcutsRequest.md)
 - [GetSimilarShortcutsResponse](docs/GetSimilarShortcutsResponse.md)
 - [GrantPermission](docs/GrantPermission.md)
 - [Group](docs/Group.md)
 - [GroupType](docs/GroupType.md)
 - [IconConfig](docs/IconConfig.md)
 - [ImageMetadata](docs/ImageMetadata.md)
 - [ImageType](docs/ImageType.md)
 - [IndexStatus](docs/IndexStatus.md)
 - [InsightsAiAppRequestOptions](docs/InsightsAiAppRequestOptions.md)
 - [InsightsRequest](docs/InsightsRequest.md)
 - [InsightsResponse](docs/InsightsResponse.md)
 - [InvalidOperatorValueError](docs/InvalidOperatorValueError.md)
 - [InviteInfo](docs/InviteInfo.md)
 - [InviteRequest](docs/InviteRequest.md)
 - [LabeledCountInfo](docs/LabeledCountInfo.md)
 - [ListAnnouncementsRequest](docs/ListAnnouncementsRequest.md)
 - [ListAnnouncementsResponse](docs/ListAnnouncementsResponse.md)
 - [ListAnswerBoardsRequest](docs/ListAnswerBoardsRequest.md)
 - [ListAnswerBoardsResponse](docs/ListAnswerBoardsResponse.md)
 - [ListAnswersRequest](docs/ListAnswersRequest.md)
 - [ListAnswersResponse](docs/ListAnswersResponse.md)
 - [ListChatsResponse](docs/ListChatsResponse.md)
 - [ListCollectionsRequest](docs/ListCollectionsRequest.md)
 - [ListCollectionsResponse](docs/ListCollectionsResponse.md)
 - [ListEntitiesRequest](docs/ListEntitiesRequest.md)
 - [ListEntitiesResponse](docs/ListEntitiesResponse.md)
 - [ListPinsResponse](docs/ListPinsResponse.md)
 - [ListShortcutsPaginatedRequest](docs/ListShortcutsPaginatedRequest.md)
 - [ListShortcutsPaginatedResponse](docs/ListShortcutsPaginatedResponse.md)
 - [ManualFeedbackInfo](docs/ManualFeedbackInfo.md)
 - [MessagesRequest](docs/MessagesRequest.md)
 - [MessagesResponse](docs/MessagesResponse.md)
 - [MoveCollectionItemRequest](docs/MoveCollectionItemRequest.md)
 - [MoveCollectionItemResponse](docs/MoveCollectionItemResponse.md)
 - [ObjectPermissions](docs/ObjectPermissions.md)
 - [OperatorMetadata](docs/OperatorMetadata.md)
 - [OperatorScope](docs/OperatorScope.md)
 - [PeopleFilters](docs/PeopleFilters.md)
 - [PeopleRequest](docs/PeopleRequest.md)
 - [PeopleResponse](docs/PeopleResponse.md)
 - [PeopleSuggestRequest](docs/PeopleSuggestRequest.md)
 - [PeopleSuggestResponse](docs/PeopleSuggestResponse.md)
 - [PeopleSuggestionCategory](docs/PeopleSuggestionCategory.md)
 - [Period](docs/Period.md)
 - [PermissionedObject](docs/PermissionedObject.md)
 - [Permissions](docs/Permissions.md)
 - [Person](docs/Person.md)
 - [PersonDistance](docs/PersonDistance.md)
 - [PersonMetadata](docs/PersonMetadata.md)
 - [PersonObject](docs/PersonObject.md)
 - [PersonSuggestionList](docs/PersonSuggestionList.md)
 - [PersonTeam](docs/PersonTeam.md)
 - [PersonToTeamRelationship](docs/PersonToTeamRelationship.md)
 - [PinCollectionRequest](docs/PinCollectionRequest.md)
 - [PinDocument](docs/PinDocument.md)
 - [PinDocumentMutableProperties](docs/PinDocumentMutableProperties.md)
 - [PinRequest](docs/PinRequest.md)
 - [PossibleValue](docs/PossibleValue.md)
 - [PreviewShortcutResponse](docs/PreviewShortcutResponse.md)
 - [PreviewStructuredTextRequest](docs/PreviewStructuredTextRequest.md)
 - [PreviewStructuredTextResponse](docs/PreviewStructuredTextResponse.md)
 - [PreviewUgcRequest](docs/PreviewUgcRequest.md)
 - [PreviewUgcResponse](docs/PreviewUgcResponse.md)
 - [ProductTerm](docs/ProductTerm.md)
 - [ProductTerms](docs/ProductTerms.md)
 - [PublicConfigRequest](docs/PublicConfigRequest.md)
 - [PublishDraftAnnouncementRequest](docs/PublishDraftAnnouncementRequest.md)
 - [QueryInsight](docs/QueryInsight.md)
 - [QueryInsightsResponse](docs/QueryInsightsResponse.md)
 - [QuerySuggestion](docs/QuerySuggestion.md)
 - [QuerySuggestionList](docs/QuerySuggestionList.md)
 - [Quicklink](docs/Quicklink.md)
 - [Reaction](docs/Reaction.md)
 - [ReadPermission](docs/ReadPermission.md)
 - [RecommendationsRequest](docs/RecommendationsRequest.md)
 - [RecommendationsRequestOptions](docs/RecommendationsRequestOptions.md)
 - [RecommendationsResponse](docs/RecommendationsResponse.md)
 - [ReferenceRange](docs/ReferenceRange.md)
 - [RelatedDocuments](docs/RelatedDocuments.md)
 - [RelatedObject](docs/RelatedObject.md)
 - [RelatedObjectEdge](docs/RelatedObjectEdge.md)
 - [RelatedObjectMetadata](docs/RelatedObjectMetadata.md)
 - [RelatedObjects](docs/RelatedObjects.md)
 - [RelatedQuestion](docs/RelatedQuestion.md)
 - [Reminder](docs/Reminder.md)
 - [ReminderRequest](docs/ReminderRequest.md)
 - [RemoveCredentialRequest](docs/RemoveCredentialRequest.md)
 - [RemovedCollections](docs/RemovedCollections.md)
 - [ResolutionStep](docs/ResolutionStep.md)
 - [RestrictionFilters](docs/RestrictionFilters.md)
 - [Result](docs/Result.md)
 - [ResultTab](docs/ResultTab.md)
 - [ResultsDescription](docs/ResultsDescription.md)
 - [ResultsRequest](docs/ResultsRequest.md)
 - [ResultsResponse](docs/ResultsResponse.md)
 - [ScopeType](docs/ScopeType.md)
 - [SearchRequest](docs/SearchRequest.md)
 - [SearchRequestInputDetails](docs/SearchRequestInputDetails.md)
 - [SearchRequestOptions](docs/SearchRequestOptions.md)
 - [SearchResponse](docs/SearchResponse.md)
 - [SearchResponseMetadata](docs/SearchResponseMetadata.md)
 - [SearchResult](docs/SearchResult.md)
 - [SearchResultProminenceEnum](docs/SearchResultProminenceEnum.md)
 - [SearchResultSnippet](docs/SearchResultSnippet.md)
 - [SearchWarning](docs/SearchWarning.md)
 - [SeenFeedbackInfo](docs/SeenFeedbackInfo.md)
 - [SessionInfo](docs/SessionInfo.md)
 - [Share](docs/Share.md)
 - [Shortcut](docs/Shortcut.md)
 - [ShortcutError](docs/ShortcutError.md)
 - [ShortcutInsight](docs/ShortcutInsight.md)
 - [ShortcutInsightsResponse](docs/ShortcutInsightsResponse.md)
 - [ShortcutMetadata](docs/ShortcutMetadata.md)
 - [ShortcutMutableProperties](docs/ShortcutMutableProperties.md)
 - [ShortcutsConfig](docs/ShortcutsConfig.md)
 - [ShortcutsPaginationMetadata](docs/ShortcutsPaginationMetadata.md)
 - [SocialNetwork](docs/SocialNetwork.md)
 - [SortOptions](docs/SortOptions.md)
 - [StructuredLink](docs/StructuredLink.md)
 - [StructuredLocation](docs/StructuredLocation.md)
 - [StructuredResult](docs/StructuredResult.md)
 - [StructuredText](docs/StructuredText.md)
 - [StructuredTextItem](docs/StructuredTextItem.md)
 - [StructuredTextMutableProperties](docs/StructuredTextMutableProperties.md)
 - [SummarizeRequest](docs/SummarizeRequest.md)
 - [SummarizeResponse](docs/SummarizeResponse.md)
 - [SummarizeResponseError](docs/SummarizeResponseError.md)
 - [Summary](docs/Summary.md)
 - [Team](docs/Team.md)
 - [TeamEmail](docs/TeamEmail.md)
 - [TeamsRequest](docs/TeamsRequest.md)
 - [TeamsResponse](docs/TeamsResponse.md)
 - [TextRange](docs/TextRange.md)
 - [Themes](docs/Themes.md)
 - [Thumbnail](docs/Thumbnail.md)
 - [TimeInterval](docs/TimeInterval.md)
 - [TimePoint](docs/TimePoint.md)
 - [ToolConfig](docs/ToolConfig.md)
 - [ToolMetadata](docs/ToolMetadata.md)
 - [ToolsConfig](docs/ToolsConfig.md)
 - [UgcDraft](docs/UgcDraft.md)
 - [UgcType](docs/UgcType.md)
 - [Unpin](docs/Unpin.md)
 - [UnpublishAnnouncementRequest](docs/UnpublishAnnouncementRequest.md)
 - [UpdateAnnouncementRequest](docs/UpdateAnnouncementRequest.md)
 - [UpdateAnswerLikesRequest](docs/UpdateAnswerLikesRequest.md)
 - [UpdateAnswerLikesResponse](docs/UpdateAnswerLikesResponse.md)
 - [UpdateDisplayableListsRequest](docs/UpdateDisplayableListsRequest.md)
 - [UpdateDisplayableListsResponse](docs/UpdateDisplayableListsResponse.md)
 - [UpdateDraftAnnouncementRequest](docs/UpdateDraftAnnouncementRequest.md)
 - [UpdateShortcutRequest](docs/UpdateShortcutRequest.md)
 - [UpdateShortcutResponse](docs/UpdateShortcutResponse.md)
 - [UploadImageResponse](docs/UploadImageResponse.md)
 - [User](docs/User.md)
 - [UserActivity](docs/UserActivity.md)
 - [UserActivityInsight](docs/UserActivityInsight.md)
 - [UserGeneratedContentId](docs/UserGeneratedContentId.md)
 - [UserInsightsResponse](docs/UserInsightsResponse.md)
 - [UserOutreachConfig](docs/UserOutreachConfig.md)
 - [UserRole](docs/UserRole.md)
 - [UserRoleSpecification](docs/UserRoleSpecification.md)
 - [UserViewInfo](docs/UserViewInfo.md)
 - [Verification](docs/Verification.md)
 - [VerificationFeed](docs/VerificationFeed.md)
 - [VerificationMetadata](docs/VerificationMetadata.md)
 - [VerifyRequest](docs/VerifyRequest.md)
 - [ViewerInfo](docs/ViewerInfo.md)
 - [WriteAction](docs/WriteAction.md)
 - [WriteActionParameter](docs/WriteActionParameter.md)
 - [WritePermission](docs/WritePermission.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="BearerAuth"></a>
### BearerAuth

- **Type**: Bearer authentication


## Author

support@glean.com


