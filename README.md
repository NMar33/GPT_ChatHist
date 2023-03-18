# GPT_ChatHist 

Hello :smiley:, thank you for being here! GPT_ChatHist is a small app that allows you to interact with OpenAI's GPT-3.5-turbo through a local web interface. The app saves dialogue history, enabling you to resume conversations effortlessly. If you prefer a version without a web interface, check out [GPT_ChatHist_no_web](https://github.com/NMar33/GPT_ChatHist_no_web).

## Why it can be useful

1. Easily resume your dialogue with ChatGPT.
2. Access dialogue history to analyze, review, or utilize past conversations for various purposes.
3. OpenAI does not use data submitted by customers via the API to train or improve models unless you explicitly opt-in to share your data. [OpenAI's API Data Usage Policies](https://openai.com/policies/api-data-usage-policies).


## Installation

1. Clone the repository or download the source code.
2. Create a virtual environment
```
python -m venv .venv
```
3. Activate the virtual environment:

- Windows:
  ```
  .venv\Scripts\activate.bat
  ```

- Linux/Mac:
  ```
  source .venv/bin/activate
  ```

4. Install the required packages:
```
pip install -r requirements.txt
```
5. Change `OPEN_API_KEY` in `config.yaml` to your OpenAI API Key
If you do not have an Open AI API key, please follow the [Open AI blogpost](https://openai.com/blog/openai-api/).


## How to use

1. Activate the virtual environment (if not already active).
2. Run the app:
```
python web_chat.py
```
3. Open a web browser and navigate to http://127.0.0.1:5000/ to access the app interface. Enter your preferred chat name and start interacting with the AI.

## Warnings

Every message you send will contain all previous chat history.

1. Keep in mind that the model has a token limit (e.g., 4096 tokens for GPT-3). If your conversation exceeds this limit, you will need to truncate or remove some messages from the list to fit within the allowed token count.
2. If your conversation is very large, it can consume a significant portion of your token limit.