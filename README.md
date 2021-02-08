# extract_links_from_odt

a script that extracts links from a OpenDocument Text file (`.odt` file)

## installation

`git` clone this repo

then run:

```plaintext

pip3 install poetry

cd <checkout_dir>

poetry shell

poetry install

python cli.py <arguments here>

```

## usage

```plaintext

PS C:\Users\auror\Code\personal\git\extract_links_from_odt> python cli.py --help
usage: cli.py [-h] --odt-file ODT_FILE [--output-file OUTPUT_FILE] [--log-to-file LOG_TO_FILE] [--filter FILTER] [--verbose]

tool to extract the links out of a odt document

optional arguments:
  -h, --help            show this help message and exit
  --odt-file ODT_FILE   The ODT file we want to extract links from
  --output-file OUTPUT_FILE
                        where to save the links we extract to
  --log-to-file LOG_TO_FILE
                        save the application log to a file as well as print to stdout
  --filter FILTER       only write urls that match this regex filter
  --verbose             Increase logging verbosity

Copyright 2021-02-07 - Mark Grandi

```

## example

```plaintext

PS C:\> python cli.py --odt-file "C:\Users\exampleuser\Desktop\example.odt" --output-file test.txt --filter "^https://clips.twitch.tv.*" --log-to-file thelog.log
2021-02-07T22:13:23.697753-08:00 MainThread root                 INFO    : opening file: `C:\Users\exampleuser\Desktop\example.odt`
2021-02-07T22:13:23.997432-08:00 MainThread root                 INFO    : found `304` links
2021-02-07T22:13:24.000472-08:00 MainThread root                 INFO    : `257` urls matched, `47` urls didn't match
2021-02-07T22:13:24.001434-08:00 MainThread root                 INFO    : Done!

```