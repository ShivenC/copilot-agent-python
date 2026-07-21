# AI Program Management Automation System

An AI-powered program management platform that automates Jira security ticket collection, storage, reporting, and executive summaries using Model Context Protocol (MCP), AWS, and Python.

## Overview

This project automates the lifecycle of security and program management tickets by collecting Jira issues, storing them centrally, exposing them through an MCP server, and allowing AI agents to generate real-time summaries and dashboards.

The system is designed to reduce manual reporting and provide program managers with quick insights into ongoing work.

## Features

- Automatically pulls Jira tickets using scheduled jobs
- Stores ticket data in Amazon S3
- MCP server for centralized ticket access
- AI Copilot agent for ticket analysis and summarization
- Interactive reporting dashboard
- EventBridge scheduling for automated execution
- Modular Python architecture for easy expansion

## Architecture

```
Jira
   │
   ▼
Scheduled Event (AWS EventBridge)
   │
   ▼
Python Ticket Collector
   │
   ▼
Amazon S3 Storage
   │
   ▼
MCP Server
   │
   ├── AI Copilot Agent
   └── Dashboard
```

## Repository Structure

```
.
├── ai_agent.py                # AI Copilot agent
├── dashboard.py               # Reporting dashboard
├── eventbridge_schedule.py    # EventBridge scheduler
├── generate_tickets.py        # Ticket generation utilities
├── mcp_server.py              # MCP server
├── mcp_tools.py               # MCP helper functions
├── pull_jira_to_mcp.py        # Imports Jira tickets into MCP
├── s3_store.py                # Amazon S3 storage logic
├── requirements.txt
└── README.md
```

## Technologies

- Python
- AWS EC2
- Amazon S3
- Amazon EventBridge
- Jira REST API
- Model Context Protocol (MCP)
- AI Copilot Agents

## Workflow

1. EventBridge triggers the scheduled job.
2. Jira tickets are collected through the Jira API.
3. Ticket data is stored in Amazon S3.
4. The MCP server exposes ticket information.
5. AI agents analyze tickets and generate summaries.
6. Dashboard displays reporting and project insights.

## Installation

Clone the repository:

```bash
git clone https://github.com/ShivenC/copilot-agent-python.git
cd copilot-agent-python
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure your environment variables for:

- Jira API credentials
- AWS credentials
- S3 bucket
- EC2 instance (if applicable)

Run the MCP server:

```bash
python mcp_server.py
```

Run the AI agent:

```bash
python ai_agent.py
```

Launch the dashboard:

```bash
python dashboard.py
```

## Future Improvements

- Slack and Microsoft Teams notifications
- LLM-powered ticket prioritization
- Automatic Jira ticket creation
- Executive KPI dashboards
- Multi-project support
- Enhanced analytics and trend reporting

## Resume Highlights

- Built an MCP server on AWS EC2 to generate, store, and manage Jira-based security tickets automatically.
- Developed AI Copilot agents that read MCP tickets and generate real-time summaries and reporting.
- Leveraged AWS EC2, EventBridge, and Amazon S3 to automate SOC ticketing workflows.

## Author

**Shiven Chhugani**

Cybersecurity | IT | AI Automation

LinkedIn: https://www.linkedin.com/in/shiven-chhugani/

GitHub: https://github.com/ShivenC
