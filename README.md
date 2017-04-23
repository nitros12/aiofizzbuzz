# Aiofizzbuzz [![Build Status](https://travis-ci.org/nitros12/aiofizzbuzz.svg?branch=master)](https://travis-ci.org/nitros12/aiofizzbuzz)
An asynchronous implementation of fizzbuzz

# Installation
To install aiofizzbuzz use the following command
`python3 -m pip install -U git+git://github.com/nitros12/aiofizzbuzz@master`

# Example Usage
```python
import asyncio
from aiofizzbuzz import AioFizzBuzz

loop = asyncio.get_event_loop()

async def main():
  async for i in AioFizzBuzz(1, 101):
    print(i)

loop.run_until_complete(main())
```
