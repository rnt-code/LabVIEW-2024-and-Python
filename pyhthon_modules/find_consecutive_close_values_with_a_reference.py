import numpy as np

def find_close_values_w_ref(data, reference, tolerance):
    try:
        # Validate input parameters
        if not isinstance(data, (list, np.ndarray)):
            raise ValueError("data must be a list or a numpy array.")
        if not isinstance(reference, (int, float)):
            raise ValueError("reference must be an integer or a float.")
        if not isinstance(tolerance, (int, float)):
            raise ValueError("tolerance must be an integer or a float.")
        if tolerance < 0:
            raise ValueError("tolerance must be a non-negative value.")
        
        # Convert list to a NumPy array if it's not already
        data = np.asarray(data)
        threshold = tolerance * reference / 100

        # Identifies 'data' indices that meet the proximity to the reference based on tolerance
        # np.where(condition, [x,y]/) return indices (of 'data') when only condition is provided
        # np.where return a tuple of arrays, close_data_indices_all is a tuple

        # close_data_indices is the first element of the array tuple of np.where(np.abs(data - reference) <= threshold), thus [0]
        close_data_indices = np.where(np.abs(data - reference) <= threshold)[0]

        if close_data_indices.size == 0:
            return np.zeros_like(data), 0, [0], 0, False, "No close data found."

        # Group consecutive indices. splits es un ndarray de booleanos con el resultado de comparar a[i+1] - a[i] con 1.
        # Si la diferencia es distinta de 1, True, si es 1, False. Las False => índices consecutivos.
        # split es un ndarray con los booleanos true y false.
        splits = np.diff(close_data_indices) != 1
        
        # Acá están los grupos de ndarrays de índices consecutivos. groups es un ndarray de ndarrays.
        groups = np.split(close_data_indices, np.where(splits)[0] + 1)

        # Find the longest series of consecutive indices
        largest_group_index = max(groups, key=len)

        # Create an array (filled with zeroes) to hold the close data series
        close_values_w_zero = np.zeros_like(data, dtype=float)

        # fill close_values_w_zero with cosecutive values of data with consecutive indices.
        close_values_w_zero[largest_group_index] = data[largest_group_index]

        # Extract the close values in a separate array (excluding zeros)
        close_values = close_values_w_zero[close_values_w_zero != 0]
        
        # Mean of element found
        average = np.mean(close_values)

        # Calculate the number of elements in the longest series
        num_elements_found = len(largest_group_index)

        return close_values_w_zero, num_elements_found, close_values, average, False, "Success"
    
    except Exception as e:
        return np.zeros_like(data), 0, [0], 0, True, str(e)