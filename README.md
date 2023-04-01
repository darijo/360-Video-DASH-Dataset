# 360-Video-DASH-Dataset

We present a software tool to source, tile, encode, and dashify VR videos. In addition, we developed a dataset composed of 9 VR videos encoded with seven tiling configurations, four segment durations, and up to four different bitrates. A corresponding tile size dataset is also provided, which can be utilised to power network simulations or trace-driven emulations.

Authors: Yogita Jadhav, Ahmed H. Zahran <a.zahran@cs.ucc.ie>, Darijo Raca <draca@etf.unsa.ba>

Contents:

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Logging](#logging)
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
    "urls": ["-xNN-bJQ4vI", "-9YJppTxIDM", 
    "93nxeejhPkU", "6TlW1ClEBLY", 
    "9XR2CZi3V5k", "AX4hWfyHr5g"],
    "folder": "dataset"
}
]}

```


