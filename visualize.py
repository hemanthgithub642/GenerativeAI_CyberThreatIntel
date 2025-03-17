import streamlit as st
import json
import pandas as pd
import plotly.express as px

st.title("Cyber Threat Intelligence Dashboard")

# Load data
with open("data/summarized_threats.json", "r") as f:
    threats = json.load(f)

df = pd.DataFrame(threats)

st.write("## Summarized Threat Intelligence")
st.dataframe(df)

fig = px.bar(df, x="title", y=df.index, title="Threat Intelligence Summary", text_auto=True)
st.plotly_chart(fig)

