# Django Blog - User Authentication System

This section explains how the **user authentication system** works in our Django Blog project, including **registration, login, logout, and profile management**.

---

## Authentication Data Flow




## User types data
 ##   ↓
## HTML form
 ##   ↓
## request.POST
 ##   ↓
## RegisterForm
 ##   ↓
## User model
 ##   ↓
## Database





### Step-by-Step Explanation

1. **User types data**  
   - The user fills in the registration or login form in the browser.

2. **HTML form**  
   - The form is created in the template (`register.html`, `login.html`)  
   - Django automatically generates input fields using `{{ form.as_p }}`  
   - CSRF token is included (`{% csrf_token %}`) to prevent security attacks

3. **request.POST**  
   - When the user submits the form, the browser sends a POST request  
   - This request contains all user inputs

4. **RegisterForm**  
   - A Django form object that validates the input  
   - Checks password match, strength, and email format  
   - Ensures the username is unique  
   - Handles errors if any validation fails

5. **User model**  
   - After validation, the data is saved to the built-in Django `User` model  
   - Passwords are automatically hashed for security

6. **Database**  
   - The `User` model stores the user data in the database (SQLite or PostgreSQL)  
   - The user can now log in and access protected pages like `/profile`

---

## Features Implemented

- **User Registration** (`/register`)  
  - Collects username, email, password1, password2  
  - Validates all input  
  - Logs in the user immediately after registration

- **User Login** (`/login`)  
  - Authenticates users with username and password  
  - Redirects logged-in users to `/profile`

- **User Logout** (`/logout`)  
  - Ends the session  
  - Redirects to login page or home

- **Profile Management** (`/profile`)  
  - Allows logged-in users to view and update their email  
  - Username is displayed but cannot be changed  

---

## Security Measures

- **CSRF Protection**: All forms include `{% csrf_token %}`  
- **Password Hashing**: Django handles secure password storage automatically  
- **Login Required**: Profile page is accessible only to logged-in users (`@login_required`)  

---

## How to Test

1. Run the server:
```bash
python manage.py runserver
