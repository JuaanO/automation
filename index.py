from selenium import webdriver
import unittest

EXE_PATH = r'./geckodriver'

class Items(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=EXE_PATH)
        self.driver.get('http://automationpractice.com/index.php')

    def test_view_item_case(self):
        self.driver.find_element_by_id('search_query_top').send_keys('dress')
        self.driver.find_element_by_name('submit_search').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//*[@id="center_column"]/ul/li[1]/div/div[1]/div/a[1]/img').click()
        title = self.driver.find_element_by_xpath('//h1[@itemprop = "name"]').text
        self.assertEqual(title, 'Printed Summer Dress', 'Text should be different')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
