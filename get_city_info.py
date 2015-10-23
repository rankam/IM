#!/usr/bin/python

import pymysql.cursors
import sys
import csv
import os

def create_connection():
    '''
    Connects to the Google Cloud MYSQL database as a guest with the
    password and host stored as local environmental variables.
    '''
    try:
    	connection = pymysql.connect(host=os.environ['HOSTNAME'],
    	    port=3306,
    	    user='guest',
    	    password=os.environ['GUEST_PASSWORD'],
    	    db='IM',
    	    cursorclass=pymysql.cursors.DictCursor)
    	return connection
    except:
        raise

def get_city_info(city):
    '''
    Taking the name of a city as an argument, the function will return all of 
    the information about that city contained in the database. Returns a list
    of dicts.
    '''
    print 'Connecting to database...'
    connection = create_connection()
    print 'Connected'
    print 'Querying\n'
    try:
        with connection.cursor() as cursor:
            sql = "SELECT ci.id AS City_ID, ci.name AS City_Name, ci.iso_code \
            AS City_Iso_Code, co.id AS Country_ID, co.alpha2 AS Alpha2, co.alpha3\
            AS Alpha3, co.name AS Country_Name, co.targetable AS Targetable, \
            r.id AS Region_ID, r.name AS Region_Name, r.iso_code AS \
            Region_Iso_Code FROM Cities ci join Countries co ON ci.country_id=\
            co.id JOIN Regions r ON r.id=ci.region_id WHERE ci.name=%s"
            cursor.execute(sql, (city,))
            result = cursor.fetchall()
    finally:
        connection.close()
    return result

def write_file(data):
    '''Writes the returned information about the city to a csv.'''
    keys = data[0].keys()

    with open('results.csv', 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)


def main(city):
    '''
    Main function that executes all other functions.
    '''
    try:
        assert(sys.argv[1])
    except:
        raise AssertionError('Please specify a city.')

    city_info = get_city_info(city)
    write_file(city_info)
    print ', '.join(city_info[0].keys())
    for i in range(0,len(city_info)):
    	print ', '.join([str(val) for val in city_info[i].values()])


if __name__ == "__main__":
    main(sys.argv[1])
