import os
import json
import csv

from datetime import datetime


dirname = os.path.dirname(__file__)
filepath = os.path.join(dirname, 'input_data.json')
writepath = os.path.join(dirname, 'output_data.csv')

class DataManager():
	"""docstring for DataManager"""

	def __init__(self):
		self.invalid_date = '2019-04-22'
		self.data = []

	def parse_json_data(self, read_file_path):
		with open(read_file_path, "r") as f:
			data = f.read()

		self.data = json.loads(data)

	def create_csv(self, write_file_path):
		if not self.data:
			 print ("File is empty or not parsed")
			 return

		colums = self._collect_columns()

		with open(write_file_path, 'w') as csvfile:
			writer = csv.DictWriter(csvfile, fieldnames=colums)
			writer.writeheader()

			for item in self.data:
				user = item.get("user")

				for event in item.get("event_times_and_quantities").keys():
					for timestamp_record in item["event_times_and_quantities"][event]:
						time_stamp_str = timestamp_record.get("d")
						time_stamp_obj = self._convert_time_stamp(time_stamp_str)
						if self._is_valid_date(time_stamp_obj):
							time_stamp_formatted = self._format_date(time_stamp_obj)
							writer.writerow({'user': user, event: time_stamp_formatted})

						

	def _convert_time_stamp(self, time_stamp_str):
		date_obj = datetime.strptime(time_stamp_str, '%Y-%m-%d %H:%M:%S')
		return date_obj

	def _format_date(self, date):
		return date.strftime("%m/%d/%y %I:%M %p")

	def _collect_columns(self):
		colums = set()

		for item in self.data:
			keys = item.get("event_times_and_quantities").keys()
			colums.update(keys)

		#'user' column to be at first position
		colums = ["user"]  + list(colums)
		return colums

	def _is_valid_date(self, time_stamp_obj):
		if self.invalid_date == time_stamp_obj.strftime('%Y-%m-%d'):
			return False

		return True

if __name__ == '__main__':
	dm = DataManager()
	dm.parse_json_data(filepath)
	dm.create_csv(writepath)