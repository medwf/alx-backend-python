#!/usr/bin/env python3
"""A module for testing the client module.
"""
import unittest
from typing import Dict
from unittest.mock import MagicMock, Mock, patch, PropertyMock
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD

from client import (
    GithubOrgClient
)


class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient define
        For testing class GithubOrgClient
    """

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch(
        "client.get_json", return_value={"payload": True}
    )
    def test_org(self, org: str, moked: Mock) -> None:
        """Tests the org method using Mock and parameterized"""
        instance = GithubOrgClient(org)
        self.assertEqual(instance.org, {"payload": True})
        moked.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

    def test_public_repos_url(self) -> None:
        """Tests the _public_repos_url method"""
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
        ) as mockProp:

            mockProp.return_value = {
                "repos_url": "https://api.github.com/orgs/google/repos"
            }

            self.assertEqual(
                GithubOrgClient('google')._public_repos_url,
                "https://api.github.com/orgs/google/repos"
            )

    @patch(
        'client.get_json',
        return_value=[{'name': 'abc'}, {'name': 'defg'}]
    )
    def test_public_repos(self, moked_get_json) -> None:
        """tests the public repos method"""
        with patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=PropertyMock,
        ) as mocked_public_repos_url:
            mocked_public_repos_url.return_value = (
                "https://api.github.com/orgs/google/repos"
            )
            inst = GithubOrgClient("google")
            self.assertEqual(
                inst.public_repos(), ["abc", "defg"]
            )
            mocked_public_repos_url.assert_called_once()
            moked_get_json.assert_called_once()

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(
            self, repo: Dict, license_key: str, expected: bool) -> None:
        """this methods for testing has_license"""
        instance = GithubOrgClient("google")
        output = instance.has_license(repo, license_key)
        self.assertEqual(output, expected)


@parameterized_class(
    ('org_payload', 'repos_payload',
     'expected_repos', 'apache2_repos'
     ), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """doc doc doc"""
    @classmethod
    def setUpClass(cls):
        """doc doc doc"""
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            """doc doc doc"""
            class MockResponse:
                def __init__(self, json_data):
                    self.json_data = json_data

                def json(self):
                    return self.json_data

            if url.endswith("/orgs/google"):
                return MockResponse(cls.org_payload)
            elif url.endswith("/orgs/google/repos"):
                return MockResponse(cls.repos_payload)
            else:
                return None

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """doc doc doc"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """doc doc doc"""
        instance = GithubOrgClient("google")
        self.assertEqual(instance.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """doc doc doc"""
        instance = GithubOrgClient("google")
        self.assertEqual(instance.public_repos(license="apache-2.0"),
                         self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
