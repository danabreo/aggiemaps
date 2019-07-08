<img src="https://raw.githubusercontent.com/danielabreo/aggiemaps/master/logo.png" alt="AggieMaps Logo" height="70" >

# AggieMaps
A routing web application for the Texas A&amp;M Bus System.

## Welcome to AggieMaps

AggieMaps is an open source web application created to increase the usability of the Texas A&M Bus System.

The web app is written in Python, HTML, and JavaScript, 
and is hosted on the Google App Engine and Heroku.

Try it now! [AggieMaps](https://aggiemapsm.appspot.com)


## Getting Started

The following instructions give potential contributors insight to how AggieMaps
was created.

### coordinates.csv
This file contains the geographical coordinates of each bus stop.
Coordinates were collected manually using the [TAMU Transportation](http://transport.tamu.edu/busroutes/) website and [Google Maps](https://www.google.com/maps/).

| [Route Name] | [Latitude in Decimal Degrees] | [Longitude in Decimal Degrees] |
|:---:|:---:|:---:|

#### Coordinate Collecters
- [Michael Abreo](https://www.linkedin.com/in/michaelabreo/)
- [Alexander Labbane](https://www.instagram.com/alexlabbane/)

### routes.csv
This file contains the stops and timing information for each bus route.
Stops and times were collected manually using the [TAMU Transportation](http://transport.tamu.edu/busroutes/) website.

| [Route Name] |  |
|:---:|:---:|
| [Stop 1 Name] | [Minutes to Stop 2] |
| [Stop 2 Name] | [Minutes to Final Stop] |
| [Final Stop] |  |

     The coordinates and routes files are used to populate the graph representing the bus system 
     They provide a user-friendly interface for updating bus stop locations, routes, and timings
