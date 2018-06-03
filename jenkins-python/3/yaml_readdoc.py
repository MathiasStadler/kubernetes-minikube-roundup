import yaml
print ("version of yaml ==> " + yaml.__version__)

stream = open("../yaml_readdoc.yml", "r")
doc = yaml.load(stream)

print (type(doc))
print (doc[0])
print (doc[1])
print (doc[2])


print (type(doc[0]))
print (type(doc[1]))
print (type(doc[2]))

txt1 = doc[0]["level_1"]
txt2 = doc[1]["level_1"]
txt3 = doc[2]["level_1"]

print (txt1)
print (txt2)
print (txt3)

stream.close
