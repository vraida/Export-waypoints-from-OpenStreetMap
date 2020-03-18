### The Goal
Export desired data from OpenStreetMap (OSM) as a .csv file with a list of geographic coordinates (longitude/latitude).
The following example shows how I exported coordinates of a railway between Wien and Retz, which I needed as a reference path for the dynamic time warping (DTW) algorithm.
Note: There is no OSM relation that would start in Wien Hbf and terminate in Retz. We thus export a larger relation (here, Wien Meidling &rarr; Znojmo), which we can later cut off.

### 1. OpenStreetMap: Find the Data ID
Go to OpenStreetMap (OSM) https://www.openstreetmap.org/ and select your data (e.g., a particular relation) to find out its ID. See Fig. 1&#8211;3.<br>
<kbd><img src="https://github.com/vraida/Export-waypoints-from-OpenStreetMap/tree/master/.data/step1.png" alt="step1" width=300><br>&nbsp;<br>Fig. 1: Right-click on an element of interest<br> and chose "Query features."<br>&nbsp;</kbd>
<kbd><img src="https://github.com/vraida/Export-waypoints-from-OpenStreetMap/tree/master/.data/step2.png" alt="step2" width=300><br>&nbsp;<br>Fig. 2: Select an appropriate relation.<br>&nbsp;<br>&nbsp;</kbd>
<kbd><img src="https://github.com/vraida/Export-waypoints-from-OpenStreetMap/tree/master/.data/step3.png" alt="step3" width=300><br>&nbsp;<br>Fig. 3: Copy the relation ID (here: 4683240).<br>&nbsp;<br>&nbsp;</kbd>

### 2. Overpass Query: Export the Data
With a specific ID, we can query the OSM database using Overpass API https://wiki.openstreetmap.org/wiki/Overpass_API.
Overpass turbo https://overpass-turbo.eu is a convenient tool that visualizes the results of Overpass queries and allows us to export the queried data in various formats. See Fig. 4&#8211;6.<br>
<kbd><img src="https://github.com/vraida/Export-waypoints-from-OpenStreetMap/tree/master/.data/step4.png" alt="step4" width=300><br>&nbsp;<br>Fig. 4: Query the relation ID. The resulting<br>group must be recursively broken with (._;>;);<br>to be displayed. We want a single path con-<br>necting Wien and Retz. The relation, however,<br>contains additional features, e.g., railway<br>platforms.<br>&nbsp;<br>&nbsp;</kbd>
<kbd><img src="https://github.com/vraida/Export-waypoints-from-OpenStreetMap/tree/master/.data/step5.png" alt="step5" width=300><br>&nbsp;<br>Fig. 5: By selecting only way-elements with<br>tag "rail" we remove all unwanted objects.<br><br><br><br><br>&nbsp;<br>&nbsp;</kbd>
<kbd><img src="https://github.com/vraida/Export-waypoints-from-OpenStreetMap/tree/master/.data/step6.png" alt="step6" width=300><br>&nbsp;<br>Fig. 6: When we are sattisfied with the query,<br>we can export the queried data in .osm format:<br>[exported_railway.osm](uploads/e62647f14d686c52a0d60992fb9813b1/exported_railway.osm).<br><br><br><br>&nbsp;<br>&nbsp;</kbd>

### 3. osmconvert: Convert the Data to .csv
osmconvert https://wiki.openstreetmap.org/wiki/Osmconvert is a program that processes and converts OSM files.
With the following osmconvert command, we convert the source file ([exported_railway.osm](https://github.com/vraida/Export-waypoints-from-OpenStreetMap/tree/master/.data/exported_railway.osm)) into a .csv file ([railway.csv](https://github.com/vraida/Export-waypoints-from-OpenStreetMap/tree/master/.data/railway.csv)):
```shell
osmconvert exported_railway.osm --all-to-nodes --csv="@id @lon @lat" --csv-headline -o="railway.csv"
```
The exported .csv file has three columns (node id, longitude, latitude) and contains a header line.
The option "--all-to-nodes" is important to convert all elements (in our case railway segments) into individual nodes (set of points).

### 4. Sorting Waypoints
The waypoints in the file railway.csv are sorted by node ID. However, as Fig. 7 shows, the ID order does not correspond to the order, in which we visit the points when traveling along the railway. We can sort the waypoints by manually selecting the starting point and then iteratively choosing the nearest neighbor as a next waypoint. See the script ```./script_sort-waypoints/sort_waypoints.py```. In this case, the starting point is the northernmost one.

<kbd><img src="https://github.com/vraida/Export-waypoints-from-OpenStreetMap/tree/master/.data/path_unordered.png" alt="fig7" width=250><br>&nbsp;<br>Fig. 7: Original, unsorted waypoints<br>([railway.csv](uploads/c9edae502750da1a1176ebbb4dd38ad7/railway.csv)).<br><br></kbd>
<kbd><img src="https://github.com/vraida/Export-waypoints-from-OpenStreetMap/tree/master/.data/path_ordered.png" alt="fig8" width=250><br>&nbsp;<br>Fig. 8: Waypoints after being sorted <br>([railway_sorted.csv](uploads/0432967de244201fb5399a8bbde223f4/railway_sorted.csv)).<br><br></kbd>




