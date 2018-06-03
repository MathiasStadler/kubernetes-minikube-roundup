import yaml
print ("version of yaml ==> " + yaml.__version__)

stream = open("../yaml_readdocs.yml", "r")
docs = yaml.load_all(stream)
for doc in docs:
    for k, v in doc.items():
        print k, "->", v
    print "\n",
stream.close
