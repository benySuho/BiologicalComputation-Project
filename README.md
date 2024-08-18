# Gene Regulation Analysis

This repository contains Python code for analyzing gene regulation conditions. The code includes helper functions: generating unary vectors, removing arrays from a list, and generating functions: finding all possible regulation functions, and printing the regulation conditions in a tabular format.

## Functions

- `remove_array_from_list(list_of_arrays, arr)`: Removes a specified numpy array from a list of numpy arrays.
- `increasing_unary_vectors(length)`: Generates a list of increasing unary vectors of specified length.
- `find_all_functions(activators_opts, repressors_opts)`: Finds all possible regulation functions given the options for activators and repressors.
- `print_all_monotonic_regulation_conditions(activators_number, repressors_number)`: Prints all possible monotonic regulation conditions for a given number of activators and repressors.

## Requirements
- numpy

## How does the Engine works
With given inputs of possible repressors configurations and activators configurations, the function runs in loops on all possible input variations, and generartes all possible outputs, and then checks if the outputs is actually poosible, if not, removes the output. For example: if all `Activators` are `On` and all `Repressors` are `Off`, it is impossible for tested Gene to be `Off`.

## Usage

To get all the monotonic regulation conditions, you can call the `find_all_functions` function with two lists:
activators_opts, repressors_opts (list of numpy arrays): Each numpy array represents a possible configuration of activators.

For example:  
```python
activators_options = increasing_unary_vectors((int)activators_number)
repressors_options = increasing_unary_vectors((int)repressors_number)

functions = find_all_functions(activators_options, repressors_options)
```

To print in nice view, all the monotonic regulation conditions of the reasoning engine, you can call the `print_all_monotonic_regulation_conditions` function with the desired number of activators and repressors. For example:

```python
print_all_monotonic_regulation_conditions(2, 2)
```

This will print all possible monotonic regulation conditions for a gene with 2 activators and 2 repressors.

## Test Cases

The code includes test cases to verify the functionality of the functions. You can run the code to see the test cases in action.
![image](https://github.com/user-attachments/assets/1bf074e0-ca02-4458-8972-e10a385b6b28)
![image](https://github.com/user-attachments/assets/a412a6ee-3fc2-4392-9783-c7807f21d178)
![image](https://github.com/user-attachments/assets/ca97731b-590d-41f0-ad2b-c6be7081c7cd)
