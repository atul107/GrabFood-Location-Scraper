# GrabFood Scraper
This is a Python script that uses Selenium and SeleniumWire to scrape GrabFood website for restaurant locations in Singapore. The script visits the website and simulates scrolling to load new content. It then extracts JSON data from the POST request made by the website to obtain data, and extracts restaurant location data from the JSON data. Finally, it saves the extracted data to a JSON file.

## Installation
1. Clone the repository to your local machine
```
git clone https://github.com/<username>/grabfood-scraper.git
```
2. Install the required Python packages
```
pip install -r requirements.txt
```
3. Install the latest version of ChromeDriver for your Chrome browser. You can download it from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). Make sure to add the path to the ChromeDriver executable to your PATH environment variable.
## Usage
1. Open `config.json` and specify the base URL for the website and the URL for the POST request made by the website to obtain data.

2. Run the `main.py` script to start scraping the website. The extracted data will be saved to a JSON file named `data.json` in the project directory.

## License
This project is licensed under the MIT License. See the [LICENSE]() file for more information.
