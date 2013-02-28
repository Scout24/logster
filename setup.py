#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='logster',
    version='0.0.1',
    description='Parse log files, generate metrics for Graphite and Ganglia',
    author='Etsy',
    url='https://github.com/etsy/logster',
    packages=[
        'logster',
        'logster/parsers'
    ],
    zip_safe=False,
    scripts=[
        'bin/logster'
    ],
    data_files=[('/etc/cron.d', ['cron.d/logster'])],
    license='GPL3',
)
