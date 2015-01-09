#!/usr/local/opt/python/bin/python2.7
# Change the line above according to your needs

# Copyright (c) 2011, Georgios Is. Detorakis
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY Georgios Is. Detorakis ''AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL Georgios Is. Detorakis BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# -----------------------------------------------------------------------------
# Author:
#
#     Georgios Detorakis - gdetor@gmail.com
#
# Contact Information:
#
#     Georgios Is. Detorakis
#     INRIA Nancy - Grand Est research center
#     CS 20101
#     54603 Villers les Nancy Cedex France
'''
A minimal script that counts the number of words in a LaTeX file.
Example of use:
    localhost@name$ wclatex filename
'''
import re
import sys


def word_counter(filename):
    try:
        fp = open(filename, 'r')
    except IOError:
        print 'File does not exist!'
    else:
        lines = fp.readlines()

        latex_pattern = re.compile('^[\\\\]|^[$]|[=]|[-]|[+]|\w\(')
        w_space_pattern = re.compile('\s')

        sp, word, latex_word = 0, 0, 0

        for i in lines:
            buf = i.split(" ")
            for j in range(len(buf)):
                if latex_pattern.match(buf[j]):
                    latex_word += 1
                elif w_space_pattern.match(buf[j]):
                    sp += 1
                else:
                    word += 1
        return word


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print word_counter(sys.argv[1])
    else:
        print 'Use >> python wclatex filename'
