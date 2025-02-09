"""
The command-line interface for the ast version of the types remover
"""
import argparse
from . import remove_types_ast


def main():
    parser = argparse.ArgumentParser(
        description="types remover"
    )
    parser.add_argument(
        "path", type=str,
        help="Path to a file that\' going to be stripped "
    )
    parser.add_argument(
        "--output", "-o",
        help="name of the output file. defaults to output.py"
    )
    args = parser.parse_args()
    remove_types_ast(args.path, output_file_path=args.output)
    print("types stripped successfully")

if __name__ == "__main__":
    main()