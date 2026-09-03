# People Analytics MCP Server

A Python-based Model Context Protocol (MCP) project demonstrating how an AI agent can interact with governed People Analytics tools.

Built with **Python, MCP, GitHub Copilot, and VS Code**, this project demonstrates self-service analytics, input validation, role-based authorization, and responsible access to people data.

> All employee data in this project is synthetic. No real employee or confidential HR data is used.

## How It Works

```text
User Question
      ↓
GitHub Copilot
      ↓
MCP Server
      ↓
People Analytics Tool
  • Authorization check
  • Input validation
  • Metric calculation
      ↓
Synthetic HR Data
      ↓
Structured Result
```

**Example:**

A user asks for Finance headcount → Copilot calls the MCP tool → the tool checks authorization and validates the division → Python calculates the metric → the result is returned to Copilot.

## MCP Tools

### `get_headcount()`

Returns the total number of active employees.

### `get_headcount_by_division(user_role, division)`

Returns active headcount for a specified division after validating the division and checking authorization.

**Example:**

```text
HR Analyst + Finance → 2 active employees
Employee + Finance → Access denied
```

## Validation and Answer Quality

The tool validates inputs before calculating headcount.

**For example:**

```text
Finance
finance
FINANCE
```

are treated as the same division.

A misspelling such as `Finace` returns an invalid-division response instead of a misleading headcount of `0`.

## Role-Based Authorization

The project includes a simplified role-based access control (RBAC) demonstration.

| Role | Division Headcount Access |
|---|---|
| Employee | Denied |
| Manager | Allowed |
| HR Analyst | Allowed |

The authorization check occurs before the analytics calculation.

For this portfolio project, the role is supplied to the MCP tool as an argument. A production system would instead verify identity and permissions through a trusted identity and access management system.

## Technologies

- Python
- Model Context Protocol (MCP)
- GitHub Copilot
- Visual Studio Code
- Git and GitHub

## Key Concepts Demonstrated

- AI-accessible analytics tools
- Self-service People Analytics
- Structured tool arguments
- Input validation and error handling
- Role-based authorization
- Data minimization and governance
- Testing valid, invalid, and unauthorized requests

## Next Steps

- Add automated regression tests
- Add additional People Analytics metrics
- Add logging and audit trails
- Explore trusted identity integration

## Disclaimer

This is an educational portfolio project demonstrating MCP and People Analytics concepts. It is not a production HR system.
