#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2016 TUNE, Inc. (http://www.tune.com)
#  @version   $Date: 2016-07-07 12:45:28 PDT $

import pytz

from pytz_convert import (
    convert_bing_ads_tz,
    convert_tz_abbrev_to_tz_offset,
    convert_tz_abbrev_to_tz_seconds,
    convert_tz_hours_to_tz_offset,
    convert_tz_name_to_date_tz_abbrev,
    convert_tz_name_to_date_tz_offset,
    convert_tz_name_to_now_tz_abbrev,
    convert_tz_name_to_now_tz_offset,
    convert_tz_offset_and_date_to_tz_name,
    convert_tz_offset_to_tz_hours,
    convert_tz_offset_to_tz_minutes,
    parse_gmt_offset_timezone,
)


class TestLoggingMvIntegration():

    def test_tz_offset(self):
        tz_name = "US/Central"
        tz_abbrev = "PST"

        tz_offset = convert_tz_abbrev_to_tz_offset(tz_abbrev)
        assert(tz_offset)
        assert(tz_offset == '-0800')

        tz_offset = convert_tz_name_to_now_tz_offset(tz_name)
        assert(tz_offset)
        assert(tz_offset == '-0600')

        tz_abbrev = convert_tz_name_to_now_tz_abbrev(tz_name)
        assert(tz_abbrev)
        assert(tz_abbrev == 'CST')

        tz_offset = convert_tz_name_to_date_tz_offset(tz_name, str_date='2016-03-01')
        assert(tz_offset)
        assert(tz_offset == '-0600')

        tz_offset = convert_tz_name_to_date_tz_offset(tz_name, str_date='2016-03-30')
        assert(tz_offset)
        assert(tz_offset == '-0500')

    def test_tz_offset_to_tz_hours(self):
        tz_name = "US/Central"
        tz_offset = convert_tz_name_to_now_tz_offset(tz_name)
        assert(tz_offset)

        tz_hours = convert_tz_offset_to_tz_hours(tz_offset)
        assert(tz_hours)

        tz_minutes = convert_tz_offset_to_tz_minutes(tz_offset)
        assert(tz_minutes)

        tz_offset = convert_tz_hours_to_tz_offset(tz_hours)
        assert(tz_offset)

        tz_seconds = convert_tz_abbrev_to_tz_seconds('PST')
        assert(tz_seconds)

    def test_tz_name_to_now_tz_abbrev(self):
        tz_name = "US/Central"
        tz_abbrev = convert_tz_name_to_now_tz_abbrev(tz_name)
        assert(tz_abbrev)
        assert(tz_abbrev == 'CST')

        tz_abbrev = convert_tz_name_to_date_tz_abbrev(tz_name, str_date='2016-03-01')
        assert(tz_abbrev)
        assert(tz_abbrev == 'CST')

        tz_abbrev = convert_tz_name_to_date_tz_abbrev(tz_name, str_date='2016-03-30')
        assert(tz_abbrev)
        assert(tz_abbrev == 'CDT')

    def test_tz_offset_and_date_to_tz_name(self):
        tz_name, tz_offset = parse_gmt_offset_timezone(tz_gmt_offset_name='(GMT-08:00) Pacific Time')
        assert(tz_name)
        assert(tz_name == 'Pacific Time')
        assert(tz_offset)

        tz_name = convert_tz_offset_and_date_to_tz_name(tz_offset=tz_offset, str_date='2016-03-01')
        assert(tz_name)
        assert(tz_name == 'America/Los_Angeles')

        tz_name = convert_tz_offset_and_date_to_tz_name(tz_offset=tz_offset, str_date='2016-03-30')
        assert(tz_name)
        assert(tz_name == 'America/Anchorage')

    def test_tz_offset_and_date_to_tz_name_range(self):
        assert(pytz.country_timezones['IN'])

        for tz_offset_num in range(-11, 13):
            if tz_offset_num >= 0:
                tz_offset = "+{:02d}00".format(tz_offset_num)
            else:
                tz_offset = "-{:02d}00".format(abs(tz_offset_num))

            tz_name = convert_tz_offset_and_date_to_tz_name(tz_offset=tz_offset, str_date='2016-03-01')
            assert(tz_name)

    def test_convert_bing_ads_tz(self):
        tz_name = convert_bing_ads_tz('AbuDhabiMuscat')
        assert(tz_name)
        assert(tz_name == 'Asia/Dubai')
