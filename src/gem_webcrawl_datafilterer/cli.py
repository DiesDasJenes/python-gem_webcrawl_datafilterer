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
import re


class SystemInterface:
    @staticmethod
    def read_csv(filepath):
        return pandas.read_csv(filepath,
                               delimiter='~',
                               parse_dates=['Timestamp'],
                               )

    @staticmethod
    def get_words_in_content_column(row):
        return re.findall(r"[A-Za-zÄÖÜäöüß-]{2,}", row['Content'])


def transform_to_lowercase_and_ascii(word):
    umlauts = {
        "ä": "ae",
        "ö": "oe",
        "ü": "ue",
        "ß": "ss",
    }
    word = word.lower()
    for umlaut, ascii_version in umlauts.items():
        word = word.replace(umlaut, ascii_version)
    return word


def is_content_mentioned_in_link(standard_system_interface, row):
    if row is not None:
        words = standard_system_interface.get_words_in_content_column(row)
        for word in words:
            word = transform_to_lowercase_and_ascii(word)
            if word in row['Link'][0]:
                return True

    return False


def delete_unwanted_rows(data_frame):
    for row in data_frame:
        print(is_content_mentioned_in_link(row))
    raise NotImplementedError('Not implemented')


# Run through rows O(n)
# On every Row check for Condition
# If True: Add index to DeletionCandidatesList False: Continoue
# At the end pandas.drop(DCList) (df_org.drop(index=['Bob', 'Dave', 'Frank'], inplace=True)

def main(argv=sys.argv):
    filepath = argv[1]
    standard_system_interface = SystemInterface()
    data_frame = standard_system_interface.read_csv(filepath)
    print(data_frame.head(10))
    return 0
