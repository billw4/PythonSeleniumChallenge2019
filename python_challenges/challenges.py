import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class Challenge1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge1(self):
        print("STG Python/Selenium Challenges 2019, Bill Witt\n")
        print("Python Challenge 1:")
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)
        print("Titles match.")

    if __name__ == '__main__':
        unittest.main()


class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.implicitly_wait(8)

    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        print("\nPython Challenge 2:")
        self.driver.get("https://www.copart.com")
        self.assertIn("Auto Auction", self.driver.title)
        types_link = self.driver.find_element_by_link_text("Types")
        types_link.click()
        time.sleep(2)

        exotics_link = self.driver.find_element_by_xpath("//a[@title='Exotics']")
        exotics_link.click()
        time.sleep(2)

        self.assertIn("Exotics", self.driver.title)
        search_results = self.driver.find_elements_by_xpath("//span[@data-uname='lotsearchLotmake']")

        exotic_cars = []
        for elem in search_results:
            exotic_cars.append(elem.text)
            print(elem.text)

        self.assertTrue(exotic_cars.__contains__("PORSCHE"))

    if __name__ == '__main__':
        unittest.main()


class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.implicitly_wait(8)

    def tearDown(self):
        self.driver.close()

    def test_challenge3(self):
        print("\nPython Challenge 3")
        self.driver.get("https://www.copart.com")
        self.assertIn("Auto Auction", self.driver.title)
        popular_models = self.driver.find_elements_by_xpath("//a[contains(@href,'popular/model')]")
        models = []
        for model in popular_models:
            models.append(model.text + " - " + model.get_attribute("href"))

        for model in models:
            print(model)

    if __name__ == '__main__':
        unittest.main()


class Challenge4(unittest.TestCase):

    def get_fibonacci(self, num):
        if num <= 1:
            return num
        else:
            return self.get_fibonacci(num - 1) + self.get_fibonacci(num - 2)

    def convert_fib_to_text(self, num):
        ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eightteen',
                 'nineteen']
        tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

        if num == 0:
            return "zero"
        elif num <= 9:
            return ones[num - 1]
        elif 9 < num <= 19:
            return teens[num - 10]
        elif 19 < num <= 99:
            first = int(str(num)[0]) - 1
            second = int(str(num)[1]) - 1

            if second == 0:
                return tens[first]
            else:
                return tens[first] + "-" + ones[second]
        elif 99 < num <= 999:
            first = int(str(num)[0]) - 1
            second = int(str(num)[1]) - 1
            third = int(str(num)[2]) - 1

            if second == 0 and third == 0:
                return ones[first] + " hundred"
            elif second == 0 and third > 0:
                return ones[first] + " hundred and " + ones[third]
            elif second > 0 and third == 0:
                return ones[first] + " hundred and " + tens[second]
            else:
                return ones[first] + " hundred and " + tens[second] + "-" + ones[third]
        elif 999 < num <= 9999:
            first = int(str(num)[0]) - 1
            second = int(str(num)[1]) - 1
            third = int(str(num)[2]) - 1
            fourth = int(str(num)[3]) - 1

            if second == 0 and third == 0 and fourth == 0:
                return ones[first] + " thousand"
            elif second > 0 and third == 0 and fourth == 0:
                return ones[first] + " thousand " + ones[second] + " hundred"
            elif second == 0 and third > 0 and fourth == 0:
                return ones[first] + " thousand and " + tens[third]
            elif second == 0 and third == 0 and fourth > 0:
                return ones[first] + " thousand and " + ones[fourth]
            elif second > 0 and third > 0 and fourth == 0:
                return ones[first] + " thousand " + ones[second] + " hundred and " + tens[third]
            elif second > 0 and third == 0 and fourth > 0:
                return ones[first] + " thousand " + ones[second] + " hundred and " + ones[fourth]
            elif second == 0 and third > 0 and fourth > 0:
                return ones[first] + " thousand " + tens[third] + "-" + ones[fourth]
            else:
                return ones[first] + " thousand " + ones[second] + " hundred and " + tens[third] + "-" + ones[fourth]

    def test_challenge4(self):
        print("\nPython Challenge 4")
        fib = 12
        for i in range(0, fib):
            f = self.get_fibonacci(i)
            t = self.convert_fib_to_text(f)
            print("F(" + str(i) + ") = " + str(f) + ", " + t)

    if __name__ == '__main__':
        unittest.main()


