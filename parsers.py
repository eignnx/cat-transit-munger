from __future__ import annotations

import datetime
from collections import OrderedDict, namedtuple
import dateutil.parser


def date(txt: str):
    ymd = txt[:4], txt[4:6], txt[6:]
    year, month, day = map(int, ymd)
    return datetime.datetime(year, month, day)


def boolean(txt: str):
    return bool(int(txt))


def time(txt: str):
    return dateutil.parser.parse(txt).time()


class RowParser:
    def __init__(self, tbl_name: str, **parsers):
        col_names = parsers.keys()
        self.schema = namedtuple(tbl_name, col_names)
        self.parsers = parsers

    def parse_row(self, data: OrderedDict) -> tuple:
        parsers = self.parsers.items()
        triples = ((key, data[key], parser) for (key, parser) in parsers)
        kwargs = {key: parser(val) for key, val, parser in triples}
        return self.schema(**kwargs)


stop = RowParser(
    "Stop",
    stop_id=int,
    stop_name=str,
    stop_lat=float,
    stop_lon=float,
    location_type=int,
)

calendar_date = RowParser(
    "CalendarDate",
    date=date,
    service_id=int,
    exception_type=int,
)

trip = RowParser(
    "Trip",
    trip_id=int,
    route_id=int,
    service_id=int,
    trip_headsign=str,
    block_id=int,
    shape_id=int,
)

stop_time = RowParser(
    "StopTime",
    stop_id=int,
    departure_time=time,
    stop_sequence=int,
    shape_dist_traveled=float,
)

shape = RowParser(
    "Shape",
    shape_id=int,
    shape_pt_sequence=int,
    shape_dist_traveled=float,
    shape_pt_lat=float,
    shape_pt_lon=float,
)

calendar = RowParser(
    "Calendar",
    service_id=int,
    monday=boolean,
    tuesday=boolean,
    wednesday=boolean,
    thursday=boolean,
    friday=boolean,
    saturday=boolean,
    sunday=boolean,
    start_date=date,
    end_date=date,
)

agency = RowParser(
    "Agency",
    agency_id=str,
    agency_name=str,
    agency_url=str,
    agency_timezone=str,
    agency_lang=str,
    agency_phone=str,
    agency_fare_url=str,
    agency_email=str,
)

route = RowParser(
    "Route",
    route_id=int,
    route_short_name=str,
    route_long_name=str,
    route_type=int,
)