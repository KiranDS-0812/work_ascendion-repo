{
  "test_cases": [
    {
      "test_case_id": 1,
      "description": "Valid login with correct username and password",
      "input": {
        "username": "validUser",
        "password": "validPass123"
      },
      "expected_result": "Access granted, user redirected to dashboard"
    },
    {
      "test_case_id": 2,
      "description": "Invalid login with incorrect username",
      "input": {
        "username": "invalidUser",
        "password": "validPass123"
      },
      "expected_result": "Access denied, error message displayed"
    },
    {
      "test_case_id": 3,
      "description": "Invalid login with incorrect password",
      "input": {
        "username": "validUser",
        "password": "wrongPass"
      },
      "expected_result": "Access denied, error message displayed"
    },
    {
      "test_case_id": 4,
      "description": "Invalid login with empty username and password",
      "input": {
        "username": "",
        "password": ""
      },
      "expected_result": "Access denied, error message displayed"
    },
    {
      "test_case_id": 5,
      "description": "Invalid login with special characters in username and password",
      "input": {
        "username": "!@#$%^",
        "password": "*&^%$#"
      },
      "expected_result": "Access denied, error message displayed"
    },
    {
      "test_case_id": 6,
      "description": "Confirm access to login page",
      "input": {},
      "expected_result": "Login page is accessible and loads successfully"
    }
  ]
}