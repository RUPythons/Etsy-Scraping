#Webscrape - Fabrics on Etsy

#Importing needed functions from our library#
from ProjectLibrary import download_image
from ProjectLibrary import build_dictionary
from ProjectLibrary import Etsy_Website_Scraper
from ProjectLibrary import Etsy_Images_Scraper
import itertools    #need this to merge list of lists into one big list

#next I will create a list to iterate through
website_list = ["https://www.etsy.com/shop/AfricanFabricsStore?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=1","https://www.etsy.com/shop/AfricanFabricsStore?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=2","https://www.etsy.com/shop/AfricanFabricsStore?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=3","https://www.etsy.com/shop/AfricanFabricsStore?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=4","https://www.etsy.com/shop/AfricanFabricsStore?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=5","https://www.etsy.com/shop/AfricanFabricsStore?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=6","https://www.etsy.com/shop/AfricanFabricsStore?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=7","https://www.etsy.com/shop/AfricanFabricsStore?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=8","https://www.etsy.com/shop/AfricanFabricsStore?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=9","https://www.etsy.com/shop/AfricanFabricsStore?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=10","https://www.etsy.com/shop/TessWorldDesigns?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=1","https://www.etsy.com/shop/TessWorldDesigns?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=2","https://www.etsy.com/shop/TessWorldDesigns?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=3","https://www.etsy.com/shop/TessWorldDesigns?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=4","https://www.etsy.com/shop/TessWorldDesigns?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=5","https://www.etsy.com/shop/TessWorldDesigns?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=6","https://www.etsy.com/shop/TessWorldDesigns?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=7","https://www.etsy.com/shop/TessWorldDesigns?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=8","https://www.etsy.com/shop/TessWorldDesigns?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=9","https://www.etsy.com/shop/TessWorldDesigns?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=10","https://www.etsy.com/shop/TessWorldDesigns?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=11","https://www.etsy.com/shop/TessWorldDesigns?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=12","https://www.etsy.com/shop/TessWorldDesigns?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=13","https://www.etsy.com/shop/TessWorldDesigns?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=14","https://www.etsy.com/shop/TessWorldDesigns?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=15","https://www.etsy.com/shop/TessWorldDesigns?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=16","https://www.etsy.com/shop/TessWorldDesigns?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=17","https://www.etsy.com/shop/TessWorldDesigns?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=18","https://www.etsy.com/shop/TessWorldDesigns?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=19","https://www.etsy.com/shop/TessWorldDesigns?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=20","https://www.etsy.com/shop/TessWorldDesigns?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=21","https://www.etsy.com/shop/TessWorldDesigns?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=22","https://www.etsy.com/shop/TessWorldDesigns?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=23","https://www.etsy.com/shop/TessWorldDesigns?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=24","https://www.etsy.com/shop/TessWorldDesigns?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=25","https://www.etsy.com/shop/TessWorldDesigns?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=26","https://www.etsy.com/shop/TessWorldDesigns?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=27","https://www.etsy.com/shop/TessWorldDesigns?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=28","https://www.etsy.com/shop/TessWorldDesigns?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=29","https://www.etsy.com/shop/TessWorldDesigns?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&page=30","https://www.etsy.com/shop/FabricGiantUSA?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=1","https://www.etsy.com/shop/FabricGiantUSA?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=2","https://www.etsy.com/shop/FabricGiantUSA?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=3","https://www.etsy.com/shop/FabricGiantUSA?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=4","https://www.etsy.com/shop/FabricGiantUSA?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=5","https://www.etsy.com/shop/FabricGiantUSA?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=6","https://www.etsy.com/shop/FabricGiantUSA?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=7","https://www.etsy.com/shop/FabricGiantUSA?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=8","https://www.etsy.com/shop/FabricGiantUSA?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=9","https://www.etsy.com/shop/FabricGiantUSA?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=10","https://www.etsy.com/shop/FabricGiantUSA?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=11","https://www.etsy.com/shop/FabricGiantUSA?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=12","https://www.etsy.com/shop/FabricGiantUSA?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=13","https://www.etsy.com/shop/FabricGiantUSA?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=14","https://www.etsy.com/shop/FabricGiantUSA?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=15","https://www.etsy.com/shop/FabricGiantUSA?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=16","https://www.etsy.com/shop/FabricGiantUSA?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=17","https://www.etsy.com/shop/FabricGiantUSA?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=18","https://www.etsy.com/shop/KitengeTextiles?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=1","https://www.etsy.com/shop/KitengeTextiles?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=2","https://www.etsy.com/shop/KitengeTextiles?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=3","https://www.etsy.com/shop/KitengeTextiles?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=4","https://www.etsy.com/shop/KitengeTextiles?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=5","https://www.etsy.com/shop/KitengeTextiles?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=6","https://www.etsy.com/shop/KitengeTextiles?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=7","https://www.etsy.com/shop/KitengeTextiles?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=8","https://www.etsy.com/shop/KitengeTextiles?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=9","https://www.etsy.com/shop/KitengeTextiles?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=10","https://www.etsy.com/shop/KitengeTextiles?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=11","https://www.etsy.com/shop/KitengeTextiles?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=12","https://www.etsy.com/shop/KitengeTextiles?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=13","https://www.etsy.com/shop/KitengeTextiles?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=14","https://www.etsy.com/shop/KitengeTextiles?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=15","https://www.etsy.com/shop/KitengeTextiles?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=african+fabric&page=16"]

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
    







        
















