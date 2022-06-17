# MCA-CSR-PSU-Scrapper
This app uses Selenium to automate the web crawling and in the end it uses pandas to scrape the data out of the webpages and save into a csv file.
- This code scrapes data from the GOV of India website csr.gov.in
- it scape the csr spend of all the PSU companies for last 5 financial year and saves it in csv format

to run the code
- Install requirements.txt
- Download Chromedriver (or other Webdriver) according to your OS compatibility and substitute its Path
- Read the comments throughout the code and disable the code you don't need and change the looping frequency

the code can fail in various ways, believe me the problem is from website side bcoz of slow server
  the same code will work if you try again

- you have to manually change the values in code for doing it for different year
- Later I will try to make an input system to run the app, so that you don't need to change the looping frequency manually in the code
