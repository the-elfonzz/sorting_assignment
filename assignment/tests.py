import unittest
from json_to_csv import DataManager
from datetime import datetime

class TestDataManager(unittest.TestCase):
    
    def test_is_valid_date_return_false(self):
    	dm = DataManager()
    	invalid_date = "2019-04-22"
    	invalid_datettime_obj = datetime.strptime(invalid_date, '%Y-%m-%d')
   
    	self.assertFalse(dm._is_valid_date(invalid_datettime_obj))

    def test_is_valid_date_return_true(self):
    	dm = DataManager()
    	valid_date = "2019-04-15"
    	valid_datettime_obj = datetime.strptime(valid_date, '%Y-%m-%d')
   
    	self.assertTrue(dm._is_valid_date(valid_datettime_obj))
    
    def test_convert_time_stamp(self):
    	dm = DataManager()

    	test_date_str = '2019-04-22 08:12:12'
    	datetime_obj = dm._convert_time_stamp(test_date_str)
    	expected_result = datetime(2019, 4, 22, 8, 12, 12)

    	self.assertEqual(datetime_obj, expected_result)

    def test_convert_format_date(self):
    	dm = DataManager()

    	test_date_str = datetime.strptime('2019-04-27 03:23:12', '%Y-%m-%d %H:%M:%S')
    	datetime_obj = dm._format_date(test_date_str)
    	expected_result = '04/27/19 03:23 AM'
