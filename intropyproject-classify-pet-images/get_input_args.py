#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#
# PROGRAMMER:
# DATE CREATED:
# REVISED DATE:
# PURPOSE: Create a function that retrieves the following 3 command line inputs
#          from the user using the Argparse Python module. If the user fails to
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse
import os
import os.path


# TODO 1: Define get_input_args function below please be certain to replace None
#       in the return statement with parser.parse_args() parsed argument
#       collection that you created with this function
#
def get_input_args():
    parser = argparse.ArgumentParser(
        description="it's for input the Command Line arguments for Image Folder 'CNN Model' and 'dogfile'"
    )
    parser.add_argument("--image_folder", default = 'AIPND-revision-master/intropyproject-classify-pet-images/pet_images', help="Image Folder path")
    parser.add_argument("--mdl", default = 'vgg', help="CNN model path")
    parser.add_argument("--dogfile", default = 'AIPND-revision-master/intropyproject-classify-pet-images/dognames.txt', help="dog file path")

    args = parser.parse_args()
    if not args.image_folder:
        args.image_folder = input("Enter the path to the image folder: ")
        if not os.path.isfile(args.image_folder):
            args.image_folder = "pet_images"
    if not args.mdl:
        args.mdl = input("Enter the CNN model type: ")
        if not os.path.isfile(args.mdl):
            args.mdl = "vgg"
    if not args.dogfile:
        args.dogfile = input("Enter the path to the dog file: ")
        if not os.path.isfile(args.dogfile):
            args.dogfile = "dognames.txt"
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to created and defined these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments. 
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object  
    """

    return args
