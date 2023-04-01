from pytube import YouTube
from pytube import exceptions
import os
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--config_url", help="Path to config file")



# list of youtube links. Please change this 
LIST_VIDEOS = ["-xNN-bJQ4vI", "-9YJppTxIDM", "93nxeejhPkU", "6TlW1ClEBLY", "9XR2CZi3V5k", "AX4hWfyHr5g"]

def download_video(url, output_folder = './', highest = True, save=True):
  """_summary_

  Args:
      url (_type_): _description_
      output_folder (str, optional): _description_. Defaults to './'.
      highest (bool, optional): _description_. Defaults to True.
      save (bool, optional): _description_. Defaults to True.
  """

  try:
    yt = YouTube(url)
    _title = yt.title
    
    if highest:
      res = yt.streams.order_by("resolution").last()
    else:
      res = yt.streams.order_by("resolution").first()
    # create output folder 
    os.system("mkdir -p %s"%output_folder)
    # download video
    filename_ = res.default_filename.replace(" ", "_")
    
    if save:
      print ("Downloading... %s"%res.default_filename)
      res.download(output_path=output_folder, filename=filename_)
    else:
      print ("Nothing to be done...")

  except exceptions.VideoUnavailable:
    print ("Youtube link is unavailable. Plese check the url.")
  except Exception as e:
    print ("Something went wrong: " + e)


if __name__ == "__main__":

  args = parser.parse_args()

  # load json file with the links            
  try:
    input_file_data = json.load(open(args.config_url))
    # iterate over Youtube links
    base_url = input_file_data['URLS'][0]['base_url']
    folder_ = input_file_data['URLS'][0]['folder']
    for url_ in input_file_data['URLS'][0]['urls']:
      url = base_url + url_
      print (url)
      download_video(url, output_folder=folder_, save=True)
  except Exception as e:
    print (e)
  
  

