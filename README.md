# ckl-scraper
It's a web scrapping tool that scrapes TechCrunch's blog in order to show my abilities to write code, comments and meaninfful git commits.

I used Djnago as the web framework and Scrapy to do the scraping. Besides that I found a cool DjangoItem in GitHub, in order to save normal Scrapy Items directly into the Django Model.

I created the requirements.txt file in order for other people to be able to rebuild the same environment I was using.

Besides that I added a init.sh file which runs the commands makemigrations, migrate (in order to create the databases, if they are not created yet) and then runs the scraper and starts the server. To see the results access http://localhost:8000/scraper/
