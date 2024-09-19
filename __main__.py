import os

from messages import *
from paths import *

from updater import *
from mgmt import *
from consolemgmt import *

def main():
    data_in()
    console_loop()
    data_out()


if __name__ == "__main__":
    main()