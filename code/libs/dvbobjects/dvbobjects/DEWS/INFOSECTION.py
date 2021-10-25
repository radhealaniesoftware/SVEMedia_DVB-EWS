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


#emergency_info_section{
# descriptor_tag
# descriptor_length
# transport_stream_id
# for (i=0; i<N; i++){
#     country_code
#     region_code
#     location_code
#     disaster_code
#     priority
#     message
#   }
# }

"""
emergency_info_section{
   descriptor_tag
   descriptor_length
   for (i=0; i<N; i++){
         server_id
         location_code
         transport_stream_id
         version
         owner_descriptor
      }
   }
"""

import string
from dvbobjects.MPEG.Section import Section
from dvbobjects.utils import *

######################################################################
class emergency_info_section(Section):

    table_id = 0x80
    section_max_size = 1024

    def pack_section_body(self):
    
        # pack program_loop_item
        pl_bytes = string.join(
            map(lambda x: x.pack(),
                self.ewsit_loop),
            "")

        self.table_id_extension = 0x01
		self.private_indicator = 1

        fmt = "!%ds" % (len(pl_bytes))
        return pack(fmt,
            pl_bytes
            )

######################################################################
class emergency_info_loop_item(DVBobject):

    """
expects the following variable
	original_network_id
    transport_stream_id
    version
    owner_descriptor - MAX 100 chars 
    """

    def pack(self):
    
        # pack program_loop_item
        fmt = "!HHHB%ds" % len(self.owner_descriptor)
	return pack(fmt,
	    self.original_network_id,
	    self.transport_stream_id,
	    self.version,
	    len(self.owner_descriptor),
	    self.owner_descriptor,
	)




