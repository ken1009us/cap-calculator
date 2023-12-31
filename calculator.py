from decimal import Decimal


def calculate_capacity(sprint_days, hours_per_day, meeting_hours, pto_hours):
    """
    Calculate the available working capacity.

    Args:
        sprint_days (str): Number of sprint days.
        hours_per_day (str): Number of working hours per day.
        meeting_hours (str): Number of hours spent in meetings.
        pto_hours (str): Number of PTO (Paid Time Off) hours.

    Returns:
        str: The calculated capacity in hours or an error message.
    """
    inputs = [sprint_days, hours_per_day, meeting_hours, pto_hours]

    try:
        inputs = [float(item) for item in inputs]
    except ValueError:
        return "Please enter valid numbers."

    capacity = (
        round((((inputs[0] * inputs[1]) * 0.9) - (inputs[2] * 1.1) - inputs[3]) * 2) / 2
    )
    return f"Your capacity is {capacity} hours."
