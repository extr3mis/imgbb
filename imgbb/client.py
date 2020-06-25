import asyncio
import aiohttp

URL = 'https://api.imgbb.com/1/upload'
class Client():
    """The default interface to interact with Imgbb."""
    def __init__(self, key, session=None):
        self.key = key
        if session is None:
            self.session = aiohttp.ClientSession()
        else: self.session=session
    async def post(self,filename,name):
        """Post using a filename like 'image.jpg'"""
        with open(filename, 'rb') as img:
            payload = {"key" : self.key, "image" : img.read(), "name" : name}
        async with self.session.post(URL, data=payload) as response:
            resp = await response.json()
        return resp
    async def postbyte(self, bytesfile, name):
        """Use when you want to upload a `bytes` object."""
        payload = {"key" : self.key, "image" : bytesfile, "name" : name}
        async with self.session.post(URL, data=payload) as response:
            resp = await response.json()
        return resp
