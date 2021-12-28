class Solution(object):
    def letterCombinations(self, digits):
        dic_digit = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '}
        all_combinations = [''] if digits != "" else []
        for digit in digits:
            curr_combinations = list()
            for letter in dic_digit[digit]:
                for x in all_combinations:
                    curr_combinations.append(x+letter)
            all_combinations = curr_combinations
        return all_combinations
