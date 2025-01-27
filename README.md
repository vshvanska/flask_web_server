# Flask web server 

This project is a Flask-based web server that interacts with a MySQL database to  handle URL verdicts.
The server provides the following functionality:
---

- **Add a URL with a verdict (legit, spam or malware)**
 ``http://localhost:5000/sources``
- **Check if specific domain exists and return its verdict**
``http://localhost:5000/sources/{{domain-name}}``
- **Delete a record from the database**
``http://localhost:5000/sources/{{domain-name}}``


The application and the MySQL database run in Docker containers managed by Docker Compose

## Setup instructions

- Clone repository
- Create the .env file and fill required variables
``cp .env.sample .env``
- build and run containers
``docker-compose up --build``

## Example usage

POST/http://localhost:5000/sources
request body: 

{"domain": "https://github.com/vshvanska/flask_web_server", "verdict": "malware" }

Output:

201
{"domain": "github.com", "verdict": "malware"}