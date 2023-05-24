from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts.prompt import PromptTemplate
import timeit # lib used to count time
from langchain.callbacks import get_openai_callback # lib used to count tokens


def config(llm = ChatOpenAI(model_name="gpt-3.5-turbo-0301",temperature=0.4), verbose_opt=False, template="Hello! No template is set:{history}{input}"):
    '''configures the AI model, conversation chain, memory and prompt'''
    # llm = OpenAI(temperature=0.5)
    
    ag_memory = ConversationBufferMemory(ai_prefix="AG Interviewer", human_prefix="Interviewee")
    # Here it is by default set to "AI"

    PROMPT = PromptTemplate(
        input_variables=["history", "input"], template=template
    )

    conversation = ConversationChain(
        prompt=PROMPT,
        llm=llm, 
        verbose=verbose_opt, 
        memory=ag_memory,
    )
    
    return conversation, ag_memory

def timed_conversation(conversation, ag_memory, timelimit, verbose_cb):
    '''timelimit = 600 in seconds
    if timelimit = 0 then won't count time
    problem: OpenAI's response takes time, so participants would have less time to respond. '''
    duration = 0
    start = timeit.default_timer()

    user_input = "Hello! Let's get started"
    with get_openai_callback() as cb: #cb as callback, this is used to count tokens
        callback = cb
        while user_input != "quit" and duration < timelimit:
            # what's the difference between conversation.run() and converstaion.predict()?
            print(conversation.run(input=user_input))
            user_input = input("\nEnter your message: ")
            ag_memory.load_memory_variables({'history'})
            now = timeit.default_timer()
            duration = now - start
            if timelimit != 0:
                print(f"\nTime used: {duration/60:.2f} min, {(timelimit/60 - duration/60):.2f} min left") # prints the current duration
            
            if duration >= timelimit and timelimit != 0:
                '''checks the timeout condition and the timeit condition'''
                print(f"\nYou've exceeded time limit of {timelimit/60} min.")
                break
        if verbose_cb == True:
            print("\n"+str(callback)) # would return 'tokens used', 'successful requests' and 'total cost (in USD)'
        else:
            pass


    memory_data = ag_memory.load_memory_variables({})
    conver_data = memory_data['history'].split('\n')
    return conver_data, callback

def save_conversation(conver_data, callback):
    '''saves the conversation and the OpenAI callback into a txt file for inspection'''
    with open('data.txt', 'w', encoding='utf-8') as f:
        for i in conver_data:
            f.writelines(i+'\n')
        f.writelines('\n')
        f.writelines('----OpenAI Callbacks----\n')
        f.writelines(str(callback))
            
def main():
    interviewer_template = ''' 
    You are an interviewer. You are interviewing a candidate for a job. You and the candidate will be given a business case.
    The goal of the interview is to solve the business case together with the candidate, but you will not give relevent information unless the candidate asks about it, and you would not make anything up.

    The information for the candidate is: "You are the Dean of a large public university in the Midwest.
    Your tenure has focused on raising the profile of the university through various initiatives. Recently, the Board of Regents has requested a plan that outlines the university’s environmental footprint and a goal to reach net-zero waste by 2040. As a former business executive, you are familiar with the principles of ESG, but need to understand what the major drivers of environmental impact at PubU are."
    Additional information is given here:
    "
    - PubU is a large research institution consisting of an undergrad (35k students), graduate school (10k) and various professional schools (~2k). Number in student body is expected to be stable. The university is very large and requires an extensive diesel-powered bus system for students to commute all over campus.
    - The average operating budget of PubU is $2B. Of that $2B, roughly 30% comes from the state, 10% from alumni donations, 20% from the university endowment (fund that pays out money each year) and 40% from student fees. 
    - PubU currently gets electricity from the local grid (which uses a mix of coal, gas, wind, and solar). The local utility is transitioning to 100% carbon-free by 2030. 
    - Net-zero waste means consuming only as much energy as produced, achieving a sustainable balance between water availability and demand, and eliminating solid waste sent to landfills.
    - PubU’s goali is to reach net-zero by 2040
    - 1 bus per route, 2 miles per gallon, each route runs on average, four times an hour, for 15 hours a day, seven days a week, 50 weeks a year.
    - $6 / gallon of diesel. Other maintenance costs include $20,000 per bus in annual maintenance
    - 20 lbs CO2 / gallon of diesel
    - Total Annual Cost of Diesel: Round 104 miles to 100 miles
    - Cost per bus: $1M 
    - Annual Maintenance Cost: $4,000 / bus
    - Bus Efficiency: 4 miles / gallon of diesel equivalent (gallon of diesel equivalent is a measure of energy)
    - Electric to Diesel Conversion: 25 gallon of diesel equivalent / megawatt-hour (MW-h) 
    - Grid Stats: $100 / MW-h generated, 1000 lbs CO2 / MW-h generated (currently, future is 0)-
    "
    Current converstaion:
    {history}
    Interviewee: {input}
    AG Interviewer:
    '''
    
    conversation, ag_memory = config(llm = OpenAI(temperature=0.5), verbose_opt=False, template=interviewer_template)
    conver_data, callback = timed_conversation(conversation,ag_memory, timelimit=600, verbose_cb=True)
    save_conversation(conver_data, callback)

if __name__ == '__main__':
    main()