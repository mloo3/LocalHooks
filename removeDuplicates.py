def remove_duplicated(nums):
	current = 1
	while current < len(nums):
		if nums[current - 1] == nums[current]:
			del nums[current-1]
		else:
			current += 1
	return len(nums)

nums = [1,1,2]
print(remove_duplicated(nums), nums)