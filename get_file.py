import os

# Class with functions for file handling
class File:
  def __init__(self, path):
    self.__path = path

  """ 
  1. The following code contains getter and setter to define the path name.
  If you want to add/delete a path, you can do this in a uniform way that's safe to use.
  """
  # return the path of your File object
  @property
  def path(self):
    return self.__path
  # set the path of your File object
  @path.setter
  def path(self, path):
    self.__path = path
  # delete the path of your File object
  @path.deleter
  def path(self):
    print("deleter of x called")
    del self.__path

# Determine and return the basename, extracted from the path.
  def get_basename_of_absolute_path(self, absolute_path):
    basename = os.path.basename(absolute_path)
    return(basename)
# Determine and return the type of format (examples: .csv .fasta .fastq)
  def get_extension_of_absolute_path(self, absolute_path):
    name, extension = os.path.splitext(absolute_path)
    return(name, extension)

# check the type of format
    def is_fasta(filename):
      with open(filename, "r") as handle:
          fasta = SeqIO.parse(handle, "fasta")
          return any(fasta)  # False when `fasta` is empty, i.e. wasn't a FASTA file

  def file_exist(self, absolute_path):
    try:
      # Open the file for reading
      fileHandler = open(absolute_path)
      # Print the following message if no exception occurs
      print("File exists")
      # close the file
      fileHandler.close()
    except FileNotFoundError:
      # Print the following message if any error occurs
      print("File is not exist or accessible")
    finally:
      # print the termination message
      print("End of the program")




  # @property
  # def abs_path(self):
  #    print("setter of absolute path called")
  #    self._x = self.abs_path
  #    return self._x
  # @abs_path.setter
  # def abs_path(self, abs_path):
  #    print("getter of x called")
  #    return self.abs_path