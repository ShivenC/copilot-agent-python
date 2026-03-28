# ai_agent.py
import openai
import json
from mcp_tools import get_ticket_details

openai.api_key = "YOUR_OPENAI_API_KEY"

def summarize_ticket(ticket_id):
    ticket = get_ticket_details(ticket_id)  # your MCP server tool
    prompt = f"""
    You are a SOC analyst.
    Read this Jira ticket and provide:
    1. A short summary
    2. Severity
    3. Recommended next steps
    Ticket: {json.dumps(ticket)}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user", "content": prompt}],
        temperature=0.2
    )
    summary = response['choices'][0]['message']['content']
    print(summary)
    return summary
