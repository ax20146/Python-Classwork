# FizzBuzz


for i in range(1, 101):
    result = ""

    if i % 3 == 0:
        result += "Fizz"

    if i % 5 == 0:
        result += "Buzz"

    print(result if result else i)


# Palindrome
def palindrome(word: str):
    return word == word[::-1]


print(palindrome("word"))
print(palindrome("level"))


# Sum of Digits
def sum_of_digits(n: int):
    return sum(int(digit) for digit in str(n))


print(sum_of_digits(199))
print(sum_of_digits(100))


# Count Vowel
def count_vowel(string: str):
    result = 0
    for letter in string.lower():
        if letter in {"a", "e", "i", "o", "u"}:
            result += 1

    return result


print(count_vowel("word"))
print(count_vowel("aeiou"))


# Reverse string
def reverse_string(string: str):
    return string[::-1]


print(reverse_string("word"))
print(reverse_string("string"))


# Anagram Checker
def anagram(str1: str, str2: str):
    return sorted(str1) == sorted(str2)


print("Anagram:", anagram("listen", "silent"))


# Unique Characters
def unique_string(string: str):
    seen: set[str] = set()

    for i in string:
        if i in seen:
            return False
        else:
            seen.add(i)

    return True


print(unique_string("Level"))
print(unique_string("word"))


# Two Sum
def two_sum(arr: list[int], target: int):
    for i in range(len(arr)):
        for j, n in enumerate(arr[i + 1 :], 1):
            if arr[i] + n == target:
                return i, j


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([5, 10, 10, 5], 10))


# String comp
def string_comp(string: str):
    current = ""
    count = 1

    result = ""
    for l in string:
        if not current:
            current = l

        elif l == current:
            count += 1
        else:
            result += f"{current}{count}"
            current = l
            count = 1
    result += f"{current}{count}"

    return result


print(string_comp("aaabbbccc"))
print(string_comp("aaaaa"))
