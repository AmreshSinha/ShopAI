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

import json

chatbot = Chatbot(config={
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJzd2NpaXRnaHlAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWV9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsidXNlcl9pZCI6InVzZXItdDkydFZ2UVducDgyQUlHZ2Z4bEM2MmpUIn0sImlzcyI6Imh0dHBzOi8vYXV0aDAub3BlbmFpLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExMzQxNDkyNDM2MjMxNzQ4OTAxMCIsImF1ZCI6WyJodHRwczovL2FwaS5vcGVuYWkuY29tL3YxIiwiaHR0cHM6Ly9vcGVuYWkub3BlbmFpLmF1dGgwYXBwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2OTA4NzA1MDAsImV4cCI6MTY5MjA4MDEwMCwiYXpwIjoiVGRKSWNiZTE2V29USHROOTVueXl3aDVFNHlPbzZJdEciLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG1vZGVsLnJlYWQgbW9kZWwucmVxdWVzdCBvcmdhbml6YXRpb24ucmVhZCBvcmdhbml6YXRpb24ud3JpdGUgb2ZmbGluZV9hY2Nlc3MifQ.pJL7L1WMfymxNvfFjMUmej-4y5syM8CIVEy9e6JU_mCXkTttJBjHysWyARePFDzp8nNxKYjYRpyYa08v6JhPLoaSOmWSBCP5LI2_MW7lp23ET2CyAmPZLvg5HiwVH-JaXYHsSvlPxRPsJ68aJBE59pr4bXFV3gYa_o-A7pbtBw0RZcOWgYrJU2E4dgCWQyJ-vgbBLgv7gIbo9HmNqfvid-rXJjGvoYeJlmgCcv8dQ7ROA3RyC2PdvBlwY--37AldIw6AUMAi_Hr7LdvOTsw-vO8zebo4C263kZqDpzbar5BkMH6d5caojOlaGg85TXCs1JkYUiCYvetH1-C1D4YmgA"
})
convo_id = ""
purchase_history = ["Men Solid Round Neck Polyester White T-Shirt", "Flip Flops  (Black 9)", "Flip Flops  (Navy, Grey 9)", "Solid Men Track Suit", "LUX INFERNO Men Top Thermal", "Woven Beanie", "Men Solid Black Track Pants", "Jockey Men's Cotton Shorts (SP26-0103-BLACK Black L)", "Hygear Men's Xpress Olive green Slippers_10 UK (HG-GE-1004)", "Jockey Men's Tailored Fit Cotton Thermal Long John (2420-Black-S_Black_S)", "Li-Ning Ultra IV Non-Marking Cushion Badminton Shoe (White, Navy, 9 UK, Unisex)", "Bewakoof Men's Cotton Solid Solid Black and White Half Sleeves | Round Neck | Regular Fit T-Shirt/Tee, Black, White", "GRITSTONES Anthramelange Full Sleeves High Neck T-Shirt (Large) Dark Grey", "DAMENSCH Men's Boy Shorts (DAM-WWB-SHT-TLB-M_D.Lit Brown_M)", "513 Men Acrylic Woolen Casual Winter Wear Striped Knitted Warm Premium Mufflers Black", "513 Girl's Self-Design Mufflers (jd423mufwmrn_Multicolored_Free Size)", "Eden & Ivy Women's Cotton Knee Length Regular Nightgown", "Eden & Ivy Women's Cotton Knee Length Relaxed Nightgown"]
browsing_history = ["Jockey SP26 Men's Super Combed Cotton Rich Regular Fit Solid Shorts with Side Pockets", "Puma Unisex-Adult Jog V3 Flip-Flop", "Woodland Men's Off Slipper", "Woodland mens Flip Flop", "Campus Men's Flip Flops", "Adidas mens Adirio Attack Slipper", "Hygear mens Xpress Slipper", "Jockey 9426 Men's Super Combed Cotton Rich Regular Fit Solid Shorts with Side Pockets", "Jockey 9411 Men's Super Combed Cotton Rich Straight Fit Solid Shorts with Side Pockets", "Hygear mens Zodiac Slipper", "Hygear mens Xpress Slipper", "Red Tape Women's Walking Shoes", "Puma Womens Reflex WNS Running Shoe", "US Polo Association mens Facundo Flip-flop", "crazymonk One Piece Monkey D Luffy Round Neck Anime T-Shirt"]

