#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009 Djordjevic Nebojsa <djnesh@gmail.com>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

import sys
import os
import codecs

CYR_TO_LAT = {
    # ucase
    u'А':u'A',
    u'Б':u'B',
    u'В':u'V',
    u'Г':u'G',
    u'Д':u'D',
    u'Ђ':u'Đ',
    u'Е':u'E',
    u'Ж':u'Ž',
    u'З':u'Z',
    u'И':u'I',
    u'Ј':u'J',
    u'К':u'K',
    u'Л':u'L',
    u'Љ':u'Lj',
    u'М':u'M',
    u'Н':u'N',
    u'Њ':u'Nj',
    u'О':u'O',
    u'П':u'P',
    u'Р':u'R',
    u'С':u'S',
    u'Т':u'T',
    u'Ћ':u'Ć',
    u'У':u'U',
    u'Ф':u'F',
    u'Х':u'H',
    u'Ц':u'C',
    u'Ч':u'Č',
    u'Џ':u'Dž',
    u'Ш':u'Š',
    # locase
    u'а':u'a',
    u'б':u'b',
    u'в':u'v',
    u'г':u'g',
    u'д':u'd',
    u'ђ':u'đ',
    u'е':u'e',
    u'ж':u'ž',
    u'з':u'z',
    u'и':u'i',
    u'ј':u'j',
    u'к':u'k',
    u'л':u'l',
    u'љ':u'lj',
    u'м':u'm',
    u'н':u'n',
    u'њ':u'nj',
    u'о':u'o',
    u'п':u'p',
    u'р':u'r',
    u'с':u's',
    u'т':u't',
    u'ћ':u'ć',
    u'у':u'u',
    u'ф':u'f',
    u'х':u'h',
    u'ц':u'c',
    u'ч':u'č',
    u'џ':u'dž',
    u'ш':u'š',
}

def convert(fname):
    newname = os.path.join('lat', fname)
    print 'converting', fname, 'to', newname
    inf = codecs.open(fname, 'rU', 'utf-8')
    outf = codecs.open(newname, 'w', 'utf-8')
    
    for line in inf:
        #print repr(line)
        if line.strip() == u'%!TEX root = /prepress/fudbal/latex/book.tex':
            line = u'%!TEX root = /prepress/fudbal/latex/lat/book.tex\n'
        elif line:
            for c,l in CYR_TO_LAT.items():
                if c in (u'Љ', u'Њ', u'Џ',):
                    if line.isupper():
                        line = line.replace(c, l.upper())
                    else:
                        line = line.replace(c, l)
                else:
                    line = line.replace(c, l)
        outf.write(line)
    inf.close()
    outf.close()

def main():
    for root, dirs, files in os.walk('.'):
        for fname in files:
            if  fname != 'preamble.tex' \
                and fname != 'preamble-base.tex' \
                and fname.endswith('.tex') \
                and not fname.endswith('-lat.tex'):
                convert(fname)
                


if __name__ == '__main__':
	main()

