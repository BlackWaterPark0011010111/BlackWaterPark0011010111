import sys

import getopt
# import argparse

# Sys.argv example
# def main():
#     if len(sys.argv) < 3:
#         print("Usage: python script.py <input_file> <output_file> [-v]")
#         sys.exit("Program terminated...")  # You can also pass a string

#     input_file = sys.argv[1]
#     output_file = sys.argv[2]

#     if len(sys.argv) == 4 and sys.argv[3] == "-v":
#         print(f"Input file: {input_file}")
#         print(f"Output file: {output_file}")
#         print("Verbose mode enabled")

#     # Perform actions based on arguments
#     # For example: read from input_file and write to output_file
#     # Example: python args_parse.py 'f1.py' 'f2.py' -v

# if __name__ == "__main__":
#     main()


# Getopt example
def main():
    input_file = ""
    output_file = ""
    verbose = False

    try:
        opts, args = getopt.getopt(
            sys.argv[1:], "hvi:o:", ["help", "verbose", "input=", "output="]
        )
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-v", "--verbose"):
            verbose = True
        elif opt in ("-i", "--input"):
            input_file = arg
        elif opt in ("-o", "--output"):
            output_file = arg

    if verbose:
        print(f"Input file: {input_file}")
        print(f"Output file: {output_file}")
        print("Verbose mode enabled")

    # Perform actions based on arguments
    # For example: read from input_file and write to output_file
    # Example: python args_parse.py -i 'h.py' -o 'h2.py' --verbose on Windows


def usage():
    print("Usage: python script.py -i <input_file> -o <output_file> [-v]")
    print("Options:")
    print("  -h, --help      Display this help message")
    print("  -v, --verbose   Enable verbose mode")
    print("  -i, --input     Specify input file")
    print("  -o, --output    Specify output file")


if __name__ == "__main__":
    main()


# # ArgumentParser
# def main():
#     parser = argparse.ArgumentParser(description="Example Argument Parser")
#     parser.add_argument(
#         "--verbose", "-v", action="store_true", help="Enable verbose mode"
#     )
#     parser.add_argument("input_file", type=str, help="Input file path")
#     parser.add_argument("output_file", type=str, help="Output file path")

#     args = parser.parse_args()

#     input_file = args.input_file
#     output_file = args.output_file

#     if args.verbose:
#         print("Verbose mode enabled")
#         print(f"Input file: {input_file}")
#         print(f"Output file: {output_file}")

#     # Perform actions based on arguments
#     # For example: read from input_file and write to output_file
#     # python args_parse.py -v "f1.py" "f2.py" on Windows


# if __name__ == "__main__":
#     main()
