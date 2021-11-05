/* data.c */

#include "include.h"

/**
 * Constructs a timestamp string from the system time
 */
char* get_timestamp() {
        /* Retrieve the timestamp value using time.h */
        int timestamp_int = (int) time( NULL );
        
	/* Allocate space to hold the result */
	char* timestamp = calloc( 64, sizeof( char ) );
        
	/* Write the timestamp into the allocated string */
	sprintf( timestamp, "%d", timestamp_int );

	/* Return the result */
	return timestamp;
}

char* get_moisture_level( Data* data ) {	
	/* Allocate space to hold the result */
	char* res = calloc( 64, sizeof( char ) );
        
	/* Write the timestamp into the allocated string */
	sprintf( res, "%d", data->moisture_level );

	return res;
}


/**
 * Builds a JSON message from the member fields of a Data structure
 *  The returned string must be freed after use as it is dynamically
 *  allocated
 * @param data --- The input data structure on the system.
 */
char* build_msg( Data* data ) {
        /* Declare a string to hold the resulting message */
        char* msg = (char*) calloc( 128, sizeof( char ) );

        /* Add open bracket ( start of JSON ) */
        msg[0] = '{';

        /* Add timestamp key & semi-colon */
        strcat( msg, TIMESTAMP_KEY );

        /* Add the timestamp key, then free it */
	char* timestamp = get_timestamp();
        strcat( msg, timestamp );
	free( timestamp );

        /* Add comma for JSON format */
        strcat( msg, "," );

	/* Add moisture key */
	strcat( msg, MOISTURE_KEY );

        /* Append moisture level, then free it */
	char* moisture_level = get_moisture_level( data );
        strcat( msg, moisture_level );
	free( moisture_level );

        /* Append close bracket ( end of JSON ) */
        msg[ strlen( msg ) ] = '}';

        /* Return the built message */
        return msg;
}
