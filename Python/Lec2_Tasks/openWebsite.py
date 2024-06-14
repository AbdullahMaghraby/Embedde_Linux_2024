#module that contain favourite websites and have function called Firefox take url and open website

import webbrowser

def firefox(url):
    webbrowser.get('firefox').open(url)

#Add your favorite websites here
websites = {
        "google": "https://www.google.com",
        "github": "https://www.github.com"}

def printWebsiteMenu():
	print("Choose a website:")
	for index,website in enumerate(websites, start=1):
        	print(f"{index}. {website}")

def open_favorite_website(website_name):
    url = websites.get(website_name.lower())
    if url:
        firefox(url)
    else:
        print("Website not found in favorites.")

