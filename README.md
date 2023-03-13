# FastServer
![logo](https://i.imgur.com/zZJa3Wc.png)</br>
FastServer is server created in [FastApi](https://fastapi.tiangolo.com/) with Gateway Interface in [Uvicorn](https://www.uvicorn.org/) and Clients in various languages available.
this shows how to create a basic server with **Users** information and how to handle users data and operations listed below.

## Server Operations.
- **Adding** - Adding user to server using `/add-user/` endpoint.
- **Updating** - Updating user information in server using `/update-user/` endpoint.
- **Removing** - Removing user in server using `/remove-user/` endpoint.
- **Retrieving** - Retrieving user information in server using `/user/?id=` endpoint.
- **Server-Info** - Retrieving server information using `/server-info/` endpoint.
- **Server DB Reset** - Resetting whole server using  `/null/` endpoint. _[BETA]_ **Risky**.

## Server Features.
- Simple and fast server using Python.
- Server with _228_ requests per second.
- Persistent Database using `Json`.
- Auto reloading source changes.

## Server Docs.
Server documentation is automatically generated using `FastApi`.
**Docs using OpenApi**</br>
![ServerDocs](https://i.imgur.com/ZYHhEV4.png)

**ReDocs using OpenApi**</br>
![ServerReDocs](https://i.imgur.com/fVJdWKW.png)

# Server
Server is created in Python and to start server first install modules from `requirements.txt`.</br>
- [FastApi](https://fastapi.tiangolo.com/) : use `pip install fastapi`</br>
- [Uvicorn](https://www.uvicorn.org/) : use `pip install vvicorn`</br>
Then run the server using following methods.
- Using Uvicorn : use `python -m uvicorn FastServer:app --reload`
- Using Python : user `python -u FastServer.py`
Server started running ![ServerStart](https://i.imgur.com/g4EJu0a.png)

# Client
Clients are created in various languages like **C++,Go,JavaScript...** to handle basic operations on users like _Adding/Updating/Removing User_ operations.
here are list of following clients available and for sake of simplicity every client is named to `FastClient`.

## Cpp - C++ Client for FastServer.
- **Client** - `Cpp\FastClient.cpp` Contains client for FastServer.
- **Requirements** - `Cpp\lib` folder contains `HTTPRequest.hpp` for sending/posting _Http_ Requests to server and `json.hpp` for parsing Json using [JsonCpp](https://github.com/nlohmann/json)

## Chsarp - C# Client for FastServer.
- **Client** - `csharp\FastClient.cs` Contains client for FastServer.
- **Requirements** - install modules from `requirements.txt` listed as [_Newtonsoft.Json_](https://www.newtonsoft.com/json),[_RestSharp_](https://restsharp.dev/) or use the command line.
command: `dotnet add package Newtonsoft.Json`

## GoLang - GO Client for FastServer.
- **Client** - `golang\FastClient.go` Contains client for FastServer.
- **Requirements** - *None* just run the _FastClient.go_ file.
- **Features**  -  Fastest client sending 200 Request/s and Adding _500 Users_ in _3.12_ seconds

## Nodejs - JavaScript Client for FastServer.
- **Client** - `nodejs\FastClient.js` Contains client for FastServer.
- **Requirements** - install modules from `requirements.txt` listed as _request_,_Faker_ or use the command line.
command: `npm install request`
- **Features**  -  Fastest client sending 200 Request/s and Adding _500 Users_ in _3.62_ seconds

## Python - Python Client for FastServer.
- **Client** - `python\FastClient.py` Contains client for FastServer.
- **Requirements** - install modules from `requirements.txt` listed as _FastApi_,_Uvicorn_,_requests_ or use the command line.
command: `pip install fastapi`

## Swift - Swift Client for FastServer.
- **Client** - swift/FastClient.swift Contains client for FastServer.
- **Requirements** - - None. The client uses built-in Swift libraries.

## Rust - Rust Client for FastServer.
- **Client** - rust/FastClient.rs Contains client for FastServer.
- **Requirements** - - Install reqwest and serde crates using the following command:
`cargo install reqwest serde`

## Java - Java Client for FastServer.
- **Client** - java/FastClient.java Contains client for FastServer.
- **Requirements** - - None. The client uses built-in Java libraries.

written and maintained by Haseeb Mir (haseebmir.hm@gmail.com)
