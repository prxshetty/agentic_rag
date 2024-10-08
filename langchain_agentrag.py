# -*- coding: utf-8 -*-
"""langchain_agentrag.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OCg60bYBD6FdAlTgIi4a24pNUr0Izhx3
"""

!pip3 install langchain-ollama langchain-openai
!pip3 install langchain_community langchain chromadb

# from dotenv import load_dotenv
import os
from langchain_ollama import ChatOllama
from langchain_ollama import OllamaEmbeddings
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
# load_dotenv()

def get_llm():
  llm_type = os.getenv("LLM_TYPE", "ollama")
  if llm_type == "ollama":
    return ChatOllama(model = "llama3.1", temperature = 0)
  else:
    return ChatOpenAI(temperature = 0, model = "gpt-4o-mini")

def get_embeddings():
  embedding_type = os.getenv("LLM_TYPE", "ollama")
  if embedding_type == "ollama":
    return OllamaEmbeddings(model = "llama3.1")
  else:
    return OpenAIEmbeddings()

from langchain.schema import Document
from langchain_community.vectorstores import Chroma
embedding_function = get_embeddings()
# collection = chroma_client.create_collection(name="HotelMenusData")
docs = [
    Document(
        page_content="Bella Vista is owned by Antonio Rossi, a renowned chef with over 20 years of experience in the culinary industry. He started Bella Vista to bring authentic Italian flavors to the community.",
        metadata={"source": "restaurant_info.txt"},
    ),
    Document(
        page_content="Bella Vista offers a range of dishes with prices that cater to various budgets. Appetizers start at $8, main courses range from $15 to $35, and desserts are priced between $6 and $12.",
        metadata={"source": "restaurant_info.txt"},
    ),
    Document(
        page_content="Bella Vista is open from Monday to Sunday. Weekday hours are 11:00 AM to 10:00 PM, while weekend hours are extended from 11:00 AM to 11:00 PM.",
        metadata={"source": "restaurant_info.txt"},
    ),
    Document(
        page_content="Bella Vista offers a variety of menus including a lunch menu, dinner menu, and a special weekend brunch menu. The lunch menu features light Italian fare, the dinner menu offers a more extensive selection of traditional and contemporary dishes, and the brunch menu includes both classic breakfast items and Italian specialties.",
        metadata = {"source": "restaurant_info.txt"},
    ),
]
db =Chroma.from_documents(docs, embedding_function, persist_directory = None)
retriever = db.as_retriever()

