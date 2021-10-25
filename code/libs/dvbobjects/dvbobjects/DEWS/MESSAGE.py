#! /usr/bin/env python

# This file is part of the dvbobjects library.
# 
# Copyright 2004, Lorenzo Pallara
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

"""
emergency_message{
   transport_stream_id
   message_total
   for (i=0; i<N; i++){
      message      
      disaster_code
      location_code
      severity_code
      geo_location_code
      }     
}
"""

######################################################################
class emergency_message_section(Section):

    """
	expects the following variable
		original_network_id	- 2byte
		disaster_code		- 2byte
		latitude			- 1byte
		longitude			- 1byte
		message_total		- 2byte
    """

    table_id = 0x80
    section_max_size = 1024

    def pack_section_body(self):
    
        # pack program_loop_item
        pl_bytes = string.join(
            map(lambda x: x.pack(),
                self.emergency_message_loop),
            "")
		self.table_id_extension = 0x02
		self.private_indicator = 1

        fmt = "!HHHHB%ds" % (len(pl_bytes))
        return pack(fmt,
		    self.original_transport_stream_id,
			self.disaster_code,
    	    self.latitude,
    	    self.longitude,
    	    len(self.emergency_message_loop),
            pl_bytes
            )
            

class emergency_message_loop_item(DVBobject):

    """
	  expects the following variable
      destination_transport_stream_id		- 2byte
      severity_code							- 2byte
      message      							- 80byte
    """

    emergency_tag = 0x80
    
    def pack(self):

        # pack program_loop_item
        fmt = "!HHB%ds" % (len(self.ews_message), len(pl_bytes))
	return pack(fmt,
	    self.destination_transport_stream_id,
        self.severity_code,
	    len(self.ews_message),
	    self.ews_message,
	)


