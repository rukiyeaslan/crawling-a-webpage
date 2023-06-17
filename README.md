# Glassdollar Crawling 

This project is a Python-based web scraping application that collects data from the [website](https://ranking.glassdollar.com/) of Glassdollar. It allows users to get all 848 enterprises and retrieve information such as their names, description, startup partners, and other relevant details. The application utilizes threading for concurrent processing to improve performance and speed up the data retrieval process

## Installation
* Clone the repository: 
```git clone https://github.com/rukiyeaslan/entrapeer-task.git```
* Navigate to the project directory: ```cd entrapeer-task```
* Run ```docker build -t  crawl .```
* Run ```docker run -p 8000:8000 crawl```

## Usage
* Access the application in your web browser at ```http://0.0.0.0:8000```
