def ismomorphic_string_check(String1, String2):
    return len(set(zip(String1, String2))) == len(set(String1)) == len(set(String2))

# Example usage
if __name__ == "__main__":
    String1 = "egg"
    String2 = "add"
    print(ismomorphic_string_check(String1, String2))  # Output: True

    String1 = "foo"
    String2 = "bar"
    print(ismomorphic_string_check(String1, String2))  # Output: False

    String1 = "paper"
    String2 = "title"
    print(ismomorphic_string_check(String1, String2))  # Output: True