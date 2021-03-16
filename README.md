# IP4

## Author

[Hunja Tom](https://github.com/BwanaQ)

## Description

This project is a Flask application that consumes a [Random quote base](http://quotes.stormconsultancy.co.uk/random.json) and allows users to login, create blogs and have them reviewed through comments and votes.
A live demo is deployed [Here](https://hunja.herokuapp.com)

## User Stories

The user would like to.... :

- Log in
- Select the ones they prefer
- See the top news articles from that news source
- See the image, description and time the news article was created
  Click on an article and read it fully from the news source

## Installation / Setup instruction

#### The application requires the following installations to operate

- python3.6
- virtualenv
- pip

#### Set Up

- Open Terminal {Ctrl+Alt+T}

- git clone `https://github.com/BwanaQ/uhondo.git`

- cd into the uhondo folder

- create a virtual environment using the command `$ virtualenv venv`

- enter the virtual environment by typing `source venv\bin\activate`

- install all dependencies using `pip install -r requirements.txt`

- create an instance/config.py file
- assign your news api key to the variable ARTICLE_API_KEY

### Running the Application

- To run the application, open the cloned file in terminal and run the following commands:

        $ chmod +x run.py
        $ ./run.py

- To run tests for the application
  $ python3 article_test.py
  $ python3 source_test.py

## Behaviour Driven Development

| Behaviour | Input | Output |
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display news sources | **On page load** | List of various news sources is displayed in cards |
| Display articles from a news source | **Click a news source** | Redirected to a page with articles from the source |
| Display the preview of an article | **On page load** | Each article displays an image,description and publication date |
| To Read an entire article | **Click an article** | Redirected to the news source's site to read the entire article |

## Technologies Used

- python3.6

## Known Bugs

- There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information

If you have any question or contributions, please email me at [thunjawax@gmail.com]

## License

- _MIT License:_
- Copyright (c) 2021 **Tom Hunja**
