from dotenv import load_dotenv ## this is for importing .env vairables, API keys etc...


from llama_index.tools import QueryEngineTool, ToolMetadata  
from llama_index.agent import ReActAgent
from llama_index.llms import OpenAI


## BELOW files and engines created by us ##
from prompts import new_prompt, instruction_str, context ## this will import the prompt template from prompts.py(we created)
from engines.note_engine import note_engine ## we created teh note_engine as tool
from engines.pdf_engine import canada_engine  ## we created this files in the project
from engines.csv_engine import population_engine  ## we created this files in the project

## load the api keys
load_dotenv()



## listing the tools that we have access to (you can create as needed)
tools = [
    note_engine,
    population_engine,
    canada_engine,
]

llm = OpenAI(model="gpt-3.5-turbo-0613")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)  ## tools coming from above list

while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    result = agent.query(prompt)
    print(result)
