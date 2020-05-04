# Write a function named readable_timedelta. 
# The function should take one argument, an integer days, and return a string that says how many weeks and days that is. 
# For example, calling the function and printing the result like this:
# print(readable_timedelta(10))

# should output the following:
# 1 week(s) and 3 day(s).

def readable_timedelta(days):
    total_weeks = days//7
    total_days = days % 7
    return "{} week(s) and {} day(s).".format(total_weeks, total_days)

# test your function
print(readable_timedelta(10))