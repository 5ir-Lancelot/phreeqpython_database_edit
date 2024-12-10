import os
import requests
import phreeqpython


# First get the path where phreeqpython databases are stored.
database_path = os.path.dirname(phreeqpython.__file__)  # may Update with the actual path

#add files from online source to the path

# GitHub repository URL for the raw file
api_url = 'https://api.github.com/repos/5ir-Lancelot/phreeqpython_database_edit/contents/database/'#


# Get the list of files from the GitHub API
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    files = response.json()  # Parse the JSON response into a list of files

    # Define the local folder to save the files
    #local_folder = 'local_folder_path'  # Change this to your desired local folder

    # Create the local folder if it doesn't exist
    if not os.path.exists(database_path):
        os.makedirs(database_path)

    # Download each file
    for file in files:
        file_name = file['name']  # Get the file name from the API response
        file_url = file['download_url']  # GitHub provides a 'download_url' for each file

        # Send a GET request to download the file
        file_response = requests.get(file_url)

        if file_response.status_code == 200:
            # Define the local file path where the file will be saved
            local_file_path = os.path.join(database_path, file_name)

            # Write the file content to the local file
            with open(local_file_path, 'wb') as f:
                f.write(file_response.content)
            print(f"Downloaded: {file_name}")
        else:
            print(f"Failed to download: {file_name}")
else:
    print(f"Failed to fetch folder contents. Status code: {response.status_code}")



# List all database files in the specified directory
databases = [f for f in os.listdir(database_path) if f.endswith('.dat')]
print("Available databases:", databases)