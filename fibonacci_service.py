#!/usr/bin/env python

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'server'))

from serv import run_serv

if __name__ == "__main__":
	run_serv()
