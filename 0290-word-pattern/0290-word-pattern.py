class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        my_dict = {}
        for i in range(len(pattern)):
            if pattern[i] not in my_dict:
                if words[i] not in my_dict.values():
                    my_dict[pattern[i]] = words[i]
            word = my_dict.get(pattern[i])
            if word != words[i]:
                return False 
        return True
