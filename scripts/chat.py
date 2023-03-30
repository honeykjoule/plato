from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
    input_variables=["user_input"]
    template = "context: you are platoGPT, respond to your interlocutor as would Socrates.\nInterlocutor: {user_input}"
)

def generate_response(user_input, chat_log):
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(user_input)

