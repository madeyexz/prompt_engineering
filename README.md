# About This Project
This project
- uses `langchain` and `timeit` to generate a chatbot that behaves like a *case interviewer*.
- is currently a proof of concept, demo product.

# Prerequisites
1. Clone this project to your working directory, if you don't know what I'm talking about, then enter`cd ~/Desktop` in your terminal, then
   ``` bash
   git clone https://github.com/madeyexz/prompt_engineering.git
   ```
   the project will be cloned to your Desktop.
2. Acquire an OpenAI API key and export it to system environment.
   - OpenAI API key can be obtained from [here](https://platform.openai.com/account/api-keys).
   - export the API key to system environment using
    ``` bash
    export OPENAI_API_KEY="your_openai_api_key"
    ```
   now in Python use
   ``` python
   import os
   os.environ["OPENAI_API_KEY"]
   ```
   to check if you have them exported to system environment, if `KeyError`, then restart the terminal upon completion (and your IDE if you are using one).
3. Install the dependencies
   ``` bash
   pip3 install langchain timeit
   ```

# Usage

``` bash
python3 demo.py
```

to quit the demo, enter `quit` in the chatbox

# Feature Request
- Add voice input (can integrate `Whisper`)
- Language support: Chinese