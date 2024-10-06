import streamlit as st
import networkx as nx
import plotly.graph_objects as go
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

        # Dynamic visualization of brute force powerset generation
        G = nx.Graph()
        G.add_node('Empty Set')
        pos = {'Empty Set': (0, 0)}
        fig = go.Figure()
        fig.update_layout(title_text="Brute Force Powerset Generation")
        fig.update_xaxes(showticklabels=False)
        fig.update_yaxes(showticklabels=False)
        y_offset = [0]  # Use a list to store y_offset

        for i in range(len(input_set)):
            st.write(f"Step {i + 1}:")
            for subset in powerset:
                if len(subset) == i and subset:
                    subset_str = ', '.join(subset)
                    if subset_str not in G:
                        G.add_node(subset_str)
                        G.add_edge(', '.join(subset[:i]), subset_str)
                        x0, y0 = pos.get(', '.join(subset[:i]), (0, 0))
                        x1, y1 = x0 + 1, y0 + y_offset[0]  # Increase y-coordinate for spacing
                        fig.add_trace(go.Scatter(x=[x0, x1], y=[y0, y1], mode='lines+text',
                                                 text=[subset_str], textposition='top left', showlegend=False))
                        pos[subset_str] = (x1, y1)
                        y_offset[0] += 0.1  # Adjust the spacing
        st.plotly_chart(fig)
        st.success("Brute Force Powerset Generation Completed!")

if st.button("Find Powerset - Backtracking"):
    if not input_set:
        st.warning("Please enter a set of elements.")
    else:
        powerset = powerset_backtracking(input_set)
        st.success(f"Powerset (Backtracking): {powerset}")

        # Dynamic visualization of backtracking powerset generation
        G = nx.Graph()
        G.add_node('Empty Set')
        pos = {'Empty Set': (0, 0)}
        fig = go.Figure()
        fig.update_layout(title_text="Backtracking Powerset Generation")
        fig.update_xaxes(showticklabels=False)
        fig.update_yaxes(showticklabels=False)
        y_offset = [0]  # Use a list to store y_offset

        def backtrack_visualization(subset):
            if not subset:
                return
            for i, element in enumerate(subset):
                subset_str = ', '.join(element)
                if subset_str not in G:
                    G.add_node(subset_str)
                    G.add_edge(', '.join(element[:i]), subset_str)
                    x0, y0 = pos.get(', '.join(element[:i]), (0, 0))
                    x1, y1 = x0 + 1, y0 + y_offset[0]  # Increase y-coordinate for spacing
                    fig.add_trace(go.Scatter(x=[x0, x1], y=[y0, y1], mode='lines+text',
                                             text=[subset_str], textposition='top left', showlegend=False))
                    pos[subset_str] = (x1, y1)
                    y_offset[0] += 0.1  # Adjust the spacing
                backtrack_visualization(subset[i + 1:])

        backtrack_visualization(input_set)
        st.plotly_chart(fig)
        st.success("Backtracking Powerset Generation Completed!")

st.sidebar.markdown("Description: This is a Minor Assignment to Find the Powerset of the given list of sets by either Bruteforce or Backtracking")
