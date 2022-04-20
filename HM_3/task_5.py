"""
Use the requests library to send a get request to some website of your choice. Save the response
content(text) to a text file.
"""

import requests

get = requests.get("https://dir.bg/")
# get.encoding = get.apparent_encoding
response = open("task_5_output.txt", 'w')
response.write(str(get.content))
