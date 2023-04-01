# 360-Video-DASH-Dataset

We present a software tool to source, tile, encode, and dashify VR videos. In addition, we developed a dataset composed of 9 VR videos encoded with seven tiling configurations, four segment durations, and up to four different bitrates. A corresponding tile size dataset is also provided, which can be utilised to power network simulations or trace-driven emulations.

Authors: Yogita Jadhav, Ahmed H. Zahran <a.zahran@cs.ucc.ie>, Darijo Raca <draca@etf.unsa.ba>

Contents:

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [360 Video Tiled Dataset](#360 Video Tiled Dataset)
- [Caveats](#caveats)
- [Acknowledgements](#acknowledgements)


## Requirements

- Python
- Kvazaar
- Pytube
- GPAC


## Installation

Clone the repository
	
	git clone https://github.com/darijo/360-Video-DASH-Dataset.git

Install Kvazaar HEVC encoder

	https://github.com/ultravideo/kvazaar

Install Pytube library
	
	https://pytube.io/en/latest/index.html

Install GPAC multimedia framework (build from source)
	https://github.com/gpac/gpac


## Usage

There are three main steps for creation of 360 Tiled DASH Videos

  - Download 360 untiled, non-dashed videos from YouTube
  - Prepare configuration outlining segment duration, bitrate ladder and tilling configuration for each downloaded video
  - Encode the downloaded videos into 360 tiled dashed video sequneces

### Step 1: Download 360 videos from Youtube

The following command downloads the video with the highest bitrate and resolution. The tool is designed to download the provided video IDs using the ___pytube___ library. It is important to ensure that the used libraries are up to date to avoid issues related to Google API updates. If the tool failed to download, an error message is printed to the screen. 

```console

$ python video_downloads.py --path_to_config_file 

```

The template for configuration file is shown below

```json

{"URLS":[
{
    "base_url": "https://www.youtube.com/watch?v=",
    "urls": ["-xNN-bJQ4vI", "-9YJppTxIDM", "93nxeejhPkU", "6TlW1ClEBLY", "9XR2CZi3V5k", "AX4hWfyHr5g"],
    "folder": "dataset"
}
]}

```

The configuration file defines the base URL,the list of videos to download, and the location where to save downloaded videos.

### Step 2: Generate configuration file for each video

The following command creates a configuration file specifying the tiling configuration, segment durations, and quality bitrate used to generate the 360 dashed tiled video dataset. 

```console

$ python gen_config_files.py --path path to folder with 360 videos --output_path location where to store config file 

```

Lower limit for quality bitrates is set to 4Mbps, while the maximum bitrate is set to native encoded bitrate (obtained using the ___mediainfo___ command) of the video file. Intermediate-quality bitrates are calculated so that the subsequent bitrate has a value 50\% higher compared to the previous one. For the tile configuration, we tile the video in seven configurations: **3x2**, **3x3**, **4x2**, **4x4**, **5x5**, **6x4**, and **8x5**. Furthermore, we use the 1s, 2s, 4s, and 6s for the duration of the segment. An example of a configuration file is depicted below

```json

{"Input":[
{
    "Name": "Closet_SetTourIn360VRSCREAMQUEENS.webm",
    "Configurations": ["3x2", "3x3", "4x2", "4x4", "5x5", "6x4", "8x5"],
    "Bitrates": [5807407, 8711111, 13066666, 19600000],
    "Segment_Durations":["1000", "2000", "4000", "6000"]
}]}

```

### Step 3: Encoding videos into 360 tiled dashed videos

The following command creates 360 dashed tiled videos based on the previously created configuration file.

```console

$ python encoding.py  

```

**NOTE**

Script encoding.py and  input.json file need to be in the same folder in order to above command work

## 360 Video Tiled Dataset

Real VR datset including 9 videos is available at https://tinyurl.com/3brdmm4s
