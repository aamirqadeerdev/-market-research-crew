
import streamlit as st
from crew import run_crew

st.set_page_config(
    page_title="Market Research Crew",
    page_icon="🔍",
    layout="centered"
)


st.title("Market Research Crew")
st.markdown("Powered by **CrewAI** + **Groq** + **Llama 3.1 8B**")
st.divider()



st.subheader("Enter a Company Name to Research")

company = st.text_input(
    label="Company Name",
    placeholder="e.g. Shopify, Apple, Tesla, Cohere...",
    help="Enter any company name and our AI agents will research it for you."
)

run_button = st.button("Run Market Research", type="primary")


if run_button and company:
    st.divider()
    st.subheader("Research in Progress...")
    
    with st.status("Running AI Agents...", expanded=True) as status:
        st.write("Agent 1 - Researching company profile...")
        st.write("Agent 2 - Analyzing market trends...")
        st.write("Agent 3 - Mapping competitor landscape...")
        st.write("Agent 4 - Writing final report...")
        
        result = run_crew(company)
        
        status.update(label="Research Complete!", state="complete")

    st.divider()
    st.subheader("Market Research Report")
    st.markdown(result.raw)
    
    st.download_button(
        label="Download Report",
        data=result.raw,
        file_name=f"{company}_market_research.md",
        mime="text/markdown"
    )

elif run_button and not company:
    st.warning("Please enter a company name before running.")








