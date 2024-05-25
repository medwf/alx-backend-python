#!/usr/bin/env python3
"""test client module"""
import unittest
from unittest.mock import patch, Mock, MagicMock
from parameterized import parameterized
from typing import Dict
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient define"""

    @parameterized.expand([
        ('google', {'api': 'google'}),
        ('abc', {'api': 'abc'}),
    ])
    @patch('client.get_json')
    def test_org(self, org: str, responce: Dict, moked: MagicMock) -> None:
        """test client"""
        moked.return_value = MagicMock(return_value=responce)
        instance = GithubOrgClient(org)
        self.assertEqual(instance.org(), responce)
        moked.assert_called_once()

