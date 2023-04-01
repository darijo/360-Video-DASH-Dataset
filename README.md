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
	


## Usage

There are three main steps for creation of 360 Tiled DASH Videos

  - Download 360 untiled, non-dashed Videos from YouTube
  - Prepare configuration outlining segment duration, bitrate ladder and tilling configuration for each downloaded video
  - Encode the downloaded videos into 360 tiled dashed video sequneces
 



