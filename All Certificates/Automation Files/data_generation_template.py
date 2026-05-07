import random
from datetime import datetime, timedelta


def generate_random_data(n):
    dates = []
    percentages = []

    start_date = datetime(2015, 1, 1)
    end_date = datetime(2025, 12, 31)

    date_range = (end_date - start_date).days

    for _ in range(n):
        random_days = random.randint(0, date_range)
        random_date = start_date + timedelta(days=random_days)

        percentage = round(random.uniform(50, 100), 2)

        dates.append(random_date.strftime("%d-%m-%Y"))
        percentages.append(percentage)

    return dates, percentages


n = 600
dates, percentages = generate_random_data(n)

with open("synthetic_data.txt", "w") as f:
    f.write("Dates = " + str(dates) + "\n\n")
    f.write("Percentages = " + str(percentages))
