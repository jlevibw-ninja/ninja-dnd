import streamlit as st

# Create two columns
col1, col2 = st.columns(2)

# Put an empty container in the first column
placeholder = col1.empty()

# Fill it with the first set of widgets
with placeholder.container():
    st.write("First Set")
    val1 = st.button("Button 1")

# To clear and replace the widgets in that column later (e.g., on an action):
if val1:
    placeholder.empty()  # This clears the first set of widgets
    with placeholder.container():
        st.write("Second Set")
        val2 = st.text_input("New Input")
