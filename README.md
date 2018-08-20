# DB-WIN
Libraries to Access and Populate Database Backend for a Revamped ChipList

# Goals
Establish a series of tools to suppor the creation, maintenance, and interaction with
the large quanities of ChipWIN data that's out there.

# Libraries
* bc_scraper - methods to scrape relevant data from bandcamp
* gs_scraper - methods to scrape relevant data from the ChipWIN Google Sheet
* sc_scraper - methods to scrape relevant data from SoundCloud
* cwdb_io - methods to interacte with the cwdb MySQL database

## Music Related Scraping Overview
The goal here is, on a broad level, to give the scraper a set of tags to hunt across, and then pull all the data we can without being rude.
Important data includes:
* albums
    * title
    * artist
    * artist website
    * release date
    * list of tracks [eventual DB link]
    * tags
* tracks
    * title
    * artist
    * artist website
    * release date
    * tags
    * lyrics

## "Map" Related Scraping Overview
Chipmom does an assload of work maintaining a list of artists, visualists, and venues and relevent information that would be useful for the
community. Our software should look at the contents of the information she provides - and pull that information into the database and link it
against albums, tracks, etc for one big beautiful picture.
* artists
* labels
* venues

#Running Tests
`python -m unittest test\gs_scraper_tests.py`

#Dependencies
 

