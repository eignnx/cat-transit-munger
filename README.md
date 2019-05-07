# cat-transit-munger
Munging functions for the Cat Transit bus line data.

The data can be found [here](https://www.cattransit.com/public-documents/) and downloaded directly from [this link](https://www.cattransit.com/GoogleTransit/Google%20Transit/GoogleTransitUpload.zip).

## Data Overview
The data seems to be a CSV export from a relational database. Each of the files in `./data` seem to have primary and foreign keys. Here is a summary of the current data:

```python
>>> from pprint import pprint
>>> import munge
>>> data = munge.read_data()
>>> pprint({file: len(data[file]) for file in data})
{'agency.txt': 1,
 'calendar.txt': 9,
 'calendar_dates.txt': 37,
 'routes.txt': 33,
 'shapes.txt': 65107,
 'stop_times.txt': 35449,
 'stops.txt': 1374,
 'trips.txt': 945}
>>> pprint(data["trips.txt"][5])
Trip(trip_id=744, route_id=8, service_id=2, trip_headsign='Outbound', block_id=7511, shape_id=7)
>>> pprint({route.route_long_name for route in data["routes.txt"]})
{'Abacus',
 'Allen Road Warehouses',
 'Cameron Street / HACC',
 . . .
 'Union Deposit / Hamilton Health Center',
 'Winding Hill Express'}
```

