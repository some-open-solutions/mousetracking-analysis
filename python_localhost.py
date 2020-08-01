import eel
import glob
import io
import json
import pygit2
import os
import platform
import shutil

from distutils.dir_util import copy_tree

eel.init('web') #allowed_extensions=[".js",".html"]
eel.start('index.html', port=8000)