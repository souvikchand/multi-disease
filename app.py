import streamlit as st
import pickle

st.title('Welcome')

css_code = """
<style>
ul {
    list-style-type: none; /* Removes bullets from unordered lists */
    padding-left: 0; /* Removes left padding */
}
li {
    margin-bottom: 10px; /* Optional: Add space between list items */
}
</style>
"""
st.markdown(css_code,unsafe_allow_html=True)

heart_link= "https://medlineplus.gov/heartdiseases.html#:~:text=What%20is%20heart%20disease%3F,many%20types%20of%20heart%20disease."


text="""
<p>Welcome to our Health Diagnostic App, your comprehensive tool for early detection and 
    management of critical health conditions. Our app specializes in identifying 
    multiple diseases, including:
</p>
<p>
<ul>
<li><strong><a href="https://www.cdc.gov/heart-disease/about/index.html">Heart Disease:</a></strong> A leading cause of death worldwide, early detection is crucial for effective treatment and management.</li>

<li><strong><a href="https://en.wikipedia.org/wiki/Parkinson%27s_disease">Parkinson’s Disease:</a></strong> A progressive neurological disorder affecting movement, early diagnosis can significantly improve quality of life.</li>

<li><strong><a href="https://en.wikipedia.org/wiki/Diabetes">Diabetes:</a></strong> A chronic condition that affects how your body processes sugar, timely detection helps in preventing serious complications.</li>

<li><strong><a href="https://en.wikipedia.org/wiki/Breast_cancer">Breast Cancer:</a></strong> One of the most common cancers among women, early detection through regular screening can save lives.</li>
</ul>
</p>
<p>
Our app combines advanced technology with medical expertise to offer you reliable and accurate health assessments, empowering you to take control of your well-being.
</p>
"""

st.markdown(text,unsafe_allow_html=True)