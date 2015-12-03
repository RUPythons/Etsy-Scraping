#Webscrape - Fabrics on Etsy updated 12/3

#Importing needed functions from our library#

from ProjectLibrary import download_image
from ProjectLibrary import build_dictionary
from ProjectLibrary import Etsy_Website_Scraper
from ProjectLibrary import Etsy_Images_Scraper
import itertools    #need this to merge list of lists into one big list

#next I will open a list to iterate through

website_file = open("websites.txt","r")
temp_sites = website_file.read()
temp_sites = temp_sites.replace('"',"")
website_list = temp_sites.split()
website_file.close()

scraped_sites_list = []     #empty list to hold a list of lists for all scraped sites
scraped_images_list = []    #empty list to hold a list of lists for all scraped images

for i in website_list:
    scraped_sites_list.append(Etsy_Website_Scraper(i))

for i in website_list:
    scraped_images_list.append(Etsy_Images_Scraper(i))

merged_websites = list(itertools.chain(*scraped_sites_list))    #this will unpack each list in the scraped sites list as one big list
merged_images = list(itertools.chain(*scraped_images_list))     #this will unpack each list in the scraped images list as one big list

#print(len(merged_websites)) - prints # of websites if needed
#print(len(merged_images)) - prints # of images if needed

etsy_dictionary = build_dictionary(merged_websites,merged_images) #creates dictionary for direct purchase website & matching image

for i in merged_images:
    download_image(i)       #this function downloads and saves each image

print(merged_websites)
print(merged_images)
print(etsy_dictionary)

#Running all this code can take a few minutes so in order to save time you may want to put hashtags next to the print statements and loops, especially after you
#run it once.  Also please note, every time you run the image download loop it will save all those images (1752).  And again you have to download and install
#BeautifulSoup in order for everything to work
    







        
















