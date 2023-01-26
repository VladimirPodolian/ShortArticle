from app import article_shorten


class TestApp:
    """
    Notes:
    1. there is no requirements for case when given sentence is empty string - test_case_6
    2. there is no requirements for case when given data is not a string - test_case_7
    3. there is no requirements for case when given sentence is one word >= 25 symbols - test_case_8
    """

    def test_case_1(self):
        """ Case with given example """
        assert 'Volvo released a new...' == article_shorten('Volvo released a new car with the following spec: V6 236HP')

    def test_case_2(self):
        """ Case when word "newcar" is fit, but dots not (sentence + dots = 26 length) """
        assert 'Volvo released a...' == article_shorten('Volvo released a newcar with the following spec: V6 236HP')

    def test_case_3(self):
        """ Case when word "fresh" is fit with dots (sentence + dots = 25 length) """
        assert 'Volvo released a fresh...' == article_shorten('Volvo released a fresh car with the following spec: V6 236HP')

    def test_case_4(self):
        """ Case with short sentence """
        assert 'Volvo released' == article_shorten('Volvo released')

    def test_case_5(self):
        """ Case without text """
        assert '' == article_shorten('')

    def test_case_6(self):
        """
        Case with different data.
        Assert for data type is more comfort for me, but it's better to convert to string if we can:
          so 'website' will not be crashed
        """
        assert '12123123112312323' == article_shorten(12123123112312323)

    def test_case_7(self):
        """ Case with one long word """
        assert '...' == article_shorten('onelongwordandtherearenoendforthis')

    def test_case_8(self):
        """ Equivalence class: 24 length with whitespace at the end """
        assert 'Volvo released a newest' == article_shorten('Volvo released a newest ')

    def test_case_9(self):
        """ Equivalence class: 25 length with whitespace at the end """
        assert 'Volvo released a new car' == article_shorten('Volvo released a new car ')

    def test_case_10(self):
        """ Equivalence class: 26 length with whitespaces at the end """
        assert 'Volvo released a new car' == article_shorten('Volvo released a new car  ')

    def test_case_11(self):
        """ Equivalence class: length is 24 """
        assert 'Volvo released a new car' == article_shorten('Volvo released a new car')

    def test_case_12(self):
        """ Equivalence class: length is 25 """
        assert 'Volvo released a new cars' == article_shorten('Volvo released a new cars')

    def test_case_13(self):
        """ Equivalence class: length is 26 """
        assert 'Volvo just released a...' == article_shorten('Volvo just released a news')
