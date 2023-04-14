#!/usr/bin/python3
""" higest_value_Palindrome file """


def higest_value_palindrome(s, n, k):
    """
    This function create the largest palindromic string of digits possible
    or the string '-1' if it is not possible to create a palindrome
    under the contstraints.

    Args:
        s (str): string representation of an integer
        n (int): length of s
        k (int): maximum number of changes allowed

    Returns:
        result (str): string representation of the highest
        value achievable or -1
    """

    # checking if s is a string
    if type(s) != str:
        print("s must be  an integer")
        return "-1"

    # checking if s is a representation of a number
    for char in s:
        if ord(char) not in range(48, 58):
            print("The string must be the representation of a number")
            return "-1"

    # cheching if the lenght of the string and the number
    # of changes allowed are integers
    if type(n) != int or type(k) != int:
        print("n and k must be integers")
        return "-1"

    # if the number of changes are equal or greater than strin´s lenght,
    # chage all characters to 9
    if k >= n:
        for char in s:
            s = s.replace(char, "9")
        return s

    s = list(s)

    # number of palindrome positions in the string
    matches = 0
    for i in range(n):
        if s[i] == s[n - 1 - i]:
            matches += 1

    # minumun mumber of changes that allow create the largest
    # palindromic possible
    min_even = (n / 2) - (matches / 2)
    min_odd = (n - matches) / 2

    # if the lenght of the string is even
    if n % 2 == 0:
        if k < min_even:
            return "-1"
        else:
            changes = 0
            for i in range(n // 2):
                if s[i] != s[n - 1 - i]:
                    # If the characters at the two ends are not equal, replace
                    # the smaller one with the larger one
                    higest = max(s[i], s[n - 1 - i])
                    s[i] = higest
                    s[n - 1 - i] = higest
                    changes += 1
            if changes < k:
                j = 0
                while j < n // 2 and changes < k:
                    # If the character is already '9', no need to make a change
                    if s[j] == '9':
                        j += 1
                        continue
                    else:
                        # checking if it's possible to change two end's values
                        if changes + 2 <= k:
                            s[j] = '9'
                            s[n - 1 - j] = '9'
                            changes += 2
                    j += 1

    # if the lenght of the string is odd
    else:
        if k < min_odd:
            print("-1")
        else:
            changes = 0
            for i in range(n // 2):
                if s[i] != s[n - 1 - i]:
                    # If the characters at the two ends are not equal, replace
                    # the smaller one with the larger one
                    higest = max(s[i], s[n - 1 - i])
                    s[i] = higest
                    s[n - 1 - i] = higest
                    changes += 1
            if changes < k:
                j = 0
                while j < n // 2 and changes < k:
                    # If the character is already '9', no need to make a change
                    if s[j] == '9':
                        j += 1
                        continue
                    else:
                        # checking if it's possible to change two end's values
                        if changes + 2 <= k:
                            s[j] = '9'
                            s[n - 1 - j] = '9'
                            changes += 2
                        else:
                            s[n // 2] = '9'
                    j += 1

    return ''.join(s)
