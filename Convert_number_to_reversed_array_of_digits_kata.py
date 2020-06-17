# Convert number to reversed array of digits
#
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
#
# Example:
#
# 348597 => [7,9,5,8,4,3]


num = int(input("Enter number "))


def reverse(n):
    new_list = []
    for i in str(n)[::-1]:
        new_list.append(int(i))
    return new_list


print(reverse(num))
