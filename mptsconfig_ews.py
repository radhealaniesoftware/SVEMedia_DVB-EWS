#! /usr/bin/env python

#
# Copyright (C) 2008  Lorenzo Pallara, l.pallara@avalpa.com
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

import os

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
#from dvbobjects.DEWS.DISASTERCODETABLE import *
from dvbobjects.DEWS.INFOSECTION import *
from dvbobjects.DEWS.MESSAGE import *

#
# Shared values
#
indtv_transport_stream_id = 1 # demo value, an official value should be demanded to dvb org
indtv_transport_stream_id_test = 2

indtv_original_transport_stream_id = 1 # demo value, an official value should be demanded to dvb org

indtv1_service_id = 1 
indtv2_service_id = 2 
indtv3_service_id = 3
indtv4_service_id = 4
indtv5_service_id = 5
indtv6_service_id = 6
 
indtv1_pmt_pid = 1031
indtv2_pmt_pid = 1032
indtv3_pmt_pid = 1033
indtv4_pmt_pid = 1034
indtv5_pmt_pid = 1035
indtv6_pmt_pid = 1036


app1_ait_pid = 3000

dsmcc1_pid = 2003
dsmcc1_associate_tag = 0x0B
dsmcc1_carrousel_id = 1



aitpidlist = [
app1_ait_pid,
]


pmtpidlist = [
indtv1_pmt_pid,
indtv2_pmt_pid,
indtv3_pmt_pid,
indtv4_pmt_pid,
indtv5_pmt_pid,
indtv6_pmt_pid
]

indews_service_id = 7
indews_pmt_pid =  1037



SITemp = "./Temp/SITemp"

#
# Network Information Table
# this is a basic NIT with the minimum desciptors, OpenCaster has a big library ready to use
#

nit = network_information_section(
	network_id = 1,
        network_descriptor_loop = [
	    network_descriptor(network_name = "IND-TV",)
	],
	transport_stream_loop = [
	    transport_stream_loop_item(
		transport_stream_id = indtv_transport_stream_id,
		original_network_id = indtv_original_transport_stream_id,
		transport_descriptor_loop = [
		    service_list_descriptor(
			dvb_service_descriptor_loop = 
			[
			    service_descriptor_loop_item(
				service_ID = indtv1_service_id,
				service_type = 1, # digital tv service type
			    ),
			    service_descriptor_loop_item(
				service_ID = indtv2_service_id,
				service_type = 1, # digital tv service type
			    ),
			    service_descriptor_loop_item(
				service_ID = indtv3_service_id,
				service_type = 1, # digital tv service type
			    ),
			    service_descriptor_loop_item(
				service_ID = indtv4_service_id,
				service_type = 1, # digital tv service type
			    ),
			    service_descriptor_loop_item(
				service_ID = indtv5_service_id,
				service_type = 1, # digital tv service type
			    ),
			    service_descriptor_loop_item(
				service_ID = indtv6_service_id,
				service_type = 1, # digital tv service type
			    ),
			    #service_descriptor_loop_item(
			    #	service_ID = indtv6_service_id,
			    #	service_type = 1, # digital tv service type
			    #),
			    service_descriptor_loop_item(
				service_ID = indews_service_id,
				service_type = 128, # digital tv service type
			    ),
			],
		    ),
			logical_channel_descriptor(
			    lcn_service_descriptor_loop = [
					lcn_service_descriptor_loop_item(
						service_ID = indtv1_service_id,
						visible_service_flag = 1,
						logical_channel_number = 100,
					),
					lcn_service_descriptor_loop_item(
						service_ID = indtv2_service_id,
						visible_service_flag = 1,
						logical_channel_number = 200,
					),
					lcn_service_descriptor_loop_item(
						service_ID = indtv3_service_id,
						visible_service_flag = 1,
						logical_channel_number = 300,
					),
					lcn_service_descriptor_loop_item(
						service_ID = indtv4_service_id,
						visible_service_flag = 1,
						logical_channel_number = 400,
					),
					lcn_service_descriptor_loop_item(
						service_ID = indtv5_service_id,
						visible_service_flag = 1,
						logical_channel_number = 500,
					),
					lcn_service_descriptor_loop_item(
						service_ID = indtv6_service_id,
						visible_service_flag = 1,
						logical_channel_number = 600,
					),
			    ],
		    ),
		],
	     ),
	  ],
	 version_number = 1, # you need to change the table number every time you edit, so the decoder will compare its version with the new one and update the table
	 section_number = 0,
	 last_section_number = 0,
        )


