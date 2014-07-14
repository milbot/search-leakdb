#!/usr/bin/python

# Copyright (c) 2014, Milbot
# https://github.com/milbot/enumerator
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import urllib
import optparse
import re

def urlhash(hash, method):
    f = urllib.urlopen("http://api.leakdb.abusix.com/?t=%s " %hash)
    j = f.read()
    f.close()
    j = "".join(j)

    if re.findall("found=true", j):

        f = urllib.urlopen("http://api.leakdb.abusix.com/?t=%s " %hash)
        if method == "True":
            print f.read()

        else:
            t = "".join([i for i in f.readlines() if re.match(method, i)])
            print t
        f.close()
    else:
        print "Sorry, hash could not be found"

if __name__=="__main__":

    parser = optparse.OptionParser("usage: %prog [options] hash")
    parser.add_option("-H", "--hash", dest="hash", default="False", type="string", help="Specify the hash / word you want to encrypt")
    parser.add_option("-E", "--encryption", dest="encryption", default="True", type="string", help="Encryption method: sha1, gost, md4, md5, mysql4_mysql5, ntlm, ripemd160, sha1, sha224, sha256, sha384, sha512, whirlpool")

    (options, args) = parser.parse_args()

    if options.hash == "False":
        parser.error("search-leakdb.py -h : display help menu")

    urlhash(options.hash, options.encryption)
