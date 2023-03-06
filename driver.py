from selenium import webdriver
from seleniumwire import webdriver


class Driver:
    #Abstract base class for browser drivers
    def __init__(self, args):
        self.browser = None
        self.setup(args)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def setup(self, args):
        #Abstract method to set up the browser
        pass

    def close(self):
        #Quit the browser
        self.browser.quit()

class ChromeDriver(Driver):
    #Chrome browser driver

    def __init__(self, args):
        super().__init__(args)

    def setup(self, args):
        #Set up the Chrome browser
        opts = webdriver.ChromeOptions()
        user_agent = args['user_agent']
        opts.add_argument(f'user-agent={user_agent}')
        for arg in args['additional_args']:
            opts.add_argument(arg)
        self.browser = webdriver.Chrome(desired_capabilities=opts.to_capabilities())