#
# Program Association Table (ISO/IEC 13818-1 2.4.4.3)
#

pat = program_association_section(
	transport_stream_id = indtv_transport_stream_id,
        program_loop = [
    	    program_loop_item(
	        program_number = indtv1_service_id,
    		PID = indtv1_pmt_pid,
    	    ),  
	    program_loop_item(
	        program_number = indtv2_service_id,
    		PID = indtv2_pmt_pid,
    	    ),  
    	    program_loop_item(
	        program_number = indtv3_service_id,
    		PID = indtv3_pmt_pid,
    	    ),
    	    program_loop_item(
	        program_number = indtv4_service_id,
    		PID = indtv4_pmt_pid,
    	    ),
    	    program_loop_item(
	        program_number = indtv5_service_id,
    		PID = indtv5_pmt_pid,
    	    ),
    	    program_loop_item(
	        program_number = indtv6_service_id,
    		PID = indtv6_pmt_pid,
    	    ),
    	    #program_loop_item(
	    #    program_number = indtv6_service_id,
    	    #	PID = indtv6_pmt_pid,
    	    #),
    	    program_loop_item(
	        program_number = indews_service_id,
    		PID = indews_pmt_pid,
    	    ),
    	    program_loop_item(
	        program_number = 0, # special program for the NIT
    		PID = 16,
    	    ),
    	    ],
    	    version_number = 1, # you need to change the table number every time you edit, so the decoder will compare its version with the new one and update the table
    	    section_number = 0,
    	    last_section_number = 0,
        )

#
# Service Description Table (ETSI EN 300 468 5.2.3) 
# this is a basic SDT with the minimum desciptors, OpenCaster has a big library ready to use
#

