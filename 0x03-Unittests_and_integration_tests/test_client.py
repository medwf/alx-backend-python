#!/usr/bin/env python3
"""A module for testing the client module."""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from typing import Dict
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient define
        For testing class GithubOrgClient
    """

    @parameterized.expand([
        ('google', {'api': 'google'}),
        ('abc', {'api': 'abc'}),
    ])
    @patch('client.get_json', )
    def test_org(self, org: str, responce: Dict, moked: MagicMock) -> None:
        """test org methods"""
        moked.return_value = MagicMock(return_value=responce)
        instance = GithubOrgClient(org)
        self.assertEqual(instance.org(), responce)
        moked.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )
