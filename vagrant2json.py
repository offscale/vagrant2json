#!/usr/bin/env python

from itertools import izip_longest, ifilter, imap, takewhile, izip, cycle
from json import dump
from sys import stdin, stdout
from argparse import ArgumentParser, FileType

__author__ = 'Samuel Marks'
__version__ = '0.0.1'


def _build_parser():
    parser = ArgumentParser(description='Convert Vagrant `--machine-readable` output to JSON',
                            usage='E.g.: `vagrant global-status --machine-readable | python -m vagrant2json`')
    parser.add_argument('infile', nargs='?', type=FileType('r'), default=stdin, help='[stdin]')
    parser.add_argument('outfile', nargs='?', type=FileType('w'), default=stdout, help='[stdout]')
    parser.add_argument('--ugly', action='store_true', help='Compress JSON output [False]')
    parser.add_argument('--version', action='version', version='%(prog)s {}'.format(__version__))
    return parser


def vagrant2dict(io):
    return (lambda get_last_col: (
        lambda headers: tuple(
            imap(dict, izip_longest(
                *([izip(cycle(headers),
                        ifilter(lambda r: r is not None and not r.endswith('\\n"vagrant destroy 1a2b3c4d'),
                                imap(get_last_col, io)))] * len(headers)))))
    )(tuple(ifilter(None, imap(get_last_col, takewhile(lambda c: c[-5] != '-', io))))))(
        lambda row: (lambda r: r if r else None)(row[row.rfind(',') + 1:-2].rstrip()))


if __name__ == '__main__':
    args = _build_parser().parse_args()
    dump(vagrant2dict(args.infile), args.outfile, ensure_ascii=False, check_circular=False, allow_nan=False,
         **({'sort_keys': True, 'indent': 4} if not args.ugly else {'separators': (',', ':')}))
    if not args.ugly:
        args.outfile.write('\n')
    args.outfile.close()
