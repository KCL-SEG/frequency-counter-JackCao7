"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    sortedItems = []

    for i in items:
        sortedItems.append(str(i))

    while sortedItems:
        key = sortedItems[0]
        value = 0
        while key in sortedItems:
            sortedItems.remove(key)
            value+=1
        frequencies[key] = value

    return frequencies
