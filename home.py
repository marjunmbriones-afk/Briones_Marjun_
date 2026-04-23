import streamlit as st

st.set_page_config(
    page_title="Marjun Portfolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 🔹 CUSTOM SIDEBAR
with st.sidebar:
    st.markdown("## 💼 Marjun Briones")
    st.markdown("### 🚀 Developer Portfolio")
    
    st.markdown("---")
    
    st.write("### 📌 Navigation")
    st.caption("Use the menu above 👆 to switch pages")
    
    st.markdown("---")
    
    st.write("### 🌐 Connect")
    st.write("🐙 GitHub")
    st.write("📘 Facebook")

# 🔹 MAIN PAGE
st.title("💼 My Portfolio")

st.markdown("""
### Welcome 👋  
This is my professional portfolio built using Streamlit.

Explore my:
- Skills  
- Projects  
- Experience  
""")

st.markdown("---")

col1, col2, col3 = st.columns(3)

col1.metric("Projects", "5+")
col2.metric("Skills", "10+")
col3.metric("Learning", "Daily 📈")

st.success("✔ Fully functional multipage app")