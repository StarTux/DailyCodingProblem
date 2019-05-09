#!/usr/bin/python3

# Problem #11 [Medium]

# Implement an autocomplete system. That is, given a query string
# s and a set of all possible query strings, return all strings in
# the set that have s as a prefix.
#
# For example, given the query string de and the set of strings
# [dog, deer, deal], return [deer, deal].
#
# Hint: Try preprocessing the dictionary into a more efficient
# data structure to speed up queries.

queries = ["dog", "deer", "deal"]
dictionary = {}
for q in queries:
    for i in range(1, len(q)):
        key = q[:i]
        ls = dictionary.get(key)
        if ls is None:
            ls = set()
            dictionary[key] = ls
        ls.add(q)
for key, value in dictionary.items():
    print(f"{key} => {value}")
print("")

def autoComplete(s):
    return list(dictionary[s])

def test(s):
    print(f"{s} => {autoComplete(s)}");

test("d")
test("de")
test("dee")
test("dea")
test("do")
