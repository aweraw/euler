combos n r
	| n == 0 = 0
	| r == 1 = n
	| n == r = 1
	| otherwise = (combos (n-1) r) + (combos (n-1) (r-1))