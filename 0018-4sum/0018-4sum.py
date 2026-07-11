class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:

        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 3):

            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Pruning: smallest possible sum is greater than target
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break

            # Pruning: largest possible sum is smaller than target
            if nums[i] + nums[-1] + nums[-2] + nums[-3] < target:
                continue

            for j in range(i + 1, n - 2):

                # Skip duplicate second numbers
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:

                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append(
                            [nums[i], nums[j], nums[left], nums[right]]
                        )

                        # Skip duplicate third numbers
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1

                        # Skip duplicate fourth numbers
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1

                    elif total < target:
                        left += 1

                    else:
                        right -= 1

        return result