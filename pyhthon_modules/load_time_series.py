import csv

def load_time_series(csv_file):
    time_series_data = []
    source = ""
    status = False
    code = int(0)
    try:
        with open(csv_file, newline='') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                for element in row:
                    time_series_data.append(float(element))
    except FileNotFoundError:
        source = "load_time_series(). " + f"Error: The file '{csv_file}' was not found."
        status = True
        code = int(5001)
    except PermissionError:
        source = "load_time_series(). " + f"Error: Insufficient permissions to open the file '{csv_file}'."
        status = True
        code = int(5002)
    except ValueError as e:
        source = "load_time_series(). " + f"Error: Could not convert an element to float. Details: {e}"
        status = True
        code = int(5003)
    except Exception as e:
        source = "load_time_series(). " + f"Unexpected error: {e}"
        status = True
        code = int(5004)

    return time_series_data, source, status, code