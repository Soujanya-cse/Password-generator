from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Character sets
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'

@app.route("/", methods=["GET", "POST"])
def home():
    password = ""
    if request.method == "POST":
        nr_letters = int(request.form.get("letters", 0))
        nr_symbols = int(request.form.get("symbols", 0))
        nr_numbers = int(request.form.get("numbers", 0))

        password_list = []
        for _ in range(nr_letters):
            password_list.append(random.choice(letters))
        for _ in range(nr_symbols):
            password_list.append(random.choice(symbols))
        for _ in range(nr_numbers):
            password_list.append(random.choice(numbers))

        random.shuffle(password_list)
        password = ''.join(password_list)

    return render_template("index.html", password=password)


if __name__ == "__main__":
    app.run(debug=True)
