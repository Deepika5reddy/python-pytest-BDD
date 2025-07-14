import requests
from payload import SignupUser
from utilities.configuration import getconfig
from utilities.resources import resources

class TestRegisterUser:

    def setup_method(self):
        config = getconfig()
        self.api_key = config['API_KEY']['api_key']
        self.base_url = config['API_URL']['endpoint']
        self.headers = {"x-api-key": self.api_key}
        self.payload = SignupUser()
        self.url = self.base_url + resources.postRegister

    def validate_post_response(self, response):
        print("URL:", response.url)
        print("Status Code:", response.status_code)
        response.raise_for_status()
        content_type = response.headers.get("Content-Type", "").split(";")[0].strip()
        assert content_type == "application/json"

    def validate_signup_response_data(self, json_response):
        print("Response JSON:", json_response)
        assert json_response["id"] == 4
        assert json_response["token"] == "QpwL5tke4Pnpja7X4"

    def test_register_user(self):
        response = requests.post(self.url, headers=self.headers, json=self.payload)
        self.validate_post_response(response)
        self.validate_signup_response_data(response.json())
