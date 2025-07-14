from behave import given, when, then
import requests
from behave import given, when, then
from utilities.configuration import getconfig
from utilities.resources import resources
from payload import SignupUser


#https://behave.readthedocs.io/en/latest/tutorial/

@given("Base url")
def step_set_base_url(context):
    context.url = getconfig()['API_URL']['endpoint'] + resources.getUsers
    context.headers = {
        "x-api-key": getconfig()['API_KEY']['api_key']
    }


@when('Perform get call')
def step_perform_get(context):
    context.response = requests.get(context.url, headers=context.headers, params={'page': '2'})
    context.json_response = context.response.json()


@then('assert 200')
def step_check_status(context):
    print("Status Code:", context.response.status_code)
    assert context.response.status_code == 200

@given("I set the base URL for POST request")
def step_set_post_url(context):
    context.url = getconfig()['API_URL']['endpoint'] + resources.postRegister
    context.headers = {
        "x-api-key": getconfig()['API_KEY']['api_key']
    }

@given("I prepare the signup user payload")
def step_prepare_payload(context):
    context.payload = SignupUser()

@when("I perform a POST call to register user")
def step_perform_post(context):
    context.response = requests.post(context.url, headers=context.headers, json=context.payload)
    context.json_response = context.response.json()

@then("the response status should be 200")
def step_validate_status_code(context):
    print("Status Code:", context.response.status_code)
    assert context.response.status_code == 200

    content_type = context.response.headers.get("Content-Type", "").split(";")[0].strip()
    assert content_type == "application/json"

@then('the response should contain user {id} and token "QpwL5tke4Pnpja7X4"')
def step_validate_response_fields(context, id):
    print("Response JSON:", context.json_response)
    assert context.json_response["id"] == int(id)
    assert context.json_response["token"] == "QpwL5tke4Pnpja7X4"

@given("I set the base URL for DELETE request")
def step_set_delete_url(context):
    context.url = getconfig()['API_URL']['endpoint'] + resources.deleteUser
    context.headers = {
        "x-api-key": getconfig()['API_KEY']['api_key']
    }

@when("I perform the DELETE call")
def step_perform_delete(context):
    context.response = requests.delete(context.url, headers=context.headers)

@then('the response status should be "{expected_status}"')
def step_validate_delete_status(context, expected_status):
    actual = context.response.status_code
    print(f"URL: {context.response.url}")
    print(f"Status Code: {actual}")
    assert actual == int(expected_status), f"Expected {expected_status}, but got {actual}"
