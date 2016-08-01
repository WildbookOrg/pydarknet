#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Initially Generated By:
    python -m utool --tf setup_repo --repo=pydarknet --codedir=~/code --modname=pydarknet
"""
from __future__ import absolute_import, division, print_function, unicode_literals


def pydarknet_main():
    ignore_prefix = []
    ignore_suffix = []
    import utool as ut
    # allows for --tf
    ut.main_function_tester('pydarknet', ignore_prefix, ignore_suffix)

if __name__ == '__main__':
    """
    Usage:
        python -m pydarknet --tf <funcname>
    """
    print('Running pydarknet main')
    pydarknet_main()