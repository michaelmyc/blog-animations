import argparse
import importlib.util
import shutil
import tomllib
from pathlib import Path

from manim import config

parser = argparse.ArgumentParser()

parser.add_argument("-c", "--config", help="Config file relative path")

args = parser.parse_args()

with open(args.config, "rb") as f:
    cfg = tomllib.load(f)

scene = importlib.import_module(cfg["import_module"])

config.media_dir = "./media"

if "frame_size" in cfg:
    config.frame_size = [int(elt) for elt in cfg["frame_size"].split(",")]
else:
    config.frame_size = 1920, 1080

if cfg["is_image"]:
    config.background_opacity = 0
    config.output_file = cfg["output_file_name"] + ".png"
else:
    config.frame_rate = cfg.get("frame_rate", 30)
    config.background_color = cfg.get("background_color", "#151b22")
    config.output_file = cfg["output_file_name"] + ".mp4"

config.preview = cfg.get("preview", False)

scene.FinalScene().render()

if not config.preview:
    shutil.copy(config.output_file, Path("..") / cfg["save_location"])
