import os
from unittest import TestCase
from tle import save_data, current_directory_path, file_name

class TestSatellite(TestCase):
    def test_save_data(self):
        test_data = ("153547","268925","353618")
        expected_data = (f"{test_data[1]}\n{test_data[2]}")
        save_data(satellite_data=test_data)
        with open(f"{current_directory_path}\{file_name}", "r") as output:
            data = output.read()
        os.remove(f"{current_directory_path}\{file_name}")
        self.assertEqual(expected_data, data)

# python -m unittest test.py
