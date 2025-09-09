"""
Bhagwad Programming Language - Lexer
Tokenizes Bhagwad source code into meaningful tokens
Inspired by the Bhagavad Gītā
"""

import re
from enum import Enum
from dataclasses import dataclass
from typing import List, Optional, Iterator

class TokenType(Enum):
    # Keywords (Spiritual constructs)
    SHLOKA = "SHLOKA"           # function
    DHARMA = "DHARMA"           # if
    ADHARMA = "ADHARMA"         # else
    KARMA = "KARMA"             # loop
    ARJUNA = "ARJUNA"           # main
    MANIFEST = "MANIFEST"       # print
    MOKSHA = "MOKSHA"           # return
    MAYA = "MAYA"               # variable
    SANKALPA = "SANKALPA"       # constant
    YUGA = "YUGA"               # module/namespace
    MEDITATION = "MEDITATION"   # try
    DISTURBANCE = "DISTURBANCE" # catch
    COSMIC = "COSMIC"           # array
    
    # Data types (Gunas)
    SATTVA = "SATTVA"           # int
    RAJAS = "RAJAS"             # string
    TAMAS = "TAMAS"             # bool
    
    # Literals
    NUMBER = "NUMBER"
    STRING = "STRING"
    BOOLEAN = "BOOLEAN"
    IDENTIFIER = "IDENTIFIER"
    
    # Operators
    PLUS = "PLUS"
    MINUS = "MINUS"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"
    MODULO = "MODULO"
    ASSIGN = "ASSIGN"
    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    LESS_THAN = "LESS_THAN"
    GREATER_THAN = "GREATER_THAN"
    LESS_EQUAL = "LESS_EQUAL"
    GREATER_EQUAL = "GREATER_EQUAL"
    
    # Delimiters
    LEFT_PAREN = "LEFT_PAREN"
    RIGHT_PAREN = "RIGHT_PAREN"
    LEFT_BRACE = "LEFT_BRACE"
    RIGHT_BRACE = "RIGHT_BRACE"
    LEFT_BRACKET = "LEFT_BRACKET"
    RIGHT_BRACKET = "RIGHT_BRACKET"
    COMMA = "COMMA"
    SEMICOLON = "SEMICOLON"
    ARROW = "ARROW"
    DOT = "DOT"
    
    # Control flow
    FROM = "FROM"
    TO = "TO"
    IN = "IN"
    
    # Special
    NEWLINE = "NEWLINE"
    EOF = "EOF"
    COMMENT = "COMMENT"

@dataclass
class Token:
    type: TokenType
    value: str
    line: int
    column: int

