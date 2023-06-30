# Glassdollar Crawling 

This project is a Python-based web scraping application that collects data from the [website](https://ranking.glassdollar.com/) of Glassdollar. It allows users to get all 848 enterprises and retrieve information such as their names, description, startup partners, and other relevant details. The application utilizes threading for concurrent processing to improve performance and speed up the data retrieval process

## Installation
1. Clone the repository:
   ```
    git clone https://github.com/rukiyeaslan/entrapeer-task.git
   ```
2. Navigate to the project directory:
   ```
   cd entrapeer-task
   ```
3. Run the following command on your terminal:
   ```
   docker build -t  crawl .
   ```
4. Run the following command on your terminal:
   ```
   docker run -p 8000:8000 crawl
   ```

## Usage
Access the application in your web browser via this [link](http://0.0.0.0:8000).
