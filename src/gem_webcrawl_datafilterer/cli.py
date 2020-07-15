"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mgem_webcrawl_datafilterer` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``gem_webcrawl_datafilterer.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``gem_webcrawl_datafilterer.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import sys
import pandas


class SystemInterface:
    @staticmethod
    def read_csv(filepath):
        return pandas.read_csv(filepath,
                               delimiter='~',
                               parse_dates=['Timestamp'],
                               )


def main(argv=sys.argv):
    filepath = argv[1]
    standard_system_interface = SystemInterface()
    data_frame = standard_system_interface.read_csv(filepath)
    print(data_frame.head(10))
    return 0
