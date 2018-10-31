This is Chris Lockard's ISE 589 project!

Within the ondemand_app directory, you will find all of the project files and dependancies:

- ondemand_app/
	|-- __init__.py
	|-- lib.py
	|-- track_data.csv
	|-- assets/
		|-- analytics_u.png
		|-- buildingq.jpg
		|-- favicon.ico


File info:

ondemand_app/
__init__.py - main project file, run this to start the web app and flask server
lib.py - library containing classes and functions to de-clutter the __init__.py file
track_data.csv - dataset that will be processed in the web app containing track data for up to one year back from the date in which it was created

assets/
analytics_u.png - logo image used in the header of the web app
buildingq.jpg - header background image
favicon.ico - icon for the browser tab (filename required by Dash)



Running the server:

To get started, run __init__.py in a command prompt. This will start the server on your machine and allow you to access it via localhost. Below is the expected output for running the file:

* Serving Flask app "__init__" (lazy loading)

* Environment: production
  
  WARNING: Do not use the development server in a production environment.

  Use a production WSGI server instead.

* Debug mode: on

* Restarting with stat

* Debugger is active!

* Debugger PIN: 108-637-091

* Running on http://127.0.0.1:8050/ (Press CTRL+C to quit)

Once prompted with the final line above, you will be able to reach the web app by typing http://127.0.0.1:8050/ into a web browser.



Thank you for your time, loved the course!

Chris Lockard