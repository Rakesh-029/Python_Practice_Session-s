n = "bob"
i = 0
j = len(n) - 1
is_palindrome = True 

while (i < j):
    if n[i] == n[j]:
        i += 1
        j -= 1
    else:
        is_palindrome = False
        break

print("palindrome" if is_palindrome else "not palindrome")