class BhagwadLexer:
    def __init__(self, source: str):
        self.source = source
        self.position = 0
        self.line = 1
        self.column = 1
        self.tokens: List[Token] = []
        
        # Keywords mapping
        self.keywords = {
            'shloka': TokenType.SHLOKA,
            'dharma': TokenType.DHARMA,
            'adharma': TokenType.ADHARMA,
            'karma': TokenType.KARMA,
            'arjuna': TokenType.ARJUNA,
            'manifest': TokenType.MANIFEST,
            'moksha': TokenType.MOKSHA,
            'maya': TokenType.MAYA,
            'sankalpa': TokenType.SANKALPA,
            'yuga': TokenType.YUGA,
            'meditation': TokenType.MEDITATION,
            'disturbance': TokenType.DISTURBANCE,
            'cosmic': TokenType.COSMIC,
            'sattva': TokenType.SATTVA,
            'rajas': TokenType.RAJAS,
            'tamas': TokenType.TAMAS,
            'from': TokenType.FROM,
            'to': TokenType.TO,
            'in': TokenType.IN,
            'true': TokenType.BOOLEAN,
            'false': TokenType.BOOLEAN,
        }
    
    def current_char(self) -> Optional[str]:
        if self.position >= len(self.source):
            return None
        return self.source[self.position]
    
    def peek_char(self, offset: int = 1) -> Optional[str]:
        peek_pos = self.position + offset
        if peek_pos >= len(self.source):
            return None
        return self.source[peek_pos]
    
    def advance(self) -> None:
        if self.position < len(self.source) and self.source[self.position] == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1
        self.position += 1
    
    def skip_whitespace(self) -> None:
        while self.current_char() and self.current_char() in ' \t\r':
            self.advance()
    
    def read_string(self) -> str:
        quote_char = self.current_char()
        self.advance()  # Skip opening quote
        
        value = ""
        while self.current_char() and self.current_char() != quote_char:
            if self.current_char() == '\\':
                self.advance()
                if self.current_char() in '"\'\\nrt':
                    escape_chars = {
                        'n': '\n',
                        'r': '\r',
                        't': '\t',
                        '\\': '\\',
                        '"': '"',
                        "'": "'"
                    }
                    value += escape_chars.get(self.current_char(), self.current_char())
                else:
                    value += self.current_char()
            else:
                value += self.current_char()
            self.advance()
        
        if self.current_char() == quote_char:
            self.advance()  # Skip closing quote
        
        return value
    
    def read_number(self) -> str:
        value = ""
        while self.current_char() and (self.current_char().isdigit() or self.current_char() == '.'):
            value += self.current_char()
            self.advance()
        return value
    
    def read_identifier(self) -> str:
        value = ""
        while (self.current_char() and 
               (self.current_char().isalnum() or self.current_char() == '_')):
            value += self.current_char()
            self.advance()
        return value
    
    def read_comment(self) -> str:
        comment = ""
        self.advance()  # Skip first /
        self.advance()  # Skip second /
        
        while self.current_char() and self.current_char() != '\n':
            comment += self.current_char()
            self.advance()
        
        return comment.strip()
    
    def tokenize(self) -> List[Token]:
        while self.position < len(self.source):
            self.skip_whitespace()
            
            if not self.current_char():
                break
            
            char = self.current_char()
            line, column = self.line, self.column
            
            # Comments
            if char == '/' and self.peek_char() == '/':
                comment = self.read_comment()
                self.tokens.append(Token(TokenType.COMMENT, comment, line, column))
                continue
            
            # Newlines
            if char == '\n':
                self.tokens.append(Token(TokenType.NEWLINE, char, line, column))
                self.advance()
                continue
            
            # Strings
            if char in '"\'':
                value = self.read_string()
                self.tokens.append(Token(TokenType.STRING, value, line, column))
                continue
            
            # Numbers
            if char.isdigit():
                value = self.read_number()
                self.tokens.append(Token(TokenType.NUMBER, value, line, column))
                continue
            
            # Identifiers and keywords
            if char.isalpha() or char == '_':
                value = self.read_identifier()
                token_type = self.keywords.get(value.lower(), TokenType.IDENTIFIER)
                self.tokens.append(Token(token_type, value, line, column))
                continue
            
            # Two-character operators
            if char == '=' and self.peek_char() == '=':
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.EQUALS, "==", line, column))
                continue
            
            if char == '!' and self.peek_char() == '=':
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.NOT_EQUALS, "!=", line, column))
                continue
            
            if char == '<' and self.peek_char() == '=':
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.LESS_EQUAL, "<=", line, column))
                continue
            
            if char == '>' and self.peek_char() == '=':
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.GREATER_EQUAL, ">=", line, column))
                continue
            
            if char == '-' and self.peek_char() == '>':
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.ARROW, "->", line, column))
                continue
            
            # Single-character tokens
            single_chars = {
                '+': TokenType.PLUS,
                '-': TokenType.MINUS,
                '*': TokenType.MULTIPLY,
                '/': TokenType.DIVIDE,
                '%': TokenType.MODULO,
                '=': TokenType.ASSIGN,
                '<': TokenType.LESS_THAN,
                '>': TokenType.GREATER_THAN,
                '(': TokenType.LEFT_PAREN,
                ')': TokenType.RIGHT_PAREN,
                '{': TokenType.LEFT_BRACE,
                '}': TokenType.RIGHT_BRACE,
                '[': TokenType.LEFT_BRACKET,
                ']': TokenType.RIGHT_BRACKET,
                ',': TokenType.COMMA,
                ';': TokenType.SEMICOLON,
                '.': TokenType.DOT,
            }
            
            if char in single_chars:
                self.tokens.append(Token(single_chars[char], char, line, column))
                self.advance()
                continue
            
            # Unknown character
            raise SyntaxError(f"Unexpected character '{char}' at line {line}, column {column}")
        
        # Add EOF token
        self.tokens.append(Token(TokenType.EOF, "", self.line, self.column))
        return self.tokens