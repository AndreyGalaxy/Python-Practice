def reverse(word):
    word = ''.join(char.lower() for char in word if char.isalnum())
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True

word = input("Type in a word or phrase: ")
if reverse(word):
    print("Your word is a palindrome.")
else:
    print("Your word is not a palindrome.")