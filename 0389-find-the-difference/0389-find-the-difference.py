class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        saved_char = {}

        for char in t:
            saved_char[char] = saved_char.get(char, 0) + 1
        for char in s:
            saved_char[char] -= 1

        for char in saved_char:
            if saved_char[char] == 1:
                return char
        