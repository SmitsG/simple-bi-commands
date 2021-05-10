import argparse

INFO = 'This pipeline performs an assembly on PacBio Sequel data'


def parse_args():
    """
    Argument parser
    :return: args: All arguments are parsed to the args. The arguments will be presented in CamelCase.
    """
    parser = argparse.ArgumentParser(description=INFO,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("--inputFile",
                        type=str,
                        required=True,
                        default=None,
                        help="The input file(full path), could be in BAM, mBAM or fastq format.,"
                             "default = None")
