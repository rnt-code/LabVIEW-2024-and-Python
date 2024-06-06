import numpy as np

def find_close_values(data, tolerance=0.01, min_threshold=10):
    
    data = np.asarray(data, dtype=float)
    
    # Inicializamos variables para el grupo mayoritario
    close_values = []
    close_values_start_index = 0
    close_values_end_index = 0

    # Inicializamos variables para mantener el seguimiento del grupo actual
    current_group = []
    current_group_start_index = 0

    for i, val in enumerate(data):
        # Si el valor está por debajo del umbral mínimo, lo ignoramos
        if val < min_threshold:
            # Si hay un grupo actual, verificamos si es el más grande hasta ahora
            if current_group:
                if len(current_group) > len(close_values):
                    close_values = current_group
                    close_values_start_index = current_group_start_index
                    close_values_end_index = i - 1
                current_group = []
            continue

        # Si el grupo actual está vacío o el valor actual es consecutivo al último valor del grupo actual,
        # agregamos el valor al grupo actual
        if not current_group or abs((val - current_group[-1]) / current_group[-1]) <= tolerance:
            current_group.append(val)
            # Si este es el primer valor del grupo, actualizamos el índice de inicio del grupo
            if len(current_group) == 1:
                current_group_start_index = i
        else:
            # Si el valor no es consecutivo, verificamos si el grupo actual es el más grande hasta ahora
            if len(current_group) > len(close_values):
                close_values = current_group
                close_values_start_index = current_group_start_index
                close_values_end_index = i - 1
            # Reiniciamos el grupo actual con el valor actual
            current_group = [val]
            current_group_start_index = i

    # Verificamos si el último grupo actual es el más grande
    if len(current_group) > len(close_values):
        close_values = current_group
        close_values_start_index = current_group_start_index
        close_values_end_index = len(data) - 1

    # Construimos el resultado con el grupo mayoritario y los ceros en otras posiciones
    close_values_w_zeros = np.zeros_like(data)
    if close_values:
        for i in range(close_values_start_index, close_values_end_index + 1):
            close_values_w_zeros[i] = data[i]

    close_values = np.array(close_values)
    num_elements_found = close_values.size

    # Calculamos el valor promedio del grupo mayoritario
    if close_values.size > 0:  # Verifica si el ndarray no está vacío
        average = np.mean(close_values)
    else:
        average = -1

    return close_values_w_zeros, num_elements_found, close_values, average