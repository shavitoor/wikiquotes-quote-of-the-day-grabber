# Description

Little demo site scraping to grab the Wikiquote "Quote of the day". The URL to the website, for reference, is `https://en.wikiquote.org/wiki/Main_Page`

## Dependencies

- Python 3
- BeautifulSoup
- Requests

## Execution steps

It is recommended to work inside a Python Virtual Environment. The following steps include this.

- Install a new python virtual environment using `python3 -m venv env`
- Activate the virtual environment using `. env/bin/activate`
- Install the required libraries using `pip install -r requirements.txt`
- Change permissions on the main executable python file `chmod u+x quote-grabber.py`
- Run the script using `./quote-grabber.py`