# Crawl-App-Store
App Store Crawler script using python

This script uses <a href="https://github.com/cowboy-bebug/app-store-scraper">app_store_scraper</a> repository. You can install it from here or you can run <b>pip install app-store-scraper</b> in the command line.

Also using BueatifulSoup to extract some extra information then store all the data in pandas dataframe.

## NOTE: All the outputs of this library functions are JSON code

This code takes a list of apps names from an CSV file, search app store to find them and return some details about them. Of course you can change what details you want to see, since the output is JSON code, it's very easy to handle with it.
