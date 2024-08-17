import numpy as np


def is_monotonic_increasing(binary_vector):
    differences = np.diff(binary_vector)
    return np.all(differences >= 0)


def is_monotonic_decreasing(binary_vector):
    differences = np.diff(binary_vector)
    return np.all(differences <= 0)


# Function to check if a list contains a numpy array
def contains_numpy_array(array, list_of_arrays):
    return any(np.array_equal(array, arr) for arr in list_of_arrays)


def remove_array_from_list(list_of_arrays, arr):
    for ind, array in enumerate(list_of_arrays):
        if np.array_equal(array, arr):
            list_of_arrays.pop(ind)
            break


def find_monotonic_increasing_vectors(binary_vector, index, monotonic_vectors):
    if index == binary_vector.size:
        return
    if is_monotonic_increasing(binary_vector) and not contains_numpy_array(binary_vector, monotonic_vectors):
        monotonic_vectors.append(binary_vector.copy())
    find_monotonic_increasing_vectors(binary_vector, index + 1, monotonic_vectors)
    binary_vector[index] = 1
    if is_monotonic_increasing(binary_vector) and not contains_numpy_array(binary_vector, monotonic_vectors):
        monotonic_vectors.append(binary_vector.copy())
    find_monotonic_increasing_vectors(binary_vector, index + 1, monotonic_vectors)


def find_all_monotonic_increasing_vectors(vector_length=1):
    if vector_length < 1:
        return [np.zeros(1).astype(np.int8)]
    binary_vector = np.zeros(vector_length).astype(np.int8)
    all_monotonic_increasing_vectors = []
    find_monotonic_increasing_vectors(binary_vector, 0, all_monotonic_increasing_vectors)
    return all_monotonic_increasing_vectors


def find_all_monotonic_decreasing_vectors(vector_length=1):
    all_monotonic_decreasing_vectors = find_all_monotonic_increasing_vectors(vector_length)
    all_monotonic_decreasing_vectors.reverse()
    return all_monotonic_decreasing_vectors


def find_all_functions(activators_opts, repressors_opts):
    options = []
    if len(activators_opts) == 0:
        options = find_all_monotonic_increasing_vectors(len(repressors_opts))
        remove_array_from_list(options, np.ones(len(repressors_opts)))
    elif len(repressors_opts) == 0:
        options = find_all_monotonic_increasing_vectors(len(activators_opts))
        remove_array_from_list(options, np.zeros(len(activators_opts)))
    else:
        for repressors in repressors_opts:
            opts = find_all_monotonic_increasing_vectors(len(activators_opts))
            for activators in activators_opts:
                if (np.array_equal(activators, np.ones(len(activators)))
                        and np.array_equal(repressors, np.zeros(len(repressors)))):
                    remove_array_from_list(opts, np.zeros(len(activators_opts)))
                elif (np.array_equal(activators, np.zeros(len(activators)))
                      and np.array_equal(repressors, np.ones(len(repressors)))):
                    remove_array_from_list(opts, np.ones(len(activators_opts)))

            if len(options) > 0:
                new_options = []
                for option in options:
                    for opt in opts:
                        if ((option[-len(opt):] - opt) >= 0).all():
                            new_options.append(np.append(option, opt))
                options = new_options
            else:
                options = opts
    return options


# gene vectors
# all zeros means all genes are off
# partially ones means part of genes are on and part are off
# more ones means more genes are on
# all ones means all genes are on
activators_options = find_all_monotonic_increasing_vectors(3)
repressors_options = find_all_monotonic_increasing_vectors(3)

functions = find_all_functions(activators_options, repressors_options)

# print in table
print("\t", *(f"\tA:{np.sum(activators)}" for repressors in repressors_options for activators in activators_options))
print("\t", *(f"\tR:{np.sum(repressors)}" for repressors in repressors_options for activators in activators_options))
for i, function in enumerate(functions):
    print(i, *(f"\t{int(f)}" for f in function), sep="\t")
