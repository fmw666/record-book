# Python 测试

## 测试框架

### 你知道哪些 Python 的测试框架？

+ unittest：Python 自带的单元测试框架

    + 使用方法：
        + 继承 `unittest.TestCase` 类
        + 以 `test_` 开头的方法
        + `assertEqual`、`assertNotEqual`、`assertTrue`、`assertFalse`、`assertIs`、`assertIsNot`、`assertIsNone` 等

        ```python
        import unittest
        

        class TestStringMethods(unittest.TestCase):

            def test_upper(self):
                self.assertEqual('foo'.upper(), 'FOO')
        
            def test_isupper(self):
                self.assertTrue('FOO'.isupper())
                self.assertFalse('Foo'.isupper())
        
            def test_split(self):
                s = 'hello world'
                self.assertEqual(s.split(), ['hello', 'world'])
                # check that s.split fails when the separator is not a string
                with self.assertRaises(TypeError):
                    s.split(2)
            ```
    
        + `setUp` 和 `tearDown` 方法
    
            ```python
            import unittest
    
            class Test(unittest.TestCase):
    
                def setUp(self):
                    print('start')
    
                def tearDown(self):
                    print('end')
    
                def test_1(self):
                    print('test_1')
    
                def test_2(self):
                    print('test_2')
    
            if __name__ == '__main__':
                unittest.main()
            ```
    
        + `setUpClass` 和 `tearDownClass` 方法
    
            ```python
            import unittest
    
            class Test(unittest.TestCase):
    
                @classmethod
                def setUpClass(cls):
                    print('start')
    
                @classmethod
                def tearDownClass(cls):
                    print('end')
    
                def test_1(self):
                    print('test_1')
    
                def test_2(self):
                    print('test_2')
    
            if __name__ == '__main__':
                unittest.main()
            ```
    
        + `setUpModule` 和 `tearDownModule` 方法
    
            ```python
            import unittest
    
            def setUpModule():
                print('start')
    
            def tearDownModule():
                print('end')
    
            class Test(unittest.TestCase):
    
                def test_1(self):
                    print('test_1')
    
                def test_2(self):
                    print('test_2')
    
            if __name__ == '__main__':
                unittest.main()
            ```
    
        + `skip` 和 `skipIf` 方法
    
            ```python
            import unittest
    
            class Test(unittest.TestCase):
    
                @unittest.skip('skip')
                def test_1(self):
                    print('test_1')
    
                @unittest.skipIf(1 > 0, 'skip')
                def test_2(self):
                    print('test_2')
    
            if __name__ == '__main__':
                unittest.main()
            ```
    
    + 注意事项：
        + 测试用例的命名必须以 `test` 开头，否则不会被执行
        + 测试用例的执行顺序是按照方法名的字母顺序执行的
        + 测试用例中的 `setUp` 和 `tearDown` 方法会在每个测试用例执行前和执行后执行一次


+ pytest：第三方单元测试框架

    + 使用方法：
        + 以 `test_` 开头的方法
        + `assert`、`assert not`、`assert a in b`、`assert a == b` 等

        ```python
        def test_upper():
            assert 'foo'.upper() == 'FOO'
        
        def test_isupper():
            assert 'FOO'.isupper()
            assert not 'Foo'.isupper()
        
        def test_split():
            s = 'hello world'
            assert s.split() == ['hello', 'world']
            # check that s.split fails when the separator is not a string
            with pytest.raises(TypeError):
                s.split(2)
        ```
    
    + 注意事项：
        + 在不指定文件名的情况下运行 pytest 将运行当前目录和子目录中格式为 test_*.py 或 *_test.py 的所有文件。 Pytest 自动将这些文件识别为测试文件。 我们可以通过明确提及它们来使 pytest 运行其他文件名。
        + Pytest 要求测试函数名称以 test 开头。 pytest 不将格式不是 test* 的函数名称视为测试函数。

+ nose：第三方单元测试框架

+ doctest：Python 自带的文档测试框架

+ tox：第三方自动化测试框架
