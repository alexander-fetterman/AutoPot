echo "Running startup script!"

# Run mosquitto in the background
echo "Starting mosquitto broker in the background"
mosquitto &
echo "Mosquitto now running in the background"

# Compile source code
gcc ~/c-code/mqtt_example.c -o ~/executables/autoCompile.out -l paho-mqtt3c

# Run source code
~/executables/autoCompile.out

