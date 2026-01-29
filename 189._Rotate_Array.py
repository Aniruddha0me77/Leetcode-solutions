def rotate(nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) != 1:
            if k != 0:
                new = nums[-k:]
                nums = [*new, *nums]
                del nums[-k:]