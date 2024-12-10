import json



if __name__=="__main__":
  with open("test.json", "w") as json_file:
    json.dump({},json_file)
    
