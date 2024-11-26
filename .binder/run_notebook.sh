#!/bin/bash
# Parse query parameters from Binder URL and inject them into the notebook

# Example: ?lat=23.45&lng=4.35
QUERY_STRING=$(echo $JUPYTERHUB_SERVICE_PREFIX | sed 's/.*?//')
LAT=$(echo $QUERY_STRING | grep -oP '(?<=lat=)[^&]*')
LNG=$(echo $QUERY_STRING | grep -oP '(?<=lng=)[^&]*')

# Set defaults if parameters are missing
LAT=${LAT:-0.0}
LNG=${LNG:-0.0}

# Run Papermill to execute the notebook with the parameters
papermill temp_ann_timeseries.ipynb temp_ann_timeseries_output.ipynb -p lat $LAT -p lng $LNG

# Open the executed notebook
jupyter notebook temp_ann_timeseries_output.ipynb