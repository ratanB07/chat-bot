# # import google.generativeai as genai
# # import os

# # os.environ["API_KEY"] = ' '
# # genai.configure(api_key=os.environ["API_KEY"])

# # instruction ='you are a text summarizer. Summarize customer service conversation in 3 lines. this is easily understand by agent'
# # model = genai.GenerativeModel('gemini-1.5-flash-latest',system_instruction=instruction)

# # with open('input.txt','r') as f:
# #     chat = f.read()
# # print(chat)

# # response = model.generate_content(chat)
# # # print(response.text,'/n')

# # import google.generativeai as genai
# # import google.generativeai as genai
# # import os
 
# # # Set the API key
# # os.environ["API_KEY"] = 'AIzaSyCyP-Dd4suFMt459CkpXhWTDZXuNcHVVCc'  # Replace with your actual API key
# # genai.configure(api_key=os.environ["API_KEY"])
# # # Define the instruction for the model
# # instruction ='you are a chat conversation summarizer. Summarize customer service conversation in 3 lines. this is easily understood by agent. give me summarized text in json file like {"customer_query":" ","agent_response":" ","information_provided":" "} '
# # # Load the generative model
# # model = genai.GenerativeModel('gemini-1.5-flash-latest',system_instruction=instruction,generation_config={"response_mime_type": "application/json"})
# # # Read the input conversation from the file
# # with open('input.txt', 'r') as f:
# #     chat = f.read()  # Use .strip() to clean up leading/trailing whitespace
# # print("Input Chat:")
# # print(chat)
# # # Generate the response
# # response = model.generate_content(chat)
# # # Print the raw response
# # print("Raw Response:")
# # print(response)
# # # Access and print the generated summary
# # print("Generated Summary:")
# # print(response.text)  # Check if this is the correct way to access the summary


# import google.generativeai as genai
# import os

# # Set up API key for generative AI
# os.environ["API_KEY"] = 'AIzaSyCyP-Dd4suFMt459CkpXhWTDZXuNcHVVCc'
# genai.configure(api_key=os.environ["API_KEY"])

# # Define the instruction for the model to summarize
# instruction = 'You are a text summarizer. Summarize customer service conversations in 3 lines. Ensure that it is easily understood by an agent.'

# # Create generative model with system instruction
# model = genai.GenerativeModel('gemini-1.5-flash-latest', system_instruction=instruction)

# # Sample input from a Citi Bank customer query
# customer_query = """
# Hello, I’m facing an issue with my Citi credit card. I made a payment a week ago, but it’s still not reflecting in my statement. 
# I tried calling customer support, but I couldn’t reach anyone. Can you please assist in resolving this issue as soon as possible?
# """

# # Use the generative model to summarize the conversation
# response = model.generate_content(customer_query)

# # Print the summarized response
# print("Summary for agent: ", response.text)





import google.generativeai as genai
import os

# Set up API key for generative AI
os.environ["API_KEY"] = 'AIzaSyCyP-Dd4suFMt459CkpXhWTDZXuNcHVVCc'
genai.configure(api_key=os.environ["API_KEY"])

# Define the instruction for the model to summarize
instruction = 'You are a text summarizer. Summarize customer service conversations in 3 lines. Ensure that it is easily understood by an agent.'

# Create generative model with system instruction
model = genai.GenerativeModel('gemini-1.5-flash-latest', system_instruction=instruction)

# Sample input: list of 10 customer queries
customer_queries = [
    "I have a problem with my Citi credit card. The payment isn't reflected in my account.",
    "I lost my Citi debit card, and I need to block it immediately. Please help!",
    "I was charged twice for a transaction I made at a store. Can you reverse the duplicate charge?",
    "I applied for a personal loan a month ago, but I haven’t received any update. What’s the status?",
    "My account was debited incorrectly for an amount I didn’t authorize. How can I get a refund?",
    "I'm having trouble accessing my Citi account online. The login page keeps giving an error.",
    "My credit limit was reduced without any notification. I need to understand why.",
    "I made a payment through the Citi app, but it’s still showing as pending. Can you resolve this?",
    "I want to increase my credit card limit. What’s the procedure for this?",
    "There are unknown charges on my statement. I need assistance in investigating this."
]

# Summarize each query using the generative model
for idx, query in enumerate(customer_queries):
    print(f"Original Query {idx + 1}: {query}")
    response = model.generate_content(query)
    print(f"Summary {idx + 1}: {response.text}\n")

