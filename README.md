# Entrapeer Internship Position Task

### First part
* Your task is to crawl [this](https://ranking.glassdollar.com/) website and get the data that we would like to have.
* You need to crawl enterprises and startups. You will see 25 enterprises on the main page. Each enterprise has multiple startup partners. 
To do that you need to surf the website and check the API calls of the website. If you are using chrome you can see the network traffic via pressing F12.
* You can pythonise these requests using "curl to python" websites available on the Internet.
* The requested data includes:
  * name
  * description
  * logo_url
  * hq_city
  * hq_country
  * website_url
  * linkedin_url
  * twitter_url
  * startup_partners_count
  * startup_partners
      -company_name
      -logo_url
      -city
      -website
      -country
      -theme_gd
  * startup_themes

* You can start with using a jupyter notebook or plain python. You need to deliver the data as JSON.

### Second part
* Then in the second phase all enterprises must be crawled. Estimated number is 848.

### Third part
Next phase will be to integrate this code to the FastAPI server and provide this operation as a service. 

### Fifth part
Finally it should be run in a docker container.

### Final part
Push all your code to a Github repository, and explain how to run it in the README.
