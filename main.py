#!/usr/bin/python3
"""
main
"""
higest_value_palindrome = __import__(
    'higest_value_palindrome').higest_value_palindrome


def print_strings():
    """
    Print the result of testing some numbers
    """

    # First examples
    s = "12546"
    print(higest_value_palindrome(s, len(s), 4))
    print(higest_value_palindrome(s, len(s), 1))
    print(higest_value_palindrome(s, len(s), 7))

    print("-" * 5)

    # Success cases
    s2 = "092282"
    print(higest_value_palindrome(s2, len(s2), 4))
    print(higest_value_palindrome(s2, len(s2), 5))
    print(higest_value_palindrome(s2, len(s2), 20))

    print("-" * 5)

    # Error cases
    s3 = "12a3"
    print(higest_value_palindrome(s3, len(s3), 1))
    s3 = "1233"
    print(higest_value_palindrome(s3, "a", 1))
    s3 = "1233"
    print(higest_value_palindrome(s3, len(s3), "a"))


if __name__ == "__main__":
    print_strings()
