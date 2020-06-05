# Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.
#
# Your task is to make 'Past' function which returns time converted to milliseconds.
#
# Example:
#
# past(0, 1, 1) == 61000

def past(h, m, s):
    return (3600*h + 60*m + s) * 1000


print(past(1, 0, 2))