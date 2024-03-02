import os
import pandas as pd  ## read csv files
from llama_index.query_engine import PandasQueryEngine ## this will query the questions from the document
from prompts import new_prompt, instruction_str, context ## this will import the prompt template from prompts.py(we created)
from llama_index.tools import QueryEngineTool, ToolMetadata 

population_path = os.path.join("data", "population.csv")
population_df = pd.read_csv(population_path)  ## panda used for structured data, for cvs (pdf will use different library)

population_query_engine = PandasQueryEngine(
    df=population_df, verbose=True, instruction_str=instruction_str
) # we passed the insturction from prompts.py (we created)
population_query_engine.update_prompts({"pandas_prompt": new_prompt}) # we will pass new promt as pandas dictionary, comes from teh prompts.py (we created)

population_engine =     QueryEngineTool(
        query_engine=population_query_engine,
        metadata=ToolMetadata(
            name="population_data",
            description="this gives information at the world population and demographics",
        ),
    )