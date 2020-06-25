# imgbb

<img src='https://img.shields.io/badge/Python-3.5+-blue'> <img src='https://img.shields.io/badge/license-MIT-green'> <img src='https://img.shields.io/badge/async-enabled-blue'>

A simple tool enabling you to asynchronously upload images to <a href='https://www.imgbb.com'>imgbb</a>.
_Requires Python 3.5+_

# Installation

Install this package using `pip`.
```console
$ pip install -e git+https://github.com/extr3mis/imgbb
```

# Usage
Import the package using the given import statement.
```console
$ from imgbb.client import Client
```
Now you can make a `Client` object and initialize it with your own API key from imgbb.
```console
$ myclient = Client(api_key_here)
```
Now you can use your `Client` to upload an image using the `Client.post()` method. Since `Client.post()` is a `coroutine` make sure to `await` it. Catch the response from the request in `request`.
```console
$ response = await myclient.post('/path_to_image/image.jpg','name')
```
Now you can get the URL to the image you've just uploaded using `response['data']['url']`.
```console
$ URL = response['data']['url']
```

# Quick Example
```py
from imgbb.client import Client
import os
import aiohttp
import asyncio
key = os.getenv('IMGBB_API_KEY')
session = aiohttp.ClientSession()
myclient = Client(key,session)

async def upload(image,name):
    response = await Client.post(image,name)
    url = response['data']['url']
    print(f'Uploaded image URL: {url}')

if __name__=='__main__':
    asyncio.run(upload('image.jpg','Cool picture'))
```