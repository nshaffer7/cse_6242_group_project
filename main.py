import streamlit as st

# Containers for UI
header = st.container()
overview = st.container()
graph = st.container()

# Title
with header:

    st.title("Transmission Outage Plan Likelihood of Deviation")
    #st.header("CSE 6242 Group Project: Team 179")

# Project intro/summary
with overview:
    st.subheader("Overview")
    st.write("We modeled and estimated the likelihood of a transmission outage plan deviating from the published plan. We classified an outage plan into groups based on the amount of deviation between the planned period and the actual period.")

# Visualization
with graph:

    # User Input
    st.subheader("Explore the graph representation")
    st.write("Select start date, end date, and region. Optionally, you can also select the retail electricity pricing level.")
    
    col_one, col_two, col_three, col_four = st.columns(4)

    start_date = col_one.selectbox("Start Date", [])
    end_date = col_two.selectbox("End Date", [])
    region = col_three.selectbox("Region", ['SPPISO', 'CAISO', 'NYISO', 'ERCOT', 'MISO', 'PJMISO', 'NEISO'])
    pricing = col_four.radio("Retail Electricity Pricing", ["High", "Average", "Low"])








