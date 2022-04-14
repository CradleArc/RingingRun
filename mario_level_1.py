#!/usr/bin/env python
__author__ = 'justinarmstrong'

"""
This is an attempt to recreate the first level of
Super Mario Bros for the NES.

"""
# New Super Mario should be artistic, and this is ring game with notation play in map-moving

import sys
import pygame as pg
from data.main import main
import cProfile


if __name__=='__main__':
   main()
   pg.quit()
   sys.exit()