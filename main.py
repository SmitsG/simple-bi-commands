from File import File
import argument_parser
import os
import logging
import time
from timeit import default_timer as timer
import datetime
import sys
##############################################################
# Simple bio-informatics tools
# Author: Gerwin Smits
__version__ = '0.1 (Gerwin)'
##############################################################

# The main
def main():

  # Receive the input arguments from command line.
  args = argument_parser.parse_args()

  """----------------------------------------------
     Create a log file
     ----------------------------------------------
  """
  logger = create_log_file(args.logname)
  logger.info("inputfile: {}".format(args.inputfile))

  """----------------------------------------------
     Start time of the application.
     ----------------------------------------------
  """
  logging.info("Set starttime") # you have to double check this.
  start_time_timer = timer()
  start_time_datetime = datetime.datetime.now()

  """ ----------------------------------------------
      Create an object my_file of the File Class in get_file.py.
      You will give your absolute_path, which can be changed later.
      Check if the object exist. If the object doesn't exist, give an error and close the program.
      -----------------------------------------------
  """ 
  try:
    my_file = File(args.inputfile)
    logging.info("Created an object {} of file class".format(my_file))
  except NameError:
    logging.info("A NameError occured")
    logging.info("Closing programm")
    sys.exit(1)

  """ -----------------------------------------------
      Check if the file on the absolute file path exist, otherwise you can quit the program immidately.
      ------------------------------------------------
  """
  my_file.file_exist(my_file.path)

  """ -----------------------------------------------
      Get the basename of the absolute path
      -----------------------------------------------
  """
  basename = my_file.get_basename_of_absolute_path(my_file.path)

  """ -----------------------------------------------
      Get the file extension of the absolute path
      -----------------------------------------------
  """
  name, extension = my_file.get_extension_of_absolute_path(my_file.path)

  """ -----------------------------------------------
      Check the format of the file
      -----------------------------------------------
  """
  any = my_file.is_fasta(my_file.path)
  logging.info("Fasta format?: {}".format(any))

  """ -----------------------------------------------
      Print the record id's
      -----------------------------------------------
  """
  my_file.print_record_id(my_file.path)

  """----------------------------------------------
     Get the total runtime of the programm.
     ----------------------------------------------
  """
  time_hours, time_min, time_sec = total_runtime_with_timer(start_time_timer)
  total = total_runtime_with_datetime(start_time_datetime)
  
def create_log_file(logname):
  # level: this will allow to log into the command line, otherwise the command line will only print the log warnings.
  # filname: This will create a logged inforation file.
  # Asctime adds a human readable time to the log file.\
  # Filemode='w' so the log file doesn't append.
  logger = logging.getLogger(__name__)
  
  logger.setLevel(logging.INFO)

  formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

  file_handler = logging.FileHandler(logname)

  file_handler.setFormatter(formatter)

  logger.addHandler(file_handler)

  # logging.basicConfig(filename=logname, level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s', filemode='w')

  logging.info("A new log file called {} has been created".format(logname)) # you have to double check this.

  return (logger)

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

# WARNING: Found ~/.bashrc but no ~/.bash_profile, ~/.bash_login or ~/.profile.
# python main.py --logname hello.log --inputfile C:/Users/gerwi/OneDrive/Documents/GitHub/simple-bi-commands/GCF_001272835.1_ASM127283v1_genomic.fna
# conda install -n base -c conda-forge mamba