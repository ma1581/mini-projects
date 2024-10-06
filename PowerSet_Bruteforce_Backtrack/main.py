import streamlit as st
import graphviz
import time

def powerset_backtracking(input_set):
    global_graph = graphviz.Digraph(format="png")
    
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
            time.sleep(2)  # Adjust the delay duration as needed
            chart_placeholder.empty()
            backtrack(i + 1, current_set)
            current_set.pop()

    powerset = []
    backtrack(0, [])
    chart_placeholder = st.empty()
    chart_placeholder.graphviz_chart(global_graph)  # Display the graph for backtracking
    return powerset

def powerset_bruteforce(input_set):
    global_graph = graphviz.Digraph(format="png")
    
    n = len(input_set)
    powerset = []

    for i in range(2 ** n):
        subset = []
        for j in range(n):
            if (i >> j) & 1:
                subset.append(input_set[j])
        powerset.append(subset)

    # Build a separate graph for brute force
    for i in range(len(powerset)):
        for j in range(i + 1, len(powerset)):
            if set(powerset[i]).issubset(set(powerset[j])):
                node_label_i = ",".join(map(str, powerset[i]))
                node_label_j = ",".join(map(str, powerset[j]))
                global_graph.edge(node_label_i, node_label_j)
                chart_placeholder = st.empty()
                chart_placeholder.graphviz_chart(global_graph)  # Update the same graph
                time.sleep(1)  # Add a delay to see each exploration
                chart_placeholder.empty()

    chart_placeholder = st.empty()
    chart_placeholder.graphviz_chart(global_graph)  # Display the final graph for brute force
    return powerset

st.title("Powerset Finder App")

input_set = st.text_input("Enter a set of elements (comma-separated):", placeholder="Ex: 1,2,6,2")

input_set = [x.strip() for x in input_set.split(',')]

if st.button("Find Powerset - Backtracking"):
    if not input_set:
        st.warning("Please enter a set of elements.")
    else:
        st.info("Finding Powerset (Backtracking)...")
        powerset_backtrack = powerset_backtracking(input_set)
        st.graphviz_chart(graphviz.Digraph())  # Clear the graph by displaying an empty graph
        st.success(f"Powerset (Backtracking): {powerset_backtrack}")

if st.button("Find Powerset - Brute Force"):
    if not input_set:
        st.warning("Please enter a set of elements.")
    else:
        st.info("Finding Powerset (Brute Force)...")
        powerset_brute = powerset_bruteforce(input_set)
        st.graphviz_chart(graphviz.Digraph())  # Clear the graph by displaying an empty graph
        st.success(f"Powerset (Brute Force): {powerset_brute}")
