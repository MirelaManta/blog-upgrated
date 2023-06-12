# Blogging Web Application

This is a blogging web application developed using Flask, a Python web framework. It showcases various skills and technologies, including:

- Flask framework for building web applications.
- Flask-Bootstrap for responsive and user-friendly frontend design.
- Flask-WTF for handling forms and form validation.
- Flask-CKEditor for integrating a rich text editor in the application.
- Flask-SQLAlchemy for working with the SQLite database.
- Flask-Login for user authentication and session management.
- Flask-Gravatar for displaying user avatars based on email addresses.
- Python's Werkzeug library for password hashing and verification.
- SQLite database for data storage and retrieval.
- HTML templates for rendering dynamic web pages.
- CSS for styling and layout.
- JavaScript for client-side interactions.

## Features

- User registration and authentication system.
- User-friendly forms for creating and editing blog posts.
- Rich text editor for writing blog content using CKEditor.
- Commenting system for users to engage in discussions.
- Access control with admin-only features.
- Responsive design using Bootstrap framework.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/MirelaManta/blog-upgrated.git
   cd blog-upgrated
   ```

2. Create a virtual environment (optional but recommended):

   ```shell
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. Set up environment variables:

   - Create a `.env` file in the project root directory.
   - Add the following variables to the `.env` file:
     - `SECRET_KEY`: Secret key for the Flask application.
     - Any other configuration variables required.

5. Run the application:

   ```shell
   python app.py
   ```

6. Open your web browser and visit `http://localhost:5000` to see the application in action.

## Usage

- Register a new account or log in with an existing account to start using the application.
- Only the admin user (user with ID 1) can create new blog posts.
- Other users can view all existing posts on the homepage.
- Click on a post to view its full content and comments.
- Leave comments on posts when logged in.
- Edit or delete posts (admin-only functionality).
- Log out when done using the application.

## File Structure

- `app.py`: Main Flask application file containing route definitions, application setup and database models using SQLAlchemy ORM.
- `forms.py`: Contains FlaskForm classes for various forms used in the application.
- `templates/`: Directory containing HTML templates for different views.
- `static/`: Directory containing static assets such as CSS, JavaScript, and images.
- `instance/blog.db`: SQLite database file (automatically created on first run).

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

