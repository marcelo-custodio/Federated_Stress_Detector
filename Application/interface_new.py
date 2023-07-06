import streamlit as st
import pandas as pd
import json

st.write("""
         # My first app
         Hello *world!*
         """)

with open('../Application/db.json') as f:
    data = json.loads(f.read())
data = data['_default']
df = pd.DataFrame(data).transpose()

print(df)

st.line_chart(df)