import streamlit as st
import graphviz
import time

# Initialize the global graph variable
global_graph = graphviz.Digraph(format="png")

def powerset_backtracking(input_set):
    def backtrack(start, current_set):
        powerset.append(current_set[:])

        node_label = ",".join(map(str, current_set))
        global_graph.node(node_label)
        if start > 0:
            parent_label = ",".join(map(str, current_set[:-1]))
            global_graph.edge(parent_label, node_label)
        for i in range(start, len(input_set)):
            current_set.append(input_set[i])
            chart_placeholder = st.empty()
            chart_placeholder.graphviz_chart(global_graph)  # Update the same graph
            time.sleep(1)  # Adjust the delay duration as needed
            chart_placeholder.empty()
            backtrack(i + 1, current_set)
            current_set.pop()     
    powerset = []
    backtrack(0, [])
    chart_placeholder = st.empty()
    chart_placeholder.graphviz_chart(global_graph)  # Update the same graph
    return powerset

def powerset_bruteforce(input_set):
    n = len(input_set)
    powerset = []

    for i in range(2 ** n):
        subset = []
        for j in range(n):
            if (i >> j) & 1:
                subset.append(input_set[j])
        powerset.append(subset)

    return powerset
st.title("Powerset Finder App")

input_set = st.text_input("Enter a set of elements (comma-separated):", placeholder="Ex: 1,2,6,2")

input_set = [x.strip() for x in input_set.split(',')]

if st.button("Find Powerset - Backtracking"):
    if not input_set:
        st.warning("Please enter a set of elements.")
    else:
        st.info("Finding Powerset (Backtracking)...")
        st.graphviz_chart(global_graph)  # Display an empty graph initially
        powerset_backtrack = powerset_backtracking(input_set)
        st.success(f"Powerset (Backtracking): {powerset_backtrack}")

if st.button("Find Powerset - Brute Force"):
    if not input_set:
        st.warning("Please enter a set of elements.")
    else:
        st.info("Finding Powerset (Brute Force)...")
        st.graphviz_chart(global_graph)  # Display an empty graph initially
        powerset_brute = powerset_bruteforce(input_set)
        st.success(f"Powerset (Brute Force): {powerset_brute}")
