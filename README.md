# Music Time Machine

A Python script generates a Spotify playlist containing the top 100 songs from a given date based on the Billboard Hot 100 chart. It uses the requests library to scrape song data from the Billboard website and the Spotipy library to create a Spotify playlist with the retrieved songs.


## Requirements

- A Spotify account
- A Spotify Client ID and Client Secret (obtainable by creating an application at https://developer.spotify.com/dashboard/)
- Python 3

## Obtaining Spotify Client ID and Client Secret

- In order to create a playlist in Spotify you must have an account with Spotify. If you don't already have an account, you can sign up for a free one here: http://spotify.com/signup/
- Once you've signed up/ signed in, go to the developer dashboard and create a new Spotify App:
- Fill in the form with your application details:
  - Application Name: Choose a name for your application. This can be anything you like, e.g., "Billboard Playlist Generator."
  - Application Description: Provide a brief description of your application. For example, "A script that generates Spotify playlists based on Billboard charts."
  - Application Website: You can leave this blank or provide a relevant URL, such as the GitHub repository link for your script.
  - Redirect URI: Enter "http://example.com" for now, as specified in the script. You can update this later if needed.
  - Review and accept the Developer Terms of Service, then click the "Create" button.
  - After creating the application, you'll be redirected to the application dashboard. Here, you'll find your Client ID and Client Secret.
  - Once you've created a Spotify app, copy the Client ID and Client Secret into the `main.py`
  - ![Information](https://github.com/GameDevMitchell/Music-Time-Machine/assets/146736445/68532953-1d70-488c-85aa-c86002767549)


## Install or upgrade required libraries

To install or upgrade the required libraries, use the following commands:
- `pip install --upgrade beautifulsoup4`
- `pip install --upgrade spotipy`
- `pip install requests`

These commands will ensure that the beautifulsoup4, spotipy, and requests libraries are installed and up-to-date. Now, you're ready to run the script.


## Installation

- Clone this repository to your local machine or download the main.py file.
- Update the `CLIENT_ID` and `CLIENT_SECRET` variables in the main.py file with your own values.
- (Optional) Update the `username` variable in the SpotifyOAuth object with your Spotify username.


## Usage

- Open a terminal or command prompt and navigate to the directory containing the main.py file.
- Execute the script using the following command: `python main.py`
- When prompted, enter the desired date in the format YYYY-MM-DD (e.g., 2021-10-01).
- Follow the instructions provided by Spotipy to authenticate your Spotify account in your web browser.
- ![Authorization](https://github.com/GameDevMitchell/Music-Time-Machine/assets/146736445/6e6b1828-9b66-4522-9390-00f5bc5b6db1)

- Once authenticated, the script will scrape the Billboard Hot 100 chart for the specified date, search Spotify for the songs, and create a new playlist containing the songs.
  <img width="425" alt="Screenshot 2024-03-16 132611" src="https://github.com/GameDevMitchell/Music-Time-Machine/assets/146736445/55a30eaa-9d7b-4cb9-9768-0dba5a5886c6">

