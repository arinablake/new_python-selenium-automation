# Create a function that will take a string as an input and return the 1st unique letter of a string.
# “Google” => “l”
# “Amazon” => “m”
# If there are no unique letters, return an empty string: “xoxoxo” => “”.
# How would you test it? How would you handle edge cases?

string1 = input('Enter a string ')


def unique(word):
    word = word.lower()
    for i in word:
        if word.count(i) == 1:
            return i
    else:
        return ''


print(unique(string1))
