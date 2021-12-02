////////////////////////////////////////////////////////////////////////////////
// INCLUDES
////////////////////////////////////////////////////////////////////////////////

#include "include.h"

/* -----  C Standard Includes ----- */
// #include <stdio.h>
// #include <stdlib.h>
// #include <string.h>
// #include <unistd.h>
// #include <time.h>

/* ----- MQTT Includes ----- */
// #include "MQTTClient.h"

/* ----- GPIO Includes ----- */

/* ----- User Defined Includes ----- */
// #include "data.h"

////////////////////////////////////////////////////////////////////////////////
// DEFINES ( CONSTANTS )
////////////////////////////////////////////////////////////////////////////////

#define ADDRESS 	"tcp://test.mosquitto.org:1883"
#define CLIENTID 	"UniqueClient123789456"
#define TOPIC 		"/AutoPot_IED_RPI"
#define PAYLOAD 	"Hello from PI"
#define QOS 		1
#define TIMEOUT 	10000L
#define PUMP		0
#define TURN_ON_MOISTURE	1.5

/**
 *  Builds a JSON message in the following format:
 *  
 *   {
 *	ts:$timestamp,
 *	msg:$input_message
 *   }
 *  and returns the result
 *  @param input_msg --- Becomes part of the output message. Can be no longer than
 *    16 characters
 *  
 *  @return The JSON message in char* format. The message can be no longer than 
 *    127 characters ( plus null terminator )
 *
 */
char* build_msg_deprecated( char* input_msg ) {
	/* Declare a string to hold the resulting message */
	char* msg = (char*) calloc( 128, sizeof( char ) );

	/* Add open bracket ( start of JSON ) */
	msg[0] = '{';

	/* Add timestamp key & semi-colon */
	strcat( msg, "ts:" );

	/* Retrieve the timestamp value using time.h */
	int timestamp_int = (int) time( NULL );
	char* timestamp = calloc( 64, sizeof( char ) );
	sprintf( timestamp, "%d", timestamp_int );

	/* Add the timestamp key */
	strcat( msg, timestamp );

	/* Add comma ( not the first key-value pair ), 
	    message key, & semi-colon */
	strcat( msg, ",msg:\"" );

	/* Append input message as the final value ( no comma ) */
	strcat( msg, input_msg );
	msg[ strlen(msg) ] = '"';

	/* Append close bracket ( end of JSON ) */
	msg[ strlen( msg ) ] = '}';
	
	/* Return the built message */
	return msg;
}

int main() {

	/* Set up variables for connection */
	MQTTClient client;
	MQTTClient_connectOptions conn_opts = MQTTClient_connectOptions_initializer;
        /* Declare a string to hold the resulting message */
        char* msg = (char*) calloc( 128, sizeof( char ) );

	/* Set up message and token */
	MQTTClient_message pubmsg = MQTTClient_message_initializer;
	MQTTClient_deliveryToken token;
	int rc;

	/* Create the client */
	MQTTClient_create( &client, ADDRESS, CLIENTID,
		       MQTTCLIENT_PERSISTENCE_NONE, NULL );
	conn_opts.keepAliveInterval = 20;
	conn_opts.cleansession = 1;
	
	/* Attempt to connect to the client */
	rc = MQTTClient_connect( client, &conn_opts );

	/* Error check the client connection */
	if( rc != MQTTCLIENT_SUCCESS ) {
		printf( "Failed to connect, return code %d\n", rc );
		exit( -1 );
	}

	/* Set message options ( before the loop, as they do not change ) */
	pubmsg.qos = QOS;
	pubmsg.retained = 0;

	/* Set up i2c communication */
	i2c_init();

	/* Set up GPIO */
	wiringPiSetup();
	pinMode( PUMP, OUTPUT );

	/* Create a system state structure */
	Data* state = calloc( 1, sizeof( Data ) ); 
	state->moisture_level = 2;

	/* Attempt to publish the message */
	while( 1 ) {
		/* Get all of the sensor info */
		state->moisture_level = adc_read();
		printf( "Moisture level: %f\n", state->moisture_level );
		
		/* If the moisture level is above the threshold,
		    turn on the pump */
		if( state->moisture_level < TURN_ON_MOISTURE ) {
			digitalWrite( PUMP, HIGH );
		} else {
			digitalWrite( PUMP, LOW );
		}

		/* Build the JSON message */
		printf( "Building message...\n" );
		char* payload = build_msg( state );
		pubmsg.payload = payload;
		pubmsg.payloadlen = strlen( payload );

		/* Output message to stdout */
		printf( "Message: %s\n", payload );

		/* Publish the message & clean up memory from previous message payload */
		printf( "Publishing message to topic %s...\n", TOPIC );
		MQTTClient_publishMessage( client, TOPIC, &pubmsg, &token );
		free( payload );

		/* Sleep for 100 milli seconds */
		sleep( 0.1 );
	}

	printf( "Hello World\n" );
}

