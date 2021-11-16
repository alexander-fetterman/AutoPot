######################################################################
## IMPORTS
######################################################################
from configparser import ConfigParser
import psycopg2 as psql

######################################################################
## CLASSES
######################################################################

class Database:
    ######################################################################
    ## CONSTANTS
    ######################################################################
    DATABASE_TYPE = 'postgresql'

    ######################################################################
    ## MEMBER VARIABLES
    ######################################################################
    

    ######################################################################
    ## CONSTRUCTORS
    ######################################################################
    
    '''
    Creates a Database object. Does not connect to any database. Defines
     all member variables. Set the connection member variable to null.
    @param filename --- The initialization filename which will be used for connection
    '''
    def __init__( self, filename ):
        self.FILENAME = filename

    ######################################################################
    ## PRIVATE METHODS
    ######################################################################

    '''
    Parses the internally stored config file, and returns the parameters
      necessary to connect to a database.
    '''
    def __parse_config( self ):
        # create a parser
        parser = ConfigParser()
        
        # read config file
        parser.read( self.FILENAME )

        # get section, default to postgresql
        db = {}
        if parser.has_section( self.DATABASE_TYPE ):
            params = parser.items( self.DATABASE_TYPE )
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format( self.DATABASE_TYPE, self.FILENAME ))

        return db
    
    '''
    Builds the string representation of the query to insert 
    '''
    def build_insert_query():
        raise Exception( 'Method not yet implemented' )

    ######################################################################
    ## PUBLIC METHODS
    ######################################################################


    '''
    Connects to a database and stores the connection within this 
     object. This is required before calling any DB operations.
    '''
    def db_connect( self ):
        # Connect to the database using the config file
        self.connection = psql.connect( **self.__parse_config() )

        # Open a cursor to the database
        self.cursor = self.connection.cursor()

    '''
    Inserts a tuple into the database
    '''
    def insert_values( self, timestamp, moisture_level ):
        # Perform the insert operation
        self.cursor.execute( "INSERT INTO sensordata VALUES( {ts}, {ms} )".format( ts = timestamp, ms = moisture_level ) )
        
        # Commit the insert operation
        self.connection.commit()






