from bs4 import BeautifulSoup
import json
import re
from pymongo import MongoClient
from django.http import HttpResponse, HttpResponseNotFound

def parse_and_store(request):
    try:
        # Load JSON data from the file with specified encoding
        with open('pressranger_scraped_pub_pages.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        return HttpResponseNotFound("JSON file not found.")
    except UnicodeDecodeError:
        return HttpResponse("Error decoding JSON file. Please ensure it is encoded in UTF-8.")
    
    if isinstance(data, list) and data:
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/') 
        db = client['webscrapr123'] 
        collection = db['webscraped_data'] 

        # Initialize index for while loop
        index = 0
        data_length = len(data)

        # Iterate over each entry in the list using a while loop
        while index < data_length:
            document = data[index]

            # Extract the URL and content
            _id = document['_id']['$oid']
            url = document['url']
            html_content = document['content']

            if html_content:
                soup = BeautifulSoup(html_content, 'html.parser')
                
                # Extract paragraphs
                paragraphs = list(set(p.get_text() for p in soup.find_all('p')))

                # Extract mobile numbers 
                mobile_numbers = list(set(re.findall(r'\b\d{10}\b', html_content)))

                # Extract email addresses
                email_addresses = list(set(re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', html_content)))

                # Extract LinkedIn URLs
                linkedin_urls = list(set(re.findall(r'https?://[www\.]*linkedin\.com/in/[A-Za-z0-9-]+', html_content)))

                # Extract Twitter handles 
                twitter_handles = list(set(re.findall(r'@([A-Za-z0-9_]+)', html_content)))

                # Extract image URLs 
                image_urls = list(set(img['src'] for img in soup.find_all('img') if 'src' in img.attrs))

                # Create a dictionary for insertion
                data_to_insert = {
                    '_id': _id,
                    'url': url,
                    'paragraphs': paragraphs,
                    'mobile_numbers': mobile_numbers,
                    'email_addresses': email_addresses,
                    'linkedin_urls': linkedin_urls,
                    'twitter_handles': twitter_handles,
                    'image_urls': image_urls
                }

                collection.insert_one(data_to_insert)
            
            # Increment index for while loop
            index += 1

        return HttpResponse("All data inserted into MongoDB")
    else:
        return HttpResponse("Unexpected JSON format.")
