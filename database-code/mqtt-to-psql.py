import paho.mqtt.client as mqtt
import time
import psycopg2 as psql
from configparser import ConfigParser

###################################
# CONSTANTS
###################################
clientName = "mqtt-to-psql"
brokerLocation = "localhost"
topic = "/Demo"
conn = None

###################################
# CALLBACKS
###################################

def on_message( client, userdata, message ):
    print("message received " ,str(message.payload.decode("utf-8")))

###################################
# MAIN
###################################

def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

def main():
    # Read config file
    params = config()

    # Connect to local postgres instance
    print( "Connecting to database..." )
    conn = psql.connect( **params )

    # create a cursor
    cur = conn.cursor()

    # execute a statement
    print('PostgreSQL database version:')
    cur.execute('select * from autopot;')

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
