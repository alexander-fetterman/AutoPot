#include <stdio.h>
#include <wiringPiI2C.h>
#include <stdint.h>

/* ----- CONSTANTS ----- */
#define DEVICE_ID 0x48
#define CONFIG_REG 0x8583
#define READ_A0 0b


int main() {
	/* Set up i2c communication */
	int fd = wiringPiI2CSetup( DEVICE_ID );

	/* Error check */
	if( fd == -1 ) {
		printf( "Failted to initalize i2c communction\n" );
		return -1;
	}
	printf( "i2c communction initialized\n" );

	/* Read the current value in the config register */
	uint16_t config = wiringPiI2CReadReg16( fd, CONFIG_REG );
	printf( "Config Register: %x\n", config );
	
	/* Set the ADC to read from channel 0 (A0)  */
	wiringPiI2CWriteReg16( fd, CONFIG_REG, config & 0xFFFE );

	/* Read the current value in the config register */
	config = wiringPiI2CReadReg16( fd, CONFIG_REG );
	printf( "Config Register: %x\n", config );

	return 0;
}




