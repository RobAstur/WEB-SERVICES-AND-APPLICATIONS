import requests

# Replace 'your_url_here' with the actual URL you're working with
page = requests.get('')

# Print the decoded content (as a string)
print(page.text)