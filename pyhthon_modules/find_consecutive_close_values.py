import numpy as np

def find_close_values(data, tolerance=0.01, min_threshold=10):
    if not data:
        return np.array([0]), 0, np.array([0])
    
    values = np.asarray(data, dtype=float)
    
    # Inicializamos variables para el grupo mayoritario
    largest_group = []
    largest_group_start_index = 0
    largest_group_end_index = 0

    # Inicializamos variables para mantener el seguimiento del grupo actual
    current_group = []
    current_group_start_index = 0

    for i, val in enumerate(values):
        # Si el valor está por debajo del umbral mínimo, lo ignoramos
        if val < min_threshold:
            # Si hay un grupo actual, verificamos si es el más grande hasta ahora
            if current_group:
                if len(current_group) > len(largest_group):
                    largest_group = current_group
                    largest_group_start_index = current_group_start_index
                    largest_group_end_index = i - 1
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
            if len(current_group) > len(largest_group):
                largest_group = current_group
                largest_group_start_index = current_group_start_index
                largest_group_end_index = i - 1
            # Reiniciamos el grupo actual con el valor actual
            current_group = [val]
            current_group_start_index = i

    # Verificamos si el último grupo actual es el más grande
    if len(current_group) > len(largest_group):
        largest_group = current_group
        largest_group_start_index = current_group_start_index
        largest_group_end_index = len(values) - 1

    # Construimos el resultado con el grupo mayoritario y los ceros en otras posiciones
    result_array = np.zeros_like(values)
    if largest_group:
        for i in range(largest_group_start_index, largest_group_end_index + 1):
            result_array[i] = values[i]

    # Calculamos el valor promedio del grupo mayoritario
    average_value = np.mean(largest_group) if largest_group else 0

    return np.array(largest_group), average_value, result_array