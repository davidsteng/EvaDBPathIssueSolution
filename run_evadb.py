# Import the EvaDB package
import evadb
#import evadb.constants
import warnings
warnings.filterwarnings("ignore")

from evadb.configuration.constants import EvaDB_INSTALLATION_DIR

# Connect to EvaDB and get a database cursor for running queries
cursor = evadb.connect().cursor()

print(cursor.query("SHOW FUNCTIONS").df())
temp = input("Method Type: ")

if int(temp) == 1:
    # Method 1 of Accessing Functions
    cursor.query("DROP FUNCTION IF EXISTS ChatGPTTest;").df()
    cursor.query(f"""
        CREATE FUNCTION ChatGPTTest
        IMPL '{evadb.constants.DBFUNCTIONS}/chatgpt.py'
    """).df()
    print("evadb function accessible through Constant")

if int(temp) == 2:
    # Method 2 of Accessing Functions
    cursor.query("DROP FUNCTION IF EXISTS SiftFeatureExtraction;").df()
    cursor.query(f"""
        CREATE FUNCTION SiftFeatureExtraction
        IMPL 'DBFUNCTIONS.sift_feature_extractor.py'
    """).df()
    print("evadb function accessible through Functions Parser")

print("end")
