# Security Policy

## Day 3 Security Improvements

### 1. Input Validation
- Checks if input is empty or invalid
- Limits input length to prevent abuse

### 2. Prompt Injection Protection
- Blocks malicious prompts like:
  - "ignore previous instructions"
  - "act as admin"
  - "bypass security"

### 3. Sanitization
- Cleans user input before sending to AI

### 4. Error Handling
- Prevents system crash during API failure
- Provides fallback response

## Notes
- API keys are stored securely using .env
- .env file is excluded from GitHub using .gitignore

## Day 9 Security Testing

### Tests Performed

* SQL Injection (`' OR 1=1 --`)
* HTML Injection (`<script>alert('hack')</script>`)
* Prompt Injection ("Ignore all instructions")

### Results

* Application did not crash
* Inputs handled as normal text
* No sensitive/system data exposed

### Status

Security verified successfully
