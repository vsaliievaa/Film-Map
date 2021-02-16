# Film-Map
Film-Map is a set of Python functions which help a user to generate an HTML map with 10 locations around the user's place on the globe, where movies were filmed.
## Installation
To generate your own map, install the code and all the files via GitHub and run it on your computer.
## Usage
To generate a map, first enter the year you would like to have a map for, then - your latitude and longitude (format: lat, lon), and press Enter.
<img align="left" src="https://drive.google.com/file/d/1eY7IlhZzcMuE6syEQQIYPgJny61o0KWO/view?usp=sharing">
While the map is being generated, you'll see the corresponding message. Generation might take up to 3 minutes.
<img align="left" src="https://drive.google.com/file/d/1FgcKYfadhmoFtsrveSFDQ16BNITm90Za/view?usp=sharing">
When the map is ready, you'll be informed about it and invited to have a look at an HTML-file, which you can open in your browser by clicking twice on a generated file (filmmap.html in the example).
<img align="left" src="https://drive.google.com/file/d/1ErBNlpB2q8HX-bno2J0JhKi9gw8iRCff/view?usp=sharing">
Your map includes three layers - you can switch them on and off via the layer control panel in the right upper corner of the map. To see what each layer is responsible for, choose a layer and click on an icon - you'll see either a movie title or a distance to the location it was filmed at.
<img align="left" src="https://drive.google.com/file/d/1jNIfSdb2kqKeQPLBlrztuADxqXxMAb_X/view?usp=sharing">

*Theoretical background and formulas for calculating haversine and distances between the two points on the Earth were taken from Wikipedia ([here](https://en.wikipedia.org/wiki/Haversine_formula#:~:text=The%20haversine%20formula%20determines%20the,and%20angles%20of%20spherical%20triangles.)) and interpreted for Python.
## License
[MIT](https://choosealicense.com/licenses/mit/)
