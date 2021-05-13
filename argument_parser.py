import argparse

INFO = 'This pipeline performs an assembly on PacBio Sequel data'


def parse_args():
    """
    Argument parser
    :return: args: All arguments are parsed to the args.
    """
    parser = argparse.ArgumentParser(description=INFO,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("--logname",
                        type=str,
                        required=True,
                        default=None,
                        help="The name of the log file.")
  

    parser.add_argument("--inputfile",
                        type=str,
                        required=True,
                        default="C:/Users/gerwi/OneDrive/Documents/GitHub/simple-bi-commands/GCF_001272835.1_ASM127283v1_genomic.fna",
                        help="The input file")

    # parse all arguments
    args = parser.parse_args()
    return args
