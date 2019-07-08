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
| **[Initial Stop]** | **[Minutes to Stop 1]** |
| **[Stop 1 Name]** | **[Minutes to 2 Stop]** |
| **[Stop 2 Name]** | **[Minutes to Initial Stop]** |
| **[Initial Stop]** |  |

     The coordinates and routes files are used to populate the graph representing the bus system 
     They provide a user-friendly interface for updating bus stop locations, routes, and timings
     
### verifydata.py
This python script checks the coordinates.csv and routes.csv files for correctness.
It detects extraneous bus stops, omitted bus stops, and duplicate coordinates.

#### To check your changes
 - Please make sure you use `Python 3.x.`, `Python 2.x` is not supported currently.
 - Place the coordinates.csv, routes.csv, and verifydata.py files in the same directory.
 - Use `Python3` to run verifydata.py.
 
 ## Program Flow
 1. User enters starting and ending location
 2. Program finds the first and second closest bus stops to the starting and ending location
 3. Dijkstra's shortest-path algorithm is used to find 4 shortest routes:
       - stop closest to starting point  :arrow_right:  stop closest to ending point
       - stop 2nd closest to starting point  :arrow_right:  stop closest to ending point
       - stop closest to starting point  :arrow_right:  stop 2nd closest to ending point
       - stop 2nd closest to starting point  :arrow_right:  stop 2nd closest to ending point
 4. Program returns the best path as a JSON object
