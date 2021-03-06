from setuptools import setup, find_packages
import os
#from portscan import __version__

requires = ['argparse','socket']
from setuptools import setup, find_packages
here = os.path.abspath(os.path.dirname(__file__))
dist = setup(
    name='scanner',
    #version=__version__,
    version='1.1.1',
    description="A system for controlling process state under UNIX",
    author="Chris McDonough",
    author_email="chrism@plope.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite="supervisor.tests",
    entry_points={
        'console_scripts': [
            'scanner = portscan.portscan:main',
        ],
    },
)
