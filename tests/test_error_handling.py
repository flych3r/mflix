"""
Test file for database methods written in db.py

All test methods must receive client as an argument,
otherwise the database variable won't be configured correctly
"""
import pytest

from mflix.db import get_movie


@pytest.mark.error_handling
def test_no_error(client):
    response = get_movie('foobar')
    assert response is None
