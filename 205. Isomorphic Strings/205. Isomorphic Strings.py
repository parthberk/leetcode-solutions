"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hset = set()
        for i, j in zip(s, t):
            if not (i, j) in hset:
                hset.add((i, j))
        return len(hset) == len(set(s)) == len(set(t))