from __future__ import unicode_literals
import unittest

from bpython.curtsiesfrontend import interpreter
from bpython.curtsiesfrontend.repl import bad_empty_lines_removed
from curtsies.fmtfuncs import *

class TestInterpreter(unittest.TestCase):
    def test_syntaxerror(self):
        i = interpreter.Interp()
        a = []

        def append_to_a(message):
            a.append(message)
        
        i.write = append_to_a
        i.runsource('1.1.1.1')

        expected = ''+''+'  File '+green('"<input>"')+', line '+bold(magenta('1'))+'\n'+'    '+'1.1'+'.'+'1.1'+'\n'+'    '+'    '+'^'+'\n'+bold(red('SyntaxError'))+': '+cyan('invalid syntax')+'\n'

        self.assertEquals(str(plain('').join(a)), str(expected))
        self.assertEquals(plain('').join(a), expected)

    def test_traceback(self):
        i = interpreter.Interp()
        a = []

        def append_to_a(message):
            a.append(message)
        
        i.write = append_to_a

        def f():
            return 1/0

        def g():
            return f()

        i.runsource('g()')

        expected = 'Traceback (most recent call last):\n'+''+'  File '+green('"<input>"')+', line '+bold (magenta('1'))+', in '+cyan('<module>')+'\n'+''+bold(red('NameError'))+': '+cyan(u"name 'g' is not defined")+'\n'

        self.assertEquals(str(plain('').join(a)), str(expected))
        self.assertEquals(plain('').join(a), expected)

class TestPreprocessing(unittest.TestCase):
    def test_bad_empty_lines_removed(self):
        self.assertEqual(bad_empty_lines_removed("def foo():\n"
                                             "    return 1\n"
                                             "\n"
                                             "    pass\n"),
                         "def foo():\n"
                         "    return 1\n"
                         "    pass\n")


