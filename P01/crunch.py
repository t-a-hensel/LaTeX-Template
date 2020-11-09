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

def job_density_data_BEC(T):
    data = np.loadtxt('DATA/DensityDataBEC.txt')
    time = data[:, 0]
    density = data[:, 1] * 1e-6

    np.savetxt('_build/xy/DensityDataBEC.txt',
               np.column_stack([time, density]))
    T['density_data_BEC_table'] = list(zip(
        siunitx(time),
        siunitx(density),
    ))
    T['init_density_BEC'] = siunitx(density[0], density[1])

def job_density_data_THE(T):
    data = np.loadtxt('DATA/DensityDataTHE.txt')
    time = data[:, 0]
    density = data[:, 1] * 1e-6

    np.savetxt('_build/xy/DensityDataTHE.txt',
               np.column_stack([time, density]))

def job_error_data_BEC(T):
    data = np.loadtxt('DATA/ErrorDataBEC.txt')
    time = data[:, 0]
    error = data[:, 1]

    np.savetxt('_build/xy/ErrorDataBEC.txt',
               np.column_stack([time, error]))

def job_error_data_THE(T):
    data = np.loadtxt('DATA/ErrorDataTHE.txt')
    time = data[:, 0]
    error = data[:, 1]

    np.savetxt('_build/xy/ErrorDataTHE.txt',
               np.column_stack([time, error]))

def job_dkc_BEC(T):
    data = np.loadtxt('DATA/dkc_BEC.dat')
    time = data[:, 0]
    size = data[:, 1]

    np.savetxt('_build/xy/dkc_BEC.dat',
               np.column_stack([time, size]))

def job_dkc_CLS(T):
    data = np.loadtxt('DATA/dkc_CLS.dat')
    time = data[:, 0]
    size = data[:, 1]

    np.savetxt('_build/xy/dkc_CLS.dat',
               np.column_stack([time, size]))

def job_nodkc_BEC(T):
    data = np.loadtxt('DATA/nodkc_BEC.dat')
    time = data[:, 0]
    size = data[:, 1]

    np.savetxt('_build/xy/nodkc_BEC.dat',
               np.column_stack([time, size]))

def job_nodkc_CLS(T):
    data = np.loadtxt('DATA/nodkc_CLS.dat')
    time = data[:, 0]
    size = data[:, 1]

    np.savetxt('_build/xy/nodkc_CLS.dat',
               np.column_stack([time, size]))

def test_keys(T):
    '''
    Testet das dict auf Schlüssel mit Bindestrichen.
    '''
    dash_keys = []
    for key in T:
        if '-' in key:
            dash_keys.append(key)

    if len(dash_keys) > 0:
        print()
        print('**************************************************************')
        print('* Es dürfen keine Bindestriche in den Schlüsseln für T sein! *')
        print('**************************************************************')
        print()
        print('Folgende Schlüssel enthalten Bindestriche:')
        for dash_key in dash_keys:
            print('-', dash_key)
        print()
        sys.exit(100)


def main():

    T = {}

    # We use bootstrap and obtain different results every single time. This is
    # bad, therefore we fix the seed here.
    random.seed(0)

    parser = argparse.ArgumentParser()
    options = parser.parse_args()

    job_density_data_BEC(T)
    job_density_data_THE(T)
    job_error_data_BEC(T)
    job_error_data_THE(T)
    job_dkc_BEC(T)
    job_dkc_CLS(T)
    job_nodkc_BEC(T)
    job_nodkc_CLS(T)

    test_keys(T)
    with open('_build/template.js', 'w') as f:
        json.dump(dict(T), f, indent=4, sort_keys=True)

    pp = pprint.PrettyPrinter()
    print()
    print('Content in T dict:')
    pp.pprint(T)



if __name__ == "__main__":
    main()
