# GENERATOR

> This mini script shows the operation of the generator. The meaning of the script: in one 
> of my commercial projects, there was a task to parse a TRON node to receive transactions. 
> But at the stage of production, we faced such a problem as our TRON node always breaking,
> and this could last for days. And we made decisions as soon as our node stops working, 
> we take and work with other nodes. Here is a simple realisation of the code.

---

#### The method that installs the generator. And sets it the URL to the nodes.
>```python
> from typing import Generator
>
>
> def set(urls: list[str]) -> Generator:
>    """Set new generator"""
>    while True: 
>       for url in urls:
>           yield url           # Returns generator object
> 
>    
> def update(generator: Generator) -> str:
>    """Update generator"""
>    return next(generator)     # Returns the URL of the node
>
> ```

----

#### Emulation of the system.
>Let's assume that this is a working script and it is constantly running and here 
> it meets with a problem and this is what happens
,
> ```python
> import time
> import requests
> from .generator import set, update
> from .updater import update_transaction
> from .config import logger
> 
>
> def parser():
>   """Parser mode"""
>   # Set generator
>   generator = set(urls=["https://main.node.com", "https://helper.node.com", ...])
>   # Put url path 
>   url = next(generator)
>   while True:
>       try:
>           data = requests.request(POST, url + "/transaction/show", json={...})
>       except requests.HTTPError as error:
>           # This code updates the node
>           logger.error(f"THE NODE DIED! UPDATE URL! NEW URL: {update(generator)}")
>       else:
>           # Add tx to db
>           update_transaction(tx=data["transaction"])
>       logger.error("WORK IS GOOD! I'M SLEEP 10 SEC!")
>       time.sleep(10)
>
> ```

-----

> A simpler example of the work:: `./example.py`
> ```shell
> python3 example.py 
> ...
> START! URL: https://main.node.com
> ERROR: This index is so bad!
> UPDATE! NEW URL: https://helper.node.com
> ERROR: This index is so bad!
> UPDATE! NEW URL: http://private.node.com
> ERROR: This index is so bad!
> UPDATE! NEW URL: https://public.node.com
> True
> ```

----
#### PS. Every time an error occurs, the URL will change. The URL can be as many as you want and everything will work endlessly.

> I do not pretend to be the best way out of this situation. I'm just learning what I advise you to do. Perhaps after 
> some time I will understand that this way of solving the problem is complete `shit`.