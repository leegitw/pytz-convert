#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2016 TUNE, Inc. (http://www.tune.com)
#  @version   $Date: 2016-07-07 12:45:28 PDT $

import sys
from pprintpp import pprint
import pytz

from pytimezone_convert import (
    convert_tz_abbrev_to_tz_offset,
    convert_tz_abbrev_to_tz_seconds,
    convert_tz_name_to_now_tz_abbrev,
    convert_tz_name_to_date_tz_abbrev,
    convert_tz_name_to_now_tz_offset,
    convert_tz_offset_and_date_to_tz_name,
    convert_tz_offset_to_tz_hours,
    convert_tz_offset_to_tz_minutes,
    convert_tz_hours_to_tz_offset,
    parse_gmt_offset_timezone
)


def main():
    tz_name = "US/Central"
    tz_abbrev = "PST"

    tz_offset = convert_tz_abbrev_to_tz_offset(tz_abbrev)
    pprint(tz_offset)

    tz_offset = convert_tz_name_to_now_tz_offset(tz_name)
    pprint(tz_offset)

    tz_abbrev = convert_tz_name_to_now_tz_abbrev(tz_name)
    pprint(tz_abbrev)

    tz_hours = convert_tz_offset_to_tz_hours(tz_offset)
    pprint(tz_hours)

    tz_minutes = convert_tz_offset_to_tz_minutes(tz_offset)
    pprint(tz_minutes)

    tz_offset = convert_tz_hours_to_tz_offset(tz_hours)
    pprint(tz_offset)

    tz_seconds = convert_tz_abbrev_to_tz_seconds('PST')
    pprint(tz_seconds)

    tz_seconds = convert_tz_abbrev_to_tz_seconds('PDT')
    pprint(tz_seconds)

    tz_abbrev = convert_tz_name_to_now_tz_abbrev(tz_name)
    pprint(tz_abbrev)

    tz_abbrev = convert_tz_name_to_date_tz_abbrev(tz_name, str_date='2016-03-01')
    pprint(tz_abbrev)

    tz_abbrev = convert_tz_name_to_date_tz_abbrev(tz_name, str_date='2016-03-30')
    pprint(tz_abbrev)

    google_adwords_tz_name, tz_offset = parse_gmt_offset_timezone(
        tz_gmt_offset_name='(GMT-08:00) Pacific Time'
    )
    print("{}, {}".format(google_adwords_tz_name, tz_offset))

    tz_names = convert_tz_offset_and_date_to_tz_name(
        tz_offset=tz_offset,
        str_date='2016-03-01'
    )
    print("{}, {}".format(tz_names, tz_offset))

    tz_names = convert_tz_offset_and_date_to_tz_name(
        tz_offset=tz_offset,
        str_date='2016-03-30'
    )
    print("{}, {}".format(tz_names, tz_offset))

    pprint(pytz.country_timezones['IN'])

    for tz_offset_num in range(-11, 13):
        if tz_offset_num >= 0:
            tz_offset = "+{:02d}00".format(tz_offset_num)
        else:
            tz_offset = "-{:02d}00".format(abs(tz_offset_num))

        tz_names = convert_tz_offset_and_date_to_tz_name(
            tz_offset=tz_offset,
            str_date='2016-03-01'
        )
        print("{}, {}".format(
            tz_offset,
            tz_names
        ))

if __name__ == '__main__':
    sys.exit(main())
