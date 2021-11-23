import paho.mqtt.client as mqtt
import time
import psycopg2 as psql
from configparser import ConfigParser
from database import Database
from MqttDriver import MqttDriver
import matplotlib.pyplot as plt

######################################################################
## CONSTANTS
######################################################################

CLIENT_NAME = "pythonScript"
LOCAL_BROKER = "localhost"
DEMO_TOPIC = "/Demo"
FILENAME = "database.ini"

######################################################################
## PLOTTING FUNCTIONS
######################################################################

'''
Takes as input a list of tuples as specified by the database,
 and returns a tuple (x, y)
@param tuples --- The list of tuples from the database

'''
def parse_tuples( tuples ):
    # Declare the x and y values as empty lists
    x = []
    y = []

    # Iterate over the tuples
    for row in tuples:
        # Take the first value (timestamp) and add 
        #  to the x values
        x.append( row[0] )
        # Take the second value (moisture) and add
        #  to the y values
        y.append( row[1] )

    return x, y

######################################################################
## MAIN
######################################################################

def main():
    # Create a database object and connect to the database
    database = Database( FILENAME )
    database.db_connect()


    # Get the values in the database
    tuples = database.get_values( 20 )

    # Parse the tuples into x (timestamp) 
    #  and y (moisture) values
    x, y =  parse_tuples( tuples )

    # Graph the values (x, y)
    plt.figure()
    plt.plot( x, y )
    plt.show()



main()
