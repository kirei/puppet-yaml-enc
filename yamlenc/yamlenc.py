#!/usr/bin/env python3
#
# Copyright (c) 2016, IPnett AS
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


"""YAML-based Puppet ENC (External Node Classifier)"""

import sys
import re
import argparse
import yaml

DEFAULT_CONF = '/etc/puppet/enc.yaml'
DEFAULT_NAME = 'DEFAULT'


class YamlENC(object):
    """Simple YAML-based Puppet ENC"""

    def __init__(self, filename):
        self.nodes_re = []
        self.nodes_exact = {}
        self.default_attrs = {}

        encstream = open(filename, "r")
        encdata = yaml.load_all(encstream)

        for yamldoc in encdata:
            for node_re_str, node_attrs in yamldoc.items():
                node_validate(node_re_str, node_attrs)
                if node_re_str == DEFAULT_NAME:
                    self.default_attrs = node_attrs
                else:
                    try:
                        node_re = re.compile(node_re_str)
                    except re.error:
                        raise Exception("Failed to compile RE: %s"
                                        % node_re_str)
                    self.nodes_re.append({'re': node_re, 'attrs': node_attrs})
                    self.nodes_exact[node_re_str] = {'attrs': node_attrs}

    def default(self):
        """Return default attributes"""
        return self.default_attrs

    def lookup(self, nodename):
        """Look up ENC by nodename"""

        # try exact match
        if nodename in self.nodes_exact:
            return self.nodes_exact[nodename]['attrs']

        # try RE match
        for node in self.nodes_re:
            if node['re'].match(nodename):
                return node['attrs']

        # resort to default attributes
        return self.default_attrs


def node_validate(node_re_str, node_attrs):
    """Validate node attributes"""
    if 'environment' in node_attrs or 'classes' in node_attrs:
        return
    else:
        raise Exception("Missing mandatory attribute for node '%s'"
                        % node_re_str)


def main():
    """ Main function """

    parser = argparse.ArgumentParser(description='Puppet YAML ENC')

    parser.add_argument('nodename', metavar='nodename', nargs=1,
                        help='nodename')

    parser.add_argument("--conf", metavar='filename',
                        help='configuration file')
    parser.set_defaults(conf=DEFAULT_CONF)

    parser.add_argument("--debug", action='store_true')
    parser.set_defaults(debug=False)

    args = vars(parser.parse_args())
    debug = args['debug']
    conf = args['conf']

    try:
        if debug:
            print >> sys.stderr, "Using configuration file %s" % conf
        enc = YamlENC(conf)
    except IOError:
        print >> sys.stderr, "Failed to parse configuration file %s" % conf
        sys.exit(1)

    nodename = args['nodename'][0]
    data = enc.lookup(nodename)

    if data:
        print(yaml.dump(data))


if __name__ == "__main__":
    main()
