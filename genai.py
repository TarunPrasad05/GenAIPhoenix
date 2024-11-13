
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
    df = pd.read_csv(r"C:\Users\DRi\Downloads\Consumer_complaints\Trouble_Filtered_Dataset.csv")  
    prompt = f"You are an agent in banking sector, address the issue of the customer and give the realtime resolution for the issue user is reporting.. Do not answer to the irrelevant questions Here is a preview of the consumer complaints dataset: {df.to_string()}"
    prompt += subIssue
    # prompt += (  
    #     "Based on the above dataset summary, provide the following insights:\n"  
    #      "Please provide the following insights:\n"  
    #     "1. Summarize the key issues reported in these complaints.\n"  
    #     "2. Identify common themes or patterns in the complaints.\n"  
    #     "3. Highlight the most frequently reported issues.\n"  
    #     "4. Analyze the sentiment of the complaints.\n"  
    #     "5. Provide recommendations for addressing the most common complaints.\n"  
    #     "6. Detect any unusual or outlier complaints.\n" 
    #     "7. What will you recommend to resolve the customer issue - Incorrect information on your report."
    # )  

    messages = [{"role": "user", "content": prompt}]  
    # make completion
    completion = client.chat.completions.create(model=deployment, messages=messages)

    genAiAnswer = completion.choices[0].message.content
    return genAiAnswer

#  Only answer to the question the customer asked,
#                 and limit the answer not more than 150 words