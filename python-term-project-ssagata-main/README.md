# python-term-project-ssagata
python-term-project-ssagata created by GitHub Classroom

# Progamming fundamentals 1st term project (Year  \<21\>/\<22\>)
Author: Agata Socha   uvus:\ agasoc

This project's objective is to analyze net of publictransport railroads based on the train stations in Europe.
Dataset posted on Kaggle which can be downloaded using the following URL (https://www.kaggle.com/headsortails/train-stations-in-europe). 
This dataset originally had 12 columns of which none where of date type. 
As such, I have chosen 11 out of them, I have deleted one column where there were a lot of null values and also I deleted some rows with null values in uic column. 
**I will add one column with randomly generates dates, which should correspond to the date when the train station had been built.**

## Folder structure for the project

* **/src**: Contains the different python modules that make up the project.
  * **\<train_stations.py\>**: Contains the functions to analyze the train_stations data.
  * **\<train_stations_test.py\>**: Contains the test functions for the module train_stations.py.
  * **\<train_stations_dataconversion.py\>**: Contains the data conversion functions
  * **\<train_stations_graph.py\>**:Contains the functions to draw graphs
* **/data**: Contiene el dataset o datasets del proyecto
    * **\<train_stations_europe.csv\>**: The original data file
<<<<<<< HEAD
    * **\<train_stations_europe_new.csv\>**: Data file with the manga information
=======
    * **\<crain_stations_europe.csv\>**: Data file with the modified dates
>>>>>>> 1583dc1 (Delivery 2)
    
## *Dataset* Structure

This data set is made out of  \<15\> columns, with the following description:

* **\<id>**: of type \<int\>, numeric internal unique identifier. Primary key.
* **\<name>**: of type \<str\>, name of the station as it is locally known. These names include accents and other special characters.
* **\<name_norm>**: of type \<str\>, normalised version of name; 
* **\<uic>**: of type \<int\>, the UIC  (International Union of Railways) code of the station. Stations with no UIC has been deleted.
* **\<longitude>**: of type \<float\>,  station lingitude coordinate
* **\<latitude>**: of type \<float\>, station latitude coordinate 
* **\<country>**: of type \<str\>, country codes in ISO 3166-1 alpha-2 format
* **\<time_zone>**: of type \<str\>, continent/Country ISO codes which are defining the time zone of the station
* **\<is_city>**: of type \<boolean\>, whether the the place is in the city or not
* **\<is_main_station>**: of type \<int\>, whether the station is the main station in the city or no
* **\<is_airport>**: of type \<int\>, whether the station is in the city where is the airport or no 



## Implemented types

Describe here the namedtuple (s) that you define in your project.

* **\<id>**: of type \<int\>, numeric internal unique identifier. \
* **\<name>**: of type \<str\>, name of the station as it is locally known. These names include accents and other special characters.
* **\<name_norm>**: of type \<str\>, normalised version of name; 
* **\<uic>**: of type \<int\>, the UIC  (International Union of Railways) code of the station. 
* **\<longitude>**: of type \<float\>,  station longitude coordinate
* **\<latitude>**: of type \<float\>, station latitude coordinate 
* **\<country>**: of type \<str\>, country codes in ISO 3166-1 alpha-2 format
* **\<time_zone>**: of type \<str\>, continent/Country ISO codes which are defining the time zone of the station
* **\<is_city>**: of type \<boolean\>, whether the the place is in the city or not
* **\<is_main_station>**: of type \<int\>, whether the station is the main station in the city or no
* **\<is_airport>**: of type \<int\>, whether the station is in the same place as airport


## Implemented functions
Add here generic descriptions of the functions, which you must then accompany with comments of type documentation in the code

### \<BLOCK 1\>

* **<read_file>**: reads the file
* **<different_countries>**: makes a list of different countries and sorts it alphabetically.
* **<stations_in_country>**: makes a list of stations which are in the given country and sorts it alphabetically
* **<avg_longitute>**: returns a list of the average longitude of all stations
* **<avg_latitude>**: returns a list of the average latitude of all stations
* **<avg_coords_in_country>**: returns a list of the average coordinators (longitude and latitude ) of the given stations


### \<test BLOCK 1 \>

* **<test_read_file>**: prints list of information of first 3 and last 3 stations
* **<test_different_countries>**: prints number of different countries and list of countrycodes of these countries
* **<test_stations_in_country>**: prints first 5 stations in given country
* **<test_avg_longitude>**: prints average longitude
* **<test_avg_latitude>**: prints average latitude
* **<test_avg_coords_in_country>**: prints average coordinates in given country


### \<BLOCK 2\>

* **<max_longitude_in_country>**: returns list of informations about the highest longitude station in given country
* **<countries_over_country>**: makes a list of countrycodes of countries which have station with higher longitude than the hishest in given country 
* **<stations_low_to_high_in_contry>**: makes a list of tuples ordered from the lowest to highest longitude of station in given country
* **<dict_country_list_of_stations>**: returns a dictionry where  key is a countrycode of country and the value is set of informations about the stations in this country



### \<test BLOCK 2 \>

* **<test_max_long_in_country>**: prints list of informations about the station with the highest longiitude in given contry
* **<test_countries_over_country>**: prints list of countrycodes oof countries which have station with higher longitude than the hishest in given country 
* **<test_stations_low_to_high_in_country>**: prints  informations about first 3 lowers stations in given country 
* **<test_country_list_of_stations>**: prints dictionary with couontrycoodes and informations about the stations in that country. 

### \<BLOCK 3\>

* **<dict_country_nr_of_stations>**: returns a dictionry where  key is a countrycode of country and the value is amount of stations in that country
* **<_country_sum_of_stations_id>** returns a dictionry where  key is a countrycode of country and the value is sum of the IDs having by stations in that country
*  **<max_stations_count>**: returns a maximum values of the stations in one country
*  **<max_station_value>**: returns a maximum values of the sum of ids of one country
*  **<dict_country_max_len_of_stations>**: returns a dictionaary with a key as a countrycode and as a value - the maximum longitude of that country
*  **<dict_country_perc_of_stations>**: returns a dictionaary with a key as a countrycode and as a value - the percentege of the stations of that country
*  **<dict_country_n_max_len_of_stations>**: returns a dictionaary with a key as a countrycode and as a value - the n maximum longitudes of the stations in that country

### \<test BLOCK 3 \>
 
* **<test_dict_country_nr_of_stations>**: prints dictionary with couontrycoodes and amount of stations. 
* **<test_dict_country_nr_of_stations>**: prints dictionary with couontrycoodes and sum of ids. 
* **<test_max_stations_count>**: prints maximum amount of stations in one country. 
* **<test_max_station_value>**: prints maximum sum of ids of one country. 
* **<test_dict_country_max_len_of_stations>**: prints dictionary with countrycodes and max longitudes of thaat country. 
* **<test_dict_country_perc_of_stations>**: prints dictionary with countrycodes and tha percentego of stations sorted from the most populat to the lowest. 
* **<test_dict_country_n_max_len_of_stations>**: prints dictionary with countrycodes and the n maximum longitudes


### \<BLOCK 4\>
*  **<plot_number_of_stations>**: returns a plot witch combine numbers of stations of every country

### \<test BLOCK 4 \>


* **<test_plot_number_of_stations>**: prints plot witch combine numbers of stations of countries

