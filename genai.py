
from openai import AzureOpenAI
import os
import dotenv
import pandas as pd


def getGenAiResponse(subIssue):
    # import dotenv
    dotenv.load_dotenv()
    # configure Azure OpenAI service client
    client = AzureOpenAI(
    azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ['AZURE_OPENAI_API_KEY'],  
    api_version = "2024-02-01"
    #  api_version = "2023-05-15"
    )

    deployment=os.environ['AZURE_OPENAI_DEPLOYMENT']

    # add your completion code
    df = pd.read_csv(r"C:\Users\DRi\Downloads\Consumer_complaints\complaints.csv")  

    messages = [{"role": "user", "content": subIssue}]  
    # make completion
    completion = client.chat.completions.create(model=deployment, messages=messages)

    genAiAnswer = completion.choices[0].message.content
    return genAiAnswer