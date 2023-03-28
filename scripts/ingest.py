import os
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import TextLoader

file_path = os.path.join(os.path.dirname(__file__), "../data/all_plato.txt")
#print(file_path)

loader = TextLoader(file_path)

index = VectorstoreIndexCreator().from_loaders([loader])

query = "What is justice?"

print(index.query_with_sources(query))