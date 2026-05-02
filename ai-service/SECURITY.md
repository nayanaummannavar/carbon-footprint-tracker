# SECURITY.md

## 1. API Key Exposure
Risk: API key can be leaked if .env is uploaded  
Fix: .env added to .gitignore

## 2. Prompt Injection
Risk: User can manipulate AI prompts  
Fix: Input validation and sanitisation

## 3. Rate Limiting
Risk: Too many API requests  
Fix: flask-limiter (30 requests/min)

## 4. Invalid Input
Risk: Empty or harmful input  
Fix: Input validation before processing

## 5. AI Failure Handling
Risk: Groq API failure  
Fix: Retry logic + fallback response    