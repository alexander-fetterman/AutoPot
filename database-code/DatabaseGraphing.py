from database import Database
import matplotlib.pyplot as plt

######################################################################
## CONSTANTS
######################################################################

CLIENT_NAME = "pythonScript"
LOCAL_BROKER = "localhost"
DEMO_TOPIC = "/Demo"
FILENAME = "database.ini"

class Graphing:

    ######################################################################
    ## CONSTRUCTORS
    ######################################################################

    '''
    Creates a database connection and connect to the database
    '''
    def __init__( self ):
        # Create a database object and connect to the database
        self.database = Database( FILENAME )
        self.database.db_connect()

    ######################################################################
    ## PRIVATE MEMBER FUNCTIONS
    ######################################################################

    '''
    Takes as input a list of tuples as specified by the database,
     and returns a tuple (x, y)
    @param tuples --- The list of tuples from the database

    '''
    def __parse_tuples( self, tuples ):
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

    
    '''
    Internal function which gets tuples from the database
     and draws a graph
    '''
    def __graph( self, maxTuples=20 ):

        # Get the values in the database
        tuples = self.database.get_values( maxTuples )

        # Parse the tuples into x (timestamp) 
        #  and y (moisture) values
        x, y = self.__parse_tuples( tuples )

        # Graph the values (x, y)
        plt.figure()
        plt.plot( x, y )
        plt.show()

        # while( 1 ):
            
            # Get the values in the database
            # tuples = self.database.get_values( maxTuples )

            # Parse the tuples into x (timestamp) 
            #  and y (moisture) values
            # x, y = self.__parse_tuples( tuples )

            # Graph the values (x, y)
            # plt.plot( x, y )
            # plt.draw()        
            # plt.pause( 0.1 )
            # plt.clf()

    ######################################################################
    ## PUBLIC MEMBER FUNCTIONS
    ######################################################################

    '''
    Outward facing function which will fetch tuples from
     the database and graph them
    @param maxTuples --- The maximum number of tuples to graph
    '''
    def handle( self, maxTuples ):
        self.__graph( maxTuples )




