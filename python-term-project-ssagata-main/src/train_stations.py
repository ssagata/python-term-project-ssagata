import csv
from math import dist, sqrt
from os import name, read
from typing import Counter
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from collections import namedtuple

#namedtuple
Station = namedtuple('Station', 'id name name_norm uic longitude latitude country time_zone is_city is_main_station is_airport')

#read file

def read_file(file):
    stations = []
    with open(file, encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        stations = [Station(int(id), str(name), str(name_norm), int(uic), float(longitude), float(latitude), str(country), str(time_zone), bool(is_city), bool(is_main_station), bool(is_airport))
        for id, name, name_norm, uic, longitude, latitude, country, time_zone, is_city, is_main_station, is_airport in reader]

    return stations


#############################################################################
#                               DELIVERY2                                 #
#############################################################################

'''
BLOCK1

'''


def different_countries(file):
    set_of_countries = set(country for _,_,_,_,_,_,country,_,_,_,_ in file)
    list_of_countries = list(set_of_countries)
    list_of_countries.sort()
    return list_of_countries

def stations_in_country(file, countrycode):
    stations = []
    for tuple in file:
        if tuple.country == countrycode:
            stations.append((tuple.name_norm))
    return stations


def avg_longitude(file):
   list_of_long  = [e.longitude for e in file]
   avg_long = [sum(list_of_long)/len(list_of_long)]
   return avg_long

def avg_latitude(file):
    list_of_lat  = [e.latitude for e in file]
    avg_lat = [sum(list_of_lat)/len(list_of_lat)]
    return avg_lat

def avg_coords_in_country(file, given_country):
    lat_in_country = []
    long_in_country = []
    for i in file:
        if i.country == given_country:
            long_in_country.append(i.longitude)
            lat_in_country.append(i.latitude)

    avg_long = [sum(long_in_country)/len(long_in_country)]
    avg_lat  = [sum(lat_in_country)/len(lat_in_country)]

    avg_coords = [avg_long, avg_lat]
    return  avg_coords

   

'''
BLOCK  2 
'''

def max_longitude_in_country(file, given_country):
    max_longitude = max([i.longitude for i in file if given_country == i.country])

    output = [i for i in file  if i.longitude == max_longitude ]
    return output


def countries_over_country(file, given_country):
    max_longitude = max([i.longitude for i in file if given_country == i.country])
    output = []
    for i in file:
        if i.longitude > max_longitude:
            output.append(i.country) 

    set_of_countries = set(i for i in output)
    list_of_countrieees  = list(set_of_countries)
    list_of_countrieees.sort()
    return list_of_countrieees

def stations_low_to_high_in_contry(file, given_country = 'PL'):
    output = []
    list_of_longitude  = [e.longitude for e in file if e.country == given_country]
    list_of_longitude.sort()
    for i in list_of_longitude:
        output = [(a.name_norm, a.longitude, a.uic) for a in file if a.country == given_country]
    
    return output


def dict_country_nr_of_stations(file):
    country = [i.country for i in file]
    country.sort()
    counter_dict = Counter(country)
    return  counter_dict

def dict_country_list_of_stations(file, given_country = 'PL'):
    country_dict = {}
    #coountry = [i.country for i in file if i.country == given_country] 
    #country_dict[coountry] = [[a.id, a.name_norm, a.time_zone] for a in file]
    
    countries = [i.country for i in file if i.country == given_country]
    lists_of_stations = []
    #lists_of_stations = [[i.id, i.name_norm, i.time_zone] for i in file if i.country == given_country]
    for i in file :
        if i.country == given_country:
            lists_of_stations.append([i.id, i.name_norm, i.time_zone]) 
    country_dict = dict(zip(countries, lists_of_stations))       
    return country_dict


    
   

#############################################################################
#                               DELIVERY 3                                  #
#############################################################################

'''
BLOCK  3
'''

# this function is from th previous delivry 
# I changed the last function of delivery 2 for a good one 

def dict_country_nr_of_stations(file):
    country = [i.country for i in file]
    country.sort()
    counter_dict = Counter(country)
    return  counter_dict

def dict_country_sum_of_stations_id(file):
    country_dict = {}
    for i in file:
        if i.country in list(country_dict.keys()):
            country_dict[i.country] = country_dict[i.country] + i.id
        else:
            country_dict[i.country] = i.id
    return  country_dict

def max_stations_count(dict_):
    res = 0
    for key in list(dict_.keys()):
        if dict_[key] > res:
            res = dict_[key]
    return  res

def max_station_value(dict_):
    res = 0
    for key in list(dict_.keys()):
        if dict_[key] > res:
            res = dict_[key]
    return  res

def dict_country_max_len_of_stations(file):
    country_dict = {}
    for i in file:
        if i.country in list(country_dict.keys()):
            if i.longitude > country_dict[i.country]:
                country_dict[i.country] = i.longitude
        else:
            country_dict[i.country] = i.longitude
    return  country_dict

def dict_country_perc_of_stations(file):
    stations_sum = len(file)
    country = [i.country for i in file]
    country.sort()
    counter_dict = Counter(country)
    for key in list(counter_dict.keys()):
        counter_dict[key] = counter_dict[key]/stations_sum*100
    return  counter_dict

def dict_country_n_max_len_of_stations(file, n=5):
    country_dict = {}
    for i in file:
        country_dict.setdefault(i.country,[]).append(i.longitude)
    for key in list(country_dict.keys()):
        country_dict[key].sort()
        new_value = []
        range_ = min(n, len(country_dict[key]))
        for i in range(range_):
            new_value.append(country_dict[key].pop())
        country_dict[key] = new_value
    return  country_dict

def plot_number_of_stations(file):
    country = [i.country for i in file]
    country.sort()
    counter_dict = Counter(country)
    plt.rcParams["figure.figsize"] = (20, 10)
    lists = sorted(counter_dict.items())
    print(lists)
    x, y = zip(*lists)
    print(y)
    plt.bar(x, y)
    plt.show()
