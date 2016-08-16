
# Write three functions:

# sort2(languages)
# sort3(langauges)
# Goal: Print exactly the below w/ three functions:
# 1:
#     Arabic
#     English
#     Koine Greek
#     Latin
#     Romanian
#     C++
#     JavaScript
#     Python
#     R
# 2:
#     R
#     C++
#     Latin
#     Arabic
#     Python
#     English
#     Romanian
#     JavaScript
#     Koine Greek
# 3:
#     JavaScript
#     R
#     Latin
#     Python
#     Romanian
#     Koine Greek
#     English
#     Arabic
#     C++
# """

import operator


languages = {'JavaScript': 'P',
             'Arabic': 'N',
             'R': 'P',
             'Python': 'P',
             'C++': 'P',
             'Koine Greek': 'N',
             'Latin': 'N',
             'Romanian': 'N',
             'English': 'N'}


def sort1(x):
    lst = sorted(sorted(x), key=x.__getitem__) #__getitem__ gives you value of an integer
    for x in lst:
        print("\t" + x)


def sort1b(x):
    import operator
    lst = sorted(sorted(x.items()), key=operator.itemgetter(1)) #items() gets list of tuples
    print("1: ")
    for language, type_ in lst:
        print("\t" + language)


def sort2(x):
    lst = sorted(x, key=len)
    print("2:")
    for item in lst:
        print("\t"+item)


def sort3(x):
    lst = sorted(sorted(x), key=last_char, reverse=True) # reversing the entire sort 
    print("2: ")
    for item in lst:
        print("\t"+item)



def last_char(string):
    return string[-1].lower()


sort1(languages)
sort1b(languages)
sort3(languages)
