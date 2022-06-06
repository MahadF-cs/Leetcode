class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1

        i = 0
        max_sub =  0
        for j in range(len(s)):
            unique = set(s[i: j])
            if len(unique) < len(s[i: j]):
                i = j -1
                pass
            else:
                if len(unique) > max_sub:
                    max_sub = len(unique)
            
        return max_sub

if __name__ == "__main__":
    test = Solution()
    print(test.lengthOfLongestSubstring(' '))
