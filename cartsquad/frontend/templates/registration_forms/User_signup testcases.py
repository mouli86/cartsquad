import pytest
from your_signup_module import signup_function  # Import your actual signup function

# Test case to check password length
def test_password_length():
    result = signup_function(username="user1", password="short", dob="2000-01-01", gender="Male")
    assert "Password must be at least 8 characters" in result

# Test case to check valid password
def test_valid_password():
    result = signup_function(username="user2", password="password123", dob="2000-01-01", gender="Female")
    assert "Success" in result

# Test case to check date of birth format
def test_date_of_birth_format():
    result = signup_function(username="user3", password="password123", dob="01-01-2000", gender="Other")
    assert "Invalid date of birth format" in result

# Test case to check gender selection
def test_gender_selection():
    result = signup_function(username="user4", password="password123", dob="2000-01-01", gender="")
    assert "Please select a gender" in result

# Test case to check empty fields
def test_empty_fields():
    result = signup_function(username="", password="", dob="", gender="")
    assert "All fields are required" in result

if __name__ == "__main__":
    pytest.main()
