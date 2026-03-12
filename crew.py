
from crewai import Crew, Process
from agents import company_researcher, market_analyst, competitor_analyst, report_writer
from tasks import company_research_task, market_analysis_task, competitor_analysis_task, report_writing_task
import time

crew = Crew(
    agents=[
        company_researcher,
        market_analyst,
        competitor_analyst,
        report_writer
    ],
    tasks=[
        company_research_task,
        market_analysis_task,
        competitor_analysis_task,
        report_writing_task
    ],
    process=Process.sequential,
    verbose=True
)

def run_crew(company):
    max_retries = 5
    for attempt in range(max_retries):
        try:
            result = crew.kickoff(inputs={"company": company})
            return result
        except Exception as e:
            if "rate_limit" in str(e).lower() or "ratelimit" in str(e).lower():
                wait_time = 45
                print(f"Rate limit hit. Waiting {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                raise e
    return None