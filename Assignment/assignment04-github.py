from github import Github
import requests
from config import config as cfg

# GitHub API key
apikey = cfg["githubkey"]

# Create a GitHub instance
g = Github(apikey)

# Access the repository
repo = g.get_repo("RobAstur/WEB-SERVICES-AND-APPLICATIONS")

# Get the file information for 'test.txt' within the 'Mywork' directory
try:
    fileInfo = repo.get_contents("Mywork/test.txt")  # File path within the repository
except Exception as e:
    print(f"Error accessing the file: {e}")
    exit()

# Get the file content
urlOffile = fileInfo.download_url
response = requests.get(urlOffile)

# Check if the file content was fetched successfully
if response.status_code != 200:
    print(f"Failed to fetch file content: {response.status_code}")
    exit()

contentOffile = response.text

# Replace "Andrew" with "Manolo"
NewContents = contentOffile.replace("Andrew", "Manolo")

# Print the new contents (optional)
print(NewContents)

# Now we need the 'sha' of the file for the update operation
try:
    gitHubResponse = repo.update_file(
        fileInfo.path,  # Path of the file in the repo
        "Updated 'Andrew' to 'Manolo' by program",  # Commit message
        NewContents,  # New content to save
        fileInfo.sha  # File SHA (important to avoid overwriting)
    )
    print(f"File updated successfully: {gitHubResponse}")
except Exception as e:
    print(f"Error updating the file: {e}")