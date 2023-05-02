# Prerequisites
1. You have to acquire OpenAI API key and export it to system environment.
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
2. Install the dependencies
   ``` bash
   pip3 install langchain timeit
   ```

# Usage

``` bash
python3 demo.py
```

to quit the demo, enter `quit` in the chatbox
