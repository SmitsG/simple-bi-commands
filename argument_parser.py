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
                        default="hello.log",
                        help="The name of the log file.")
  # parse all arguments
    args = parser.parse_args()

    return args
