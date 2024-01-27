import requests
from bs4 import BeautifulSoup

Page = input("Whats the page URL? ")

def get_html_content(url):
  """Gets the HTML content of the web page."""
  response = requests.get(url)
  return response.content

def parse_html_content(html_content):
  """Parses the HTML content and extracts the desired information."""
  soup = BeautifulSoup(html_content, 'html.parser')
  return soup

def main():
  """Runs the web scraper."""
  url = Page
  html_content = get_html_content(url)
  soup = parse_html_content(html_content)
  title = soup.find('head').text
  body = soup.find('body').text
  print(title)
  print(body)
  

if __name__ == "__main__":
  main()