from gem_webcrawl_datafilterer.cli import main
import pandas


class MockedSystemInterface:
    @staticmethod
    def read_csv(filepath):
        d = {'Type': 'combination', 'Keywords': 'Frau & Mord', 'Content': 'Bla', 'Timestamp': '01:53:46-08.10.19',
             'Link': 'https://FunFun.de'}
        return pandas.DataFrame(data=d)


def test_main():
    assert main([]) == 0