sdt = service_description_section(
	transport_stream_id = indtv_transport_stream_id,
	original_network_id = indtv_original_transport_stream_id,
        service_loop = 
        [
	    service_loop_item(
		service_ID = indtv1_service_id,
		EIT_schedule_flag = 0, # 0 no current even information is broadcasted, 1 broadcasted
		EIT_present_following_flag = 0, # 0 no next event information is broadcasted, 1 is broadcasted
		running_status = 4, # 4 service is running, 1 not running, 2 starts in a few seconds, 3 pausing
		free_CA_mode = 0, # 0 means service is not scrambled, 1 means at least a stream is scrambled
		service_descriptor_loop = [
		    service_descriptor(
			service_type = 1, # digital television service
			service_provider_name = "INDTV",
			service_name = "IND-TV1",
		    ),    
		],
	    ),	

	    service_loop_item(
		service_ID = indtv2_service_id,
		EIT_schedule_flag = 0, # 0 no current even information is broadcasted, 1 broadcasted
		EIT_present_following_flag = 0, # 0 no next event information is broadcasted, 1 is broadcasted
		running_status = 4, # 4 service is running, 1 not running, 2 starts in a few seconds, 3 pausing
		free_CA_mode = 0, # 0 means service is not scrambled, 1 means at least a stream is scrambled
		service_descriptor_loop = [
		    service_descriptor(
			service_type = 1, # digital television service
			service_provider_name = "INDTV",
			service_name = "IND-TV2",
		    ),    
		],
	    ),	

	    service_loop_item(
		service_ID = indtv3_service_id,
		EIT_schedule_flag = 0, # 0 no current even information is broadcasted, 1 broadcasted
		EIT_present_following_flag = 0, # 0 no next event information is broadcasted, 1 is broadcasted
		running_status = 4, # 4 service is running, 1 not running, 2 starts in a few seconds, 3 pausing
		free_CA_mode = 0, # 0 means service is not scrambled, 1 means at least a stream is scrambled
		service_descriptor_loop = [
		    service_descriptor(
			service_type = 1, # digital television service
			service_provider_name = "INDTV",
			service_name = "IND-TV3",
		    ),    
		],
	    ),	

	    service_loop_item(
		service_ID = indtv4_service_id,
		EIT_schedule_flag = 0, # 0 no current even information is broadcasted, 1 broadcasted
		EIT_present_following_flag = 0, # 0 no next event information is broadcasted, 1 is broadcasted
		running_status = 4, # 4 service is running, 1 not running, 2 starts in a few seconds, 3 pausing
		free_CA_mode = 0, # 0 means service is not scrambled, 1 means at least a stream is scrambled
		service_descriptor_loop = [
		    service_descriptor(
			service_type = 1, # digital television service
			service_provider_name = "INDTV",
			service_name = "IND-TV4",
		    ),    
		],
	    ),	

	    service_loop_item(
		service_ID = indtv5_service_id,
		EIT_schedule_flag = 0, # 0 no current even information is broadcasted, 1 broadcasted
		EIT_present_following_flag = 0, # 0 no next event information is broadcasted, 1 is broadcasted
		running_status = 4, # 4 service is running, 1 not running, 2 starts in a few seconds, 3 pausing
		free_CA_mode = 0, # 0 means service is not scrambled, 1 means at least a stream is scrambled
		service_descriptor_loop = [
		    service_descriptor(
			service_type = 1, # digital television service
			service_provider_name = "INDTV",
			service_name = "IND-TV5",
		    ),    
		],
	    ),	

	    service_loop_item(
		service_ID = indtv6_service_id,
		EIT_schedule_flag = 1, # 0 no current even information is broadcasted, 1 broadcasted
		EIT_present_following_flag = 1, # 0 no next event information is broadcasted, 1 is broadcasted
		running_status = 4, # 4 service is running, 1 not running, 2 starts in a few seconds, 3 pausing
		free_CA_mode = 0, # 0 means service is not scrambled, 1 means at least a stream is scrambled
		service_descriptor_loop = [
		    service_descriptor(
			service_type = 1, # digital television service
			service_provider_name = "PT. AZMI JAYA SENTOSA",
			service_name = "Azmi Jaya Sentosa Televisi (Siaran Martabak)",
		    ),    
		],
	    ),	

	#	service_loop_item(
	#	service_ID = indtv6_service_id,
	#	EIT_schedule_flag = 0, # 0 no current even information is broadcasted, 1 broadcasted
	#	EIT_present_following_flag = 0, # 0 no next event information is broadcasted, 1 is broadcasted
	#	running_status = 4, # 4 service is running, 1 not running, 2 starts in a few seconds, 3 pausing
	#	free_CA_mode = 0, # 0 means service is not scrambled, 1 means at least a stream is scrambled
	#	service_descriptor_loop = [
	#	    service_descriptor(
	#		service_type = 1, # digital television service
	#		service_provider_name = "INDTV",
	#		service_name = "IND-TV6",
	#	    ),    
	#	],
	#    ),	

	    service_loop_item(
		service_ID = indews_service_id,
		EIT_schedule_flag = 0, # 0 no current even information is broadcasted, 1 broadcasted
		EIT_present_following_flag = 0, # 0 no next event information is broadcasted, 1 is broadcasted
		running_status = 4, # 4 service is running, 1 not running, 2 starts in a few seconds, 3 pausing
		free_CA_mode = 0, # 0 means service is not scrambled, 1 means at least a stream is scrambled
		service_descriptor_loop = [
		    service_descriptor(
			service_type = 128, # digital television service
			service_provider_name = "BMKG",
			service_name = "Disaster Emergency Warning System",
		    ),    
		],
	    ),
	    ],
	version_number = 1, # you need to change the table number every time you edit, so the decoder will compare its version with the new one and update the table
	section_number = 0,
	last_section_number = 0,
        )
#
# Event Information Table (ETSI EN 300 468 5.2.4) 
#

# eit = event_information_section(
# 	table_id = EIT_ACTUAL_TS_PRESENT_FOLLOWING,
# 	service_id = indtv6_service_id,
# 	transport_stream_id = indtv_transport_stream_id,
# 	original_network_id = indtv_original_transport_stream_id,
#         event_loop = [
# 	    event_loop_item(
# 		event_id = 1,
# 		start_year = 108, # since 1900
# 		start_month = 6, 
# 		start_day = 10, 
# 		start_hours = 0x00, # use hex like decimals
# 		start_minutes = 0x00,
# 		start_seconds = 0x00,
# 		duration_hours = 0x23,
# 		duration_minutes = 0x00,
# 		duration_seconds = 0x00,
# 		running_status = 4, # 4 service is running, 1 not running, 2 starts in a few seconds, 3 pausing
# 		free_CA_mode = 0, # 0 means service is not scrambled, 1 means at least a stream is scrambled
# 		event_descriptor_loop = [
# 		    short_event_descriptor (
# 			ISO639_language_code = "ita", 
# 			event_name = "epg event name",
# 			text = "this is an epg event text example",
# 		    ),
# 		],
# 	    ),	    	
#             ],
#         version_number = 1,
#         section_number = 0,
#         last_section_number = 1, # pay attention here, we have another section after this!
#         )


