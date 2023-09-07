#### 
# Author: Abhimanyu Anand
# email: manyu252@gmail.com
# Date: 7 September 2023
# Description: Read a Nifti file and display.
# Usage: python read_nifti_file.py --file <path of nifti file>
# To kill the program, open another terminal and
#    type: ps aux | grep read_nifti_file.py
#    then: kill -9 <pid>
####

import nibabel as nib
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='Read a Nifti file and display.')
parser.add_argument('--file', '-f', metavar='file', type=str, nargs='+',
                    help='Path of Nifti file')

args = parser.parse_args()

# Change the path to your path
path = args.file[0]
Nifti_img  = nib.load(path)
nii_data = Nifti_img.get_fdata()
nii_aff  = Nifti_img.affine
nii_hdr  = Nifti_img.header
print(nii_aff ,'\n',nii_hdr)
print(nii_data.shape)

if(len(nii_data.shape)==3):
   for slice_Number in range(nii_data.shape[2]):
       plt.imshow(nii_data[:,:,slice_Number ])
       plt.show()
if(len(nii_data.shape)==4):
   for frame in range(nii_data.shape[3]):
       for slice_Number in range(nii_data.shape[2]):
           plt.imshow(nii_data[:,:,slice_Number,frame])
           plt.show()
