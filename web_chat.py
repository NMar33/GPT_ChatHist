from flask import Flask, render_template, request, redirect, url_for, flash
import openai
import os
import json
import yaml

# CONFIGS
CONFIG_FILE = "config.yaml"

with open(CONFIG_FILE, "r") as f:
    configs = yaml.safe_load(f)

OPEN_API_KEY = configs["OPEN_API_KEY"]
SECRET_KEY = configs["SECRET_KEY"]
PATH_HIST_FOLDER = configs["PATH_HIST_FOLDER"]
MAX_TOKENS = configs["MAX_TOKENS"]
TEMPERATURE = configs["TEMPERATURE"]

app = Flask(__name__)
app.secret_key = SECRET_KEY

openai.api_key = OPEN_API_KEY

def send_request(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        # engine="davinci-codex",
        messages=messages,
        # prompt=prompt,              
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    message = response.choices[0].message['content']
    return message.strip()

def load_chat_history(chatname, path_hist=PATH_HIST_FOLDER):
    filename = f"{path_hist}/{chatname}.txt"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.loads(file.read())
    return []

def save_chat_history(chatname, messages, path_hist=PATH_HIST_FOLDER):
    filename = f"{path_hist}/{chatname}.txt"
    with open(filename, "w") as file:
        file.write(json.dumps(messages))

@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        chatname = request.form["chatname"]
        user_input = request.form["user_input"]

        messages = load_chat_history(chatname)
        messages.append({"role": "user", "content": user_input})
        response = send_request(messages)
        messages.append({"role": "assistant", "content": response})
        save_chat_history(chatname, messages)

        return render_template("chat.html", chatname=chatname, messages=messages, user_input="")

    return render_template("chat.html", chatname="", messages=[], user_input="")

if __name__ == "__main__":
    app.run(debug=True)
