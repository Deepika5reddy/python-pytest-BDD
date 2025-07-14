import requests
from utilities.configuration import getconfig
from utilities.resources import resources

class TestGetUsers:

    def setup_method(self):
        config = getconfig()
        self.api_key = config['API_KEY']['api_key']
        self.base_url = config['API_URL']['endpoint'] + resources.getUsers
        self.headers = {"x-api-key": self.api_key}

    def validate_response(self, response):
        print("Request URL:", response.url)
        print("Status Code:", response.status_code)
        assert response.status_code == 200
        assert response.headers["Content-Type"].split(";")[0].strip() == 'application/json'

    def extract_and_validate_data(self, json_response):
        fname = json_response['data'][0]['first_name']
        print("First name:", fname)
        assert fname == 'Michael'

        target_email = None
        for user in json_response['data']:
            if user["email"] == 'lindsay.ferguson@reqres.in':
                target_email = user
                print("Found email:", target_email)
                break

        first_names = [user["first_name"] for user in json_response['data']]
        print("All first names:", first_names)

    def test_get_users(self):
        response = requests.get(self.base_url, headers=self.headers, params={'page': '2'})
        self.validate_response(response)
        self.extract_and_validate_data(response.json())
