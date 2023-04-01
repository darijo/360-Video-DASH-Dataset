import subprocess
from os import listdir
from os.path import isfile, join
import re
import json
import os



# Overall bit rate                         : 17.3 Mb/s
REG_BITRATE = r"Overall bit rate\s+:\s+([0-9]+[\.?|\s?][0-9]+).*"




if __name__ == "__main__":

  onlyfiles = [f for f in listdir("./") if f.endswith('.webm')]


  print (onlyfiles)

  _file = open('input.json', 'w')
  _file.write('''{"Input":[''')
  final_str = str()
  for video_file in onlyfiles:
    
    process = subprocess.run(["mediainfo", "./" + video_file], capture_output=True)
    m = re.search(REG_BITRATE, process.stdout.decode())


    bitrate = -1
    if m:
      raw_val = m.group(1).replace(" ", ".")
      bitrate = float(raw_val)
    print ("Overall bitrate: %f"%bitrate)
     
    if bitrate < 4:
      print ("File: %s encoded with lower bitrate...skipping"%video_file)
      continue
    
    list_bitrate = []
 
    while bitrate > 4:

      list_bitrate.append(int(bitrate * (10**6)))
      bitrate = (bitrate / 1.5) 

    if list_bitrate[-1] / 1.5 >= 4*(10**6): 
      list_bitrate.append(4*(10**6))
    list_bitrate.sort()
    print (list_bitrate) 

    js = '"Bitrates": %s,' % json.dumps(list_bitrate)


    temp_conf = '''{
    "Name": %s,
    "Configurations": ["3x2","3x3","4x2","4x4","5x5"],
    %s
    "Segment_Durations":["1000", "2000", "4000", "6000"]
},'''

    temp_conf = temp_conf%("""\""""+ video_file+"""\"""", js)
    final_str += temp_conf

    #_file.write(temp_conf) 
  _file.write(final_str[:-1])
  _file.write(''']}''')
  _file.close()

