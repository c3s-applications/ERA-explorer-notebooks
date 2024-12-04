import cdsapi
import pandas as pd

def retrieve_data(KEY, variable, date_range, lat, lng, do_retrieve=True):
    # Define the URL for the CDS API
    # URL = 'https://cads-mini-cci1.copernicus-climate.eu/api'
    URL = 'https://cds-dev-cci2.copernicus-climate.eu/api'

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
    if not do_retrieve:
        return timeseries_file

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

def truncate_data(var):
    # Create a range of the final hours of each year in the dataset
    start_year = var.valid_time.dt.year.min().item()
    end_year = var.valid_time.dt.year.max().item()

    final_hours = pd.date_range(f"{start_year}-12-31T23:00:00", 
                                f"{end_year}-12-31T23:00:00", 
                                freq="YE")

    # Filter only the years where the final hour is in the dataset
    valid_years = [dt.year for dt in final_hours if dt in var.valid_time]

    # Select data for those years
    var_truncated =var.sel(
        valid_time=var.valid_time.dt.year.isin(valid_years)
    )

    return var_truncated
