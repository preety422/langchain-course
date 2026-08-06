from dotenv import load_dotenv;
load_dotenv()
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama


def main():
    print("Hello from langchain-course!")

information= """
Elon Reeve Musk (/ˈiːlɒn/ ⓘ EE-lon; born June 28, 1971) is a businessman and former public official who is the CEO and largest shareholder of Tesla and SpaceX. Musk has been the wealthiest person in the world since 2025, and became the only trillionaire in terms of US dollars in June 2026; as of July 23, 2026, Forbes estimates his net worth to be US$744 billion.
"""

summay_template = """
given the information {information} about a person 
I want you to do
1. SUmmarize in 2 line
2. Give 2 interesting facts.
"""

summary_prompt_template=PromptTemplate(template=summay_template, input_variables=["information"])
llm= ChatOpenAI(model="gpt-5", temperature=0)
llm= ChatOllama(temperature=0, model="gemma3:270m")

chain=summary_prompt_template | llm
result=chain.invoke({"information": information})
print(result.content)


if __name__ == "__main__":
    main()
