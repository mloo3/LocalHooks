def is_subsequence(s,t):
	if len(s) == 0:
		return True
	if len(t) == 0 or len(s) > len(t):
		return False
	current = 0
	for i,letter in enumerate(s):
		while current < len(t):
			if letter is t[current]:
				if i == len(s) - 1:
					return True
				current += 1
				break
			if letter is not t[current]:
				current += 1
	return False