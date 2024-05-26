#!/usr/bin/env python3
"""A module for testing the client module.
"""
import unittest
from typing import Dict
from unittest.mock import (
    MagicMock,
    patch,
    PropertyMock,
)
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
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org: str, responce: Dict, moked: MagicMock) -> None:
        """Tests the org method using Mock and parameterized"""
        moked.return_value = MagicMock(return_value=responce)
        instance = GithubOrgClient(org)
        self.assertEqual(instance.org(), responce)
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

    @patch('client.get_json',
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
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                [
                    "abc",
                    "defg",
                ],
            )
            mocked_public_repos_url.assert_called_once()
            moked_get_json.assert_called_once()
