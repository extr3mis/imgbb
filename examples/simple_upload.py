#Imports
from imgbb.client import Client
import os
import aiohttp
import asyncio

#Setting up required vars
key = os.getenv('IMGBB_API_KEY')

#Creating a session to upload images
session = aiohttp.ClientSession()

#Making a Client() object to interact with imgbb
myclient = Client(key,session)

async def upload(image,name):
    response = await myclient.post(image,name) #Posting to imgbb and collecting response
    url = response['data']['url']
    print(f'Uploaded image URL: {url}')

if __name__=='__main__':
    asyncio.run(upload('image.jpg','Cool picture')) #Runs in an async context
