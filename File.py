import os
from pathlib import Path
import logging
import sys
from Bio import SeqIO

""" ---------------------------------------------- 
    Create Class with functions for file handling
    ---------------------------------------------- 
"""
class File:
  # init of Class
  def __init__(self, path):
      self.__path = path

  def file_exist(self, absolute_path):
    """------------------------------------------------
       Check if the file exists
       ------------------------------------------------
    """
    try:
      logging.info("Checking if {} exists.".format(absolute_path))
      logging.info("Opening the file for reading {}".format(absolute_path))
      fileHandler = open(absolute_path)
      logging.info("File {} opened succesfully.".format(absolute_path))
      # Log the following message if no exception occurs.
      logging.info("File {} exists ...".format(absolute_path))
      # close the file.
      fileHandler.close()
      logging.info("Closed File {}  ...".format(absolute_path))
    except FileNotFoundError:
      # Print the following message if any error occurs
      print("File is not exist or accessible")
      logging.info("File not exist or accesible, Closing program")
      sys.exit(1)
    finally:
      # print the termination message
      logging.info("Done with file-exist check {}".format(absolute_path))

  """ ---------------------------------------------- 
      Getters and Setters
      The following code contains getter and setter to define the path name.
      If you want to add/delete a path, you can do this in a uniform way that's safe to use.
      ---------------------------------------------- 
  """
  @property
  def path(self):
    # return the path of your File object
    logging.info("Returning {}...".format(self.__path))
    return self.__path

  @path.setter
  def path(self, path):
    # set the path of your File object
    self.__path = path
    logging.info("Set the path of File object to {}...".format(self.__path))

  @path.deleter
  def path(self):
    # delete the path of your File object
    del self.__path
    logging.info("Deleted the path of File object {}...".format(self.__path))

  def get_basename_of_absolute_path(self, absolute_path):
    # Determine and return the basename, extracted from the path.
    logging.info("Get the basename of the absolute file path: {}".format(absolute_path))
    basename = os.path.basename(absolute_path)
    logging.info("{} is the basename of the {}.".format(basename, absolute_path))
    return(basename)

  def get_extension_of_absolute_path(self, absolute_path):
    # Determine and return the type of format (examples: .csv .fasta .fastq)
    logging.info("Get the file extension of the absolute file path: {}".format(absolute_path))
    name, extension = os.path.splitext(absolute_path)
    logging.info("{} is the file extension of {}".format(extension, absolute_path))
    return(name, extension)

  def is_fasta(self, absolute_path):
    # check the type of format
    logging.info("Checking if input path {} is fasta file.".format(absolute_path))
    with open(absolute_path, "r") as handle:
        fasta = SeqIO.parse(handle, "fasta")
        return any(fasta)  # False when `fasta` is empty, i.e. wasn't a FASTA file
  
  def print_record_id(self, absolute_path):
    #Print the record id's
    logging.info("Start record id")
    for record in SeqIO.parse(absolute_path, "fasta"):
      print(record.id)
    logging.info("Finished record id")



class Logfile(File):
  pass