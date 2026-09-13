class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = {}
        left = 0 
        max_len = 0

        for right in range(len(s)):
            char = s[right]

            if char in longest:
                left = max(left, longest[char] + 1)

            longest[char] = right

            max_len = max(max_len, right - left + 1)

        return max_len 