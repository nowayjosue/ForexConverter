# Example test using pytest
import pytest
from flask import Flask
from forex import is_valid_currency, convert_currency
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_valid_currency_code():
    assert is_valid_currency('USD') == True
    assert is_valid_currency('XYZ') == False

def test_convert_currency():
    result = convert_currency('USD', 'EUR', 100)
    assert isinstance(result, float)