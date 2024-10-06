import streamlit as st
from bruteforce import powerset_bruteforce
from backtrack import powerset_backtracking

st.title("Powerset Finder App")


input_set = st.text_input("Enter a set of elements (comma-separated):",placeholder="Ex: 1,2,6,2")

input_set = [x.strip() for x in input_set.split(',')]

if st.button("Find Powerset - Brute Force"):
    if not input_set:
        st.warning("Please enter a set of elements.")
    else:
        powerset = powerset_bruteforce(input_set)
        st.success(f"Powerset (Brute Force): {powerset}")

if st.button("Find Powerset - Backtracking"):
    if not input_set:
        st.warning("Please enter a set of elements.")
    else:
        powerset = powerset_backtracking(input_set)
        st.success(f"Powerset (Backtracking): {powerset}")

st.sidebar.markdown("Description: This is a Minor Assignment to Find the Powerset of given list of set by either Bruteforce or Backtracking")

