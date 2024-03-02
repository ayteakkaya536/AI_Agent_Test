import os
from llama_index import StorageContext, VectorStoreIndex, load_index_from_storage   ## load_..from sotrage if index cerated, it will take it from there, will not create again
from llama_index.readers import PDFReader ## this will be used for unstructured data such as pdf
from llama_index.tools import QueryEngineTool, ToolMetadata 

def get_index(data, index_name):
    index = None
    if not os.path.exists(index_name):
        print("building index", index_name)
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        index.storage_context.persist(persist_dir=index_name)
    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
        )

    return index


pdf_path = os.path.join("data", "Canada.pdf")
canada_pdf = PDFReader().load_data(file=pdf_path)
canada_index = get_index(canada_pdf, "canada")  ## this will create a folder named Canada, and store the vectors in it
canada_engine = canada_index.as_query_engine()  

canada_engine = QueryEngineTool(
        query_engine=canada_engine,  ## this comes from pdf.py file, engine is defined inside
        metadata=ToolMetadata(
            name="canada_data",
            description="this gives detailed information about canada the country",
        ),
    )