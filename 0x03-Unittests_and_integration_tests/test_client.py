#!/usr/bin/env python3
""" A script for unit tests of client.GithubOrgClient class.
"""

import unittest
from parameterized import parameterized
from unittest.mock import PropertyMock, patch
import client
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Unit test class for GithubOrgClient."""

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False)  # Edge case: repo without a license
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test GithubOrgClient.has_license method."""
        inst = GithubOrgClient("org_name")
        self.assertEqual(inst.has_license(repo, license_key), expected)

    @patch('client.get_json')
    def test_org(self, input, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        test_class = GithubOrgClient(input)
        test_class.org()
        mock_get_json.assert_called_once_with(test_class.ORG_URL)
    def test_public_repos_url(self):
        """Unit test for GithubOrgClient._public_repos_url."""
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_property:
            mock_property.return_value = 'mock_value'
            inst = GithubOrgClient('org_name')

            self.assertEqual(inst._public_repos_url, 'mock_value')
    
    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Unit test for GithubOrgClient.public_repos."""
        mock_get_json.return_value = [
                {"name": "repo1"},
                {"name": "repo2"},
                {"name": "repo3"}
        ]

        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_public_url:
            mock_public_url.return_value = 'mock_url'
            inst = GithubOrgClient('org_name')

            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertEqual(inst.public_repos(), expected_repos)

            # Ensure that both mocks were called correctly
            mock_public_url.assert_called_once()
            mock_get_json.assert_called_once_with('mock_url')

if __name__ == '__main__':
    unittest.main()
