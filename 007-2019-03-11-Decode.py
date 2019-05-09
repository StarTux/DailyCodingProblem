#!/usr/bin/python3

# Problem #7 [Medium]
#
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded
# message, count the number of ways it can be decoded.
#
# For example, the message '111' would give 3, since it could be
# decoded as 'aaa', 'ka', and 'ak'.
#
# You can assume that the messages are decodable. For example,
# '001' is not allowed.

alphabet = "abcdefghijklmnopqrstuvwxyz"
code = {}
for i in range(26):
    code[str(i + 1)] = alphabet[i]

def ways(input):
    list = []
    options = []
    for _ in range(len(input)): list += [1]
    waysHelper(input, list, options)
    return options

def countWays(input):
    return len(ways(input))

def waysHelper(input, list, options):
    strindex = 0
    option = ""
    for strlen in list:
        snip = input[strindex:strindex + strlen]
        if snip not in code:
            return 0
        option += code[snip]
        strindex += strlen
    options += [option]
    result = 1
    for i in range(len(list) - 1):
        if list[i] == 1 and list[i + 1] == 1:
            result += waysHelper(input, list[0:i] + [2] + list[i + 2:], options)
    return result

def test(input):
    options = ways(input)
    print(input + ": " + str(len(options)) + ": " + str(options))

test("111")
test("222")
test("333")
test("1221")
