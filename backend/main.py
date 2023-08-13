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

@app.get("/items/{userQuery}")
def scrape_flipkart(userQuery):
    options = Options()
    options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Call ChatGPT for flipkart search
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
    response = ""
    for data in chatbot.ask(
            prompt
    ):
        global convo_id
        convo_id = data["conversation_id"]
        response = data["message"]
    return {"response": response}