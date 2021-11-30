import paho.mqtt.client as mqtt
import time
import psycopg2 as psql
from configparser import ConfigParser
from database import Database
from MqttDriver import MqttDriver
######################################################################
## CONSTANTS
######################################################################

CLIENT_NAME = "pythonScript"
LOCAL_BROKER = "localhost"
DEMO_TOPIC = "/Demo"
FILENAME = "database.ini"

######################################################################
## MAIN
######################################################################

def main():
    # Create a database object and connect to the database
    database = Database( FILENAME )
    database.db_connect()

    # Create an MQTT Driver
    print( "Creating Mqtt Driver" )
    driver = MqttDriver( CLIENT_NAME, database )

    # Create MQTT client and connect to the broker hosted locally
    print( "Connecting client..." )
    driver.connect( LOCAL_BROKER )

    # Subscribe to topics
    print( "Subscribing to topics..." )
    driver.subscribe( DEMO_TOPIC )

    # Start the subscriber loop to listen for incoming messages
    driver.run()


main()
