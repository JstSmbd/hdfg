from flask import Flask, render_template, url_for
import openai
from random import choice, randint


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html", word=choice(("счастья", "здоровья", "денег", "удачи", "спокойствия")), src=f"img/img_{randint(1, 10)}.png")


if __name__ == '__main__':
    app.run()