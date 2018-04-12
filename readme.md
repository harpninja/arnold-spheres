# Arnold Spheres
How to create a Maya 2018 scene using Python. The shaders are configured for Arnold render.

### Run the script in Maya
* Open the Script Editor.
* Switch tabs from MEL to Python.
* Paste the code into the window.
* Press the Execute button on the tool bar at the top of the window.

### Maya scene render configuration
* Add a 42 x 42 plane to the scene at the origin.
* Apply an aiStandardSurface to the plane and make it white.
* In the Render Settings choose Arnold Renderer.
* On the Arnold Render tab in Sampling set:
    * Camera (AA) = 8
    * Diffuse = 4
    * Specular = 2
* On the Arnold Render tab in Environment set:
    * Atmosphere to aiFog -> defaults
    * Background to aiSky -> defaults
* Place an Area Light at x = 0, y = 20, z = 0.  Rotate x = -90.
    * Change the light to be type aiAreaLight.
    * Colour = white.
* Add a camera

### Final generated image
![alt text](http://www.animatedcreations.net/images/arnoldspheres.jpg "Final image of Arnold rendered spheres")
