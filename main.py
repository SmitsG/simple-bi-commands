from get_file import File
import os
import logging
import time
from timeit import default_timer as timer
import datetime
##############################################################
# Simple bio-informatics tools
# Author: Gerwin Smits
__version__ = '0.1 (Gerwin)'
##############################################################

# The main
def main():

# Start time of the application.
  start_time = timer()
  start_time2 = datetime.datetime.now()

  """ ---------------------------------------------- 
      Step 1. give your absolute path
      ----------------------------------------------
  """ 
  absolute_path = "C:/Users/gerwi/OneDrive/Documents/GitHub/simple-bi-commands/GCF_001272835.1_ASM127283v1_genomic.fna" # Obviously not FASTA

  """ ----------------------------------------------
      Step 2. create an object my_file of the File Class in get_file.py.
      You will give your absolute_path, which can be changed later.
      -----------------------------------------------
  """ 
  print()
  my_file = File(absolute_path)

  """ -----------------------------------------------
    Step 3. Check if the file on the absolute file path exist, otherwise you can quit the program immidately.
      ------------------------------------------------
  """
  my_file.file_exist(my_file.path)

  """ -----------------------------------------------
    Step 4. Get the basename of the absolute path
    -----------------------------------------------
  """
  basename = my_file.get_basename_of_absolute_path(my_file.path)

  """ -----------------------------------------------
    Step 5. Get the file extension of the absolute path
    -----------------------------------------------
  """
  name, extension = my_file.get_extension_of_absolute_path(my_file.path)

  total_runtime(start_time, start_time2)
  

def total_runtime(start_time, start_time2):
# Log the total run time
  end_time = timer()
  seconds = end_time - start_time
  m, s = divmod(seconds, 60)
  h, m = divmod(m, 60)
  logging.info("The total amount of time that the application ran is: {}"
                .format("%d : hours : %02d minutes and %02d seconds" % (h, m, s)))

  end_time2 = datetime.datetime.now()
  total = end_time2 - start_time2
  logging.info("The total amount of time that the application ran is: {}".format(total))

main()