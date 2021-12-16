from collections import Counter


class Solution:
    def __init__(self) -> None:
        s = "bcabc"
        self.removeDuplicateLetters(s)

    def removeDuplicateLetters(self, s):
        visited = set()
        letter_count = Counter(s)
        stack = []
        for letter in s:
            letter_count[letter] -= 1
            if letter in visited:
                continue
            while (stack and letter < stack[-1] and letter_count[stack[-1]] > 0):
                visited.remove(stack[-1])
                stack.pop()
            stack.append(letter)
            visited.add(letter)
        print("".join(stack))
        return "".join(stack)


Solution()
