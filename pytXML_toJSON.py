import xmltodict
import pprint
import json
import requests

def xml_toJSON(url):
    my_url = requests.get(url) 
    #join the byte stream into a single string after removing "b..."
    x = ''.join([str(e)[2:-1] for e in my_url])
    # remove all the \n and \r
    x = x.replace(r"\n","")
    x = x.replace(r"\r","")
    #for readability we should prettify JSON while stringification
    return json.dumps(xmltodict.parse(x), indent = 2)

f = open('JSON_Output.json','w')
f.write(xml_toJSON("https://www.crosscountrysearch.com/careermd"))
f.close()





    

