#!/usr/bin/env python3
""" A script for unit tests of client.GithubOrgClient class.
"""

import unittest
from parameterized import parameterized
from unittest.mock import PropertyMock, patch
import client
from client import GithubOrgClient
import requests
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos

@parameterized_class([
    {"org_payload": org_payload, "repos_payload": repos_payload,
           "expected_repos": expected_repos, "apache2_repos": apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test class for GithubOrgClient.public_repos."""

    @classmethod
    def setUpClass(cls):
        """Set up the class by mocking requests.get."""
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

        # Define side_effect to return different payloads based on URL
        def get_json_side_effect(url):
            if url == GithubOrgClient.ORG_URL.format("org_name"):
                return cls.org_payload
            elif url == GithubOrgClient._public_repos_url(cls.org_payload):
                return cls.repos_payload
            return {}
        cls.mock_get.return_value.json.side_effect = get_json_side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher after tests."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test that public_repos method returns correct repo list."""
        inst = GithubOrgClient("org_name")
        self.assertEqual(inst.public_repos(), self.expected_repos)

    def test_public_repos_with_apache2(self):
        """Test that public_repos correctly filters Apache-licensed repos."""
        inst = GithubOrgClient("org_name")
        self.assertEqual(inst.public_repos("apache-2.0"), self.apache2_repos)

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