# eit_follow = event_information_section(
# 	table_id = EIT_ACTUAL_TS_PRESENT_FOLLOWING,
# 	service_id = indtv6_service_id,
# 	transport_stream_id = indtv_transport_stream_id,
# 	original_network_id = indtv_original_transport_stream_id,
#         event_loop = [
# 	    event_loop_item(
# 		event_id = 2, 
# 		start_year = 108, # since 1900
# 		start_month = 06, 
# 		start_day = 10,
# 		start_hours = 0x23,
# 		start_minutes = 0x30,
# 		start_seconds = 0x00, 
# 		duration_hours = 0x12, 
# 		duration_minutes = 0x00,
# 		duration_seconds = 0x00, 
# 		running_status = 4, # 4 service is running, 1 not running, 2 starts in a few seconds, 3 pausing
# 		free_CA_mode = 0, # 0 means service is not scrambled, 1 means at least a stream is scrambled
# 		event_descriptor_loop = [
# 		    short_event_descriptor (
# 			ISO639_language_code = "ita", 
# 			event_name = "epg event name 2",
# 			text = "this is the following text example", 
# 		    )    
# 		],
# 	    ),
#             ],
#         version_number = 1, 
#         section_number = 1, # this is the second section
#         last_section_number = 1, 
#         )





#
# Program Map Table (ISO/IEC 13818-1 2.4.4.8)
# this is a basic PMT the the minimum desciptors, OpenCaster has a big library ready to use
#	

