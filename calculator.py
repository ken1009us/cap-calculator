from decimal import Decimal


def calculation(sprint_days, hours_per_day, meeting_hours, pto_hours):
    lst = [sprint_days, hours_per_day, meeting_hours, pto_hours]
    for i in range(len(lst)):
        try:
            lst[i] = float(lst[i])
        except:
            text = "Please enter a valid number."
            return text

    res = round(((((lst[0] * lst[1]) * 0.9) - (lst[2] * 1.1)) - lst[3]) * 2) / 2
    text = f"Your capacity is {res} hours."

    return text
