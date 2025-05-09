import calendar

year = 2025

# Loop through all 12 months
for month in range(1, 13):
    # Get the month's name
    month_name = calendar.month_name[month]
    # Get the number of days in the month
    num_days = calendar.monthrange(year, month)[1]
    
    print(f"\n {month_name} {year}")
    print("-" * (len(month_name) + 6))
    
    # Print all the days in the month
    for day in range(1, num_days + 1):
        print(f"{day:02d} {month_name} {year}")
