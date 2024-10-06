import streamlit as st
import time

global_graph = """digraph {
    A -> B
    B -> C
    C -> D
    D -> A
}"""

# Show the graph initially
chart_placeholder = st.empty()
chart_placeholder.graphviz_chart(global_graph)

# Set a timer to remove the graph after a few seconds (e.g., 5 seconds)
timeout = 5  # seconds
start_time = time.time()

while True:
    elapsed_time = time.time() - start_time
    if elapsed_time >= timeout:
        # Clear the chart by updating the placeholder with an empty string
        chart_placeholder.empty()
        break

    # Update Streamlit to trigger a refresh and check the elapsed time
    st.text(f"Elapsed Time: {int(elapsed_time)} seconds")
    time.sleep(1)  # Sleep for 1 second to avoid high CPU usage
