# TODO: (STATUS: DITCHED) Browser Extension for tracking user's flipkart browsing session and purchase history
# TODO: Discuss on showing extra Product Details like size, color, etc
# TODO: Filter (Budget, Brand, Size, Color, etc)
# TODO: Improve tagging using chain of thought prompting
# TODO: Social Media Trends using https://github.com/acheong08/EdgeGPT
# TODO: Switch over to official OpenAI API

from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from revChatGPT.V1 import Chatbot
import os
import openai
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import openai
import json

# chatbot = Chatbot(config={
#   "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJzd2NpaXRnaHlAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWV9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsidXNlcl9pZCI6InVzZXItdDkydFZ2UVducDgyQUlHZ2Z4bEM2MmpUIn0sImlzcyI6Imh0dHBzOi8vYXV0aDAub3BlbmFpLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExMzQxNDkyNDM2MjMxNzQ4OTAxMCIsImF1ZCI6WyJodHRwczovL2FwaS5vcGVuYWkuY29tL3YxIiwiaHR0cHM6Ly9vcGVuYWkub3BlbmFpLmF1dGgwYXBwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2OTA4NzA1MDAsImV4cCI6MTY5MjA4MDEwMCwiYXpwIjoiVGRKSWNiZTE2V29USHROOTVueXl3aDVFNHlPbzZJdEciLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG1vZGVsLnJlYWQgbW9kZWwucmVxdWVzdCBvcmdhbml6YXRpb24ucmVhZCBvcmdhbml6YXRpb24ud3JpdGUgb2ZmbGluZV9hY2Nlc3MifQ.pJL7L1WMfymxNvfFjMUmej-4y5syM8CIVEy9e6JU_mCXkTttJBjHysWyARePFDzp8nNxKYjYRpyYa08v6JhPLoaSOmWSBCP5LI2_MW7lp23ET2CyAmPZLvg5HiwVH-JaXYHsSvlPxRPsJ68aJBE59pr4bXFV3gYa_o-A7pbtBw0RZcOWgYrJU2E4dgCWQyJ-vgbBLgv7gIbo9HmNqfvid-rXJjGvoYeJlmgCcv8dQ7ROA3RyC2PdvBlwY--37AldIw6AUMAi_Hr7LdvOTsw-vO8zebo4C263kZqDpzbar5BkMH6d5caojOlaGg85TXCs1JkYUiCYvetH1-C1D4YmgA"
# })
# convo_id = ""

openai.api_key = "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"

app = FastAPI()

load_dotenv()
userData = {}

messages=[]

