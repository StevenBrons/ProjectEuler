digits = range(0,999)
def isPalindrome(p):
	if (len(p) > 1):
		return p[0] == p[len(p) - 1] and isPalindrome(p[1:len(p) - 2])
	return True
