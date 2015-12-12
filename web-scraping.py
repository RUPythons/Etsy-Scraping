#Webscrape - Fabrics on Etsy updated 12/11, part 3

#Importing needed functions from our library#

from ProjectLibrary import download_image
from ProjectLibrary import build_dictionary
from ProjectLibrary import Scraper
from ProjectLibrary import Image_Name
import os           #need this to make a folder to save the images in  
import itertools    #need this to merge list of lists into one big list

#next I will open a list to iterate through

website_file = open("websites.txt","r")
temp_sites = website_file.read()
temp_sites = temp_sites.replace('"',"")
website_list = temp_sites.split()
website_file.close()

scraped_sites_list = []     #empty list to hold a list of lists for all scraped sites
scraped_images_list = []    #empty list to hold a list of lists for all scraped images

for site in website_list:
    temp_var = Scraper(site) #temporary variable to initiate Scraper class
    scraped_sites_list.append(temp_var.scrapedSites()) #appends lists of scraped websites to website list

for site in website_list:
    temp_var = Scraper(site) #temporary variable to initiate Scraper class
    scraped_images_list.append(temp_var.scrapedImages()) #appends lists of scraped images to images list

merged_websites = list(itertools.chain(*scraped_sites_list))    #this will unpack each list in the scraped sites list as one big list
merged_images = list(itertools.chain(*scraped_images_list))     #this will unpack each list in the scraped images list as one big list

#print(len(merged_websites)) - prints # of websites if needed
#print(len(merged_images)) - prints # of images if needed

etsy_dictionary = build_dictionary(merged_websites,merged_images) #creates dictionary for direct purchase website & matching image

create_folder = os.path.dirname(os.path.abspath(__file__)) #returns the path name to create a folder on a given computer
destination = os.path.join(create_folder,'Group14') #merges that path name with any other given directory information
try:
    os.makedirs(destination)            #this will try to create a folder 
except OSError:
    pass                                #however if you run it twice it will return an error, so this will ignore the error

for i in merged_images:
    download_image(i)       #this function downloads and saves each image

print(merged_websites)
print(merged_images)
print(etsy_dictionary)

#Running all this code can take a few minutes so in order to save time you may want to put hashtags next to the print statements and loops, especially after you
#run it once.  Also please note, every time you run the image download loop it will save all those images (1752).  And again you have to download and install
#BeautifulSoup in order for everything to work
    







        
















