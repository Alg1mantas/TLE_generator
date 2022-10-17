import time
import os.path
import logging
from satellite_tle import fetch_tle_from_celestrak


SATELLITE_NAME = "M6P"
M6P_SATELLITE_ID = 44109

date_time = (time.strftime("%Y-%m-%d %H.%M.%S"))
current_directory_path = os.path.dirname(os.path.realpath(__file__))
file_name = SATELLITE_NAME + " " + date_time + ".txt"
log_file_name = (f"{current_directory_path}\ tle.log")

logging.basicConfig(filename=log_file_name, encoding="UTF-8", level=logging.DEBUG)

def get_data() -> tuple:
    satelitte_data = fetch_tle_from_celestrak(M6P_SATELLITE_ID)
    return satelitte_data

def save_data(satellite_data) -> None:
    with open(f"{current_directory_path}\{file_name}", "w") as text_file:
        text_file.write(f"{str(satellite_data[1])}\n{str(satellite_data[2])}")
    logging.info(f"Received and saved {SATELLITE_NAME} satellite (TLE) data in '{file_name}' file. ")


if __name__=="__main__":
    satelitte_data = get_data()
    save_data(satelitte_data)
