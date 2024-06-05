from load_time_series import *
from find_consecutive_close_values import *

csv_file_path = 'C:/Users/Taboada.r248/Documents/LabVIEW Projects/LabVIEW-2024 & Python/csv data/low-1.csv'

result = load_time_series(csv_file_path)
data, source, status, code = result

if not status:
    print('raw data = ', data)
    largest_group, average_value, result_array = find_close_values(data, 0.02, 10)
    # find_close_values(data, tolerance=0.01, min_threshold=10)
    # return largest_group, average_value, result_array
    
    print('largest_group = ', largest_group)
    print('average value = ', average_value)
    print('result_array = ', result_array)