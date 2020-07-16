import pandas
from gem_webcrawl_datafilterer.cli import transform_to_lowercase_and_ascii


class MockedSystemInterfaceUnwantedRow:
    @staticmethod
    def read_csv(filepath):
        d = {'Type': 'combination', 'Keywords': 'NotFun', 'Content': 'Bla', 'Timestamp': '01:53:46-08.10.19',
             'Link': 'https://www.bild.de/'}
        return pandas.DataFrame(data=d)

    @staticmethod
    def get_words_in_content_column(row):
        return ['Bla']


class MockedSystemInterfaceWantedRow:
    @staticmethod
    def read_csv(filepath):
        d = {'Type': 'combination', 'Keywords': 'House',
             'Content': '"videoTitle": Löwe in the house</h2><p><strong>17:10 Uhr:</strong> Die Wilke Waldecke',
             'Timestamp': '01:53:46-08.10.19',
             'Link': 'https://www.media.de/video/startseite/funchannel-home/video-loewe-home-15713248.bild.html'}
        return pandas.DataFrame(data=d)

    @staticmethod
    def get_words_in_content_column(row):
        return ['videoTitle', 'Löwe', 'in', 'the', 'house', 'strong', 'Uhr', 'strong', 'Die', 'Wilke', 'Waldecke']


class TestTransformWords:

    def test_should_transform_to_lowercase(self):
        lowercase_word = transform_to_lowercase_and_ascii('UPPERCASE')
        assert lowercase_word == 'uppercase'

    def test_should_transform_utf8_letter_to_ascii(self):
        ascii_word = transform_to_lowercase_and_ascii('Löwe')
        assert ascii_word == 'loewe'

    def test_should_transform_utf8_letters_to_ascii(self):
        ascii_word = transform_to_lowercase_and_ascii('Übergrößenträger')
        assert ascii_word == 'uebergroessentraeger'


class TestClearDataFrameFromUnwantedRows:
    mocked_positive_standard_interface = MockedSystemInterfaceWantedRow()
    mocked_negative_standard_interface = MockedSystemInterfaceUnwantedRow()

    def test_should_be_false_with_null_value(self):
        # result = is_content_mentioned_in_link(self.mocked_positive_standard_interface, None)
        # assert result is False
        pass

    def test_should_be_false_when_keywords_are_not_reflected_in_link(self):
        # unwanted_row = self.mocked_negative_standard_interface.read_csv('someFile').head()
        # result = is_content_mentioned_in_link(self.mocked_negative_standard_interface, unwanted_row)
        # assert result is False
        pass

    def test_should_be_true_when_keywords_are_reflected_in_link(self):
        # wanted_row = self.mocked_positive_standard_interface.read_csv('someFile').head()
        # result = is_content_mentioned_in_link(self.mocked_negative_standard_interface, wanted_row)
        # assert result is True
        pass