class Challenge5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.implicitly_wait(100)

    def tearDown(self):
        self.driver.close()

    def test_challenge5(self):
        print("\nPython Challenge 5:")
        self.driver.get("https://www.copart.com")
        self.assertIn("Auto Auction", self.driver.title)

        search_box = self.driver.find_element_by_id("input-search")
        search_box.send_keys("PORSCHE")
        search_button = self.driver.find_element_by_xpath("//button[@data-uname='homepageHeadersearchsubmit']")
        search_button.click()
        time.sleep(2)
        self.assertIn("PORSCHE".lower(), self.driver.title.lower())

        select = Select(self.driver.find_element_by_xpath("(//select[@name='serverSideDataTable_length'])[1]"))
        select.select_by_visible_text("100")
        time.sleep(2)

        search_result_models = self.driver.find_elements_by_xpath("//span[@data-uname='lotsearchLotmodel']")
        search_result_damages = self.driver.find_elements_by_xpath("//span[@data-uname='lotsearchLotdamagedescription']")

        porsche_models = []
        for elem in search_result_models:
            if len(elem.text) > 0:
                porsche_models.append(elem.text)

        damage_types = []
        for elem in search_result_damages:
            damage_types.append(elem.text)

        rear_end = 0
        front_end = 0
        minor_dent = 0
        undercarriage = 0
        misc = 0
        for i in damage_types:
            if i == "REAR END":
                rear_end += 1
            elif i == "FRONT END":
                front_end += 1
            elif i == "MINOR DENT/SCRATCHES":
                minor_dent += 1
            elif i == "UNDERCARRIAGE":
                undercarriage += 1
            else:
                misc += 1

        print("PORSCHE Model count: " + str(len(set(porsche_models))))
        print("REAR END Damage Count: " + str(rear_end))
        print("FRONT END Damage Count: " + str(front_end))
        print("MINOR DENT/SCRATCHES Damage Count: " + str(minor_dent))
        print("UNDERCARRIAGE Damage Count: " + str(undercarriage))
        print("MISC Damage Count: " + str(misc))

    if __name__ == '__main__':
        unittest.main()


class Challenge6(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.close()

    def test_challenge6(self):
        print("\nPython Challenge 6:")
        self.driver.get("https://www.copart.com")
        self.assertIn("Auto Auction", self.driver.title)
        self.driver.maximize_window()

        search_box = self.driver.find_element_by_id("input-search")
        search_box.send_keys("NISSAN")
        search_button = self.driver.find_element_by_xpath("//button[@data-uname='homepageHeadersearchsubmit']")
        search_button.click()
        time.sleep(2)
        self.assertIn("NISSAN".lower(), self.driver.title.lower())

        model_option = self.driver.find_element_by_xpath("//a[@data-uname='ModelFilter']")
        model_option.click()
        model_search = self.driver.find_element_by_xpath("//div[@id='collapseinside4']//input[@placeholder='Search']")
        model_search.send_keys("skyline")
        time.sleep(2)

        try:
            search_result = self.driver.find_element_by_xpath("//input[@type='checkbox' and @value='Skylinegtr']")
            search_result.click()
            time.sleep(1)
            self.assertIn("skyline", self.driver.find_element_by_xpath("//span[@data-uname='lotsearchLotmodel']").text.lower())
            print("Nissan Skyline found successfully!")
        except (Exception, TimeoutError):
            print("Nissan Skyline not found.")
            self.driver.save_screenshot("elementException.png")

    if __name__ == '__main__':
        unittest.main()


class Challenge7(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.implicitly_wait(100)

    def tearDown(self):
        self.driver.close()

    def test_challenge7(self):
        print("\nPython Challenge 7:")
        self.driver.get("https://www.copart.com")
        self.assertIn("Auto Auction", self.driver.title)
        self.driver.maximize_window()

        makes = self.driver.find_elements_by_xpath("//div[@ng-if='popularSearches']//a")

        make_names = []
        for elem in makes:
            make_names.append(elem.text)

        make_links = []
        for elem in makes:
            make_links.append(elem.get_attribute("href"))

        make_names_and_links = dict(zip(make_names, make_links))
        for name, link in make_names_and_links.items():
            try:
                self.driver.get(link)
                time.sleep(1)
                new_url = f"https://www.copart.com/popular/model/{name.lower()}?query={name.lower()}&free"
                self.assertEqual(new_url, self.driver.current_url)
                print(name + " link, '" + link + "' is valid.")
            except Exception:
                print(name + " link was invalid.")
                self.driver.save_screenshot("linkException.png")
            self.driver.back()

    if __name__ == '__main__':
        unittest.main()
