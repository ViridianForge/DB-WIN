# This set of tests provides a series
# of test cases for the bc_scraper script to ensure the
# logic is working correctly.

import unittest
from lib.gs_scraper import getGSheetData

#ID of meaningless test data spreadsheet. :)
#Sheet 0 -- WINDex test data
#Sheet 1 -- Artist Map test data
#Sheet 2 -- Venue Map test data
#Sheet 3 -- Label Map test data
testWrkBk = "2PACX-1vQZMuXDyJsH6PZ_YpXxzosJaI_6eJLktkK0v0SIZ-zkoWJOlDFDAzizZ3av7FGJfE70KRPrcZA-N8Jo"

class bc_scraper_tests(unittest.TestCase):

    #Test one - Make sure Genre Scraping Works
    def test_getGSheetData(self):
        result = getGSheetData(testWrkBk, 0)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()