import json

from Scraper import Scraper
from Driver import *
from Dataparser import JsonParser


def main():
    # Open the config.json file and read the data into a dictionary
    with open('config.json') as config_file:
        config_data = json.load(config_file)
    
    # Read the values of the variables from the dictionary
    base_url = config_data['base_url']
    post_url = config_data['post_url']
    user_agent = config_data['user_agent']
    additional_args = config_data['additional_args']
    output_file = config_data['output_file']

    # Arguments to be passed to the ChromeDriver constructor
    args = {
        'user_agent': user_agent,
        'additional_args': additional_args,
    }
    # Creates a ChromeDriver instance with the specified arguments.
    chromeDriver = ChromeDriver(args)  
    # Creates a Scraper instance with the ChromeDriver instance and base and POST URLs.
    scraper = Scraper(chromeDriver, base_url, post_url) 
    # Scrapes the web page using the Scraper instance and obtains the desired data.
    locations = scraper.scrape() 
    # Creates a JsonParser instance and saves the data to a file in JSON format.
    jsonParser = JsonParser()
    jsonParser.save_data_to_file(locations, output_file) 

if __name__ == "__main__":
    main()
