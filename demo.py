from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
# library used to count time
import timeit

llm = OpenAI(temperature=0.5)
# Here it is by default set to "AI"

from langchain.prompts.prompt import PromptTemplate

template=''' 
You are an interviewer. You are interviewing a candidate for a job. You and the candidate will be given a business case.
The goal of the interview is to solve the business case together with the candidate, but you will only be giving necessary hints to the candidate (according to the given case information), and you would not make anything up.
If you understand your role, please say "AG".
The given case is: "A company is looking to expand its business. What should it do?"
Current converstaion:
{history}
Interviewee: {input}
AG Interviewer:
'''
case_1 = "A company is looking to expand its business. What should it do?"
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
timelimit = 60 # in seconds

user_input = "Hello! Let's get started"
while user_input != "quit" and duration < timelimit:
    # what's the difference between conversation.run() and converstaion.predict()?
    print(conversation.run(input=user_input))
    user_input = input("Enter your message: ")
    ag_memory.load_memory_variables({'history'})
    now = timeit.default_timer()
    duration = now - start
    print(duration)

if duration >= timelimit:
    print(f"you've exceeded time limit of {timelimit} seconds")

memory_data = ag_memory.load_memory_variables({})
conver_data = memory_data['history'].split('\n')

with open('data.txt', 'w', encoding='utf-8') as f:
    for i in conver_data:
        f.writelines(i+'\n')

