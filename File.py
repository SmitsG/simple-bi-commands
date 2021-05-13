import os
from pathlib import Path
import logging

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
    finally:
      # print the termination message
      logging.info("Opening the file for reading {}".format(absolute_path))

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
    basename = os.path.basename(absolute_path)
    return(basename)

  def get_extension_of_absolute_path(self, absolute_path):
    # Determine and return the type of format (examples: .csv .fasta .fastq)
    name, extension = os.path.splitext(absolute_path)
    return(name, extension)

  def is_fasta(absolute_path):
    # check the type of format
    with open(absolute_path, "r") as handle:
        fasta = SeqIO.parse(handle, "fasta")
        return any(fasta)  # False when `fasta` is empty, i.e. wasn't a FASTA file

class Logfile(File):
  pass