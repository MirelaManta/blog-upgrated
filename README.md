# Blog Application Upgraded

This is a simple Flask application that serves as a blog. It allows users to view blog posts, read individual posts, and contact the author through a contact form.

## Prerequisites

Make sure you have the following dependencies installed:

- Python 3
- Flask
- requests
- dotenv

## Getting Started

1. Clone the repository or download the code files.

2. Install the required dependencies by running the following command:

   ```
   pip install -r <dependency>
   ```

3. Create a `.env` file in the root directory and set the following environment variables:

   ```
   MY_EMAIL=<your-email>
   MY_PASSWORD=<your-email-password>
   ```

   Replace `<your-email>` with your Gmail email address and password. These credentials will be used for sending contact form emails.

4. Run the Flask application by executing the following command:

   ```
   python main.py
   ```

   The application will start running on `http://localhost:5000`.

5. Open your web browser and navigate to `http://localhost:5000` to view the blog.

## File Structure

- `main.py`: This is the main Python script that defines the Flask application and its routes.

- `templates/`: This directory contains the HTML templates used by the application.

  - `index.html`: The home page that displays a list of blog posts.

  - `about.html`: The about page that provides information about the author.

  - `post.html`: The page that displays a full blog post.

  - `contact.html`: The contact page that allows users to send messages to the author.

- `static/`: This directory contains static files such as CSS stylesheets and images.

  - `assets/`: This directory contains images used in the application.

- `README.md`: This file provides information about the project.

## Skills and Technologies Used

- Flask: Python web framework used for building the application.
- HTML: Markup language for creating the structure of web pages.
- CSS: Styling language used to design the appearance of web pages.
- JavaScript: Programming language used to add interactivity to the application.
- Python: Programming language used for the backend development.
- Git: Version control system for tracking changes in the code.
- GitHub: Web-based platform for hosting and collaborating on Git repositories.
- SMTP: Protocol used for sending emails through the application.
- Gmail: Email service provider used for sending contact form emails.
