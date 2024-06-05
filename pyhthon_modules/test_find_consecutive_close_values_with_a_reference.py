from load_time_series import *
from find_consecutive_close_values_with_a_reference import *

csv_file_path = 'D:/LabVIEW/LabVIEW-2024-and-Python/csv_data/low-1.csv'
# csv_file_path = 'C:/Users/Taboada.r248/Documents/LabVIEW Projects/LabVIEW-2024 & Python/csv_data/low-1.csv'

result = load_time_series(csv_file_path)
data, source, status, code = result

if not status:
    print('raw data = ', data)
    close_data, number_items_found, close_values, _, _ = find_close_values_w_ref(data, 48, 4)
    # find_close_values_w_ref(data, reference, tolerance)
    # return close_data, num_elements_in_final_series, close_values, False, "Success"

    print('close data = ', close_data)
    print('#items found = ', number_items_found)
    print('close values = ', close_values)
