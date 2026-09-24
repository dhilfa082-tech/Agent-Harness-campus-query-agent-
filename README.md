# Campus Query Agent

An AI agent built with Google's Agent Development Kit (ADK) that answers
campus-related questions by autonomously selecting and calling the right
tool — rather than just generating a text response.

## What it does

The agent receives a natural-language question and decides, on its own,
whether to:
- Look up an answer in a campus FAQ (course info, library hours, faculty contacts)
- Calculate the number of days remaining until a given date (e.g. exam deadlines)
- Respond that it doesn't know, if neither tool applies

This demonstrates core **agent harness** behavior: planning, tool selection,
and execution — not just prompt-response chat.

## Tools

| Tool | Purpose |
|------|---------|
| `search_faq` | Searches a local FAQ dataset for a matching answer |
| `days_until` | Calculates days remaining until a given YYYY-MM-DD date |

## Tech stack

- **Google Agent Development Kit (ADK)** — agent orchestration and tool-calling
- **Gemini** (`gemini-3.6-flash`) — underlying LLM
- **Python**

## Skills demonstrated

Built as a hands-on project after completing Google Cloud Skills Boost's
**"Build Your First Agent with Agent Development Kit (ADK)"** course —
applying agent configuration, tool integration, and autonomous tool
selection in a real, working project.

## Running locally

1. Clone the repo
2. Install dependencies: `pip install google-adk`
3. Add your Gemini API key to a `.env` file (see `.env.example` if provided)
4. Run the ADK dev server and open the Dev UI to chat with the agent