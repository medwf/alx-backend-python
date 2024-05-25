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

    @patch('client.get_json')
    def test_public_repos(self, moked_get_json: MagicMock) -> None:
        """tests the public repos method"""
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "node_id": "MDEwOlJlcG9zaXRvcnk3Njk3MTQ5",
                    "name": "episodes.dart",
                    "full_name": "google/episodes.dart",
                    "private": False,
                    "license": {
                        "key": "bsd-3-clause",
                        "name": "BSD 3-Clause \"New\" or \"Revised\" License",
                        "spdx_id": "BSD-3-Clause",
                        "url": "https://api.github.com/licenses/bsd-3-clause",
                        "node_id": "MDc6TGljZW5zZTU="
                    },
                    "forks": 22,
                    "open_issues": 0,
                    "watchers": 12,
                    "default_branch": "master",
                    "permissions": {
                        "admin": False,
                        "push": False,
                        "pull": True
                    }
                },
                {
                    "id": 7776515,
                    "node_id": "MDEwOlJlcG9zaXRvcnk3Nzc2NTE1",
                    "name": "cpp-netlib",
                    "full_name": "google/cpp-netlib",
                    "license": {
                        "key": "bsl-1.0",
                        "name": "Boost Software License 1.0",
                        "spdx_id": "BSL-1.0",
                        "url": "https://api.github.com/licenses/bsl-1.0",
                        "node_id": "MDc6TGljZW5zZTI4"
                    },
                    "forks": 59,
                    "open_issues": 0,
                    "watchers": 292,
                    "default_branch": "master",
                    "permissions": {
                        "admin": False,
                        "push": False,
                        "pull": True
                    }
                }
            ]
        }
        moked_get_json.return_value = test_payload["repos"]
        with patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=PropertyMock,
        ) as mocked_public_repos_url:
            mocked_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                [
                    "episodes.dart",
                    "cpp-netlib",
                ],
            )
            mocked_public_repos_url.assert_called_once()
        moked_get_json.assert_called_once()
