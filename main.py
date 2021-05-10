from File import File
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


  """----------------------------------------------
     Create a log file
     ----------------------------------------------
  """
  create_log_file(logfile_name="hello.log")

  """----------------------------------------------
     Start time of the application.
     ----------------------------------------------
  """
  start_time_timer = timer()
  start_time_datetime = datetime.datetime.now()

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

  """----------------------------------------------
     Get the total runtime of the programm.
     ----------------------------------------------
  """
  time_hours, time_min, time_sec = total_runtime_with_timer(start_time_timer)
  total = total_runtime_with_datetime(start_time_datetime)
  print(time_hours,time_min,time_sec)
  
def create_log_file(logfile_name):
  # level: this will allow to log into the command line, otherwise the command line will only print the log warnings.
  # filname: This will create a logged inforation file.
  logging.basicConfig(filename=logfile_name, level=logging.INFO)
  logging.info("A new log file called {} has been created".format(logfile_name))

def total_runtime_with_timer(start_time_timer):
  # Log the total run time
  end_time = timer()
  seconds = end_time - start_time_timer
  time_min, time_sec = divmod(seconds, 60)
  time_hours, time_min = divmod(time_min, 60)
  logging.info("The total amount of time that the application ran is: {}"
                 .format("%d : hours : %02d minutes and %02d seconds" % (time_hours, time_min, time_sec)))
  return(time_hours, time_min, time_sec)

def total_runtime_with_datetime(start_time_datetime):
  end_time = datetime.datetime.now()
  total = end_time - start_time_datetime
  logging.info("The total amount of time that the application ran is: {}".format(total))
  return(total)

main()