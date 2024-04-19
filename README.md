# Music Time Machine

A Python script generates a Spotify playlist containing the top 100 songs from a given date based on the Billboard Hot 100 chart.It uses the requests library to scrape song data from the Billboard website and the Spotipy library to create a Spotify playlist with the retrieved songs.

Table of Contents
[Requirements](#Requirements)
[Obtaining Spotify Client ID and Client Secret](#Obtaining Spotify Client ID and Client Secret)
[Installation](#Installation)
[Usage](#Usage)
[Known Limitations]

## Requirements

A Spotify account
A Spotify Client ID and Client Secret (obtainable by creating an application at https://developer.spotify.com/dashboard/)
Python 3

## Obtaining Spotify Client ID and Client Secret

Visit the Spotify Developer Dashboard and log in with your Spotify account.
Click the "Create a Client ID" button in the top-right corner.
Fill in the form with your application details:
Application Name: Choose a name for your application. This can be anything you like, e.g., "Billboard Playlist Generator."
Application Description: Provide a brief description of your application. For example, "A script that generates Spotify playlists based on Billboard charts."
Application Website: You can leave this blank or provide a relevant URL, such as the GitHub repository link for your script.
Redirect URI: Enter "http://example.com" for now, as specified in the script. You can update this later if needed.
Review and accept the Developer Terms of Service, then click the "Create" button.
After creating the application, you'll be redirected to the application dashboard. Here, you'll find your Client ID and Client Secret.

## Installation

Clone this repository to your local machine or download the main.py file.
Update the CLIENT_ID and CLIENT_SECRET variables in the main.py file with your own values.
(Optional) Update the username variable in the SpotifyOAuth object with your Spotify username.

## Install or upgrade required libraries

To install or upgrade the required libraries, use the following commands:
pip install --upgrade beautifulsoup4
pip install --upgrade spotipy
pip install requests
These commands will ensure that the beautifulsoup4, spotipy, and requests libraries are installed and up-to-date. Now, you're ready to run the script.

## Usage

Open a terminal or command prompt and navigate to the directory containing the main.py file.
Execute the script using the following command:
When prompted, enter the desired date in the format YYYY-MM-DD (e.g., 2021-10-01).
Follow the instructions provided by Spotipy to authenticate your Spotify account in your web browser.
Once authenticated, the script will scrape the Billboard Hot 100 chart for the specified date, search Spotify for the songs, and create a new playlist containing the songs.
