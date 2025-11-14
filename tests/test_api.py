import requests
import pytest
from resources.urls import API_URLS  # Import the list of URLs from the separate module

@pytest.mark.parametrize("url", API_URLS)
def test_get_api_response(url):
    # Perform the GET request
    response = requests.get(url)

    # Assert that the response status code is 200
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    # Assert that the response contains JSON data
    try:
        data = response.json()
    except ValueError:
        pytest.fail(f"Response from {url} is not in JSON format")

    # Basic validation: Check if response has expected keys
    if "productsList" in url:
        assert "products" in data, f"Response from {url} does not contain 'products'"
        assert isinstance(data["products"], list), "'products' should be a list"
    elif "brandsList" in url:
        assert "brands" in data, f"Response from {url} does not contain 'brands'"
