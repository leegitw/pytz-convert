#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @namespace pytimezone-convert

__title__ = 'pytimezone-convert'
__version__ = '0.1.3'
__build__ = 0x000103
__version_info__ = tuple(__version__.split('.'))

__author__ = 'jefft@tune.com'
__license__ = 'Apache 2.0'

__python_required_version__ = (3, 0)

from .timezone_utils import (
    validate_tz_abbrev,
    validate_tz_name,

    convert_tz_abbrev_to_tz_hours,
    convert_tz_abbrev_to_tz_offset,
    convert_tz_abbrev_to_tz_seconds,
    convert_tz_hours_to_tz_offset,
    convert_tz_name_to_date_tz_abbrev,
    convert_tz_name_to_date_tz_offset,
    convert_tz_name_to_now_tz_abbrev,
    convert_tz_name_to_now_tz_offset,
    convert_tz_offset_and_date_to_tz_name,
    convert_tz_offset_to_now_tz_abbrev,
    convert_tz_offset_to_tz_hours,
    convert_tz_offset_to_tz_minutes,
    convert_tz_offset_to_tz_seconds,
    parse_gmt_offset_timezone
)
