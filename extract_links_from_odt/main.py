#!/usr/bin/env python3

# library imports
import argparse
import logging
import sys

# third party imports
import logging_tree

# lirary imports
from extract_links_from_odt import application as application
from extract_links_from_odt import utils as utils

def main():
    # if we are being run as a real program

    parser = argparse.ArgumentParser(
        description="tool to extract the links out of a odt document",
        epilog="Copyright 2021-02-07 - Mark Grandi",
        fromfile_prefix_chars="@")

    parser.add_argument("--odt-file",
        dest="odt_file",
        type=utils.isFileType(True),
        required=True,
        help="The ODT file we want to extract links from")
    parser.add_argument("--output-file",
        dest="output_file",
        type=utils.isFileType(False),
        help="where to save the links we extract to")
    parser.add_argument("--log-to-file",
        dest="log_to_file",
        type=utils.isFileType(False),
        help="save the application log to a file as well as print to stdout")
    parser.add_argument("--filter",
        type=utils.regexType,
        help="only write urls that match this regex filter")

    parser.add_argument("--verbose",
        action="store_true",
        help="Increase logging verbosity")



    try:
        root_logger = logging.getLogger()

        parsed_args = parser.parse_args()


        # set up logging stuff
        logging.captureWarnings(True) # capture warnings with the logging infrastructure
        logging_formatter = utils.ArrowLoggingFormatter("%(asctime)s %(threadName)-10s %(name)-10s %(levelname)-8s: %(message)s")
        logging_handler = logging.StreamHandler(sys.stdout)
        logging_handler.setFormatter(logging_formatter)
        root_logger.addHandler(logging_handler)


        # set logging level based on arguments
        if parsed_args.verbose:
            root_logger.setLevel("DEBUG")
        else:
            root_logger.setLevel("INFO")

        if parsed_args.log_to_file:
            file_handler = logging.FileHandler(parsed_args.log_to_file, mode='a', encoding="utf-8")
            file_handler.setFormatter(logging_formatter)
            root_logger.addHandler(file_handler)

        root_logger.debug("argv: `%s`", sys.argv)
        root_logger.debug("Parsed arguments: %s", parsed_args)
        root_logger.debug("Logger hierarchy:\n%s", logging_tree.format.build_description(node=None))

        # run the application
        app = application.Application(parsed_args)
        app.run()

        root_logger.info("Done!")

    except Exception as e:
        root_logger.exception("Something went wrong!")
        sys.exit(1)