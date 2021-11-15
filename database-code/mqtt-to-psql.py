import paho.mqtt.client as mqtt
import time
import psycopg2 as psql
from configparser import ConfigParser
from database import Database

######################################################################
## CONSTANTS
######################################################################
clientName = "mqtt-to-psql"
brokerLocation = "localhost"
topic = "/Demo"
conn = None
FILENAME = "database.ini"

######################################################################
## CALLBACKS
######################################################################

def on_message( client, userdata, message ):
    print("message received ", str(message.payload.decode("utf-8")))

######################################################################
## MAIN
######################################################################

def main():
    # Create a database object and connect to the database
    database = Database( FILENAME )
    database.db_connect()

    # Create MQTT client and connect to the broker hosted locally
    print( "Creating client..." )
    client = mqtt.Client( clientName )

    # Set the client message received callback
    client.on_message = on_message

    print( "Connecting client..." )
    client.connect( brokerLocation )

    # Subscribe to topics
    print( "Subscribing to topics..." )
    client.subscribe( topic )

    # Start the subscriber loop to listen for incoming messages
    print( "Starting loop..." )
    client.loop_start()

    time.sleep( 60 )

    client.loop_stop()

main()
