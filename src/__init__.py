"""
Bhagwad Programming Language
A spiritual programming language inspired by the Bhagavad Gītā

"Just as the Gītā guides the soul toward moksha, 
 Bhagwad guides the programmer toward computational enlightenment."
"""

from .lexer import BhagwadLexer, Token, TokenType
from .parser import BhagwadParser, parse_bhagwad, ParseError
from .transpiler import BhagwadTranspiler, transpile_bhagwad
from .interpreter import BhagwadInterpreter
from . import ast_nodes

__version__ = "1.0.0"
__author__ = "Inspired by the eternal wisdom of the Bhagavad Gītā"

# Sacred constants
SACRED_NUMBERS = {
    'OM': 108,      # The sacred number representing completeness
    'NAVA': 9,      # Number of devotion (Navagraha) 
    'CHAKRA': 7,    # Number of chakras and spiritual levels
    'TRINITY': 3    # Creator, Preserver, Destroyer
}

def execute_bhagwad(source: str, debug: bool = False):
    """Execute Bhagwad source code directly"""
    interpreter = BhagwadInterpreter()
    interpreter.set_debug(debug)
    interpreter.execute_source(source)

def compile_bhagwad(source: str) -> str:
    """Compile Bhagwad source code to Python"""
    interpreter = BhagwadInterpreter()
    return interpreter.interpret_source(source)

__all__ = [
    'BhagwadLexer', 'BhagwadParser', 'BhagwadTranspiler', 'BhagwadInterpreter',
    'Token', 'TokenType', 'ParseError', 
    'parse_bhagwad', 'transpile_bhagwad', 'execute_bhagwad', 'compile_bhagwad',
    'ast_nodes', 'SACRED_NUMBERS'
]