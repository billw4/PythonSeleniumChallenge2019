import requests
import unittest
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class AdvancedChallenge1(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome("../chromedriver.exe", options=options)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.close()

    def test_advanced1(self):
        print("\nAdvanced Python Challenge 1: REST web service")
        self.driver.get("https://www.copart.com")
        cookies = {c["name"]: c["value"] for c in self.driver.get_cookies()}
        api_endpoint = "https://www.copart.com/public/lots/search"
        car_queries = ["toyota camry",
                       "nissan skyline",
                       "Cadillac ATS",
                       "Mercedes-Benz E350",
                       "BMW 320",
                       "Mercedes-Benz CLA250",
                       "Chrysler 300",
                       "Lexus IS-250",
                       "Infiniti Q50",
                       "Lexus ES-350"]

        file = open("output.txt", "a")
        for car in car_queries:
            data = {"query": car}
            response = requests.post(url=api_endpoint, data=data, cookies=cookies)
            print("\nMake and Model: " + car.upper() + "\n" + response.text, file=file)
        file.close()

        print("Copart Make/Model JSON responses saved successfully to 'output.txt'")

    if __name__ == '__main__':
        unittest.main()


class AdvancedChallenge2(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome("../chromedriver.exe", options=options)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.close()

    def test_advanced2(self):
        print("\nAdvanced Python Challenge 2: Objects, JSON, and validating values in a JSON")
        self.driver.get("https://www.copart.com")

        api_endpoint = "https://www.copart.com/public/lots/search"
        data = {"query": "toyota camry"}
        cookies = {c["name"]: c["value"] for c in self.driver.get_cookies()}
        response = requests.post(url=api_endpoint, data=data, cookies=cookies)

        json_dict = json.loads(response.text)
        for k, v in json_dict['data']['results']['content'][1].items():
            print("Variable: " + k + ", Type: " + str(type(v).__name__))

    if __name__ == '__main__':
        unittest.main()
