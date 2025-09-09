"""
Bhagwad Programming Language - Parser
Converts tokens into Abstract Syntax Tree (AST)
Inspired by the Bhagavad Gītā
"""

from typing import List, Optional, Union
from .lexer import Token, TokenType, BhagwadLexer
from .ast_nodes import *

class ParseError(Exception):
    def __init__(self, message: str, token: Token):
        self.message = message
        self.token = token
        super().__init__(f"{message} at line {token.line}, column {token.column}")

class BhagwadParser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0
    
    def peek(self) -> Token:
        """Get current token without consuming it"""
        if self.current >= len(self.tokens):
            return self.tokens[-1]  # EOF token
        return self.tokens[self.current]
    
    def previous(self) -> Token:
        """Get previous token"""
        return self.tokens[self.current - 1]
    
    def advance(self) -> Token:
        """Consume current token and move to next"""
        if not self.is_at_end():
            self.current += 1
        return self.previous()
    
    def is_at_end(self) -> bool:
        """Check if we're at end of tokens"""
        return self.peek().type == TokenType.EOF
    
    def check(self, token_type: TokenType) -> bool:
        """Check if current token is of given type"""
        if self.is_at_end():
            return False
        return self.peek().type == token_type
    
    def match(self, *token_types: TokenType) -> bool:
        """Check if current token matches any of the given types"""
        for token_type in token_types:
            if self.check(token_type):
                self.advance()
                return True
        return False
    
    def consume(self, token_type: TokenType, message: str) -> Token:
        """Consume token of expected type or raise error"""
        if self.check(token_type):
            return self.advance()
        raise ParseError(message, self.peek())
    
    def skip_newlines(self):
        """Skip newline tokens"""
        while self.match(TokenType.NEWLINE):
            pass
    
    def parse(self) -> Program:
        """Parse tokens into AST"""
        statements = []
        
        while not self.is_at_end():
            self.skip_newlines()
            if not self.is_at_end():
                stmt = self.statement()
                if stmt:
                    statements.append(stmt)
            self.skip_newlines()
        
        return Program(statements)
    
    def statement(self) -> Optional[Statement]:
        """Parse a statement"""
        try:
            if self.match(TokenType.ARJUNA):
                return self.arjuna_statement()
            elif self.match(TokenType.SHLOKA):
                return self.shloka_statement()
            elif self.match(TokenType.YUGA):
                return self.yuga_statement()
            elif self.match(TokenType.MAYA, TokenType.SANKALPA):
                return self.variable_declaration()
            elif self.match(TokenType.SATTVA, TokenType.RAJAS, TokenType.TAMAS):
                return self.typed_variable_declaration()
            elif self.match(TokenType.COSMIC):
                return self.array_declaration()
            elif self.match(TokenType.MANIFEST):
                return self.manifest_statement()
            elif self.match(TokenType.DHARMA):
                return self.dharma_statement()
            elif self.match(TokenType.KARMA):
                return self.karma_statement()
            elif self.match(TokenType.MOKSHA):
                return self.moksha_statement()
            elif self.match(TokenType.MEDITATION):
                return self.meditation_statement()
            elif self.check(TokenType.IDENTIFIER):
                return self.assignment_or_expression()
            elif self.match(TokenType.COMMENT):
                return None  # Skip comments
            else:
                raise ParseError(f"Unexpected token: {self.peek().value}", self.peek())
        except ParseError as e:
            # Error recovery - skip to next statement
            self.synchronize()
            raise e
    
    def synchronize(self):
        """Recover from parse error by finding next statement"""
        self.advance()
        while not self.is_at_end():
            if self.previous().type == TokenType.NEWLINE:
                return
            if self.peek().type in [TokenType.ARJUNA, TokenType.SHLOKA, TokenType.YUGA, 
                                   TokenType.MAYA, TokenType.SANKALPA, TokenType.MANIFEST,
                                   TokenType.DHARMA, TokenType.KARMA, TokenType.MOKSHA]:
                return
            self.advance()
    
    def arjuna_statement(self) -> Arjuna:
        """Parse arjuna (main) block"""
        self.consume(TokenType.LEFT_BRACE, "Expected '{' after 'arjuna'")
        body = self.block()
        return Arjuna(body)
    
    def shloka_statement(self) -> Shloka:
        """Parse shloka (function) definition"""
        name = self.consume(TokenType.IDENTIFIER, "Expected function name").value
        
        self.consume(TokenType.LEFT_PAREN, "Expected '(' after function name")
        
        parameters = []
        if not self.check(TokenType.RIGHT_PAREN):
            parameters = self.parameter_list()
        
        self.consume(TokenType.RIGHT_PAREN, "Expected ')' after parameters")
        
        return_type = None
        if self.match(TokenType.ARROW):
            if self.match(TokenType.SATTVA, TokenType.RAJAS, TokenType.TAMAS):
                return_type = self.previous().value
            else:
                raise ParseError("Expected return type after '->'", self.peek())
        
        self.consume(TokenType.LEFT_BRACE, "Expected '{' before function body")
        body = self.block()
        
        return Shloka(name, parameters, return_type, body)
    
    def parameter_list(self) -> List[Parameter]:
        """Parse function parameters"""
        parameters = []
        
        # First parameter
        param_type = self.consume_type("Expected parameter type")
        param_name = self.consume(TokenType.IDENTIFIER, "Expected parameter name").value
        parameters.append(Parameter(param_name, param_type))
        
        # Additional parameters
        while self.match(TokenType.COMMA):
            param_type = self.consume_type("Expected parameter type")
            param_name = self.consume(TokenType.IDENTIFIER, "Expected parameter name").value
            parameters.append(Parameter(param_name, param_type))
        
        return parameters
    
    def consume_type(self, message: str) -> str:
        """Consume a type token"""
        if self.match(TokenType.SATTVA, TokenType.RAJAS, TokenType.TAMAS):
            return self.previous().value
        elif self.match(TokenType.COSMIC):
            # Handle cosmic array type
            array_type = self.consume_type("Expected array element type after 'cosmic'")
            self.consume(TokenType.LEFT_BRACKET, "Expected '[' after array type")
            self.consume(TokenType.RIGHT_BRACKET, "Expected ']' after '['")
            return f"{array_type}[]"
        raise ParseError(message, self.peek())
    
    def yuga_statement(self) -> Yuga:
        """Parse yuga (module) definition"""
        name = self.consume(TokenType.IDENTIFIER, "Expected module name").value
        self.consume(TokenType.LEFT_BRACE, "Expected '{' after module name")
        body = self.block()
        return Yuga(name, body)
    
    def variable_declaration(self) -> VariableDeclaration:
        """Parse maya (variable) or sankalpa (constant) declaration"""
        is_constant = self.previous().type == TokenType.SANKALPA
        
        name = self.consume(TokenType.IDENTIFIER, "Expected variable name").value
        
        data_type = None
        value = None
        
        if self.match(TokenType.ASSIGN):
            value = self.expression()
        
        return VariableDeclaration(name, data_type, value, is_constant)
    
    def typed_variable_declaration(self) -> VariableDeclaration:
        """Parse typed variable declaration"""
        data_type = self.previous().value
        name = self.consume(TokenType.IDENTIFIER, "Expected variable name").value
        
        value = None
        if self.match(TokenType.ASSIGN):
            value = self.expression()
        
        return VariableDeclaration(name, data_type, value, False)
    
    def array_declaration(self) -> VariableDeclaration:
        """Parse cosmic (array) declaration"""
        array_type = self.consume_type("Expected array element type")
        self.consume(TokenType.LEFT_BRACKET, "Expected '[' after array type")
        self.consume(TokenType.RIGHT_BRACKET, "Expected ']' after '['")
        
        name = self.consume(TokenType.IDENTIFIER, "Expected array name").value
        
        value = None
        if self.match(TokenType.ASSIGN):
            value = self.expression()
        
        return VariableDeclaration(name, f"{array_type}[]", value, False)
    
    def manifest_statement(self) -> Manifest:
        """Parse manifest (print) statement"""
        expr = self.expression()
        return Manifest(expr)
    
    def dharma_statement(self) -> Dharma:
        """Parse dharma (if-else) statement"""
        self.consume(TokenType.LEFT_PAREN, "Expected '(' after 'dharma'")
        condition = self.expression()
        self.consume(TokenType.RIGHT_PAREN, "Expected ')' after condition")
        
        self.consume(TokenType.LEFT_BRACE, "Expected '{' after condition")
        then_block = self.block()
        
        else_block = None
        if self.match(TokenType.ADHARMA):
            self.consume(TokenType.LEFT_BRACE, "Expected '{' after 'adharma'")
            else_block = self.block()
        
        return Dharma(condition, then_block, else_block)
    
    def karma_statement(self) -> Karma:
        """Parse karma (loop) statement"""
        if self.check(TokenType.IDENTIFIER):
            variable = self.advance().value
            
            if self.match(TokenType.FROM):
                # karma i from 1 to 10
                start = self.expression()
                self.consume(TokenType.TO, "Expected 'to' after start value")
                end = self.expression()
                
                self.consume(TokenType.LEFT_BRACE, "Expected '{' after loop range")
                body = self.block()
                
                return Karma("range", variable, start, end, None, body)
            elif self.match(TokenType.IN):
                # karma num in array
                iterable = self.expression()
                
                self.consume(TokenType.LEFT_BRACE, "Expected '{' after iterable")
                body = self.block()
                
                return Karma("foreach", variable, None, None, iterable, body)
            else:
                raise ParseError("Expected 'from' or 'in' after loop variable", self.peek())
        else:
            raise ParseError("Expected loop variable after 'karma'", self.peek())
    
    def moksha_statement(self) -> Moksha:
        """Parse moksha (return) statement"""
        expr = None
        if not self.check(TokenType.NEWLINE) and not self.check(TokenType.RIGHT_BRACE):
            expr = self.expression()
        return Moksha(expr)
    
    def meditation_statement(self) -> Meditation:
        """Parse meditation (try-catch) statement"""
        self.consume(TokenType.LEFT_BRACE, "Expected '{' after 'meditation'")
        try_block = self.block()
        
        catch_variable = None
        catch_block = None
        
        if self.match(TokenType.DISTURBANCE):
            self.consume(TokenType.LEFT_PAREN, "Expected '(' after 'disturbance'")
            catch_variable = self.consume(TokenType.IDENTIFIER, "Expected error variable name").value
            self.consume(TokenType.RIGHT_PAREN, "Expected ')' after error variable")
            
            self.consume(TokenType.LEFT_BRACE, "Expected '{' after disturbance clause")
            catch_block = self.block()
        
        return Meditation(try_block, catch_variable, catch_block)
    
    def assignment_or_expression(self) -> Statement:
        """Parse assignment or expression statement"""
        if self.check(TokenType.IDENTIFIER):
            name = self.advance().value
            if self.match(TokenType.ASSIGN):
                value = self.expression()
                return Assignment(name, value)
            else:
                # Put the identifier back and parse as expression
                self.current -= 1
                expr = self.expression()
                return ExpressionStatement(expr)
        else:
            expr = self.expression()
            return ExpressionStatement(expr)
    
    def block(self) -> Block:
        """Parse block of statements"""
        statements = []
        
        self.skip_newlines()
        
        while not self.check(TokenType.RIGHT_BRACE) and not self.is_at_end():
            self.skip_newlines()
            if not self.check(TokenType.RIGHT_BRACE) and not self.is_at_end():
                stmt = self.statement()
                if stmt:
                    statements.append(stmt)
            self.skip_newlines()
        
        self.consume(TokenType.RIGHT_BRACE, "Expected '}' after block")
        return Block(statements)
    
    def expression(self) -> Expression:
        """Parse expression"""
        return self.equality()
    
    def equality(self) -> Expression:
        """Parse equality expressions"""
        expr = self.comparison()
        
        while self.match(TokenType.EQUALS, TokenType.NOT_EQUALS):
            operator = self.previous().value
            right = self.comparison()
            expr = BinaryOperation(expr, operator, right)
        
        return expr
    
    def comparison(self) -> Expression:
        """Parse comparison expressions"""
        expr = self.term()
        
        while self.match(TokenType.GREATER_THAN, TokenType.GREATER_EQUAL, 
                         TokenType.LESS_THAN, TokenType.LESS_EQUAL):
            operator = self.previous().value
            right = self.term()
            expr = BinaryOperation(expr, operator, right)
        
        return expr
    
    def term(self) -> Expression:
        """Parse addition and subtraction"""
        expr = self.factor()
        
        while self.match(TokenType.PLUS, TokenType.MINUS):
            operator = self.previous().value
            right = self.factor()
            expr = BinaryOperation(expr, operator, right)
        
        return expr
    
    def factor(self) -> Expression:
        """Parse multiplication and division"""
        expr = self.unary()
        
        while self.match(TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.MODULO):
            operator = self.previous().value
            right = self.unary()
            expr = BinaryOperation(expr, operator, right)
        
        return expr
    
    def unary(self) -> Expression:
        """Parse unary expressions"""
        if self.match(TokenType.MINUS):
            operator = self.previous().value
            right = self.unary()
            return UnaryOperation(operator, right)
        
        return self.call()
    
    def call(self) -> Expression:
        """Parse function calls, array access, and member access"""
        expr = self.primary()
        
        while True:
            if self.match(TokenType.LEFT_PAREN):
                expr = self.finish_call(expr)
            elif self.match(TokenType.LEFT_BRACKET):
                index = self.expression()
                self.consume(TokenType.RIGHT_BRACKET, "Expected ']' after array index")
                expr = ArrayAccess(expr, index)
            elif self.match(TokenType.DOT):
                member = self.consume(TokenType.IDENTIFIER, "Expected member name after '.'").value
                from .ast_nodes import MemberAccess
                expr = MemberAccess(expr, member)
            else:
                break
        
        return expr
    
    def finish_call(self, callee: Expression) -> Expression:
        """Parse function call arguments"""
        arguments = []
        
        if not self.check(TokenType.RIGHT_PAREN):
            arguments.append(self.expression())
            while self.match(TokenType.COMMA):
                arguments.append(self.expression())
        
        self.consume(TokenType.RIGHT_PAREN, "Expected ')' after arguments")
        
        if isinstance(callee, Identifier):
            return FunctionCall(callee.name, arguments)
        else:
            raise ParseError("Invalid function call", self.peek())
    
    def primary(self) -> Expression:
        """Parse primary expressions"""
        if self.match(TokenType.BOOLEAN):
            value = self.previous().value.lower() == 'true'
            return Literal(value, 'tamas')
        
        if self.match(TokenType.NUMBER):
            value = self.previous().value
            if '.' in value:
                return Literal(float(value), 'sattva')
            else:
                return Literal(int(value), 'sattva')
        
        if self.match(TokenType.STRING):
            return Literal(self.previous().value, 'rajas')
        
        if self.match(TokenType.IDENTIFIER):
            return Identifier(self.previous().value)
        
        if self.match(TokenType.LEFT_PAREN):
            expr = self.expression()
            self.consume(TokenType.RIGHT_PAREN, "Expected ')' after expression")
            return expr
        
        if self.match(TokenType.LEFT_BRACKET):
            elements = []
            if not self.check(TokenType.RIGHT_BRACKET):
                elements.append(self.expression())
                while self.match(TokenType.COMMA):
                    elements.append(self.expression())
            
            self.consume(TokenType.RIGHT_BRACKET, "Expected ']' after array elements")
            return ArrayLiteral(elements)
        
        raise ParseError(f"Unexpected token: {self.peek().value}", self.peek())

def parse_bhagwad(source: str) -> Program:
    """Parse Bhagwad source code into AST"""
    lexer = BhagwadLexer(source)
    tokens = lexer.tokenize()
    parser = BhagwadParser(tokens)
    return parser.parse()