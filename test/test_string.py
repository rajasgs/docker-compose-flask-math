import pytest
import requests

def test_reverse_string():

    r = requests.get('http://localhost:8071/reverse?content=hello')
    r_json = r.json()

    assert r_json == 'olleh'