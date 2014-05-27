#!/usr/bin/env python
from soco import SoCo
from soco.services import MusicServices
import xml.etree.cElementTree as XML

s=SoCo('192.168.178.25')  #<---- Use your own Sonos IP here
ms = MusicServices(s)

response = ms.ListAvailableServices()
services = XML.fromstring(response['AvailableServiceDescriptorList'])
type_list = response['AvailableServiceTypeList'].split(',')

name_max_len = 0
id_max_len = 0
type_max_len = 0
index = 0
for s in services:
	if len(s.attrib['Name']) > name_max_len:
		name_max_len = len(s.attrib['Name'])
	if len(s.attrib['Id']) > id_max_len:
		id_max_len = len(s.attrib['Id'])
	if len(type_list[index]) > type_max_len:
		type_max_len = len(type_list[index])
	index = index + 1

index = 0
for s in services:
	print("%s|%s|%s" % (s.attrib['Name'].ljust(name_max_len), s.attrib['Id'].rjust(id_max_len), type_list[index].rjust(type_max_len)))
	index = index + 1

