import requests
import json


class PathUrl:
    def __init__(self, url_address: str):
        """
        :param url_address: Take url address in a string!
        """
        self.url_address = url_address

    def serialize(self):
        """
        :return: JSON format
        """
        return requests.get(url=self.url_address).json()

    @staticmethod
    def save_to_json(obj):
        """
        :param: Take JSON-like object to save!
        :return: "Success" or Error!
        """
        try:
            json.dumps(obj)
            with open('data.json', "w") as file:
                json.dump(obj, file)
                return "Success"
        except Exception as Error:
            return Error


url = PathUrl("https://jsonplaceholder.typicode.com/todos").serialize()
PathUrl.save_to_json(url)
