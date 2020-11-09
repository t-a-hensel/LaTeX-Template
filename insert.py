#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2013-2014, 2016 Martin Ueding <dev@martin-ueding.de>
# Licensed under The GNU Public License Version 2 (or later)

import argparse
import shlex
import json

import jinja2

def render_template(template_fn, data_fn, output_fn, options_fn):
    # Setting up Jinja
    env = jinja2.Environment(
        "%<", ">%",
        "<<", ">>",
        "/*", "*/",
        loader=jinja2.FileSystemLoader(".")
    )
    template = env.get_template(template_fn)

    with open(data_fn) as handle:
        data = json.load(handle)
        data['git_version'] = options_fn#XXX übergebe hier zusätzliche daten als json
        data['color_setup'] = options_fn

    # Rendering LaTeX document with values.
    with open(output_fn, "w") as handle:
        handle.write(template.render(**data))
        

def arg_parser_shlex(string):
    """Argument parser for shell token lists."""
    try:
        return shlex.split(string)
    except ValueError as e:
        raise argparse.ArgumentTypeError(str(e)) from None

def main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("template", help="LaTeX template with Jinja 2")
    parser.add_argument("data", help="JSON encoded data file")
    parser.add_argument("output", help="Output LaTeX File")
#	XXX add the submission argument here
    parser.add_argument(
        '--submission-args', metavar='ARGS', #type=arg_parser_shlex,
        help='Additional command-line arguments for submission rules.'
        ' This will be parsed and split using POSIX shell rules.')

    options = parser.parse_args()
    options.submission_args = options.submission_args #or []

    render_template(options.template, options.data, options.output, options.submission_args)

if __name__ == '__main__':
    main()
