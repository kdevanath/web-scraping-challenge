# web-scraping-challenge

Created a Jupyter Notebook file called mission_to_mars.ipynb and completed scraping and analysis tasks. 
NASA Mars News

Scraped the NASA Mars News Site and collected the latest News Title and Paragraph Text. Assigned the text to a dictionary mars_dict to be rendered.

Visit the url for JPL Featured Space Image here.


Used splinter to navigate the site and found the image url for the current Featured Mars Image and assigned the url string to a variable called featured_image_url.


Acraped the url for full size .jpg image.

Saved the string
Visit the Mars Facts webpage https://space-facts.com/mars/
and used Pandas to scrape the table containing facts about the planet including Diameter, Mass,

Visited the USGS Astrogeology site https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars to obtain high resolution images for each of Mar's hemispheres.

Get the partial link first andthen find the image url to the full resolution image.
Stored the information in the dictionary.
Appended the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
routes used / and /scrape
Created a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements.
snapshot contains a snapshot of the output.
