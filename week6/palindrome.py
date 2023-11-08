def isPalindrome(s):
	return s == s[::-1]

# Driver code
s = "kayak"
ans = isPalindrome(s)

if ans:
	print("Yes, kayak is a palindrome")

else:
	print("No")
