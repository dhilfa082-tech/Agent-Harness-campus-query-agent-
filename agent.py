from google.adk.agents import Agent
from .tools import search_faq, days_until

root_agent = Agent(
    model="gemini-3.6-flash",
    name="campus_query_agent",
    description="An agent that answers campus questions using tools",
    instruction=(
        "You are a campus assistant. Use the search_faq tool for questions "
        "about courses, faculty, or deadlines. Use the days_until tool for "
        "date or countdown questions. If neither tool applies, say you don't know."
    ),
    tools=[search_faq, days_until],
)