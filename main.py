from get_file import File
import os

# The main
def main():
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
  
main()