from flask import Flask, render_template, redirect, request
import random
import string
import json

app = Flask(__name__)
shortened_urls = {}

def generate_short_url(length=6):
    chars = string.ascii_letters + string.digits
    short_url = "".join(random.choice(chars) for _ in range(length))
    return short_url

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        long_url = request.form['long_url']
        short_url = generate_short_url()
        while short_url in shortened_urls:
            short_url = generate_short_url()
        
        shortened_urls[short_url] = long_url

        # Save the shortened_urls dictionary to a JSON file
        with open("myurls.json", "w") as file:
            json.dump(shortened_urls, file)  # Corrected this line

        return f"Shortened URL: {request.url_root}{short_url}"
    return render_template("index.html")


    # Pass the shortened_urls dictionary to the template context
    return render_template("index.html", shortened_urls=shortened_urls)

@app.route("/<short_url>")
def redirect_url(short_url):
    long_url = shortened_urls.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return "URL not found", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