pmtlist = [

    program_map_section(
	program_number = indtv1_service_id,
	PCR_PID =0x24,
	program_info_descriptor_loop = [],
	stream_loop = [
		stream_loop_item(
			stream_type = 2, # mpeg2 video stream type
			elementary_PID = 0x24,
			element_info_descriptor_loop = []
		),
		stream_loop_item(
			stream_type = 4, # mpeg2 audio stream type
			elementary_PID = 0x23,
			element_info_descriptor_loop = []
		),
		stream_loop_item(
			stream_type = 5, # AIT stream type
			elementary_PID = app1_ait_pid,
			element_info_descriptor_loop = [ 
			    application_signalling_descriptor(
				application_type = 1, # 1 DVB-J application, 2 DVB-HTML
				AIT_version = 1,  # current ait version
			    ),
			]	
		),
		stream_loop_item(
			stream_type = 11, # DSMCC stream type
			elementary_PID = dsmcc1_pid,
			element_info_descriptor_loop = [
				# a number of descriptors follow specifying the DSMCC properites
				association_tag_descriptor(
					association_tag = dsmcc1_associate_tag,  # this association tag identifys the carousel, it is used also while generating the DSMCC with oc-update.sh and referenced by the AIT
					use = 0,  # some default values follow, don't change then, different values are not supported
					selector_lenght = 0, # ...
					transaction_id = 0x80000000, # ...
					timeout = 0xFFFFFFFF, # ...
					private_data = "",
				),
				stream_identifier_descriptor(
					component_tag = dsmcc1_associate_tag, # it is the same as the assocation tag, some decoders will look for the component tag, others for the association tag, the same value should be used
				),
				carousel_identifier_descriptor(
					carousel_ID = dsmcc1_carrousel_id, # carousel id number, it's a different number from association/component tag, but it has a similiar purpouse: identifying the carousel
					format_ID = 0, # no enhanced boot supported
					private_data = "",
				),
				data_broadcast_id_descriptor(
					data_broadcast_ID = 240, # 240 is the code specifying this is an MHP Object Carousel
					ID_selector_bytes = "",
				),
			]
		),	


	],
        version_number = 1, # you need to change the table number every time you edit, so the decoder will compare its version with the new one and update the table
        section_number = 0,
        last_section_number = 0,
        ),    

    program_map_section(
	program_number = indtv2_service_id,
	PCR_PID = 0x29,
	program_info_descriptor_loop = [],
	stream_loop = [
		stream_loop_item(
			stream_type = 2, # mpeg2 video stream type
			elementary_PID = 0x29,
			element_info_descriptor_loop = []
		),
		stream_loop_item(
			stream_type = 4, # mpeg2 audio stream type
			elementary_PID = 0x28,
			element_info_descriptor_loop = []
		),
	],
        version_number = 1, # you need to change the table number every time you edit, so the decoder will compare its version with the new one and update the table
        section_number = 0,
        last_section_number = 0,
        ),
    program_map_section(
	program_number = indtv3_service_id,
	PCR_PID = 0x2e,
	program_info_descriptor_loop = [],
	stream_loop = [
		stream_loop_item(
			stream_type = 2, # mpeg2 video stream type
			elementary_PID = 0x2e,
			element_info_descriptor_loop = []
		),
		stream_loop_item(
			stream_type = 4, # mpeg2 audio stream type
			elementary_PID = 0x2d,
			element_info_descriptor_loop = []
		),
	],
        version_number = 1, # you need to change the table number every time you edit, so the decoder will compare its version with the new one and update the table
        section_number = 0,
        last_section_number = 0,
        ),
    program_map_section(
	program_number = indtv4_service_id,
	PCR_PID = 0x33,
	program_info_descriptor_loop = [],
	stream_loop = [
		stream_loop_item(
			stream_type = 2, # mpeg2 video stream type
			elementary_PID = 0x33,
			element_info_descriptor_loop = []
		),
		stream_loop_item(
			stream_type = 4, # mpeg2 audio stream type
			elementary_PID = 0x32,
			element_info_descriptor_loop = []
		),
	],
        version_number = 1, # you need to change the table number every time you edit, so the decoder will compare its version with the new one and update the table
        section_number = 0,
        last_section_number = 0,
        ),    

    program_map_section(
	program_number = indtv5_service_id,
	PCR_PID = 0x38,
	program_info_descriptor_loop = [],
	stream_loop = [
		stream_loop_item(
			stream_type = 2, # mpeg2 video stream type
			elementary_PID = 0x38,
			element_info_descriptor_loop = []
		),
		stream_loop_item(
			stream_type = 4, # mpeg2 audio stream type
			elementary_PID = 0x37,
			element_info_descriptor_loop = []
		),
	],
        version_number = 1, # you need to change the table number every time you edit, so the decoder will compare its version with the new one and update the table
        section_number = 0,
        last_section_number = 0,
        ),

    program_map_section(
	program_number = indtv6_service_id,
	PCR_PID = 0x3d,
	program_info_descriptor_loop = [],
	stream_loop = [
		stream_loop_item(
			stream_type = 2, # mpeg2 video stream type
			elementary_PID = 0x3d,
			element_info_descriptor_loop = []
		),
		stream_loop_item(
			stream_type = 4, # mpeg2 audio stream type
			elementary_PID = 0x3c,
			element_info_descriptor_loop = []
		),
	],
        version_number = 1, # you need to change the table number every time you edit, so the decoder will compare its version with the new one and update the table
        section_number = 0,
        last_section_number = 0,
        ),

    #program_map_section(
#	program_number = indtv6_service_id,
#	PCR_PID = 0x3d,
#	program_info_descriptor_loop = [],
#	stream_loop = [
#		stream_loop_item(
#			stream_type = 2, # mpeg2 video stream type
#			elementary_PID = 0x3d,
#			element_info_descriptor_loop = []
#		),
#		stream_loop_item(
#			stream_type = 4, # mpeg2 audio stream type
#			elementary_PID = 0x3c,
#			element_info_descriptor_loop = []
#		),
#	],
#        version_number = 1, # you need to change the table number every time you edit, so the decoder will compare its version with the new one and update the table
#        section_number = 0,
#        last_section_number = 0,
#        ),
    
]


#
# Application Informaton Table (ETSI TS 101 812 10.4.6)
#

