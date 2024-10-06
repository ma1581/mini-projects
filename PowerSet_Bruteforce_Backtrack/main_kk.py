# import streamlit as st
# from itertools import chain, combinations
# import time

# # Function to generate the power set using a brute force approach
# def generate_power_set_brute_force(elements):
#     start_time = time.time()
#     power_set = []
#     for subset_len in range(len(elements) + 1):
#         for subset in combinations(elements, subset_len):
#             power_set.append(subset)
#     end_time = time.time()
#     time_complexity = f"O(2^{len(elements)})"  # Calculate time complexity
#     space_complexity = f"O(2^{len(elements)})"
#     return power_set, time_complexity, space_complexity, end_time - start_time

# # Function to generate the power set using backtracking
# def generate_power_set_backtracking(elements):
#     def backtrack(subset, start):
#         power_sets.append(subset[:])  # Add the current subset to the power set

#         for i in range(start, len(elements)):
#             subset.append(elements[i])
#             backtrack(subset, i + 1)
#             subset.pop()  # Backtrack

#     start_time = time.time()
#     power_sets = []
#     backtrack([], 0)
#     end_time = time.time()
#     time_complexity = f"O(2^{len(elements)})"
#     space_complexity = f"O(n)"  # Backtracking uses O(n) space for the call stack
#     return power_sets, time_complexity, space_complexity, end_time - start_time

# # Set page title and description
# st.set_page_config(
#     page_title="Power Set Generator",
#     page_icon="✨",
#     layout="wide"
# )

# # Page layout
# st.title("Power Set Generator")

# # Ask the user to select the method
# method = st.radio("Select the method", ("Brute Force", "Backtracking"))

# # Input for number of elements
# n = st.number_input("Enter the number of elements (n):", min_value=0, step=1, value=0)

# # Input for elements
# elements = []
# for i in range(n):
#     element = st.text_input(f"Enter element {i + 1}:", key=f"element_{i}")
#     elements.append(element)

# # Button to generate power set
# if st.button("Generate Power Set"):
#     # Remove empty string elements
#     elements = [e for e in elements if e]

#     if len(elements) == 0:
#         st.warning("Please enter at least one element.")
#     else:
#         if method == "Brute Force":
#             power_set, time_complexity, space_complexity, execution_time = generate_power_set_brute_force(elements)
#         else:
#             power_set, time_complexity, space_complexity, execution_time = generate_power_set_backtracking(elements)

#         st.success(f"Power Set using {method} method:")
#         st.info(f"Time Complexity: {time_complexity}")
#         st.success(f"Space Complexity: {space_complexity}")
#         st.info(f"Execution Time: {execution_time:.6f} seconds")

#         for subset in power_set:
#             st.write(subset)

import streamlit as st
from itertools import chain, combinations
import time
import sys

# Function to calculate the estimated space complexity
def estimate_space_complexity(elements, method):
    if method == "Brute Force":
        space_used = sys.getsizeof(generate_power_set_brute_force(elements))
    else:
        space_used = sys.getsizeof(generate_power_set_backtracking(elements))
    return space_used

# Function to generate the power set using a brute force approach
def generate_power_set_brute_force(elements):
    start_time = time.time()
    power_set = []
    for subset_len in range(len(elements) + 1):
        for subset in combinations(elements, subset_len):
            power_set.append(subset)
    end_time = time.time()
    time_complexity = f"O(2^{len(elements)})"  # Calculate time complexity
    space_complexity = f"O(2^{len(elements)})"
    return power_set, time_complexity, space_complexity, end_time - start_time

# Function to generate the power set using backtracking
def generate_power_set_backtracking(elements):
    def backtrack(subset, start):
        power_sets.append(subset[:])  # Add the current subset to the power set

        for i in range(start, len(elements)):
            subset.append(elements[i])
            backtrack(subset, i + 1)
            subset.pop()  # Backtrack

    start_time = time.time()
    power_sets = []
    backtrack([], 0)
    end_time = time.time()
    time_complexity = f"O(2^{len(elements)})"
    space_complexity = f"O(n)"  # Backtracking uses O(n) space for the call stack
    return power_sets, time_complexity, space_complexity, end_time - start_time

# Set page title and description
st.set_page_config(
    page_title="Power Set Generator",
    page_icon="✨",
    layout="wide"
)

# Page layout
st.title("Power Set Generator")

# Ask the user to select the method
method = st.radio("Select the method", ("Brute Force", "Backtracking"))

# Input for number of elements
n = st.number_input("Enter the number of elements (n):", min_value=0, step=1, value=0)

# Input for elements
elements = []
for i in range(n):
    element = st.text_input(f"Enter element {i + 1}:", key=f"element_{i}")
    elements.append(element)

# Button to generate power set
if st.button("Generate Power Set"):
    # Remove empty string elements
    elements = [e for e in elements if e]

    if len(elements) == 0:
        st.warning("Please enter at least one element.")
    else:
        if method == "Brute Force":
            power_set, time_complexity, space_complexity, execution_time = generate_power_set_brute_force(elements)
        else:
            power_set, time_complexity, space_complexity, execution_time = generate_power_set_backtracking(elements)

        space_used = estimate_space_complexity(elements, method)

        st.info(f"Time Complexity: {time_complexity}")
        st.success(f"Execution Time: {execution_time:.6f} seconds")
        st.info(f"Space Complexity: {space_complexity}")
        st.success(f"Estimated Space Used: {space_used} bytes")
        

        st.info(f"Power Set using {method} method:")

        for subset in power_set:
            st.write(subset)
