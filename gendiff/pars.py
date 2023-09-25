import json
import deepdiff


dict1 = json.load(open('/home/roodmann/Dev/file1.json'))
dict2 = json.load(open('/home/roodmann/Dev/file2.json'))

print(deepdiff.DeepDiff(dict1, dict2))
#def compare_dict(data1, data2):
    #equal = all([data1[key] == data2[key] for key in data1.keys() if key in data2])
    #return equal

#print(compare_dict(dict1, dict2))

