import os
import sys
import random
import subprocess
from datetime import datetime
from flask import Blueprint, render_template
bp = Blueprint('main', __name__)

scrape_cmd = 'instagram-scraper --maximum 30 --tag'
path_to_static_images = 'wedesign/static/images/'
instagram_tag = 'whoisunknown'


def what_minute_is_it() -> int:
    return datetime.time(datetime.now()).minute


class Timer:
    time = None # time is in minutes

    def __init__(self, time_in_mins):
        minutes = time_in_mins

    def set_time(self, time):
        self.time = time

    def get_time(self) -> int:
        return self.time


timer = Timer(what_minute_is_it())

def scrapeInstagram():
    # run scraping script on load if another minute has passed
    last_time = timer.get_time()
    curr_time = what_minute_is_it()

    if curr_time is not last_time:
        timer.set_time(curr_time)
        print('new minute {time}'.format(time=curr_time))
        
        # change directory to /static/images
        os.chdir( \
            os.path.join( \
                os.path.abspath(sys.path[0]), 
                path_to_static_images))

        # scrape from instagram
        subprocess.call(scrape_cmd.split(' ') + [instagram_tag])

    # get list of names from pulled images
    os.chdir( \
        os.path.join( \
            os.path.abspath(sys.path[0]), \
            path_to_static_images + instagram_tag))

    proc = subprocess.Popen('ls', stdout=subprocess.PIPE)
    instagram_images = proc \
        .stdout \
        .read() \
        .decode('utf-8') \
        .split('\n')

    # add url path to list of images
    instagram_images_paths = []
    for i, val in enumerate(instagram_images):
        if len(val) == 0:
            print("breaking out!")
            break
        if '.mp4' in val:
            print("breaking out!")
            break
        instagram_images_paths.append(instagram_tag + '/' + val)

    # randomize list and pick first 20 images
    random.shuffle(instagram_images_paths)
    instagram_images_paths = instagram_images_paths[0:20]

    return instagram_images_paths
 
def getTileImages():
    # change directory to /static/images/tiles
    os.chdir( \
        os.path.join( \
            os.path.abspath(sys.path[0]), 
            path_to_static_images + 'tiles'))

    proc = subprocess.Popen('ls', stdout=subprocess.PIPE)
    tile_images = proc \
        .stdout \
        .read() \
        .decode('utf-8') \
        .split('\n')

    tile_images_paths = []
    for i, val in enumerate(tile_images):
        if len(val) == 0:
            print("breaking out!")
            break
        tile_images_paths.append('tiles/' + val)

    random.shuffle(tile_images_paths)
    return tile_images_paths
    

@bp.route('/')
def main():

    # scape new images from instagram 
    instagram_images_paths = scrapeInstagram()

    # fetch all images from /images/tiles folder
    tile_images_paths = getTileImages()
   
    return render_template('index.html', 
            instagram_images_url=instagram_images_paths,
            tile_images_url=tile_images_paths)

