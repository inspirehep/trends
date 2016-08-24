# -*- coding: utf-8 -*-
#
# This file is part of inspirehep.
# Copyright (C) 2016 CERN.
#
# inspirehep is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# inspirehep is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with inspirehep; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Project utilities."""

from werkzeug.routing import BaseConverter
from datetime import datetime


def print_iso_date(obj):
    """Print given date to ISO8601 without timezone."""
    if isinstance(obj, list):
        return [print_iso_date(e) for e in obj]
    return obj.isoformat()


def parse_iso_date(str):
    """Parse given date to ISO8601 without timezone."""
    try:
        return datetime.strptime(str, '%Y-%m-%dT%H:%M:%S.%f')
    except:
        return datetime.strptime(str, '%Y-%m-%dT%H:%M:%S.%fZ')


class DatetimeConverter(BaseConverter):
    """Datetime/url converter."""

    def to_python(self, value):
        return parse_iso_date(value)

    def to_url(self, value):
        return BaseConverter.to_url(self, str(value))