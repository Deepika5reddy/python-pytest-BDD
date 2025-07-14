import requests
from utilities.configuration import getconfig
from utilities.resources import resources

class TestDeleteUser:

    def setup_method(self):
        config = getconfig()
        self.api_key = config['API_KEY']['api_key']
        self.base_url = config['API_URL']['endpoint'] + resources.deleteUser
        self.headers = {"x-api-key": self.api_key}

    def validate_delete_response(self, response, expected_status=204):
        print("URL:", response.url)
        print("Status Code:", response.status_code)
        assert response.status_code == expected_status

    def test_delete_user(self):
        response = requests.delete(self.base_url, headers=self.headers)
        self.validate_delete_response(response)
