from dotenv import load_dotenv ## this is for importing .env vairables, API keys etc...
import os
import pandas as pd  ## read csv files
from llama_index.query_engine import PandasQueryEngine  ## this will query the questions from the document
from prompts import new_prompt, instruction_str  ## this will import the prompt template from prompts.py(we created)


## load the api keys
load_dotenv()

population_path = os.path.join("data","population.csv" )
population_df = pd.read_csv(population_path)


population_query_engine = PandasQueryEngine(df=population_df, verbose = True, instruction_str=instruction_str ) # we passed the insturction from prompts.py (we created)
population_query_engine.update_prompts({"pandas_prompt":new_prompt}) # we will pass new promt as pandas dictionary, comes from teh prompts.py (we created)

## !! $$ each query got charged from OPENAI platform $$
# population_query_engine.query("What is the population of Canada") # type in your query here


# print(population_df.head())