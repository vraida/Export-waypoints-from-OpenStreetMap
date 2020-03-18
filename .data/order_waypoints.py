import numpy as np
import pandas as pd

# Initialization
path_in  = pd.read_csv('railway.csv', sep='\t')  # Load the unsorted path
mask_in  = np.full(path_in.shape[0], True)       # Remaining unused rows in the original path
path_out = pd.DataFrame({'lat':[], 'lon':[]})    # Sorted path

# Identify the first point (check manually)
idx = path_in['@lat'].idxmax()                   # In this case, the first point is the northernmost one
mask_in[idx] = False                             # We mark that point as used...
previous_lat = path_in['@lat'].loc[idx]          # ...and initialize the "previous" latitude and longitude
previous_lon = path_in['@lon'].loc[idx]

# Add the first point to the output path
path_out = path_out.append( pd.DataFrame({'lat':[previous_lat], 'lon':[previous_lon]}), ignore_index=True )

# Iterate all remaining points. Always select the nearest neighbor.
while np.any(mask_in):
    distances = np.sqrt( (path_in[mask_in]['@lat']-previous_lat)**2 + (path_in[mask_in]['@lon']-previous_lon)**2 )
    idx = distances.idxmin()
    mask_in[idx] = False
    previous_lat = path_in['@lat'].loc[idx]
    previous_lon = path_in['@lon'].loc[idx]
    path_out = path_out.append( pd.DataFrame({'lat':[previous_lat], 'lon':[previous_lon]}), ignore_index=True )

# Save the resulting path
path_out.to_csv('railway_sorted.csv')
