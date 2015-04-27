#!/usr/local/opt/python/bin/python2.7
# Change the line above according to your needs
#
# Copyright (c) 2014, Georgios Is. Detorakis (gdetor@gmail.com)
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.
'''
A minimal script that generates a LaTeX file in your current directory
containing some very basic and some non-basic packages
Example of use:
    localhost@name$ latex_init desired_filename_without_extension
'''
import os
import sys


def current_path():
    ''' Get the current path '''
    return os.getcwd()


def goto_directory(path):
    ''' Change directory moving to path'''
    return os.chdir(path)


def create_latex_file(fname):
    ''' Write to a file (fname) the very basic commands of latex '''

    sep = os.linesep
    basic_commands = '\\documentclass[]{}'+sep + \
                     '% \\usepackage{graphicx}'+sep + \
                     '% \\usepackage{amssymb,amsmath,array,amsthm}'+sep + \
                     '% \\usepackage{graphicx}'+sep + \
                     '% \\usepackage{fullpage}'+sep + \
                     '% \\usepackage{url}'+sep + \
                     '% \\usepackage{psfrag}'+sep + \
                     '% \\usepackage{marvosym}'+sep + \
                     '% \\usepackage{algorithmic}'+sep + \
                     '% \\usepackage{algorithm}'+sep + \
                     '% \\numberwithin{algorithm}{chapter}'+sep + \
                     '% \\usepackage{hyperref}' + \
                     (3*sep)+'\\begin{document}'+(3*sep)+'\\end{document}'
    try:
        ''' If the file cannot be opened an exception is raised '''
        with open(fname, "w") as latex_f:
            latex_f.write(basic_commands)
    except IOError, e:
        print e.errno
        print e

if __name__ == '__main__':
    ''' If the length of command prompt argument is not equal to 2 the script
        terminates '''

    if len(sys.argv) == 2:
        cp = current_path()
        goto_directory(cp)
        create_latex_file(sys.argv[1]+'.tex')
    else:
        print 'Please give the name of the file!'
