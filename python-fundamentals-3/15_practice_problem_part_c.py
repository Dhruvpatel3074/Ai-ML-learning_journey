# Practice problem (Part c)

text = "hello world"
vowels = "aeiou"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Vowel count:", count)
