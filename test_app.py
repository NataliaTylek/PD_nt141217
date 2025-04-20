import pytest
import requests

BASE_URL = "http://127.0.0.1:4000/api/v1.0/predict"

def test_valid_prediction():
    response = requests.get(BASE_URL, params={"x1": 3.0, "x2": 4.0})
    assert response.status_code == 200
    data = response.json()
    assert data["features"] == {"x1": 3.0, "x2": 4.0}
    assert data["prediction"] == 1

def test_below_threshold():
    response = requests.get(BASE_URL, params={"x1": 2.0, "x2": 2.0})
    assert response.status_code == 200
    data = response.json()
    assert data["features"] == {"x1": 2.0, "x2": 2.0}
    assert data["prediction"] == 0

def test_default_values():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    data = response.json()
    assert data["features"] == {"x1": 0.0, "x2": 0.0}
    assert data["prediction"] == 0

def test_invalid_input():
    response = requests.get(BASE_URL, params={"x1": "abc", "x2": 3})
    assert response.status_code == 400
    data = response.json()
    assert "error" in data
