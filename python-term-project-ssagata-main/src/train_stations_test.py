# -*- coding: utf-8 -*-

from train_stations import *

DATA = read_file('/Users/agatasocha/Desktop/STUDIA/sem5Erasmuss/Python/projekt/python-term-project-ssagata/data/train_stations_europe_new.csv')


def test_read_file():
    print("Function: read_file:\n")
    print("First 3:")
    print(DATA[0:3])
    print("\nLast 3:")
    print(DATA[:3])
    print("\nNumber of stations: ")
    print(len(DATA)+1)


def test_different_countries():  
    print("*******\tBLOCK1\n") 
    print("\nFunction: different_countries:\n")

    country = different_countries(DATA)
    print("In our database there are " , len(country), "different countries")
    print("Their countrycodes: " , country)

def test_stations_in_country():
    print("\nFunction: station_in_country:\n")
    stations  = stations_in_country(DATA, 'PL')
    #sorted(stations)
    print("Stations in Poland: ", sorted(stations)[:5])
    print("And the best town in the world is : ", sorted(stations)[5])

def test_avg_longitude():
    print("\nFunction: avg_longitude:\n")
    print("Average longitude: ", avg_longitude(DATA))

def test_avg_latitude():
    print("\nFunction: avg_latitude:\n")
    print("Average latitude: ", avg_latitude(DATA))

def test_avg_coords_in_country():
    print("\nFunction: avg_coords_in_country:\n")
    print("Avg coords in Poland: ", avg_coords_in_country(DATA, 'PL'))


#BLOCK 2
def test_max_long_in_country():
    print("\n\n*******\tBLOCK 2\n") 
    print("\nFunction: max_longitude_in_country:\n")
    print("MAX longitude in Poland is: ", max_longitude_in_country(DATA, 'PL'))

def test_countries_over_country():
    print("\nFunction: countries over country:\n")
    print("Countries over Poland: ", countries_over_country(DATA, 'PL'))

def test_stations_low_to_high_in_country():
    print("\n Functoin: form low to high: \n")
    print("ordered Stations in Poland: ", stations_low_to_high_in_contry(DATA)[:3])

   
def test_dict_country_list_of_stations():
    print("\n Function: Country : list of stations: \n")
    print("Lists of station in Poland : ")
    print(dict_country_list_of_stations(DATA, 'PL'))  



#BLOCK 3 

def test_dict_country_nr_of_stations():
    print("\n Function: Country : nr of stations: \n")
    print("Nr of stations in country: ")
    print(dict_country_nr_of_stations(DATA))

def test_country_sum_of_stations_id():
    print("\n Function: Country : sum of ids vaalues: \n")
    print(dict_country_sum_of_stations_id(DATA))

def test_max_stations_count():
    print("\n Function: MAX stations count: \n")
    test_dict = dict_country_nr_of_stations(DATA)
    print(max_stations_count(test_dict))

def test_max_station_value():
    print("\n Function: MAX stations values: \n")
    test_dict = dict_country_sum_of_stations_id(DATA)
    print(max_station_value(test_dict))

def test_dict_country_max_len_of_stations():
    print("\n Function: dict_country_max_len_of_stations: \n")
    print(dict_country_max_len_of_stations(DATA))

def test_dict_country_perc_of_stations():
    print("\n Function: dict_country_perc_of_stations: \n")
    print(dict_country_perc_of_stations(DATA))

def test_dict_country_n_max_len_of_stations():
    print("\n Function: dict_country_n_max_len_of_stations \n")
    print(dict_country_n_max_len_of_stations(DATA))

def test_plot_number_of_stations():
    print("\n Function: plot_number_of_stations \n")
    print(plot_number_of_stations(DATA))

    

print("############################################")
print("#####            DELIVERY  1        ########")
print("############################################\n\n")
test_read_file()


print("\n\n############################################")
print("#####            DELIVERY  2       ########")
print("############################################\n\n")
#BLOCK 1
test_different_countries()
test_stations_in_country()
test_avg_longitude()
test_avg_latitude()
test_avg_coords_in_country()

#BLOCK2
test_max_long_in_country()
test_countries_over_country()
test_stations_low_to_high_in_country()
test_dict_country_list_of_stations()


print("\n\n############################################")
print("#####            DELIVERY  3       ########")
print("############################################\n\n")

#BLOCK3
test_dict_country_nr_of_stations()
test_country_sum_of_stations_id()
test_max_stations_count()
test_max_station_value()
test_dict_country_max_len_of_stations()
test_dict_country_perc_of_stations()
test_dict_country_n_max_len_of_stations()
test_plot_number_of_stations()




