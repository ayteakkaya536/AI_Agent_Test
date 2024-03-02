from dotenv import load_dotenv ## this is for importing .env vairables, API keys etc...
import os
import pandas as pd  ## read csv files
from llama_index.query_engine import PandasQueryEngine ## this will query the questions from the document
from prompts import new_prompt, instruction_str, context ## this will import the prompt template from prompts.py(we created)
from note_engine import note_engine ## we created teh note_engine as tool
from llama_index.tools import QueryEngineTool, ToolMetadata  
from llama_index.agent import ReActAgent
from llama_index.llms import OpenAI
from pdf import canada_engine  ## we caretd this files in the project

## load the api keys
load_dotenv()

population_path = os.path.join("data", "population.csv")
population_df = pd.read_csv(population_path)  ## panda used for structured data, for cvs (pdf will use different library)

population_query_engine = PandasQueryEngine(
    df=population_df, verbose=True, instruction_str=instruction_str
) # we passed the insturction from prompts.py (we created)
population_query_engine.update_prompts({"pandas_prompt": new_prompt}) # we will pass new promt as pandas dictionary, comes from teh prompts.py (we created)

## listing the tools that we have access to (you can create as needed)
tools = [
    note_engine,
    QueryEngineTool(
        query_engine=population_query_engine,
        metadata=ToolMetadata(
            name="population_data",
            description="this gives information at the world population and demographics",
        ),
    ),
    QueryEngineTool(
        query_engine=canada_engine,  ## this comes from pdf.py file, engine is defined inside
        metadata=ToolMetadata(
            name="canada_data",
            description="this gives detailed information about canada the country",
        ),
    ),
]

llm = OpenAI(model="gpt-3.5-turbo-0613")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)

while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    result = agent.query(prompt)
    print(result)
