/* data.h */

#ifndef _DATA_H_
#define _DATA_H_

////////////////////////////////////////////////////////////////////////////////
// INCLUDES
////////////////////////////////////////////////////////////////////////////////

#include "include.h"

////////////////////////////////////////////////////////////////////////////////
// DEFINES ( CONSTANTS )
////////////////////////////////////////////////////////////////////////////////

/* Structure JSON Keys */
#define TIMESTAMP_KEY "\"ts\":"
#define MOISTURE_KEY "\"ms\":"

////////////////////////////////////////////////////////////////////////////////
// STRUCTURES
////////////////////////////////////////////////////////////////////////////////

/**
 * The Data structure stores all data relating to the external
 *  system's state. This is represented by the member fields of
 *  the structure.  
 */
typedef struct {
	int timestamp;
	float moisture_level;
} Data;

////////////////////////////////////////////////////////////////////////////////
// FUNCTION DEFINITIONS
////////////////////////////////////////////////////////////////////////////////

/**
 * Constructs a timestamp string from the system time
 */
char* get_timestamp();

/**
 * Constructs a moisture level string from the input structure
 * @param data --- The data struct to get the moisture int value from
 */
char* get_moisture_level( Data* data );

/**
 * Builds a JSON message from the member fields of a Data structure
 * @param data --- The input data structure on the system.
 */
char* build_msg( Data* data );


#endif


