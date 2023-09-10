This program is a client-server program pair for sending chat messages back and forth. The server opens a socket and waits for the client to connect. After connecting the client and server take turns sending messages back and forth.  On the client the server IP address is hard coded as 127.0.0.1 for the sake of demos.

This project was more about network sockets so the chat is pretty rudimentary.


Run `pip install pynput`

In one command prompt window run `python server.py`

In another command prompt window run `python client.py`


Cited sources: 
https://www.delftstack.com/howto/python/python-clear-console/
https://www.geeksforgeeks.org/how-to-detect-if-a-specific-key-pressed-using-python/
https://docs.python.org/3/howto/sockets.html
https://realpython.com/python-sockets/
