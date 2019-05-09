#!/usr/bin/python3

# Problem #13 [Hard]
#
# Given an integer k and a string s, find the length of the
# longest substring that contains at most k distinct characters.
#
# For example, given s = "abcba" and k = 2, the longest substring
# with k distinct characters is "bcb".

# Return True if string s has exactly k distinct characters, False
# otherwise.
def hasChars(k, s):
    done = set()
    total = 0
    for c in s:
        if c in done: continue
        done.add(c)
        total += 1
        if total > k: return False
    return total == k

# Brute force solution.
def solution1(k, s):
    if (len(s) < k): return ""
    result = s[0:k]
    longest = k
    size = len(s)
    for begin in range(size - k):
        if longest > size - begin: break
        for length in range(longest, size - begin):
            if (length <= longest): continue
            sub = s[begin:begin + length]
            if hasChars(k, sub):
                longest = length
                result = sub
    return result

def test(k, s):
    sol = solution1(k, s)
    print(f"{k}, {s} => {len(sol)}, \"{sol}\"")

test(2, "abcba")
test(3, "abcba")
test(10, "fjweiorukuwerwerwerwerwerelhjrkowuerhfksljflaewriujasdvnmweufh")
