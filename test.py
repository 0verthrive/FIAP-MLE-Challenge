from data_extraction.data_extraction import requests_download, urls
import time

extracted_urls = urls()
for url in extracted_urls:
    requests_download(url)

