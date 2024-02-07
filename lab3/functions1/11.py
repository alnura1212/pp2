def palindrome(s):
    k=0
    for x in range(0, len(s)):
        if s[x]!=s[len(s)-x-1]:
            print ("No")
            return
    print ("Yes")
    return

word=str(input())
palindrome(word)