aitlist = [
	application_information_section(
        application_type = DVB_J_application_type,
        common_descriptor_loop = [],
        application_loop = [
		# here we list only 1 application, adding another application loop item will signal a second application in the sam AIT
		# you can signal applications in the same AIT or more AITs
		application_loop_item(
		organisation_id = 10,  # this is a demo value, dvb.org should assign an unique value
	        application_id = 1001, # your application id, should be unique for every organisation id present in the same program
	        application_control_code = 2, # 2 is PRESENT, the decoder will add this application to the user choice of application
					# 1 is AUTOSTART, the application will start immedtiatly to load and to execute
					# 3 is DESTROY, it will signal to the application to stop executing
					# 4 is KILL, it will stop execute the application
		# Some required application descriptor follows application id
	        application_descriptors_loop = [
			transport_protocol_descriptor(
			        protocol_id = MHP_OC_protocol_id, # the application is broadcasted on a MHP DSMCC
			        transport_protocol_label = 1, # carousel id
			        remote_connection = 0,
			        component_tag = 0xB, # carousel common tag and association tag
			),
			application_descriptor(
			        application_profile = 0x0001, # Profile and MHP version of the application MHP 1.0.2
			        version_major = 1,
			        version_minor = 0,
			        version_micro = 2,
			        service_bound_flag = 1, # 1 means the application is expected to die on service change, 0 will wait after the service change to receive all the AITs and check if the same app is signalled or not
			        visibility = 3, # 3 the applications is visible to the user, 1 the application is visible only to other applications
			        application_priority = 1, # 1 is lowset, it is used when more than 1 applications is executing
			        transport_protocol_labels = [1], # carousel Id
			),
			application_name_descriptor(application_name = "Text input example"),
			dvb_j_application_descriptor(parameters = ["dvb://1/sample8"]), # parameter passed to the xlet
			dvb_j_application_location_descriptor(
				base_directory = "/", # base directory, if set to "/hello" the xlet will act as "/hello" is its root directory
				class_path_extension = "", # an additiona classpath inside the carousel can be specified
				initial_class = "tv.cineca.apps.yambo.Wizard",  # the starting class implementing Xlet interface
			),
        	]
        	),
   	],
        version_number = 1,
        section_number = 0,
        last_section_number = 0,
	)

]





#
# Time Description Table (ETSI EN 300 468 5.2.5) 
# it should be replaced at run time with tstdt
#
tdt = time_date_section(
	year = 108, # since 1900
	month = 6,
	day = 16,
	hour = 0x11, # use hex like decimals
	minute = 0x30,
	second = 0x21,
        version_number = 1,
        section_number = 0,
        last_section_number = 0,
        )


ewspmt = program_map_section(
	program_number = indews_service_id,
	PCR_PID = 0,
	program_info_descriptor_loop = [],
	stream_loop = [
		stream_loop_item(
			stream_type = 128, # EWS
			elementary_PID = indews_pmt_pid,
			element_info_descriptor_loop = []
		),
	],
        version_number = 1, # you need to change the table number every time you edit, so the decoder will compare its version with the new one and update the table
        section_number = 0,
        last_section_number = 0,
        )    


ewsit = emergency_info_section(
	ewsit_loop = [
	    emergency_info_loop_item(
		original_network_id = 1,
        transport_stream_id = indtv_transport_stream_id,
        version = 1
        owner_descriptor = "BMKG DEWS Server",
	    ),
	],	
    version_number = 1, # you need to change the table number every time you edit, so the decoder will compare its version with the new one and update the table
    section_number = 0,
    last_section_number = 0,
)

ewsmsgtable = [
    emergency_message_section
    (
	original_transport_stream_id = indtv_transport_stream_id,
	disaster_code = 3,
	latitude = 6,
	longitude = 1,
	message_total = 2,
	
	emergency_message_loop = [
	    emergency_message_loop_item
	    (
		destination_transport_stream_id = indtv_transport_stream_id, 
		severity_code = 0,
		message = "Potensi tsunami, mohon untuk pindah ketempat yang lebih tinggi.",
	    ),
	    emergency_message_loop_item
	    (
		destination_transport_stream_id = indtv_transport_stream_id_test, 
		severity_code = 1,
		message = "Potensi tsunami, mohon untuk pindah ketempat yang lebih tinggi.",
	    ),	
	],	
	version_number = 1, # you need to change the table number every time you edit, so the decoder will compare its version with the new one and update the table
    section_number = 0,
    last_section_number = 0,
    ),
]

