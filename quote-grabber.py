#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def quote_extractor(response):
  """
  Function to extract the Quote of the Day from the Wikiquote HTML.

  The function returns the quote as a string object back to the calling function.
  """
  # parse the requests object to a soup object
  soup = BeautifulSoup(response.text, 'html.parser')

  return soup.find("table",style="text-align:center; width:100%").text

if __name__ == "__main__":
  # define the URL
  URL = "https://en.wikiquote.org/wiki/Main_Page"

  # fetch the page html
  response = requests.get(URL)

  if response.ok:
    quote = quote_extractor(response)

    # print the quote on the stdout
    print(quote)

  else:
    print(f"Script encountered a problem connecting to the Wikiquote URL.\nThe error returned is {response.status_code}: {response.text}")
    exit(99)
