"""
Quest: Who likes it? (6 Kyu)

You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Note: For 4 or more names, the number in "and 2 others" simply increases.

"""

def likes (name):
    n = len(name)

    if n == 0:
        return "no one likes this"
    elif n == 1:
        return f"{name[0]} likes this"
    elif n == 2:
        return f"{name[0]} and {name[1]} like this"
    elif n == 3:
        return f"{name[0]}, {name[1]} and {name[2]} like this"
    else:
        return f"{name[0]}, {name[1]} and {n - 2} others like this"

likes_list = ["Alex", "Jacob", "Mark", "Max"]
print(likes(likes_list))