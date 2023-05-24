# import the case_database, ingest them into case_info and addition_info
# generate the prompt for the conversation and store them in a database

# This file is used to generate the prompt for the conversation
def prompt_generation(case_info, addition_info):
    '''spawn the prompt used in the conversation using the given case_info and addition_info'''
    role_defining = "You are an interviewer.\
        You are interviewing a candidate for a job. You and the candidate will be given a business case. The goal of the interview is to solve the business case together with the candidate, but you will only be giving necessary hints to the candidate (according to the given case information), and you would not make anything up.\
        The given case is:"
        
    # case_info = "A major chemical manufacturer produces a chemical product used to preserve foods in containers. Despite an increase in market share, the manufacturer has experienced a decline in profits. The CEO of the company is worried about this trend and hires you to investigate."
    # addition_info = '''- The company experienced no significant increase in cost in the last couple of years related to any additional fixed or variable cost.
    #     - On the revenue side, the company's output increased slightly, slightly higher than the industry average
    #     - Competition has decreased. A number of players have exited the industry because they were losing money.
    #     - The companies which left felt that the industry had gotten saturated.
    #     - Sales for the industry overall have decreased in the last few years, indicating a general negative trend and less demand for the product.
    #     - Substitute products are not really being used. This is because preservatives, in general, are being used less in foods, and many consumers now prefer fresh food as their top choice.
    #     - The makers of food are experiencing decreased volume, as the entire industry has been slowing down.
    #     - They are forced to lower their prices to survive, and in order to lower costs, they are also using their leverage to renegotiate price structures of raw materials.
    #     - Costs have stayed the same.'''
        
    formatiing = '''
        Current converstaion:
        {history}
        Interviewee: {input}
        AG Interviewer:
        '''
    prompt = role_defining + case_info + "\n additional information is given here" + addition_info + formatiing
    return prompt
def prompt_database_storage(prompt):
    '''stores the prompt into a database'''
    with open('prompt_database.txt', 'w', encoding='utf-8') as f:
        f.write()
        
def main():
    # for i,j in case_database:
    #     prompt = prompt_generation(i,j)
    #     prompt_database_storage(prompt)

if __name__ == '__main__':
    main()