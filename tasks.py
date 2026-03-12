

from crewai import Task
from agents import company_researcher, market_analyst, competitor_analyst, report_writer


company_research_task = Task(
    description="Research the company {company} thoroughly. "
                "Find their complete overview, history, products "
                "and services, team size, headquarters location, "
                "funding history, key people, and any latest news "
                "or developments. Be as detailed as possible.",
    expected_output="A detailed company profile containing all "
                    "key information about {company} including "
                    "overview, products, team, funding, location "
                    "and latest news. Minimum 200 words.",
    agent=company_researcher
)


market_analysis_task = Task(
    description="Analyze the industry that {company} operates in. "
                "Using the company research already completed, "
                "find the total market size, annual growth rate, "
                "key market trends, major opportunities, potential "
                "threats, and future market outlook. Include "
                "TAM, SAM and SOM estimates where possible.",
    expected_output="A comprehensive market analysis report covering "
                    "industry size, growth rate, key trends, "
                    "opportunities, threats and future outlook "
                    "for the industry that {company} operates in. "
                    "Minimum 200 words.",
    agent=market_analyst,
    context=[company_research_task]
)



competitor_analysis_task = Task(
    description="Identify the top 3 competitors of {company}. "
                "Using the company research and market analysis "
                "already completed, compare their strengths and "
                "weaknesses against {company}. Build a detailed "
                "competitive landscape. Create a SWOT analysis "
                "for {company} based on your findings.",
    expected_output="A detailed competitor analysis containing "
                    "the top 3 competitors of {company}, their "
                    "strengths and weaknesses, a competitive "
                    "landscape overview, and a full SWOT analysis "
                    "for {company}. Minimum 200 words.",
    agent=competitor_analyst,
    context=[company_research_task, market_analysis_task]
)


report_writing_task = Task(
    description="Using all the research completed about {company}, "
                "write a comprehensive and professional market "
                "research report in clean Markdown format. "
                "The report must include all findings from the "
                "company research, market analysis, and competitor "
                "analysis. Make it professional enough to present "
                "to a board of directors or investment committee.",
    expected_output="""A complete professional market research report 
    in Markdown format with the following sections:
    
    # Market Research Report — {company}
    
    ## 1. Executive Summary
    ## 2. Company Overview
    ## 3. Market Analysis
    ## 4. Competitor Landscape
    ## 5. SWOT Analysis
    ## 6. Key Insights and Recommendations
    
    Each section must be detailed and well written.
    Minimum 500 words total.""",
    agent=report_writer,
    context=[company_research_task, market_analysis_task, competitor_analysis_task]
)












