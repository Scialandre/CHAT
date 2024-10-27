import os

from messages import *
from paths import *

from updater import *
from mgmt import *
from consolemgmt import *
from advmgmt import *

def main():
    adv_data_in()
    console_loop()
    data_out()
    adv_data_out()


if __name__ == "__main__":
    main()