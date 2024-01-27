import pytest
import requests
import sys

# Define the base URL for your API (assuming it's running locally on port 8000)
BASE_URL = "http://localhost:8000"

# Test 1: Get a list of all displays
@pytest.mark.run(order=1)
def test_list_displays():
    response = requests.get(f"{BASE_URL}/displays")
    assert response.status_code == 200


# Test 2: Get the details of the first display
def test_get_display_details():
    # Assuming you have the 'id' of the first display
    display_id = "1d7ad5fe-c7c3-4922-8766-4f6e8b0880dc"
    response = requests.get(f"{BASE_URL}/display/{display_id}")
    assert response.status_code == 200

    # You can add more assertions to check the response content if needed

# Test 3: Check the auth status of the display
def test_check_auth_status():
    # Assuming you have the 'id', 'web_app', and 'api_key' for the display
    display_id = "1d7ad5fe-c7c3-4922-8766-4f6e8b0880dc"
    web_app = "webapp1"
    api_key = "VALID_KEY"
    response = requests.get(f"{BASE_URL}/auth/{display_id}/{web_app}/{api_key}")
    assert response.status_code == 200

    # You can add more assertions to check the response content if needed

# Test 4: Disable the display
def __test_disable_display():
    # Assuming you have the 'id' for the display
    display_id = "1d7ad5fe-c7c3-4922-8766-4f6e8b0880dc"
    response = requests.put(f"{BASE_URL}/disable/{display_id}")
    assert response.status_code == 200

    # You can add more assertions to check the response content if needed

# Test 5: Check the auth status of the display after disabling
def ___test_check_auth_status_after_disable():
    # Assuming you have the 'id', 'web_app', and 'api_key' for the display
    display_id = "1d7ad5fe-c7c3-4922-8766-4f6e8b0880dc"
    web_app = "webapp1"
    api_key = "api_key"
    response = requests.get(f"{BASE_URL}/auth/{display_id}/{web_app}/{api_key}")
    assert response.status_code == 200

    # You can add more assertions to check the response content if needed

# Test 6: Activate the display
def ___test_activate_display():
    # Assuming you have the 'id', 'web_app', and 'challenge_code' for the display
    display_id = "1d7ad5fe-c7c3-4922-8766-4f6e8b0880dc"
    web_app = "webapp1"
    challenge_code = "challenge_code"
    response = requests.put(f"{BASE_URL}/activate/{display_id}/{web_app}/{challenge_code}")
    assert response.status_code == 200

    # You can add more assertions to check the response content if needed

# Run the tests using 'pytest'
if __name__ == "__main__":
    import pytest
    pytest.main()
