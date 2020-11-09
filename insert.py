#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2013-2014, 2016 Martin Ueding <dev@martin-ueding.de>
# Licensed under The GNU Public License Version 2 (or later)

import argparse
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

#TODO:	-how to properly format git_version when (not given)-> should be in header...
#		-how to handle mutliple submission arguments, i.e. access the different entries?
#			Maybe just handle a complete dictionary?
#		-how to incorporate arxiv collector for submission?
#		-in the main makefile, 'make submission' throws the switch such that the gitversion is stored as one option. 
#			Is that a good way or is there a better way to do this?
    with open(data_fn) as handle:
        data = json.load(handle)
        if options_fn == None:
            data['git_version'] = ''#XXX übergebe hier zusätzliche daten als json
            data['header_setup'] = 'bibatend'
        else:
            data['git_version'] = options_fn#XXX which should be the git-version
            data['header_setup'] = 'color, bibatend'

    # Rendering LaTeX document with values.
    with open(output_fn, "w") as handle:
        handle.write(template.render(**data))

def main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("template", help="LaTeX template with Jinja 2")
    parser.add_argument("data", help="JSON encoded data file")
    parser.add_argument("output", help="Output LaTeX File")
    parser.add_argument(
        '--submission-args', metavar='ARGS', default=None,
        help='Additional command-line arguments for submission rules.')

    options = parser.parse_args()
    options.submission_args = options.submission_args #or []

    render_template(options.template, options.data, options.output, options.submission_args)

if __name__ == '__main__':
    main()
