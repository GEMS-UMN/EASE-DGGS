© Regents of the University of Minnesota. All rights reserved.

This software is released under an Apache 2.0 license. Further details about the Apache 2.0 license are available in the license.txt file.

# EASE-DGGS
EASE-DGGS is a discrete global grid system (DGGS) that based upon Version 2 of the [global Equal-Area Scalable Earth (EASE) Grids](https://nsidc.org/data/user-resources/help-center/guide-ease-grids). The rational for developing the EASE-DGGS library is described in the publication titled: ['EASE-DGGS: a hybrid discrete global grid system for Earth sciences'](https://doi.org/10.1080/20964471.2021.2017539) published in the journal [Big Earth Data](https://www.tandfonline.com/journals/tbed20). 

EASE Grid was originally designed as an early discrete global grid system. From the start it was hierarchical in nature and consisted of raster of various nested resolutions. The main innovation of EASE-DGGS is to replace the cooridnate pair (e.g. longitude, latitude; northings, easting) traditional used to identify spatial locations, with using grid indexex to indicate spatial location. This library contains code to convert traditional WGS84 cooridinate pairs (longitude, latitude) into the Grid ID of the DGGS cell that contains the point. The Grid ID returned will depend on the desired spatial resolution defined in the following specification: 

## EASE-DGGS specifications

We standardize the data to the coordinate system described below and offer multiple spatial resolution choices.

- Coordinate Reference System: EPSG:6933, WGS 84 / NSIDC EASE-Grid 2.0 Global https://epsg.io/6933.
- Resolution at different levels is described in the table below:

| level   | resolution | 
| ------- | -----------|
| 0       | 36 km      |
| 1       | 9 km       |
| 2       | 3 km       |
| 3       | 1 km       |
| 4       | 100 m      |
| 5       | 10 m       |
| 6       | 1 m        |

## Setup
EASE-DDGS is now installable as a library! To install the library, simply:
   + clone/pull the repo to your local environment
   + cd into the repo directory
   + `pip install .`

Once completed, you will now have the package `easedggs` in your current python environment. 

To uninstall the library, simply:
   + `pip uninstall easedggs`

## Usage
Once the package has been installed, you can use the functions as you would any other package. For example:

```
# load the library as you would any other library
from easedggs.dggs.grid_addressing import geos_to_grid_ids, grid_ids_to_geos, grid_ids_to_ease
```

To faciliate reuse and reproducability, the grid and levels specification parameters have been moved to external JSON files.
   + Grid specifications are in: `src\easedggs\grid_spec.json`
   + Level specifications are in: `src\easedggs\levels_spec.json`

### converting to/from geographic coordinates to Grid IDs 
One of the main uses of the library is to transform from geographic coordinates to Grid IDs, and to tranform back to geographic cooridnated using Grid IDs. This process is straightforward with the EASE-DGGS library

#### Transforming from Geographic Cooridnates to EASE-DGGS Grid IDs using `geos_to_grid_ids`
```
# load the library as you would any other library
from easedggs.dggs.grid_addressing import geos_to_grid_ids
geos_to_grid_ids(coords_lon_lat=[(-178.81327800830186, 8)])
# {'success': True, 'result': {'data': ['L0.174003']}}

geos_to_grid_ids(coords_lon_lat=[(-178.81327800830186, 8)], level= 4)
# {'success': True, 'result': {'data': ['L4.174003.30.02.00.54']}}

geos_to_grid_ids(coords_lon_lat=[(-178.81327800830186, 8)], level= 6)
# {'success': True, 'result': {'data': ['L6.174003.30.02.00.54.40.80']}}
```

#### Transforming from EASE-DGGS Grid IDs to Geographic Coordinates using `grid_ids_to_geos`
```
from easedggs.dggs.grid_addressing grid_ids_to_geos
grid_ids_to_geos(grid_ids = ['L0.174003'])
# {'success': True, 'result': {'data': [(-178.69294605809128, 8.07563685558577)]}}

grid_ids_to_geos(grid_ids = ['L4.174003.30.02.00.54'])
# {'success': True, 'result': {'data': [(-178.81275933609956, 7.9999873507686745)]}}

grid_ids_to_geos(grid_ids = ['L6.174003.30.02.00.54.40.80'])
# {'success': True, 'result': {'data': [(-178.81327282157676, 7.9999992318131845)]}}
```


To go from 
## Background information the EASE DGGS
This section is intended to provide an understanding of the EASE-DGGS. The EASE-DGGS is a hybrid Discrete Global Grid System. Much of what is below is now described in the publication [EASE-DGGS: a hybrid discrete global grid system for Earth sciences](https://dx.doi.org/10.1080/20964471.2021.2017539).

### Uber H3
An early contender, due to:
 + Sizeable user community
 + Satisfied most/all of the OGC Criteria for DGGS
 + Hexagon's make some applications (pest dispersion, market navigation)

Disadvantages:
 + Lack of support in existing geospsatial software (e.g. can't import layer with native H3 'projection')
 + Existing spatial algorythims all need reworked for hexagons

Fatal Flaw for GEMS:
 + Lack of perfect child containment (mathematics of resampling to high resolutions are not invertable)

### EASE Grid v2
Advantages:
 + Used for to store several data for several satellite missions
 + a projected grid: (distorions easy to understand)
 + Maleable to GEMS needs (mainly a
 + EPSG code makes the coordinate system for the grid compatable with existing GIS

Disadvantages
 + Componets exist for a hierarchical system, but noone yet applied a DGGS framework (e.g. no one has yet specified how to grid cells numbered/filled/identified


 #### Grid Specs
![Schematic of the nesting heirarch](https://nsidc.org/sites/nsidc.org/files/images/ease-grid%202_0%20perfect%20nesting.png)

this indicates that the aperature is not fixed, so is something of a hybrid. 36 to 9: aperature 4, 9 to 3: aperature 3: 3 to 1: aperature 3

if I wanted 1km to 100 m: aperature 10; 100 m to 10 m: aperature 10

 ### Options for Cell Naming/ordering conventions

##### Address/Indexing Scheme
The bit-mask range idea can be modified, to form a more human readable. The idea would be, address/index location. Again, some specification of Row or Column ordering woudl be required, but the basic scheme would be something like:

LX.RRRCCC.RC.RC.RC.RC.RC.RC

Here:
 + L = shorthard for 'level'
 + X = integer indicating level of heirarchy;
 + R = Row index;
 + C = Column index.
The `.` is used to make it human readable, and also tells you what the row/column index is for a given level. Using a 0-9 numbering scheme also means that the addressing is compact, single digit for each Level 1-6.

The Address-Indexing Noation is represented in the figure below.

![Address-Index_Scheme Figure](./docs/images/Address-Index_Scheme.png)

This scheme is extensible, meaning that the Level 6 need not be the 'final' resolution suppoted. Level 6 corresponds to ~1 m resolution. Aperature 10 on 1 m would result in cells ~ 0.1 m, or 10 cm. Though convenient, most geospatial professionals will not be equiped with survey grade, precisions GPS kit.

 ##### Address-Indexing mapped to bit-mask notation
 One idea is to use 64 bit memory space and partition it to indicate parent/child relationships. Efficient on memory space, but not so user friendly. Here, some version of column or row major partitioning whould be implmeneted. Thinknig of working in row major order, a partent would


| Bit Range | Type  | Description |
| --- | --- | --- |
| 0 - 6 | Bit flag  |  indicating level of heriarcy.  |
| 7 - 15 | Integer |  indicating Level 0 row.  |
| 16 - 25 | Integer |  indicating Level 0 column.  |
| 26 - 29 | Integer |  indicating Level 1 pixel location in Level 0 cell. Can map the index to product of level 1 row * column   |
| 30 - 33 | Integer |  indicating Level 2 pixel location in Level 1 cell.  Can map the index to product of level 2 row * column |
| 34 - 37 | Integer |  indicating Level 3 pixel location in Level 2 cell. Can map the index to product of level 3 row * column  |
| 38 - 45 | Integer |  indicating Level 4 pixel location in Level 3 cell. Can map the index to product of level 4 row * column  |
| 46 - 52 | Integer |  indicating Level 5 pixel location in Level 4 cell. Can map the index to product of level 5 row * column  |
| 53 - 59 | Integer |  indicating Level 6 pixel location in Level 5 cell.  Can map the index to product of level 6 row * column |
| 60 - 63 | -  | unused |


#### From lon,lat to EASE-DGGS ID and back again

Converting from real-world geographic coordinate pair (lon, lat) to EASE-DGGS ID and back is the first step needed to operationalize the EASE-DGGS. In simple terms, there are two transforms involved in this operation. These overview steps are outlined in the figure below. Going from geograhpic cooridnates first involves transforming into EASE Grid v2 coordidnates. These coordinates are are projected and the basic units are Eastings, Norhtings which are measured in meters. From there, the second step is to recenter that grid, and transform to a smaller number space. This transformation made it easier to work with the data, as the large numbers involved in EASE Grid made the book keeping and computation harder to keep track of.

![Overview of Geo to Grid image](./docs/images/geo_to_grid_id_functions.png)

Going from EASE-DGGS ID to geographic cooridnates is basically the reverse. Since the cell ID is basically a positional index, its simply a matter of converting that index to cooridnate pair on the EASE-DGGS (x_grid, y_grid), reverse transforming that to EASE grid cooridnates (x_ease, y_ease), and then converting those to lon, lat (x_lon, y_lat).

Note, going from geograhic coordinates to EASE-DGGS ID and then back will **not** produce identicle results. Upon completing the cycle, the cooridnate that is returned represents the centroid of the grid cell. This is a property of Discrete Global Grid Systems, and it requires a user to think about the positional accuracy of their data. While it is possible to describe _relative_ spatial accuracy to the nano-scale or beyond, current state of the art in GPS technology effectivley only allows _absolute_ locational accuracy down to about the centimeter scale.


If not, this seems like a spatial recursion problem. Find the intersection of supplied cooridnates in L0 cells. Next, find interscetion of point in L1 children cells of the specific L0 cell. Next find interscetion of point in L2 children cells of the specific L1 cell. Recurse until specific cell location at desired Level is identified.

Code for the schematic with grid ID parsing and

test2

![geo to grid id algorythm](./docs/images/GridID_to_geo_algorythm.png)
