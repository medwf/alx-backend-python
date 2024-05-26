#!/usr/bin/env python3
"""A module for testing the client module.
"""
import unittest
from typing import Dict
from unittest.mock import MagicMock, Mock, patch, PropertyMock
from parameterized import parameterized

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
            self, repo, license_key, expected) -> None:
        """this methods for testing has_license"""
        instance = GithubOrgClient("google")
        output = instance.has_license(repo, license_key)
        self.assertEqual(output, expected)


if __name__ == "__main__":
    unittest.main()
