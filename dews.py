import os
import sys

from dvbobjects.PSI.PAT import *
from dvbobjects.PSI.NIT import *
from dvbobjects.PSI.SDT import *
from dvbobjects.PSI.PMT import *
from dvbobjects.PSI.TDT import *
from dvbobjects.PSI.EIT import *
from dvbobjects.DVB.Descriptors import *
from dvbobjects.MPEG.Descriptors import *
from dvbobjects.MHP.AIT import *
from dvbobjects.MHP.Descriptors import *
from dvbobjects.DEWS.INFOSECTION import *
from dvbobjects.DEWS.MESSAGE import *

#
# Shared values
#
i = 0
indews_pmt_pid =  1037

for arg in sys.argv: 
    if i == 0 :
		v_original_network_id = arg
	elif i == 1 :
		v_disaster_code = arg
	elif i == 2 :
		v_latitude = arg
	elif i == 3 :
		v_longitude = arg
	elif i == 4 :
		v_message_total = arg
	elif i == 5 :
		v_destination_transport_stream_id = arg
	elif i == 6 :
		v_severity_code = arg	
	elif i == 7 :
		v_message = arg	

	i = i + 1


ewsmsgtable = [
    emergency_message_section
    (
	original_transport_stream_id = v_original_network_id,
	disaster_code = v_disaster_code,
	latitude = v_latitude,
	longitude = v_longitude,
	message_total = v_message_total,
	
	emergency_message_loop = [
	    emergency_message_loop_item
	    (
		destination_transport_stream_id = v_destination_transport_stream_id, 
		severity_code = v_severity_code,
		message = v_message,
	    ),
	],	
	version_number = 1, # you need to change the table number every time you edit, so the decoder will compare its version with the new one and update the table
    section_number = 0,
    last_section_number = 0,
    ),
]

#
out = open("./ewsmessage.sec", "wb")
out.write(ewsit.pack())
out.close
out = open("./ewsmessage.sec", "wb") # python   flush bug
out.close
os.system('/usr/local/bin/sec2ts ' + str(indews_pmt_pid) + ' < ./ewsmessage.sec > ' + SITemp + '/ewsmessage.ts')
