# coding: utf-8

"""
    Glean Client API

    # Introduction These are the public APIs to enable implementing a custom client interface to the Glean system.  # Usage guidelines This API is evolving fast. Glean will provide advance notice of any planned backwards incompatible changes along with a 6-month sunset period for anything that requires developers to adopt the new versions.  # SDK Client bindings for the API can be generated for most popular languages (Python, Java, NodeJS, etc). To do so:  Download the OpenAPI specification for the API, by clicking on one of the following options: 1. [Download JSON specification](https://api.redocly.com/registry/bundle/glean/Glean%20Client%20API%20SDK%20source/v1/openapi.json?branch=main&download=true) 2. [Download YAML specification](https://api.redocly.com/registry/bundle/glean/Glean%20Client%20API%20SDK%20source/v1/openapi.yaml?branch=main&download=true)  Use [openapi-generator-cli](https://github.com/OpenAPITools/openapi-generator-cli) to generate bindings for your language of choice, for example: ```bash shell $ npx @openapitools/openapi-generator-cli@latest generate -i client_api.yaml -g go ```  To see available languages: ```bash shell $ npx @openapitools/openapi-generator-cli@latest list ```  Determine the host you need to connect to. This will be the URL of the backend for your Glean deployment, for example, customer-be.glean.com 

    The version of the OpenAPI document: 0.9.0
    Contact: support@glean.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.chat_api import ChatApi


class TestChatApi(unittest.TestCase):
    """ChatApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ChatApi()

    def tearDown(self) -> None:
        pass

    def test_ask(self) -> None:
        """Test case for ask

        Detect and answer questions
        """
        pass

    def test_chat(self) -> None:
        """Test case for chat

        Chat
        """
        pass

    def test_deleteallchats(self) -> None:
        """Test case for deleteallchats

        Deletes all saved Chats owned by a user
        """
        pass

    def test_deletechatfiles(self) -> None:
        """Test case for deletechatfiles

        Delete files uploaded by a user for chat.
        """
        pass

    def test_deletechats(self) -> None:
        """Test case for deletechats

        Deletes saved Chats
        """
        pass

    def test_getchat(self) -> None:
        """Test case for getchat

        Retrieves a Chat
        """
        pass

    def test_getchatapplication(self) -> None:
        """Test case for getchatapplication

        Gets the metadata for a custom Chat application
        """
        pass

    def test_getchatfiles(self) -> None:
        """Test case for getchatfiles

        Get files uploaded by a user for Chat.
        """
        pass

    def test_listchats(self) -> None:
        """Test case for listchats

        Retrieves all saved Chats
        """
        pass

    def test_uploadchatfiles(self) -> None:
        """Test case for uploadchatfiles

        Upload files for Chat.
        """
        pass


if __name__ == '__main__':
    unittest.main()
