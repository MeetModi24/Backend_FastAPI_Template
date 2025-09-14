What is uvicorn?

Uvicorn is a lightweight, high-performance web server for Python that is specifically designed for running asynchronous web applications. Uvicorn acts as the bridge between your web application and the outside world, handling all network communication. Uvicorn is an ASGI (Asynchronous Server Gateway Interface) server. 
ASGI vs. WSGI: Before ASGI, Python used WSGI (Web Server Gateway Interface) for communication between servers and applications. However, WSGI is synchronous, meaning it can only process one request at a time per worker. ASGI overcomes this limitation, enabling asynchronous frameworks to handle many requests concurrently and efficiently.

You write the app: You build your application using a web framework like FastAPI, which defines how to handle incoming requests and send responses.
Uvicorn runs the app: Uvicorn is the program that listens for network requests, directs them to your FastAPI application for processing, and then returns the response back to the client.

What is starlette?
Starlette is a lightweight ASGI (Asynchronous Server Gateway Interface) framework/toolkit for Python. It provides the core functionalities for building asynchronous web applications, including:
Routing: Defining URL patterns and mapping them to handler functions.
Middleware: Intercepting requests and responses to perform actions like authentication, logging, or error handling.
WebSockets: Handling real-time, bidirectional communication between clients and the server.
HTTP Request/Response Handling: Managing the low-level details of HTTP communication.
