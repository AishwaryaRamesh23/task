from collections import Counter

def is_palindrome(s):
    s = s.replace(" ", "").lower()                                     # to ensure the comparison is case-insensitive and space-insensitive
    return s == s[::-1]

def can_form_palindrome(s):
    s = s.replace(" ", "").lower()
    count = Counter(s)                                                 # count occurrences of elements in string
    odd_count = sum(1 for count in count.values() if count % 2 != 0)
    return odd_count <= 1

def check_palindromes(words):
    """Check if each word is a palindrome and if it can be rearranged to form a palindrome."""
    results = {}
    for word in words:
        results[word] = {
            "is_palindrome": is_palindrome(word),
            "can_form_palindrome": can_form_palindrome(word)
        }
    return results

input_words = ["madam", "admam", "mdama", "dmama"]                  # Input list of words

results = check_palindromes(input_words)                            # Check each word

for word, res in results.items():
    print(f'"{word}" is a palindrome: {res["is_palindrome"]}')
    print(f'"{word}" can be rearranged into a palindrome: {res["can_form_palindrome"]}')
