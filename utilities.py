import cdsapi

def retrieve_data(KEY, variable, date_range, lat, lng):
    # Define the URL for the CDS API
    URL = 'https://cads-mini-cci1.copernicus-climate.eu/api'

    # Define the dataset and request parameters
    dataset = "test-adaptor-arco"
    request = {
        "variable": [
        variable,  # Variable to retrieve
        ],
        "date": [date_range[0] + "/" + date_range[1]],  # Date range for the data
        "location": {"longitude": lng, "latitude": lat},  # Location coordinates
        "data_format": "netcdf"  # Format of the retrieved data
    }

    # Define the filename for the data download
    timeseries_file = f"{variable}_{date_range[0]}_{date_range[1]}_{lat}_{lng}.nc"

    print(request)
    print(timeseries_file)

    # Initialize the CDS API client with the URL and API key
    client = cdsapi.Client(url=URL, key=KEY)

    # Retrieve the data from the CDS API and save it to the specified file
    client.retrieve(dataset, request, timeseries_file)

    print("Retrieving data in to: ", timeseries_file)

    return timeseries_file

def cumulative_days_in_months():
    # Number of days in each month for a leap year
    days_in_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Calculate the cumulative days for each month
    cumulative_days = []
    total_days = 0
    for days in days_in_months:
        total_days += days
        cumulative_days.append(total_days)

    return cumulative_days