@app.on_event('startup')
def init_data():
    print("init call")
    global userData
    userData["purchase_history"] = ["Men Solid Round Neck Polyester White T-Shirt", "Flip Flops  (Black 9)", "Flip Flops  (Navy, Grey 9)", "Solid Men Track Suit", "LUX INFERNO Men Top Thermal", "Woven Beanie", "Men Solid Black Track Pants", "Jockey Men's Cotton Shorts (SP26-0103-BLACK Black L)", "Hygear Men's Xpress Olive green Slippers_10 UK (HG-GE-1004)", "Jockey Men's Tailored Fit Cotton Thermal Long John (2420-Black-S_Black_S)", "Li-Ning Ultra IV Non-Marking Cushion Badminton Shoe (White, Navy, 9 UK, Unisex)", "Bewakoof Men's Cotton Solid Solid Black and White Half Sleeves | Round Neck | Regular Fit T-Shirt/Tee, Black, White", "GRITSTONES Anthramelange Full Sleeves High Neck T-Shirt (Large) Dark Grey", "DAMENSCH Men's Boy Shorts (DAM-WWB-SHT-TLB-M_D.Lit Brown_M)", "513 Men Acrylic Woolen Casual Winter Wear Striped Knitted Warm Premium Mufflers Black", "513 Girl's Self-Design Mufflers (jd423mufwmrn_Multicolored_Free Size)", "Eden & Ivy Women's Cotton Knee Length Regular Nightgown", "Eden & Ivy Women's Cotton Knee Length Relaxed Nightgown"]
    userData["browsing_history"] = ["Jockey SP26 Men's Super Combed Cotton Rich Regular Fit Solid Shorts with Side Pockets", "Puma Unisex-Adult Jog V3 Flip-Flop", "Woodland Men's Off Slipper", "Woodland mens Flip Flop", "Campus Men's Flip Flops", "Adidas mens Adirio Attack Slipper", "Hygear mens Xpress Slipper", "Jockey 9426 Men's Super Combed Cotton Rich Regular Fit Solid Shorts with Side Pockets", "Jockey 9411 Men's Super Combed Cotton Rich Straight Fit Solid Shorts with Side Pockets", "Hygear mens Zodiac Slipper", "Hygear mens Xpress Slipper", "Red Tape Women's Walking Shoes", "Puma Womens Reflex WNS Running Shoe", "US Polo Association mens Facundo Flip-flop", "crazymonk One Piece Monkey D Luffy Round Neck Anime T-Shirt"]
    global messages
    messages=[
       {
            "role": 'system',
            "content": """You are a fashion assistant at an online fashion e-commerce website. You only speak JSON and all responses should be in JSON format strictly and the JSON Object should be of one of the following two types delimeted in angle brackets:
1. < ASSISTANT_QUESTION_FORMAT >: The example for this format is given below enclosed in triple backticks:

'''
{
	"question" : "What is the budget for your outfit"
}
'''
The value of the key "question" in  ASSISTANT_QUESTION_FORMAT should contain the question you want to ask the user

2. < ASSISTANT_OUTPUT_FORMAT > : The example for this format given below enclosed in triple backticks:
'''
	{
"recommendation": ['black colored full sleeved chinos','Red Sport Shoes'],
"budget": "5000",
"gender": "Male",
"occasion": "Diwali Party"
"assistant_notes": "The user wants a outfit for a diwali party which is an traditional event hence the clothes recommended must be traditional"
}
'''
The explanation for the values of the keys in ASSISTANT_OUTPUT_FORMAT are as follows:
"recommendation" : This field consists the list of the recommendations that you generate. Please ensure that the recommendations is an tags of tags relating to each part of  the outfit. These tags will then be directly used to search for the items in a ecommerce site.
"budget": The budget specified by the user. 
"gender" : The gender of the user (male, female or unisex).
"occasion": The occasion for which the user wants the outfit.
"assistant _notes": These are the notes that you may generate while deciding the perfect outfit for the user.
To specify the user's details you will be given a RFC8259 compliant json object along with the request from the user. The request json will always be in the format as shown in the example below enclosed in backticks.
'''
		{
		  "past_purchases" : ["black colored full sleeved chinos","Red Sport Shoes"],
		  "browsing_history" : ["Oversized Tshirts","Red Trousers"],
		  "gender" : "Male",
		  "trends" : ["Oversized Printed Tshirts", "Ripped Jeans"],
		  "user_request" : "Suggest an outfit for a diwali party"
		  "user_instructions" : "Don't Suggest slim fit clothes",
		  "location" : "Mumbai",
		  "date": "10/08/2023",
          "age": "23"
		  "budget"  : "5000"
        	}
	'''

Let us call this the USER_REQUEST_FORMAT.
The explanations for the value of the keys in the User request JSON Object given in the USER_REQUEST_FORMAT format can be found below.
	    "past_purchases" : This will be an array of previous purchases of outfit items. use this to understand user's outfit preference strictly
        "browsing_history" : This will be an array of names of the items searched by the user online in the past. Analyze this to understand the user's outfit preferences and you are strictly not supposed to recommend these names directly.
        "gender" : This value represents the gender of the user.
        "trends" : This will be an array containing clothing categories currently trending among people.
        "user_request" : This field contains the actual request from the user. It must contain the occasion for which the user is requesting an outfit. If it doesn't contain the occasion, ask for the occasion in the format for questioning ( ASSISTANT_QUESTION_FORMAT) specified before.
        "user_instructions" : Some specific instructions from the user about the clothes that they wants. You are strictly supposed to follow these instructions. Do not generate responses that does not follow these instructions. You can ask for clarifications from user by asking questions in the ASSISTANT_QUESTION_FORMAT and try to ask relevant questions only.
        "location" : User's geographic location.
        "date": The date when the user makes a request. Use the location field's value and the date provided value to decide recommendations which can be worn in the weather in that location around this date. Also look for major events around that date in that location and make suggestions accordingly.
        "age": The age of the user
        "budget" : This value determines the budget of the user. If this value doesn’t exist in the json object take its default value to be 10000.
          
If you wish to ask any question to the user. ask it as a RFC8259 compliant json object in  ASSISTANT_QUESTION_FORMAT format specified before.

The user’s request must contain the occasion for which he needs an outfit. If it does not contain the occasion assume that the outfit recommendation is for casual wear.

While generating the response break down the problem into multiple smaller chunks. Before recommending anything, answer the below questions:
1. What is the type of the occasion for which the user is searching a outfit. occasion may be formal, informal, traditional or casual or something else. What is the significance of the occasion and what kind of clothes do people usually wear on such occasions.
2. What do you understand about the user's preferences from his purchasing history and browsing history. What are his preferred brands and clothing style.
3. What do you understand from the data given about the current trends. Is the data about current trends relevant while recommending outfit for the occasion given by the user. Do the trends is relevant for occasion or should the trends be ignored?
4. What would be an approximate price of each component of the outfit recommended?
5. If a user requests outfit like some personality. First think about who may be that personality and what kind of clothes does that personality usually wear and then think of some options.
6. What are some important events/festivals around the date specified in the request in the location of the user and what outfit style may be followed. What is the usual weather at that time at that location and what kind of clothes can be worn in that weather.
Add the answers to the above questions in the "assistant_notes" field of the ASSISTANT_OUTPUT_FORMAT format while generating the output.
Use the answers to these questions to recommend the outfits to the user. Do not recommend something which violates the answers of the questions given above. Make sure the outfit recommendations are complete and well coordinated including clothing,accessories and footwear.

Please give the recommendations as a set of searchable tags which can be then searched directly on ecommerce website. Please strictly adhere to the nature of the occasion being specified ( i.e whether it is traditional, formal etc) while recommending outfit.
The output should always be given as a RFC8259 compliant JSON response in the ASSISTANT_OUTPUT_FORMAT format specified at the start of the message.
Do not return anything response which are not in the 2 JSON Object formats specified at the start of the message namely: ASSISTANT_OUTPUT_FORMAT and ASSISTANT_QUESTION_FORMAT. The user’s request will follow this message
"""}
   ]


origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


def get_product_details(product_link:str,driver):
    driver.get(product_link)
    time.sleep(2)
    return {}

def chatgpt_query(userQuery):
    global messages
    messages.append({'role' : 'user','content' : userQuery})
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=0)
    print(response['choices'][0]['message']['content'])
    gpt_response = json.loads(response['choices'][0]['message']['content'])
    print(gpt_response)
    if "question" in gpt_response:
        messages.append({'role' : 'assistant','content' : gpt_response["question"]})
    else:
        messages.append({'role' : 'assistant','content' : gpt_response["recommendation"]})
    return gpt_response
    

@app.get("/items/{userQuery}")
def scrape_flipkart(age:int,location:str,gender:str,user_instructions:str,curr_date:str,userQuery:str):

    user_requests = {
		  "past_purchases" : ["black colored full sleeved chinos","Red Sport Shoes"],
		  "browsing_history" : ["Oversized Tshirts","Red Trousers"],
		  "gender" : gender,
		  "trends" : ["Oversized Printed Tshirts", "Ripped Jeans"],
		  "user_request" : userQuery,
		  "user_instructions" : user_instructions,
		  "location" : location,
		  "date": curr_date,
		  "budget"  : "10000"
        }
    user_message = {
        "role": "user",
        "content": json.dumps(user_requests)
    }
    messages.append(user_message)
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo-0613", messages=messages)
    gpt_response = json.loads(chat_completion['choices'][0]['message']['content'])
    if "question" in gpt_response:
        messages.append({'role' : 'assistant','content' : gpt_response["question"]})
        return gpt_response
    else:
        messages.append({'role' : 'assistant','content' : gpt_response["recommendation"]})
    # Call ChatGPT for flipkart search
    print(chat_completion)
    options = Options()
    options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    chatGPTresponse = gpt_response["recommendation"]

    response=[]

    # Get the products from flipkart
    for search_query in chatGPTresponse:
        try:
            driver.get(f"https://www.flipkart.com/search?q={search_query}")
            product_cards = driver.find_elements(By.CLASS_NAME, "_373qXS")
            product_description={}
            for product_card in product_cards:
                try:
                    if (product_card.find_element(By.CLASS_NAME, "_2I5qvP").find_element(By.TAG_NAME, "span").text):
                        print("Sponsored")
                except:
                    product_description["product_link"] = str(product_card.find_element(By.TAG_NAME, "a").get_attribute("href"))
                    product_description["product_name"] = str(product_card.find_element(By.CLASS_NAME, "IRpwTa").text)
                    product_description["product_price"] = product_card.find_element(By.CLASS_NAME, "_30jeq3").text
                    product_description["image_link"] = str(product_card.find_element(By.TAG_NAME, "img").get_attribute("src"))
                    break
            response.append(product_description)
        except:
            print("Outer except")
            pass

    # get_product_details(product_description["product_link"],driver)
    driver.close()
    print(response)
    return response


# @app.get("/deleteChat")
# def deleteChat():
#     chatbot.delete_conversation(convo_id=convo_id)
#     return {"status": "success"}

@app.post("/chat/{prompt}")
def chat(prompt: str):
    gpt_response = chatgpt_query(prompt)
    return gpt_response
