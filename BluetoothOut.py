#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 00:48:10 2018

@author: pi
"""

from bluetooth import discover_devices

nearby_devices = discover_devices(lookup_names=True)
