"""Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively."""

from datetime import datetime

def dayOfTheWeek(day, month, year):
    """
    :type day: int
    :type month: int
    :type year: int
    :rtype: str
    """
    date = datetime(year, month, day)
    weekDays = ("Monday", "Tuesday",
                "Wednesday", "Thursday",
                "Friday", "Saturday",
                "Sunday")
    week = datetime.weekday(date)
    return weekDays[week]
