"""
Unit Tests for Config
"""

from common.config import PROJECT_ID, DATABASE_PREFIX

def test_config():
  assert PROJECT_ID is not None
  assert DATABASE_PREFIX is not None
