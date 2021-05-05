from get_file import File
import os

# The main
def main():
  # give your absolute path
  absolute_path = "C:/Users/gerwi/OneDrive/Documents/example.csv" # Obviously not FASTA

  """ Step 1. create an object my_file of the File Class in get_file.py.
      You will give your absolute_path, which can be changed later.
  """  
  my_file = File(absolute_path)
  # step 2. get basename of the path
  basename = my_file.get_basename_of_absolute_path(my_file.path)
  print(basename)
main()