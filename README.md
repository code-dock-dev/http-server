# Python Web Server Project

## 📘 Overview
This project is a **from-scratch Python web server** built entirely using the **Python Standard Library**. It starts from a basic socket-based "Hello, Browser!" example and evolves into a fully-fledged, production-ready API framework.

The project follows a step-by-step progression inspired by the interactive guide found in `index.html`, covering all essential topics — from basic HTTP handling to building an asynchronous, secure, and extensible web server.

---

## 🧩 Project Structure

```
.
├── index.html              # Interactive guide and documentation
├── main.py                 # Entry point for the web server
├── server.py               # Core server setup and socket listener
├── router.py               # URL routing logic
├── request_handler.py      # Parses HTTP requests
├── response_builder.py     # Builds structured HTTP responses
├── mime_type_handler.py    # Handles MIME type detection for assets
└── __init__.py             # Package initializer
```

---

## 🚀 Features

- ✅ Serve static HTML, CSS, JS, and image files  
- ✅ Custom routing and 404 handling  
- ✅ Multi-threaded request handling  
- ✅ Support for POST requests and form data  
- ✅ Modular architecture using OOP principles  
- ✅ MIME type detection and response management  
- ✅ Async I/O support for high-performance concurrency  
- ✅ Secure with basic best practices and error handling  

---

## 🧠 How It Works

The server uses **Python sockets** to communicate with browsers.  
Each incoming HTTP request is parsed, routed, and responded to using custom-built components.

### Main Components:
- **`Server`** — Starts and manages socket connections  
- **`Router`** — Maps URLs to functions or files  
- **`RequestHandler`** — Parses and validates incoming requests  
- **`ResponseBuilder`** — Constructs proper HTTP responses  
- **`MimeTypeHandler`** — Determines correct content-type headers  

---

## ⚙️ Running the Server

1. **Clone this project** or copy all files into a directory.
2. Run the main server file:

   ```bash
   python3 main.py
   ```

3. Open your browser and visit:

   ```bash
   http://localhost:8080
   ```

You should see your first **"Hello, Browser!"** message.

---

## 🧱 Progressive Learning Path

The included `index.html` provides a full roadmap divided into 4 main phases:

1. **Basic Server Foundations** — Learn sockets and HTTP fundamentals  
2. **Advanced Features** — Add threading, POST requests, and async I/O  
3. **Production Readiness** — Secure, deploy, and manage gracefully  
4. **Framework Evolution** — Add routing, middleware, DI, and auto docs  

---

## 🔐 Future Enhancements

- Add SSL/TLS for HTTPS support  
- Implement middleware system for logging/authentication  
- Connect to a database (SQLite, PostgreSQL, etc.)  
- Add REST API with JSON request/response handling  
- Generate OpenAPI-style documentation automatically  

---

## 🧑‍💻 Author
Developed by **Janith Madarasinghe**  
Inspired by modern Python frameworks like Flask, FastAPI, and Sanic — but written completely **from scratch** for educational and experimental purposes.

---

## 📄 License
This project is licensed under the **MIT License**.  
Feel free to modify and distribute it with proper attribution.
