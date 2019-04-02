# BikeShareSystem
Bike Share Data
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, I have used data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. Main moto is to compare the system usage between three large cities: Chicago, New York City, and Washington, DC.

<h3>The Datasets</h3>
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

<li>Start Time (e.g., 2017-01-01 00:07:57)</li>
<li>End Time (e.g., 2017-01-01 00:20:53)</li>
<li>Trip Duration (in seconds - e.g., 776)</li>
<li>Start Station (e.g., Broadway & Barry Ave)</li>
<li>End Station (e.g., Sedgwick St & North Ave)</li>
<li>User Type (Subscriber or Customer)</li>

<h5>The Chicago and New York City files also have the following two columns:</h5>

<li>Gender</li>
<li>Birth Year</li>

Data for the first 10 rides in the new_york_city.csv file

<h3>Statistics Computed</h3>
You will learn about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. In this project, code is written to provide the following information:

<h5>#1 Popular times of travel (i.e., occurs most often in the start time)</h5>
<li>most common month</li>
<li>most common day of week</li>
<li>most common hour of day</li>
<h5>#2 Popular stations and trip</h5>
<li>most common start station</li>
<li>most common end station</li>
<li>most common trip from start to end (i.e., most frequent combination of start station and end station)</li>
<h5>#3 Trip duration</h5>
<li>total travel time</li>
<li>average travel time</li>
#4 User info
counts of each user type</li>
<li>counts of each gender (only available for NYC and Chicago)</li>
<li>earliest, most recent, most common year of birth (only available for NYC and Chicago)</li>

<h5>The Files</h5>
To answer these questions using Python, code is written using Python Script[bikeshare.py]. 

<h3>FILES NEEDED TO SUCCESSFULLY RUN THE TERMINAL APPLICATION</h3>

bikeshare.py,
chicago.csv,
new_york_city.csv,
washington.csv

All three csv files are zipped up in CsvData file. You may download and open up that zip file to execute the project work on your local machine.

<h3>TO EXECUTE THE BIKESHARE PROJECT</h3>
<li>You need tp have Python 2.7 or the upgraded version installed in your local machine </li>
<li>You need to install third part libraries such as Numpy and Pandas.</li>
<li>Run the bikeshare.py file and give inputs whenever it prompts to see the result of the computed statistics.</li>
