from datetime import datetime

FAQ_DATA = {
    "library hours": "The library is open 8 AM to 8 PM on weekdays.",
    "exam dates": "Semester exams start on the date announced in the academic calendar.",
    "faculty contact": "Contact your HOD's office for faculty email IDs.",
}

def search_faq(query: str) -> str:
    """Searches the campus FAQ for an answer matching the query.

    Args:
        query: The user's question, e.g. 'library hours' or 'exam dates'.

    Returns:
        The matching FAQ answer, or a message saying nothing was found.
    """
    query_lower = query.lower()
    for key, answer in FAQ_DATA.items():
        if key in query_lower:
            return answer
    return "I couldn't find that in the FAQ. Try asking about library hours, exam dates, or faculty contact."


def days_until(date_str: str) -> str:
    """Calculates the number of days from today until a given date.

    Args:
        date_str: A date in YYYY-MM-DD format, e.g. '2026-12-15'.

    Returns:
        A string stating how many days remain.
    """
    try:
        target = datetime.strptime(date_str, "%Y-%m-%d")
        delta = (target - datetime.now()).days
        if delta < 0:
            return f"That date has already passed, {abs(delta)} days ago."
        return f"There are {delta} days until {date_str}."
    except ValueError:
        return "Please provide the date in YYYY-MM-DD format."