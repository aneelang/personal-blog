import streamlit as st
import mymodel as m

st.write("""# Sales Model
Below are the sales predictions for this customer""")

st.write(m.run(window=15))