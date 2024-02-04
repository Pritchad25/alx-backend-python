#!/usr/bin/env python3
""" A script for unit tests of uclient.GithubOrgClient class.
"""

import unittest
from parameterized import parameterized
from unittest import mock
from unittest.mock import PropertyMock, patch
import requests
import client
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """A class that implements the test_org method.
    """
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """A test method that GithubOrgClient.org returns the correct value."""
        test_class = GithubOrgClient(input)
        test_class.org()
        mock.called_with_once(test_class.ORG_URL)

    def test_public_repos_url(self):
        """A unit-test method for GithubOrgClient._public_repos_url"""
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_property:
            mock_property.return_value = 'mock_value'
            inst = GithubOrgClient('org_name')

            self.assertEqual(inst._public_repos_url, 'mock_value')


if __name__ == '__main__':
    unittest.main()
