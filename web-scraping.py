#Webscrape - Fabrics on Etsy updated 12/13, finalized

#Importing needed functions from our library#

from ProjectLibrary import download_image
from ProjectLibrary import List_Ops
from ProjectLibrary import scrapedSites
from ProjectLibrary import scrapedImages
from ProjectLibrary import MakeDictionary
import os           #need this to make a folder to save the images in  

#next I will open a list to iterate through

website_file = open("websites.txt","r")
temp_sites = website_file.read()
temp_sites = temp_sites.replace('"',"")
website_list = temp_sites.split()
website_file.close()

scraped_sites_list = []     #empty list to hold a list of lists for all scraped sites
scraped_images_list = []    #empty list to hold a list of lists for all scraped images

for site in website_list:
    scraped_sites_list.append(scrapedsites(site)) #appends lists of scraped websites to website list

for site in website_list:
    scraped_images_list.append(scrapedimages(site)) #appends lists of scraped images to images list

merged_websites = List_Ops(scraped_sites_list)  
merged_websites = merged_websites.buildlist()  #this will build a large list of the scraped websites

merged_images = List_Ops(scraped_images_list)  
merged_images = merged_images.buildlist()  #this will build a large list of websites to download the images


#print(len(merged_websites)) #prints of websites if needed
#print(len(merged_images)) #prints of images if needed
#print(merged_websites) #prints list of websites if needed
#print(merged_images) #prints list of images if needed

etsy_dictionary = MakeDictionary(merged_websites,merged_images) #creates dictionary for direct purchase website & matching image
etsy_dictionary = etsy_dictionary.dictionarybuild()
#print(etsy_dictionary) #prints dictionary if needed

create_folder = os.path.dirname(os.path.abspath(__file__)) #returns the path name to create a folder on a given computer
destination = os.path.join(create_folder,'Group14') #merges that path name with any other given directory information

try:
    os.makedirs(destination)            #this will try to create a folder 
except OSError:
    pass                                #however if you run it twice it will return an error, so this will ignore the error

for sites in merged_images:
    download_image(sites)               #will download and save images to a folder on user's computer

#Running all this code can take a few minutes so in order to save time you may want to put hashtags next to the print statements and loops, especially after you
#run it once.  Also please note, every time you run the image download loop it will save all those images (1752).  And again you have to download and install
#BeautifulSoup in order for everything to work








        
















