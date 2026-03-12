
# Market Research Crew

An AI-powered multi-agent market research application built with CrewAI, Groq, and Streamlit. Enter any company name and four specialized AI agents will research it and generate a comprehensive professional market research report.

## Live Demo
[Click here to try the app] https://market-research-crew.streamlit.app/ ← We will add this link after Streamlit deployment

## What It Does

Enter any company name and the app will automatically generate a full market research report covering company overview, market analysis, competitor landscape, SWOT analysis, and key business insights.

## How It Works

Four specialized AI agents work sequentially to research and write the report:

- **Agent 1 — Company Researcher** finds the company overview, history, products, team, funding, and latest news
- **Agent 2 — Market Analyst** analyzes the industry size, growth rate, trends, opportunities, and threats
- **Agent 3 — Competitor Analyst** identifies top 3 competitors and builds a SWOT analysis
- **Agent 4 — Report Writer** synthesizes all findings into a professional markdown report

## Tech Stack

- **CrewAI** — multi-agent orchestration framework
- **Groq** — ultra-fast LLM inference platform
- **Llama 3.3 70B** — large language model by Meta
- **Streamlit** — web application framework
- **Python** — core programming language

## Project Structure
```
market-research-crew/
├── config.py        # LLM connection and API configuration
├── agents.py        # Four specialized AI agent definitions
├── tasks.py         # Task assignments and context passing
├── crew.py          # Crew orchestration and kickoff function
├── app.py           # Streamlit web interface
├── requirements.txt # Project dependencies
└── .gitignore       # Git ignore rules
```

## How to Run Locally

**1. Clone the repository**
```
git clone https://github.com/aamirqadeerdev/-market-research-crew.git
cd market-research-crew
```

**2. Create and activate virtual environment**
```
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**
```
pip install -r requirements.txt
pip install litellm
pip install "crewai[google-genai]"
```

**4. Create .env file**
```
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=dummy-key-not-used
```

**5. Run the app**
```
streamlit run app.py
```

## Key Concepts Demonstrated

- Multi-agent AI system design and orchestration
- Sequential pipeline with context passing between agents
- LLM API integration with rate limit handling
- Professional web application development
- Secure API key management with environment variables
- Clean project structure and documentation

## Author

Aamir Qadeer — Full Stack Developer and AI Engineer
- Available for Canadian remote opportunities
- Open to relocation to Canada