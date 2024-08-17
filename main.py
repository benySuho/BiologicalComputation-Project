import numpy as np


def remove_array_from_list(list_of_arrays, arr):
    """
    Removes a specified numpy array from a list of numpy arrays.

    This function iterates over the given list of numpy arrays and checks for equality with the specified array.
    If a match is found, the array is removed from the list using the `pop` method.

    Parameters:
    list_of_arrays (list of numpy arrays): The list from which to remove the specified array.
    arr (numpy array): The array to be removed from the list.

    Returns:
    None. The function modifies the original list in-place.
    """
    for ind, array in enumerate(list_of_arrays):
        if np.array_equal(array, arr):
            list_of_arrays.pop(ind)
            break


def increasing_unary_vectors(length):
    """
    Generate a list of increasing unary vectors of specified length.

    This function creates a list of numpy arrays, where each array represents a unary vector of increasing length.
    The unary vector starts with all zeros and ends with all ones. The length of each vector is determined by the input parameter.

    Parameters:
    length (int): The desired length of the unary vectors. Must be a non-negative integer.

    Returns:
    list of numpy arrays: A list of unary vectors of increasing length. Each vector is a numpy array of integers.
    """
    if length < 1:
        return [np.zeros(1).astype(int)]
    return [np.concatenate((np.zeros(length - i), np.ones(i))).astype(int) for i in range(length + 1)]


def find_all_functions(activators_opts, repressors_opts):
    """
    This function finds all possible regulation functions given the options for activators and repressors.

    Parameters:
    activators_opts (list of numpy arrays): Each numpy array represents a possible configuration of activators.
    repressors_opts (list of numpy arrays): Each numpy array represents a possible configuration of repressors.

    Returns:
    list of numpy arrays: Each numpy array represents a possible regulation function.
    """
    options = []

    for repressors in repressors_opts:
        opts = increasing_unary_vectors(len(activators_opts))
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


def print_all_monotonic_regulation_conditions(activators_number, repressors_number):
    """
    Prints all possible monotonic regulation conditions for a given number of activators and repressors.

    This function generates all possible combinations of activator and repressor configurations,
    calculates the corresponding regulation functions, and prints them in a tabular format.
    The function uses color-coding to highlight the presence of activators (red background) and repressors (gray background).

    Parameters:
    activators_number (int): The number of activators. Must be a non-negative integer.
    repressors_number (int): The number of repressors. Must be a non-negative integer.

    Returns:
    None. The function prints the regulation conditions directly to the console.
    """
    # gene vectors
    # all zeros means all genes are off
    # partially ones means part of genes are on and part are off
    # more ones means more genes are on
    # all ones means all genes are on
    activators_options = increasing_unary_vectors(activators_number)
    repressors_options = increasing_unary_vectors(repressors_number)

    functions = find_all_functions(activators_options, repressors_options)

    # print in table
    print("\t",
          *(f"\tA:{np.sum(activators)}"
            for _ in repressors_options
            for activators in activators_options))
    print("\t",
          *(f"\tR:{np.sum(repressors)}"
            for repressors in repressors_options
            for _ in activators_options))
    red_background = '\033[0;30;41m'
    gray_background = '\x1b[0m\x1b[0;30;47m'
    regular = '\x1b[0m\x1b[0;38;47m'
    for i, function in enumerate(functions):
        print(f"{i}",
              *(f"{red_background if f == 1 else gray_background}\t{int(f)}" for f in function),
              regular, sep="\t")


# test cases
print("Testing gene without repressors or activators")
print_all_monotonic_regulation_conditions(0, 0)
print("---------------------------------------------------------------------------")
print("Testing gene without repressors, only activators affect, they can be all active or all off\n")
print_all_monotonic_regulation_conditions(1, 0)
print("---------------------------------------------------------------------------")
print("Testing gene with conditions given in Exercise\n")
print_all_monotonic_regulation_conditions(2, 2)
