####
# Author: Abhimanyu Anand
# email: manyu252@gmail.com
# Date: 4 September 2023
# Usage: python3 read_dicom_file.py --file <path_to_dicom_file>
# To kill the program, open another terminal and 
#    type: ps aux | grep read_dicom_file.py
#    then: kill -9 <pid>
####

import matplotlib.pyplot as plt
from pydicom import dcmread
import argparse
import os

parser = argparse.ArgumentParser(description='Read a DICOM dataset and display it one after the other.')
parser.add_argument('--folder', '-f', metavar='folder', type=str, nargs='+',
                    help='folder of DICOM files')

args = parser.parse_args()
folder = args.folder[0]

for file in os.listdir(folder):
    filename = os.fsdecode(file)

    if filename.endswith(".dcm"):
        file = os.path.join(folder, filename)
        ds = dcmread(file)
        arr = ds.pixel_array
        plt.imshow(arr, cmap="gray")
        plt.show()
        continue