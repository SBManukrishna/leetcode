class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for c in range(len(haystack)-len(needle)+1):
            if(haystack[c:c+len(needle)]==needle):
                return c
        return -1