## Infectious Media Challenge

### Database Design Questions

The answers to the database design questions can be found in Database.md

### Programming Challenge

im.sql is the sql file that creates the tables and loads the data into the MYSQL database

get_city_info.py is the script that queries the database and prints the information about the given city and also well as writing a file with the results. The script is a command line program and can be used as follows:

```
$ python get_city_info.py [city_name]
``` 

The program will not work unless you have the guest password and hostname for the cloud database stored as environmental variables.

### Todo

Write unit tests.