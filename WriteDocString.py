# Definition of Docstring: 
# Like a comment, to document a specific segment of code, 
# but unlike conventional source code comments, 
# the docstring should describe what the function does, not how.

def readable_timedelta(days):
    """returns number of weeks and days in days as string"""
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)