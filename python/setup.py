#!/usr/bin/env python

"""MeCab 0.996 python binding modified for Python 3.5 on Windows"""

from distutils.core import setup, Extension, os
import string


def cmd1(str):
    return os.popen(str).readlines()[0][:-1]

def cmd2(str):
    return string.split (cmd1(str))

# setup(name = "mecab-python",
	# version = cmd1("mecab-config --version"),
	# py_modules=["MeCab"],
	# ext_modules = [
		# Extension("_MeCab",
			# ["MeCab_wrap.cxx",],
			# include_dirs=cmd2("mecab-config --inc-dir"),
			# library_dirs=cmd2("mecab-config --libs-only-L"),
			# libraries=cmd2("mecab-config --libs-only-l"))
			# ])
setup(name="mecab-python",
      version="0.996",
      py_modules=["MeCab"],
      ext_modules=[
          Extension("_MeCab",
                    ["MeCab_wrap.cxx",],
                    include_dirs=[r"C:\mecab\sdk"],
                    library_dirs=[r"C:\mecab\sdk"],
                    libraries=['libmecab'])])
