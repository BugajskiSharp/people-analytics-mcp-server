from mcp.server import MCPServer

mcp = MCPServer("HR Analytics Demo")

employees = [
    {
        "employee_id": 1001,
        "name": "Jordan Lee",
        "division": "Human Resources",
        "manager": "Taylor Smith",
        "status": "Active"
    },
    {
        "employee_id": 1002,
        "name": "Morgan Hill",
        "division": "Finance",
        "manager": "Alex Green",
        "status": "Active"
    },
    {
        "employee_id": 1003,
        "name": "Casey Brown",
        "division": "Human Resources",
        "manager": None,
        "status": "Active"
    },
    {
        "employee_id": 1004,
        "name": "Jamie Chen",
        "division": "IT",
        "manager": "Sam Patel",
        "status": "Inactive"
    },
    {
        "employee_id": 1005,
        "name": "Riley Davis",
        "division": "Finance",
        "manager": "Alex Green",
        "status": "Active"
    }
]

@mcp.tool()
def get_headcount() -> int:
    """Return the number of active employees."""
    return sum(
        1 for employee in employees
        if employee["status"] == "Active"
    )

@mcp.tool()
def get_headcount_by_division(user_role: str, division: str) -> dict:
    """Return active headcount for a valid division if the user is authorized."""

    authorized_roles = ["Manager", "HR Analyst"]

    if user_role not in authorized_roles:
        return {
            "success": False,
            "authorized": False,
            "message": "You are not authorized to access division headcount."
        }

    valid_divisions = {
        employee["division"]
        for employee in employees
    }

    matched_division = next(
        (
            valid_division
            for valid_division in valid_divisions
            if valid_division.lower() == division.lower()
        ),
        None
    )

    if matched_division is None:
        return {
            "success": False,
            "authorized": True,
            "message": "Division not found.",
            "available_divisions": sorted(valid_divisions)
        }

    count = sum(
        1 for employee in employees
        if employee["status"] == "Active"
        and employee["division"] == matched_division
    )

    return {
        "success": True,
        "authorized": True,
        "role": user_role,
        "division": matched_division,
        "active_headcount": count
    }