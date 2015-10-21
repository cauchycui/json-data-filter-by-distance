#!/usr/bin/python
'''
Hengguan Cui    intercom interview assignment: sorting customers by distance
python 2.7.9

'''
import math
import json



def calculate_distance (lat_1, lon_1, lat_2 = 53.3381985, lon_2 = -6.2592576):
	abs_lat = math.fabs(lat_1-lat_2)    #float 
	abs_lon = math.fabs(lon_1-lon_2)
	
	tmp_a = math.sin(lat_1) * math.sin(lat_2) + 				\
		math.cos(lat_1) * math.cos(lat_2) * math.cos(abs_lon) 
	central_angle = math.acos(tmp_a)
	radian_cent_angle = central_angle * 3.1415926 / 180 
	
	distance = radian_cent_angle * 6371			#mean earch radius 6371km
	return distance

	
def byUsrID_key(cust):
	return cust['user_id']
	
def sort_out_invites(path_str):
	parsed_json = []
	with open(path_str) as fd:
	    for line in fd:					
			parsed_json.append(json.loads(line))
		
	qualified_customers = [elem for elem in parsed_json 		\
		if calculate_distance(float(elem['latitude']), float(elem['longitude']))<= 100]
	
	
	result = sorted(qualified_customers, key = byUsrID_key)
	
	with open('result.txt', 'w') as outfile:
	   	for elem in result:
			entry_str = "{: >20} {: >20}".format(elem['name'], str(elem['user_id'])+" \n")
			print entry_str
			outfile.write(entry_str)

			
if __name__ == "__main__":
    sort_out_invites('customers.txt')

