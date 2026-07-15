class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        digits[len(digits) - 1] += 1
        if digits[len(digits) - 1] > 9:
            carry = digits[len(digits) - 1] // 10
            digits[len(digits) - 1] = int(digits[len(digits) - 1] % 10)
        if carry > 0:
            for i in range(len(digits) - 2, -1, -1):
                digits[i] = digits[i] + carry
                if digits[i] > 9:
                    carry = digits[i] // 10
                    digits[i] = int(digits[i] % 10)
                else:
                    carry = 0
        if carry > 0:
            digits.insert(0, carry)
        return digits