#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2013-2014, 2016 Martin Ueding <dev@martin-ueding.de>
# Licensed under The GNU Public License Version 2 (or later)

import argparse
import itertools
import json
import os
import pprint
import random
import sys

import matplotlib.pyplot as pl
import numpy as np
import scipy.interpolate
import scipy.misc
import scipy.ndimage.filters
import scipy.optimize as op
import scipy.stats
import scipy.special as sp
import mpl_toolkits.mplot3d.axes3d as p3

import shutil

from unitprint2 import siunitx
import bootstrap

SAMPLES = 100


def main():
    
    shutil.copy2('DATA/DensityDataBEC.txt', '_build/xy/')# target filename is /dst/dir/file.ext
    shutil.copy2('DATA/DensityDataTHE.txt', '_build/xy/')
    shutil.copy2('DATA/ErrorDataBEC.txt', '_build/xy/')
    shutil.copy2('DATA/ErrorDataTHE.txt', '_build/xy/')
    shutil.copy2('DATA/dkc_BEC.dat', '_build/xy/')
    shutil.copy2('DATA/dkc_CLS.dat', '_build/xy/')
    shutil.copy2('DATA/nodkc_BEC.dat', '_build/xy/')
    shutil.copy2('DATA/nodkc_CLS.dat', '_build/xy/')

if __name__ == "__main__":
    main()
