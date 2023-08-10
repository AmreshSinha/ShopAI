from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from revChatGPT.V1 import Chatbot

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time



chatbot = Chatbot(config={
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJzd2NpaXRnaHlAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWV9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsidXNlcl9pZCI6InVzZXItdDkydFZ2UVducDgyQUlHZ2Z4bEM2MmpUIn0sImlzcyI6Imh0dHBzOi8vYXV0aDAub3BlbmFpLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExMzQxNDkyNDM2MjMxNzQ4OTAxMCIsImF1ZCI6WyJodHRwczovL2FwaS5vcGVuYWkuY29tL3YxIiwiaHR0cHM6Ly9vcGVuYWkub3BlbmFpLmF1dGgwYXBwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2OTA4NzA1MDAsImV4cCI6MTY5MjA4MDEwMCwiYXpwIjoiVGRKSWNiZTE2V29USHROOTVueXl3aDVFNHlPbzZJdEciLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG1vZGVsLnJlYWQgbW9kZWwucmVxdWVzdCBvcmdhbml6YXRpb24ucmVhZCBvcmdhbml6YXRpb24ud3JpdGUgb2ZmbGluZV9hY2Nlc3MifQ.pJL7L1WMfymxNvfFjMUmej-4y5syM8CIVEy9e6JU_mCXkTttJBjHysWyARePFDzp8nNxKYjYRpyYa08v6JhPLoaSOmWSBCP5LI2_MW7lp23ET2CyAmPZLvg5HiwVH-JaXYHsSvlPxRPsJ68aJBE59pr4bXFV3gYa_o-A7pbtBw0RZcOWgYrJU2E4dgCWQyJ-vgbBLgv7gIbo9HmNqfvid-rXJjGvoYeJlmgCcv8dQ7ROA3RyC2PdvBlwY--37AldIw6AUMAi_Hr7LdvOTsw-vO8zebo4C263kZqDpzbar5BkMH6d5caojOlaGg85TXCs1JkYUiCYvetH1-C1D4YmgA"
})
convo_id = ""
purchase_history = ["Men Solid Round Neck Polyester White T-Shirt", "Flip Flops  (Black 9)", "Flip Flops  (Navy, Grey 9)", "Solid Men Track Suit", "LUX INFERNO Men Top Thermal", "Woven Beanie", "Men Solid Black Track Pants", "Jockey Men's Cotton Shorts (SP26-0103-BLACK Black L)", "Hygear Men's Xpress Olive green Slippers_10 UK (HG-GE-1004)", "Jockey Men's Tailored Fit Cotton Thermal Long John (2420-Black-S_Black_S)", "Li-Ning Ultra IV Non-Marking Cushion Badminton Shoe (White, Navy, 9 UK, Unisex)", "Bewakoof Men's Cotton Solid Solid Black and White Half Sleeves | Round Neck | Regular Fit T-Shirt/Tee, Black, White", "GRITSTONES Anthramelange Full Sleeves High Neck T-Shirt (Large) Dark Grey", "DAMENSCH Men's Boy Shorts (DAM-WWB-SHT-TLB-M_D.Lit Brown_M)", "513 Men Acrylic Woolen Casual Winter Wear Striped Knitted Warm Premium Mufflers Black", "513 Girl's Self-Design Mufflers (jd423mufwmrn_Multicolored_Free Size)", "Eden & Ivy Women's Cotton Knee Length Regular Nightgown", "Eden & Ivy Women's Cotton Knee Length Relaxed Nightgown"]
browsing_history = ["Jockey SP26 Men's Super Combed Cotton Rich Regular Fit Solid Shorts with Side Pockets", "Puma Unisex-Adult Jog V3 Flip-Flop", "Woodland Men's Off Slipper", "Woodland mens Flip Flop", "Campus Men's Flip Flops", "Adidas mens Adirio Attack Slipper", "Hygear mens Xpress Slipper", "Jockey 9426 Men's Super Combed Cotton Rich Regular Fit Solid Shorts with Side Pockets", "Jockey 9411 Men's Super Combed Cotton Rich Straight Fit Solid Shorts with Side Pockets", "Hygear mens Zodiac Slipper", "Hygear mens Xpress Slipper", "Red Tape Women's Walking Shoes", "Puma Womens Reflex WNS Running Shoe", "US Polo Association mens Facundo Flip-flop", "crazymonk One Piece Monkey D Luffy Round Neck Anime T-Shirt"]

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items")
def scrape_flipkart():
    options = Options()
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.flipkart.com/")
    time.sleep(10)
    print(driver)
    print(driver.title)
    time.sleep(10)
    # closeButton = driver.find_element(By.CLASS_NAME,"_2KpZ6l _2doB4z")
    # print(closeButton)
    time.sleep(10)
    searchButton = driver.find_element(By.CLASS_NAME,"Pke_EE")
    print(searchButton)
    driver.close()
    # return {}

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