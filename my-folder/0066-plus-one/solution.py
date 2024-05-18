class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        # move along the input array starting from the end
        for i in range(n):
            idx = n - 1 - i

            # Set all the nines at the end of the array to zeros
            if digits[idx] == 9:
                digits[idx] = 0

            # Here we have the rightmost not-nine
            else:
                # Increase this rightmost not-nine by 1
                digits[idx] += 1

                # and the job is done
                return digits

        # We're here because all the digits are nines
        return [1] + digits
