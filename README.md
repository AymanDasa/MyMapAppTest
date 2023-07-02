# Read Me - Get My Location
This is a simple Python application that retrieves the latitude and longitude coordinates for a given address using the Google Geocoding API. The application prompts the user to enter an address and then makes a request to the API to obtain the corresponding location information.
## Prerequisites
To run this application, you need to have Python installed on your system. You can download the latest version of Python from the official website: [Python Pages](https://www.python.org/downloads/) 
## Getting Started
1. Download the Python script and save it with a **.py** extension, for example, **get_location.py**.
1. Open a command prompt or terminal and navigate to the directory where the script is saved.
1. Execute the script by running the following command:
```
python get_location.py
```
## Usage
1. When prompted, enter the address for which you want to retrieve the location coordinates.
1. Press Enter to submit the address.
1. The application will send a request to the Google Geocoding API and retrieve the response.
1. If the response status is "OK," the latitude and longitude coordinates will be printed to the console in the format: **lat < latitude > - lng < longitude >**.
1. If the response status is not "OK," an error message will be displayed.
1. Repeat steps 1-5 to retrieve location coordinates for different addresses. To exit the application, leave the address input empty and press Enter.
## API Key
This application requires an API key to access the Google Geocoding API. In the current implementation, the API key is set to **42** for demonstration purposes. However, this key may not be valid or functional.
To use a valid API key, you need to replace **'key' = 42** with **'key' = '<your_api_key>'** in the url_parm dictionary in the git_my_location function. You can obtain an API key by creating a project on the Google Cloud Platform and enabling the Geocoding API.
## Note
This application uses the **urllib** library to handle HTTP requests and the **json** library to parse the response data. These libraries are part of Python's standard library, so no additional installations are required.
Please ensure you have a stable internet connection for the application to communicate with the Google Geocoding API.
## Disclaimer
This application is provided as-is without any warranty. The use of this application is at your own risk. Please refer to the Google Geocoding API documentation for any questions or concerns regarding the usage and terms of the API.
