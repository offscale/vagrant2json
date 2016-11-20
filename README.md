vagrant2json
===============

Convert Vagrant `--machine-readable` output to JSON

## Install package

    pip install .

## Usage

    $ python -m vagrant2http --help
    usage: E.g.: `vagrant global-status --machine-readable | python -m vagrant2json`
    
    Convert Vagrant `--machine-readable` output to JSON
    
    positional arguments:
      infile      [stdin]
      outfile     [stdout]
    
    optional arguments:
      -h, --help  show this help message and exit
      --ugly      Compress JSON output [False]
      --version   show program's version number and exit
