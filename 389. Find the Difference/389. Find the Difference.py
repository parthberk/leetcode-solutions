"""
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
"""
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hmap_s = collections.Counter(s)
        hmap_t = collections.Counter(t)
        for k,v in hmap_t.items():
            if not k in hmap_s:
                return k
            elif k in hmap_s and hmap_s[k] < hmap_t[k]:
                return k