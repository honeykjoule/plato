from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
    input_variables = ["vibe"],
    template = "You are vibeGPT. You must pass the vibecheck based on the user's input: '{vibe}.' You have one shot to tell a joke that makes the user laugh."
)

chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run("happy"))