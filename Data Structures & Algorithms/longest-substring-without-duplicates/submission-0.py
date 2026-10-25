class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = [0] * 128
        max_len = 0
        curr_len = 0

        for i in range(len(s)):
            counter[ord(s[i])] += 1

            while(counter[ord(s[i])] > 1):
                counter[ord(s[i-curr_len])] -= 1
                curr_len -= 1
            
            curr_len += 1
            max_len = max(curr_len, max_len)

        return max_len


