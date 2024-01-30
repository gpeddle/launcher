import pytest
import requests
import sys, os
import argparse

# NOTE: These tests are intended to be run in the order specified below
# Test 1: Get a list of all displays
# Test 2: Get the details of the first display
# Test 3: Check the auth status of the display
# Test 4: Disable the display
# Test 5: Check the auth status of the display after disabling
# Test 6: Activate the display
# Test 7: Check the auth status of the display after activation
# Test 8: Get the details of the first display after activation


# retrieve the host ip from environment variable
host_ip = os.environ.get('HOST_IP')

BASE_URL = f'http://{host_ip}:8000'

# Test 1: Get a list of all displays
#@pytest.mark.run(order=1)
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
    json_response = response.json()
    # verify the response status is 'Success'
    assert json_response["status"] == "Success"
    # verify the challenge code is empty
    assert json_response["challenge_code"] == None
    

# Test 4: Disable the display
def test_disable_display():
    # Assuming you have the 'id' for the display
    display_id = "1d7ad5fe-c7c3-4922-8766-4f6e8b0880dc"
    response = requests.put(f"{BASE_URL}/disable/{display_id}")
    assert response.status_code == 200
    json_response = response.json()
    # verify the response status is 'Success'
    assert json_response["status"] == "Success"


# Test 5: Check the auth status of the display after disabling
def test_check_auth_status_after_disable():
    # Assuming you have the 'id', 'web_app', and 'api_key' for the display
    display_id = "1d7ad5fe-c7c3-4922-8766-4f6e8b0880dc"
    web_app = "webapp1"
    api_key = "api_key"
    response = requests.get(f"{BASE_URL}/auth/{display_id}/{web_app}/{api_key}")
    assert response.status_code == 200
    json_response = response.json()
    # verify the response status is 'Success'
    assert json_response["status"] == "Success"
    # verify the challenge code is not empty
    assert json_response["challenge_code"] != "" and json_response["challenge_code"] != None


    # You can add more assertions to check the response content if needed

# Test 6: Activate the display
def test_activate_display():
    # Assuming you have the 'id', 'web_app', and 'challenge_code' for the display
    display_id = "1d7ad5fe-c7c3-4922-8766-4f6e8b0880dc"
    web_app = "webapp1"
    challenge_code = "challenge_code"
    response = requests.put(f"{BASE_URL}/activate/{display_id}/{web_app}/{challenge_code}")
    assert response.status_code == 200
    json_response = response.json()
    # verify the response status is 'Success'
    assert json_response["status"] == "Success"
    # verify the api key is returned
    assert json_response["api_key"] != "" and json_response["api_key"] != None

def test_check_auth_status_after_activation():
    # Assuming you have the 'id', 'web_app', and 'api_key' for the display
    display_id = "1d7ad5fe-c7c3-4922-8766-4f6e8b0880dc"
    web_app = "webapp1"
    api_key = "VALID_KEY"
    response = requests.get(f"{BASE_URL}/auth/{display_id}/{web_app}/{api_key}")
    assert response.status_code == 200
    json_response = response.json()
    # verify the response status is 'Success'
    assert json_response["status"] == "Success"
    # verify the challenge code is empty
    assert json_response["challenge_code"] == None
    # verify the api key is not empty
    assert json_response["api_key"] != "" and json_response["api_key"] != None


def test_get_display_details_after_activation():
    # Assuming you have the 'id' of the first display
    display_id = "1d7ad5fe-c7c3-4922-8766-4f6e8b0880dc"
    response = requests.get(f"{BASE_URL}/display/{display_id}")
    assert response.status_code == 200
    json_response = response.json()
    # verify the display is active
    assert json_response["status"] == "active"
    # verify the challenge code is empty
    assert json_response["challenge_code"] == None
    # verify the api key is not empty
    assert json_response["api_key"] != "" and json_response["api_key"] != None



# Run the tests using 'pytest'
if __name__ == "__main__":
    import pytest
    pytest.main()
