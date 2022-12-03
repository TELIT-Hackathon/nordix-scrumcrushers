import pandas as pd
import streamlit as st

st.write("""
# HELLO!
""")

data1 = pd.read_json("data.json")

df = pd.DataFrame(list(data1.get("summary")))
del df["logo"], df["title"], df["addresses"], df["verificationStatus"]
x = st.slider("Select element", min_value=0, max_value=len(df))
st.write(x, """ # Summary Data """, df.iloc[x].tolist())

# st.write("""# Scores Data""", df2)
