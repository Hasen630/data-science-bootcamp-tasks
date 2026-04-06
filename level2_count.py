def count_vowels(text):
    """Count the number of vowels in a string."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


# Example usage
text = input("\nEnter a string: ")
print("Number of vowels:", count_vowels(text))