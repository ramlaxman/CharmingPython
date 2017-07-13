"""
When you import a module, the Python interpreter searches for the module in the following sequences
The current directory.
If the module isn't found, Python then searches each directory in the shell variable PYTHONPATH.
If all else fails, Python checks the default path. On UNIX, this default path is normally /usr/local/lib/python/
"""

import helloPrinter

helloPrinter.printHello()

helloPrinter.printString("this is sampleString")
