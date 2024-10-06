import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from bruteforce import powerset_bruteforce
from backtrack import powerset_backtracking

st.title("Powerset Finder App")

input_set = st.text_input("Enter a set of elements (comma-separated):", placeholder="Ex: 1,2,6,2")
input_set = [x.strip() for x in input_set.split(',')]

if st.button("Find Powerset - Brute Force"):
    if not input_set:
        st.warning("Please enter a set of elements.")
    else:
        powerset = powerset_bruteforce(input_set)
        st.success(f"Powerset (Brute Force): {powerset}")
        
        # Visualize the brute force process
        G = nx.Graph()
        G.add_node('Empty Set')
        for subset in powerset:
            G.add_node(', '.join(subset))
            G.add_edge('Empty Set', ', '.join(subset))
        
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue')
        plt.title("Brute Force Powerset Generation")
        plt.axis('off')
        st.pyplot(plt)

if st.button("Find Powerset - Backtracking"):
    if not input_set:
        st.warning("Please enter a set of elements.")
    else:
        powerset = powerset_backtracking(input_set)
        st.success(f"Powerset (Backtracking): {powerset}")

        # Visualize the backtracking process
        G = nx.Graph()
        G.add_node('Empty Set')
        def backtrack_visualization(subset):
            if not subset:
                return
            for i, element in enumerate(subset):
                G.add_node(', '.join(element))
                G.add_edge('Empty Set', ', '.join(element))
                backtrack_visualization(subset[i+1:])
        backtrack_visualization(input_set)
        
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue')
        plt.title("Backtracking Powerset Generation")
        plt.axis('off')
        st.pyplot(plt)

st.sidebar.markdown("Description: This is a Minor Assignment to Find the Powerset of given list of set by either Bruteforce or Backtracking")