# print items for debugging
#nit.test()
#sdt.test()
#pat.test()
#ewsit.test()

print('Print items for testing:')
print('==============================================')
print('Disaster Table')
disastercodetable[0].test()
print('==============================================')
print('Message')
ewsmsgtable[0].test()
print('==============================================')


#
# PSI marshalling and encapsulation
#

out = open("./nit.sec", "wb")
out.write(nit.pack())
out.close
out = open("./nit.sec", "wb") # python  flush bug
out.close
os.system('/usr/local/bin/sec2ts 16 < ./nit.sec > ' + SITemp + '/nit.ts')

out = open("./pat.sec", "wb")
out.write(pat.pack())
out.close
out = open("./pat.sec", "wb") # python   flush bug
out.close
os.system('/usr/local/bin/sec2ts 0 < ./pat.sec > ' + SITemp + '/pat.ts')

out = open("./sdt.sec", "wb")
out.write(sdt.pack())
out.close
out = open("./sdt.sec", "wb") # python   flush bug
out.close
os.system('/usr/local/bin/sec2ts 17 < ./sdt.sec > ' + SITemp + '/sdt.ts')

out = open("./tdt.sec", "wb")
out.write(tdt.pack())
out.close
out = open("./tdt.sec", "wb") # python   flush bug
out.close
os.system('/usr/local/bin/sec2ts 20 < ./tdt.sec > ' + SITemp + '/tdt.ts')

for index  in range (len(pmtlist)):
    out = open('./pmt' + str(index) + '.sec', "wb")
    out.write(pmtlist[index].pack())
    out.close
    out = open('./pmt'+ str(index)+'.sec', "wb")
    out.close
    os.system('/usr/local/bin/sec2ts ' + str(pmtpidlist[index]) + ' < ./pmt'+ str(index) +'.sec >> ' + SITemp + '/pmt'+str(index)+'.ts')

for index  in range (len(aitlist)):
    out = open('./ait' + str(index) + '.sec', "wb")
    out.write(aitlist[index].pack())
    out.close
    out = open('./ait'+ str(index)+'.sec', "wb")
    out.close
    os.system('/usr/local/bin/sec2ts ' + str(aitpidlist[index]) + ' < ./ait'+ str(index) +'.sec >> ' + SITemp + '/ait'+str(index)+'.ts')


# EWS Info Begin
#=================================
out = open("./ewspmt.sec", "wb")
out.write(ewspmt.pack())
out.close
out = open("./ewspmt.sec", "wb") # python   flush bug
out.close
os.system('/usr/local/bin/sec2ts ' + str(indews_pmt_pid) + ' < ./ewspmt.sec > ' + SITemp + '/ewspmt.ts')

#
out = open("./ewsit.sec", "wb")
out.write(ewsit.pack())
out.close
out = open("./ewsit.sec", "wb") # python   flush bug
out.close
os.system('/usr/local/bin/sec2ts ' + str(indews_pmt_pid) + ' < ./ewsit.sec > ' + SITemp + '/ewsit.ts')

for index  in range (len(ewsmsgtable)):
    out = open('./ewsmessage' + str(index) + '.sec', "wb")
    out.write(ewsmsgtable[index].pack())
    out.close
    out = open('./ewsmessage'+ str(index)+'.sec', "wb")
    out.close
    os.system('/usr/local/bin/sec2ts ' + str(indews_pmt_pid) + ' < ./ewsmessage'+ str(index) +'.sec >> ' + SITemp + '/ewsmessage.ts')
#==============================================EWS DONE================

# out = open("./eit.sec", "wb")
# out.write(eit.pack())
# out.close
# out = open("./eit.sec", "wb") # python   flush bug
# out.close
# os.system('/usr/local/bin/sec2ts 18 < ./eit.sec > ' + SITemp + '/firsteit.ts')

# out = open("./eit_follow.sec", "wb")
# out.write(eit_follow.pack())
# out.close
# out = open("./eit_follow.sec", "wb") # python   flush bug
# out.close
# os.system('/usr/local/bin/sec2ts 18 < ./eit_follow.sec >> ' + SITemp + '/firsteit.ts')

os.system('rm ./*.sec')
print('==============================================')
print('D O N E')
    
