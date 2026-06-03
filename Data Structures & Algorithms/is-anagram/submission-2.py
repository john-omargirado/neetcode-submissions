class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = ''.join(sorted(s))
        str2 = ''.join(sorted(t))

        if str1 in str2 and len(str1) == len(str2):
            return True
        else:
            return False