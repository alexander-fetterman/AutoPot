######################################################################
## IMPORTS
######################################################################
from database import Database
import paho.mqtt.client as paho
import time
import json
import threading

######################################################################
## CLASSES
######################################################################

class MqttDriver:
    ######################################################################
    ## CONSTANTS
    ######################################################################
    DATABASE_CONFIG_FILENAME = 'database.ini'

    ######################################################################
    ## MEMBER VARIABLES
    ######################################################################


    ######################################################################
    ## CONSTRUCTORS
    ######################################################################

    '''
    Creates the member client. THIS METHOD DOES NOT DO ANY CONNECTING
     OR SUBSCRIBING!
    @param clientName --- The (unique) client name to be assigned to the
     member client.
    @param database --- A (user defined) database object, supplied externally
    '''
    def __init__( self, clientName, database ):
        # Create an MQTT client
        self.client = paho.Client( clientName )

        # Set the callback method for message received
        self.client.on_message = self.__message_received

        # Use the argument database as the member database
        self.database = database

    ######################################################################
    ## PRIVATE CALLBACKS
    ######################################################################

    '''
    Acts as a driver for all logic following a message being received.
    '''
    def __message_received( self, client, userdata, message ):
        print( "Message received: ", str( message.payload.decode("utf-8") ) )
        
        # Parse the message into a dictionary
        msg_values = json.loads( str( message.payload.decode("utf-8") ) )
        print( "Timestamp: {ts}".format( ts = msg_values[ 'ts' ] ) )
        print( "Moisture Level: {ms}".format( ms = msg_values[ 'ms' ] ) )

        # Insert the tuple into the database
        print( 'Inserting tuple...' )
        self.database.insert_values( msg_values[ 'ts' ], msg_values[ 'ms' ] )


    ######################################################################
    ## PRIVATE METHODS
    ######################################################################


    ######################################################################
    ## PUBLIC METHODS
    ######################################################################
    
    '''
    Connects the member Mqtt Client to the remote broker
    @param brokerURI --- The URI (universal resource identifier) of the broker
     to connect to. This should be in the form specified by the paho library.
    '''
    def connect( self, broker_uri ):
        # Connect the member client to the broker at the parameter
        #  specified URI
        self.client.connect( broker_uri )
    
    '''
    Subscribes the member Mqtt Client to a given topic
    @param topic --- The topic to subscribe to
    '''
    def subscribe( self, topic ):
        # Subcribe to the input topic
        self.client.subscribe( topic )

    '''
    Runs the client loop. This must be called after the connect method
     has been called.
    '''
    def run( self ):
        # Start the client loop - use loop forever because we do not
        #  want to return.
        self.client.loop_forever()

        # Start the client loop
        # thread = threading.Thread( target=self.client.loop_start )
        # thread.start()

        # Wait for the thread to join back...
        #  If it does there has been an error
        # thread.join()

        # Infinite loop ( for now )
        # while( 1 ):
            # time.sleep( 60 )

        # self.client.loop_stop()




