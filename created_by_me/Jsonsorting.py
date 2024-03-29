from collections import OrderedDict
import json

locs = [ {"lng":-79.425509,"lat": 43.70097},
 {"lng":-79.425445,"lat": 43.700768},
 {"lng":-79.424028,"lat": 43.697185},
 {"lng":-79.422462,"lat": 43.693337},
 {"lng":-79.4214,"lat": 43.690785},
 {"lng":-79.419833,"lat": 43.686882},
 {"lng":-79.418546,"lat": 43.683802},
 {"lng":-79.415102,"lat": 43.684539},
 {"lng":-79.412216,"lat": 43.685199},
 {"lng":-79.412881,"lat": 43.687177},
 {"lng":-79.41227,"lat": 43.687348},
 {"lng":-79.41242,"lat": 43.687674},
 {"lng":-79.412506,"lat": 43.687984},
 {"lng":-79.412677,"lat": 43.688651},
 {"lng":-79.409373,"lat": 43.689318},
 {"lng":-79.409437,"lat": 43.689458},
 {"lng":-79.407248,"lat": 43.689908},
 {"lng":-79.40506,"lat": 43.690327},
 {"lng":-79.402614,"lat": 43.690792},
 {"lng":-79.400854,"lat": 43.691149},
 {"lng":-79.401155,"lat": 43.692049},
 {"lng":-79.402034,"lat": 43.694206},
 {"lng":-79.402313,"lat": 43.695106},
 {"lng":-79.402313,"lat": 43.695509},
 {"lng":-79.404652,"lat": 43.695028},
 {"lng":-79.405811,"lat": 43.698069},
 {"lng":-79.409072,"lat": 43.699232},
 {"lng":-79.409351,"lat": 43.699899},
 {"lng":-79.40933,"lat": 43.700055},
 {"lng":-79.410939,"lat": 43.704103},
 {"lng":-79.414308,"lat": 43.703359},
 {"lng":-79.420037,"lat": 43.702133},
 {"lng":-79.425509,"lat": 43.7009}]

json_formatted_str = json.dumps(locs, sort_keys=True,)
print("\n")
print(json_formatted_str)
print("\n")