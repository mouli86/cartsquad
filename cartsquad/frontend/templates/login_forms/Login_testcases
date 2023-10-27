import pytest

# Your function to check password length
def check_password_length(password):
    return len(password) >= 8

# Test case to check if the password has a minimum length of 8 characters
def test_password_length():
    assert check_password_length("short") == False
    assert check_password_length("eight888") == True
    assert check_password_length("password123") == True
    assert check_password_length("verylongpassword") == True

if __name__ == "__main__":
    pytest.main()
