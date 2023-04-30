from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
# library used to count time
import timeit

from langchain.callbacks import get_openai_callback # this lib is used to count tokens

llm = OpenAI(temperature=0.5)
# Here it is by default set to "AI"

from langchain.prompts.prompt import PromptTemplate

template=''' 
You are an interviewer. You are interviewing a candidate for a job. You and the candidate will be given a business case.
The goal of the interview is to solve the business case together with the candidate, but you will only be giving necessary hints to the candidate (according to the given case information), and you would not make anything up.

The given case is: "A major chemical manufacturer produces a chemical product used to preserve foods in containers. Despite an increase in market share, the manufacturer has experienced a decline in profits. The CEO of the company is worried about this trend and hires you to investigate."
Additional information is given here:
"
- The company experienced no significant increase in cost in the last couple of years related to any additional fixed or variable cost.
- On the revenue side, the company's output increased slightly, slightly higher than the industry average
- Competition has decreased. A number of players have exited the industry because they were losing money.
- The companies which left felt that the industry had gotten saturated.
- Sales for the industry overall have decreased in the last few years, indicating a general negative trend and less demand for the product.
- Substitute products are not really being used. This is because preservatives, in general, are being used less in foods, and many consumers now prefer fresh food as their top choice.
- The makers of food are experiencing decreased volume, as the entire industry has been slowing down.
- They are forced to lower their prices to survive, and in order to lower costs, they are also using their leverage to renegotiate price structures of raw materials.
- Costs have stayed the same.
"
Current converstaion:
{history}
Interviewee: {input}
AG Interviewer:
'''
ag_memory = ConversationBufferMemory(ai_prefix="AG Interviewer", human_prefix="Interviewee")


PROMPT = PromptTemplate(
    input_variables=["history", "input"], template=template
)
conversation = ConversationChain(
    prompt=PROMPT,
    llm=llm, 
    verbose=True, 
    memory=ag_memory,
)

duration = 0
start = timeit.default_timer()
timelimit = 600 # in seconds

user_input = "Hello! Let's get started"
with get_openai_callback() as cb: #cb as callback, this is used to count tokens
     
    while user_input != "quit" and duration < timelimit:
        # what's the difference between conversation.run() and converstaion.predict()?
        print(conversation.run(input=user_input))
        user_input = input("Enter your message: ")
        ag_memory.load_memory_variables({'history'})
        now = timeit.default_timer()
        duration = now - start
        print(duration)
    
    print(cb) # would return 'tokens used', 'successful requests' and 'total cost (in USD)'

if duration >= timelimit:
    print(f"you've exceeded time limit of {timelimit} seconds")

memory_data = ag_memory.load_memory_variables({})
conver_data = memory_data['history'].split('\n')

with open('data.txt', 'w', encoding='utf-8') as f:
    for i in conver_data:
        f.writelines(i+'\n')