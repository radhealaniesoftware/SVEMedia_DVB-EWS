#! /usr/bin/env python

# This file is part of the dvbobjects library.
# 
# Copyright � 2004, Lorenzo Pallara
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import string
from dvbobjects.MPEG.Section import Section
from dvbobjects.utils import *

######################################################################
class ews_info_section(Section):

    table_id = 0x80
    section_max_size = 1024

    def pack_section_body(self):
    
        # pack program_loop_item
        pl_bytes = string.join(
            map(lambda x: x.pack(),
                self.ewsit_loop),
            "")

        self.table_id_extension = 0x01
	self.private_indicator = 0

        fmt = "!%ds" % (len(pl_bytes))
        return pack(fmt,
            pl_bytes
            )

######################################################################
class ews_info_loop_item(DVBobject):

    """
	expects the following variable
	
	    ews_serverid
	    ews_country_id
	    transport_stream_id
	    ews_version_no
	    ews_owner_descriptor  - MAX 100 chars 
	 
    """

    def pack(self):
    
        # pack program_loop_item
        fmt = "!HHHHB%ds" % len(self.ews_owner_descriptor)
	return pack(fmt,
	    self.ews_serverid,
	    self.ews_country_id,
	    self.transport_stream_id,
	    self.ews_version_no,
	    len(self.ews_owner_descriptor),
	    self.ews_owner_descriptor,
	)




