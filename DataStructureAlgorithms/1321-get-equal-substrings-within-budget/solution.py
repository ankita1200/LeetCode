class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = cost = total_cost = answer = 0
        curr = []

        for right in range(len(s)):
            cost = abs(ord(s[right]) - ord(t[right]))
            curr.append(cost)

            total_cost += cost

            while total_cost > maxCost:
                total_cost -= curr[left]
                left += 1

            answer = max(answer, right - left + 1)

        return answer