app = FastAPI()

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

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

@app.post("/items")
def scrape_flipkart(userQuery:str):
    
    BASE_PROMPT = "You are a fashion expert at Flipkart which is an online e commerce site and your role is to recommend good outfits to people according to their preferences. You have access to some data about the people like their previous purchases, browsing history, gender, age, location etc. People may also specify the occasion for which they might want a outfit for. If the occasion is not specified you are supposed to ask for the occasion before giving the result. You have to understand the customer's preferences from the data given and recommend outfits for the occasion keeping in mind the location , gender, age of the user as well as the current trends. You also need to take care of the customer's preferred style , color and brand. Make sure the outfit recommendations are complete and well coordinated including clothing,accessories and footwear. Also if the user doesn't specify any budget do ask for it before recommending. You may also be given the current date in the data and you need to use your knowledge of events or festivals in India near this date to recommend outfits. While generating the response think step by step. Answer the following questions before generating any response. \n 1. What is the type of the occasion for which the user is searching for a outfit. Whether it is formal, informal, traditional event etc. What is the significance of the occasion and what kind of clothes do people usually wear to such events \n 2. What do you understand about the user's preferences from his purchasing and browsing history. \n3. What do you understand from the data given about the current trends. Is the data about current trends relevant while recommending outfit for the occasion given by the user. Do the trends lie in line with type of occasion or should the trends be ignored.\n 4. What would be an approximate price of each component of the outfit recommended. \nUse the answers to these questions while recommending outfits. Instructions for input and output will be given in the next prompt. Donot reply to this prompt."

    RESPONSE_INSTRUCTION = '''An example input would be :
    {
    "past_purchases": ["Men Solid Round Neck Polyester White T-Shirt", "Flip Flops  (Black 9)"],
    "browsing_history":  ["Jockey SP26 Men's Super Combed Cotton Rich Regular Fit Solid Shorts with Side Pockets", "Puma Unisex-Adult Jog V3 Flip-Flop"],
    “gender” : “male”,
    “trends”: ["Jockey 9426 Men's Super Combed Cotton Rich Regular Fit Solid Shorts with Side Pockets", "Jockey 9411 Men's Super Combed Cotton Rich Straight Fit Solid Shorts with Side Pockets"]
    “Specific_request”: “Please recommend only cotton clothes”
    “location” : “Mumbai”
    “Date”: “10th June”
    }
    If any of the fields are not given in the input ignore them.
    For the output the output should always be given as a json object. If you are asking an additional question make sure to give it as a json object like:
    {
    “question”: “What is your budget”
    }
    While recommending outfits return it as a json object. Along with the recommendation also return the budget and gender of the user Example of a outfit recommendation would be:
    {
    “recommendation”:  ['black colored full sleeved chinos','Red Sport Shoes'],
    “budget”: 5000
    “gender”: “male”
    }
    Please give the recommendations as a set of searchable tags which can be then searched directly on ecommerce website. Please strictly adhere to the nature of the occasion being specified ( i.e whether it is traditional, formal etc) while recommending clothes.
    You are strictly not supposed to return any other than the json object. Strictly donot reply to the prompt. The users requirements will follow next '''

    messages = [
        {
            "role" : "user",
            "content":BASE_PROMPT
        },
        {
            "role": "system",
            "content": "Understood"
        },
        {
            "role":"user",
            "content": RESPONSE_INSTRUCTION
        },
        {
            "role": "system",
            "content": "Understood"
        },
        {
            "role": "user", 
            "content": userQuery
        }
    ]
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo-0613", messages=messages)
    # Call ChatGPT for flipkart search
    print(chat_completion)
    options = Options()
    options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    chatGPTresponse = ["Red Anime Shirt","Black Ripped Pant","Superhero Sneakers"]

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
    return json.dumps(response);


@app.get("/deleteChat")
def deleteChat():
    chatbot.delete_conversation(convo_id=convo_id)
    return {"status": "success"}

@app.post("/chat")
def chat(prompt: str):
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo-0613", messages=[{"role": "user", "content": "Hello world"}])
    return chat_completion