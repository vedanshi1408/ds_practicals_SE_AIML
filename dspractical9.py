# Naive String Matching Algorithm

text = input("Enter Text: ")
pattern = input("Enter Pattern: ")

n = len(text)
m = len(pattern)

found = False

print("\nPattern found at index:")

for i in range(n - m + 1):
    if text[i:i + m] == pattern:
        print(i)
        found = True

if not found:
    print("Pattern not found")