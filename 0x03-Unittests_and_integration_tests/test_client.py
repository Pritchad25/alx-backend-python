#!/usr/bin/env python3
""" The Unittest module """

from unittest import TestCase, mock
from unittest.mock import patch, Mock
from parameterized import parameterized

import client
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """A Class for testing GithubOrgClient """

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_json):
        """ The Test method returns correct output """
        gc = GithubOrgClient(org_name)
        gc.org()
        mock_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
            )
        self.assertEqual(wrong_output, e.exception)


class TestGetJson(TestCase):
    """ A Class for testing get_json function """
    # order of args: test_url, test_payload
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """The Test method returns correct output """
        # create Mock object with json method that returns test_payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        # function calls requests.get, need patch to get mock return value
        with patch('requests.get', return_value=mock_response):
            real_response = get_json(test_url)
            self.assertEqual(real_response, test_payload)
            # check that mocked method called once per input
            mock_response.json.assert_called_once()


class TestMemoize(TestCase):
    """A Class for testing memoization """

    def test_memoize(self):
        """A Tests memoize function """

        class TestClass:
            """A Test class """

            def a_method(self):
                """A Method to always return 42 """
                return 42

            @memoize
            def a_property(self):
                """ The property returns memoized property """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as patched:
            test_class = TestClass()
            real_return = test_class.a_property
            real_return = test_class.a_property

            self.assertEqual(real_return, 42)
            patched.assert_called_once()
