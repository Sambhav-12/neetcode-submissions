class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}
        left = 0
        have = 0
        min_length = float("inf")
        result = ""
        for n in t:
            if n in need:
                need[n] += 1
            else:
                need[n] = 1

        for right in range(len(s)):
            if s[right] in window:
                window[s[right]] += 1
            else:
                window[s[right]] = 1

            
            if s[right] in need:
                if window[s[right]] == need[s[right]]:
                    have += 1

            while have == len(need):
                current_length = right - left + 1
                if current_length < min_length:
                    min_length = current_length
                    result = s[left: right+1]

                if s[left] in need:
                    if window[s[left]] == need[s[left]]:
                        have -= 1
                
                window[s[left]] -= 1
                left += 1
            
        return result