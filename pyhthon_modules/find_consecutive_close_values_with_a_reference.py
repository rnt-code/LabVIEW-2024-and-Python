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

        # Identify indices of data close to the reference value
        close_data_indices = np.where(np.abs(data - reference) <= threshold)[0]

        if close_data_indices.size == 0:
            return np.zeros_like(data), 0, [0], False, "No close data found."

        # Group consecutive indices
        splits = np.diff(close_data_indices) != 1
        groups = np.split(close_data_indices, np.where(splits)[0] + 1)
        
        # Find the longest series of consecutive indices
        longest_consecutive = max(groups, key=len)
    
        # Create an array to hold the close data series
        close_data = np.zeros_like(data, dtype=float)
        close_data[longest_consecutive] = data[longest_consecutive]

        # Extract the close values in a separate array (excluding zeros)
        close_values = close_data[close_data != 0]

        # Calculate the number of elements in the longest series
        num_elements_in_final_series = len(longest_consecutive)

        return close_data, num_elements_in_final_series, close_values, False, "Success"
    
    except Exception as e:
        return np.zeros_like(data), [0], 0, True, str(e)