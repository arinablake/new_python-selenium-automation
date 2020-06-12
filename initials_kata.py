# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
#
# The output should be two capital letters with a dot separating them.
#
# It should look like this:
#
# Sam Harris => S.H
#
# Patrick Feeney => P.F


name1 = input('Enter name ')
def name_to_initials(name):
    name = name.upper()
    list1 = name.split(' ')
    ni = list1[0][0]
    li = list1[1][0]
    print(f'{ni}.{li}')

name_to_initials(name1)

# def abbrevName(name):
#     name = name.upper()
#     list1 = name.split(' ')
#     ni = list1[0][0]
#     li = list1[1][0]
#     return f'{ni}.{li}'