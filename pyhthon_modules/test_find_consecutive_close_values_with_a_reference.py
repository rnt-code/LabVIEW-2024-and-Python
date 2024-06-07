from load_time_series import *
from find_consecutive_close_values_with_a_reference import *

# base_path = 'D:/LabVIEW/LabVIEW-2024-and-Python/csv_data/'
base_path = 'C:/Users/Taboada.r248/Documents/LabVIEW Projects/LabVIEW-2024-and-Python/csv_data/'
file_name = 'low-1.csv'

csv_file_path = base_path + file_name

data, source, status, code = load_time_series(csv_file_path)

if not status:
    print('data = ', data)
    close_values_w_zeros, num_elements_found, close_values, average, _, _ = find_close_values_w_ref(data, 48, 4)
    # find_close_values_w_ref(data, reference, tolerance)
    # return close_values_w_zero, num_elements_found, close_values, average, False, "Success"

    print('close_values_w_zeros = ', close_values_w_zeros)
    print('num_elements_found = ', num_elements_found)
    print('close values = ', close_values)
    print('average = ', average)