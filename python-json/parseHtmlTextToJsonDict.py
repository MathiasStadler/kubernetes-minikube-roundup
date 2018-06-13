
import json

# Read JSON file
with open('./test.html') as data_file:

    dump = json.dumps(data_file)
    data_loaded = json.loads(dump)
