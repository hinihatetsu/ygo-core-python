import os
from typing import Callable
from unittest import TestCase
from tempfile import mkstemp


from ygo_core.deck import Deck

class TestDeck(TestCase):

    def setUp(self) -> None:
        self.deck = Deck()


    def base_test_load(self, content: str, assertfunc: Callable[[], None]) -> None:
        fd, name = mkstemp(suffix='.ydk')
        with open(name, 'w') as f:
            f.write(content)
        try:
            self.deck.load(name)
            assertfunc()
        except Exception as e:
            raise e
        finally:
            os.close(fd)
            os.remove(name)


    def test_load_with_valid_suffixx(self) -> None:
        assert self.deck.count_main == 0
        assert self.deck.count_extra == 0
        assert self.deck.count_side == 0
        content = """
        #created by llk
        #main
        #extra
        !side
        """
        self.base_test_load(content, lambda: self.assertEqual(0, self.deck.count_main))


    def test_load_with_main_result_main_count_should_be_1(self) -> None:
        content = """
        #created by llk
        #main
        0
        #extra
        !side
        """
        self.base_test_load(content, lambda: self.assertEqual(1, self.deck.count_main))


    def test_load_with_main_result_extra_count_should_be_0(self) -> None:
        content = """
        #created by llk
        #main
        0
        #extra
        !side
        """
        self.base_test_load(content, lambda: self.assertEqual(0, self.deck.count_extra))


    def test_load_with_main_result_side_count_should_be_0(self) -> None:
        content = """
        #created by llk
        #main
        0
        #extra
        !side
        """
        self.base_test_load(content, lambda: self.assertEqual(0, self.deck.count_side))


    def test_load_with_extra_result_main_count_should_be_0(self) -> None:
        content = """
        #created by llk
        #main
        #extra
        0
        !side
        """
        self.base_test_load(content, lambda: self.assertEqual(0, self.deck.count_main))


    def test_load_with_extra_result_extra_count_should_be_1(self) -> None:
        content = """
        #created by llk
        #main
        #extra
        0
        !side
        """
        self.base_test_load(content, lambda: self.assertEqual(1, self.deck.count_extra))


    def test_load_with_extra_result_side_count_should_be_0(self) -> None:
        content = """
        #created by llk
        #main
        #extra
        0
        !side
        """
        self.base_test_load(content, lambda: self.assertEqual(0, self.deck.count_side))


    def test_load_with_side_result_main_count_should_be_0(self) -> None:
        content = """
        #created by llk
        #main
        #extra
        !side
        0
        """
        self.base_test_load(content, lambda: self.assertEqual(0, self.deck.count_main))


    def test_load_with_side_result_extra_count_should_be_0(self) -> None:
        content = """
        #created by llk
        #main
        #extra
        !side
        0
        """
        self.base_test_load(content, lambda: self.assertEqual(0, self.deck.count_extra))


    def test_load_with_side_result_side_count_should_be_1(self) -> None:
        content = """
        #created by llk
        #main
        #extra
        !side
        1
        """
        self.base_test_load(content, lambda: self.assertEqual(1, self.deck.count_side))



    def test_load_with_invalid_suffix(self) -> None:
        fd, name = mkstemp(suffix='.pdf')
        try:
            self.assertRaises(ValueError, self.deck.load, name)
        finally:
            os.close(fd)
            os.remove(name)

    
    def test_load_with_unexist_path(self) -> None:
        path = 'unexist'
        if os.path.exists(path):
            raise Exception(f'`path`:{path} already exists')
        self.assertRaises(FileNotFoundError, self.deck.load, path)


    def test_prop_count_main(self) -> None:
        self.assertEqual(0, self.deck.count_main)


    def test_prop_count_extra(self) -> None:
        self.assertEqual(0, self.deck.count_extra)


    def test_prop_count_side(self) -> None:
        self.assertEqual(0, self.deck.count_side)

    
    def test_prop_count(self) -> None:
        self.assertEqual(0, self.deck.count)
        
