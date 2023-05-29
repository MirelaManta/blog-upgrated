from flask import Flask, render_template, request
from dotenv import load_dotenv
import requests
import smtplib
import os

app = Flask(__name__)

load_dotenv()

POSTS_API_ENDPOINT = "https://api.npoint.io/5808b1a3304a496f4c65"
posts_response = requests.get(POSTS_API_ENDPOINT)
all_posts = posts_response.json()

my_email = os.environ["MY_EMAIL"]
password = os.environ["MY_PASSWORD"]


@app.route("/")
def home():
    return render_template("index.html", posts=all_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post/<int:index>")
def show_full_post(index):
    requested_post = None
    for post in all_posts:
        if post["id"] == index:
            requested_post = post
    return render_template("post.html", post=requested_post)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone_num = request.form["phone"]
        message = request.form["message"]
        send_email(name, email, phone_num, message)
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        )


if __name__ == "__main__":
    app.run(debug=True)

