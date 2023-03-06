import json
from time import sleep

from Driver import Driver

from selenium.common.exceptions import TimeoutException
from seleniumwire.utils import decode as sw_decode


class Scraper:  
    def __init__(self, driver: Driver, base_url, post_url) -> None: 
        self.driver = driver 
        self.base_url = base_url
        self.post_url = post_url 
        self._init_request() # initialize the request by visiting the base URL

    def _init_request(self):
        self.driver.browser.get(self.base_url)
        sleep(10) # sleep for 10 seconds to allow page to load

    def scroll(self):
        del self.driver.browser.requests # clear previous requests
        last_height = self.driver.browser.execute_script("return document.body.scrollHeight")
        while True:
            # scroll to the bottom of the page
            self.driver.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            sleep(10) # sleep for 10 seconds to allow new content to load
            try:
                new_height = self.driver.browser.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break # if page height doesn't change anymore, break the loop
                last_height = new_height
            except TimeoutException:
                break # if timeout exception is raised, break the loop

    def extract_post_response(self):
        post_data = []
        for r in self.driver.browser.iter_requests():
            if r.method == 'POST' and r.url == self.post_url:
                content_encoding = r.response.headers.get('Content-Encoding', 'identity')
                data = sw_decode(r.response.body, content_encoding).decode('utf8')
                post_data.append(json.loads(data)) # extract and append the JSON data to post_data list
        return post_data

    def extract_locations(self, post_data):
        locations = {}
        for p in post_data:
            merchants = p.get('searchResult', {}).get('searchMerchants', [])
            for merchant in merchants:
                chain_id = merchant.get('chainID')
                name = merchant.get('address', {}).get('name', None)
                latlng = merchant.get('latlng', {})
                location_data = {'chainName': merchant.get('chainName'), 'latlng': latlng}
                if chain_id:
                    locations[chain_id] = location_data # add the chain_id as key to the dictionary
                elif name:
                    locations[name] = location_data # add the name as key to the dictionary
        return locations

    def scrape(self):
        self.scroll() # scroll the page to load new content
        post_data = self.extract_post_response()  # extract the JSON data from the response
        locations = self.extract_locations(post_data)  # extract the locations from the JSON data
        print(locations) # print the extracted locations
        return locations # return the extracted locations as a dictionary