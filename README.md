# mecab-win

MeCab v0.996 compiled under Windows 7 for Python 3.

Use VS Community 2017 x64 and Anaconda Python 3.5.

A trick is to install the Windows distribution first,
so do not bother to compile the dictionary by yourself...

Thanks to the original MeCab!

* in src, `nmake -f Makefile.msvc.x64.in`
* copy all exe and dll to the place you like
* create a directory structure like mecab/{etc,sdk,...}
* in python, modify setup.py to specify the directory
* run `python setup.py install` should be fine







