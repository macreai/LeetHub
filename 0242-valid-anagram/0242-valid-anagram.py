class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        saved_char_s = {}
        saved_char_t = {}

        for char in s:
            saved_char_s[char] = saved_char_s.get(char, 0) + 1

        for char in t:
            saved_char_t[char] = saved_char_t.get(char, 0) + 1

        return saved_char_s == saved_char_t
        