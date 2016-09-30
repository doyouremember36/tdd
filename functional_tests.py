import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# make selenium use the "marionette" executable instead of the old "wires" one
caps = DesiredCapabilities.FIREFOX
caps["marionette"] = True

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(capabilities=caps)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Nancy has heard about this cool new online to-do list app. She goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She type "Buy peacock feathers" into a text box (Nancy's hobby is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists:
        # "1. Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.asserTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # There is still a text box inviting her to add another item. She enters "Use peacock feathers to make a fly" (Nancy is very methodical)
        self.fail('Reminder: Finish the test!')

        # The page updates again, and now shows both items on her list

        # Nancy wonders whether the site will remember her list. Then she sees that the site has generated a unique URL for her -- there is some explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep


if __name__ == '__main__':
    unittest.main()



