"""
Bhagwad Programming Language - Abstract Syntax Tree (AST) Nodes
Defines the structure of parsed Bhagwad code
Inspired by the Bhagavad Gītā
"""

from abc import ABC, abstractmethod
from typing import List, Optional, Any, Union
from dataclasses import dataclass

# Base AST Node
class ASTNode(ABC):
    pass

# Expressions
class Expression(ASTNode):
    pass

class Literal(Expression):
    def __init__(self, value: Any, data_type: str):
        self.value = value
        self.data_type = data_type

class Identifier(Expression):
    def __init__(self, name: str):
        self.name = name

class BinaryOperation(Expression):
    def __init__(self, left: Expression, operator: str, right: Expression):
        self.left = left
        self.operator = operator
        self.right = right

class UnaryOperation(Expression):
    def __init__(self, operator: str, operand: Expression):
        self.operator = operator
        self.operand = operand

class FunctionCall(Expression):
    def __init__(self, name: str, arguments: List[Expression]):
        self.name = name
        self.arguments = arguments

class ArrayAccess(Expression):
    def __init__(self, array: Expression, index: Expression):
        self.array = array
        self.index = index

class ArrayLiteral(Expression):
    def __init__(self, elements: List[Expression]):
        self.elements = elements

class MemberAccess(Expression):
    def __init__(self, object: Expression, member: str):
        self.object = object
        self.member = member

# Statements
class Statement(ASTNode):
    pass

class Block(Statement):
    def __init__(self, statements: List[Statement]):
        self.statements = statements

class VariableDeclaration(Statement):
    """Maya (variable) or Sankalpa (constant) declaration"""
    def __init__(self, name: str, data_type: Optional[str], value: Optional[Expression], is_constant: bool = False):
        self.name = name
        self.data_type = data_type
        self.value = value
        self.is_constant = is_constant

class Assignment(Statement):
    def __init__(self, target: str, value: Expression):
        self.target = target
        self.value = value

class Manifest(Statement):
    """Print/output statement"""
    def __init__(self, expression: Expression):
        self.expression = expression

class Dharma(Statement):
    """If-else condition"""
    def __init__(self, condition: Expression, then_block: Block, else_block: Optional[Block] = None):
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block

class Karma(Statement):
    """Loop statement"""
    def __init__(self, loop_type: str, variable: Optional[str] = None, 
                 start: Optional[Expression] = None, end: Optional[Expression] = None,
                 iterable: Optional[Expression] = None, body: Optional[Block] = None):
        self.loop_type = loop_type  # "range" or "foreach"
        self.variable = variable
        self.start = start
        self.end = end
        self.iterable = iterable
        self.body = body

class Moksha(Statement):
    """Return statement"""
    def __init__(self, expression: Optional[Expression] = None):
        self.expression = expression

class Shloka(Statement):
    """Function definition"""
    def __init__(self, name: str, parameters: List['Parameter'], return_type: Optional[str], body: Block):
        self.name = name
        self.parameters = parameters
        self.return_type = return_type
        self.body = body

@dataclass
class Parameter:
    name: str
    data_type: str

class Arjuna(Statement):
    """Main function block"""
    def __init__(self, body: Block):
        self.body = body

class Yuga(Statement):
    """Module/namespace definition"""
    def __init__(self, name: str, body: Block):
        self.name = name
        self.body = body

class Meditation(Statement):
    """Try-catch block"""
    def __init__(self, try_block: Block, catch_variable: Optional[str] = None, catch_block: Optional[Block] = None):
        self.try_block = try_block
        self.catch_variable = catch_variable
        self.catch_block = catch_block

class ExpressionStatement(Statement):
    """Statement that wraps an expression"""
    def __init__(self, expression: Expression):
        self.expression = expression

# Program root
class Program(ASTNode):
    def __init__(self, statements: List[Statement]):
        self.statements = statements

# AST Visitor Pattern for traversal
class ASTVisitor(ABC):
    @abstractmethod
    def visit_program(self, node: Program):
        pass
    
    @abstractmethod
    def visit_literal(self, node: Literal):
        pass
    
    @abstractmethod
    def visit_identifier(self, node: Identifier):
        pass
    
    @abstractmethod
    def visit_binary_operation(self, node: BinaryOperation):
        pass
    
    @abstractmethod
    def visit_unary_operation(self, node: UnaryOperation):
        pass
    
    @abstractmethod
    def visit_function_call(self, node: FunctionCall):
        pass
    
    @abstractmethod
    def visit_array_access(self, node: ArrayAccess):
        pass
    
    @abstractmethod
    def visit_array_literal(self, node: ArrayLiteral):
        pass
    
    @abstractmethod
    def visit_block(self, node: Block):
        pass
    
    @abstractmethod
    def visit_variable_declaration(self, node: VariableDeclaration):
        pass
    
    @abstractmethod
    def visit_assignment(self, node: Assignment):
        pass
    
    @abstractmethod
    def visit_manifest(self, node: Manifest):
        pass
    
    @abstractmethod
    def visit_dharma(self, node: Dharma):
        pass
    
    @abstractmethod
    def visit_karma(self, node: Karma):
        pass
    
    @abstractmethod
    def visit_moksha(self, node: Moksha):
        pass
    
    @abstractmethod
    def visit_shloka(self, node: Shloka):
        pass
    
    @abstractmethod
    def visit_arjuna(self, node: Arjuna):
        pass
    
    @abstractmethod
    def visit_yuga(self, node: Yuga):
        pass
    
    @abstractmethod
    def visit_meditation(self, node: Meditation):
        pass
    
    @abstractmethod
    def visit_expression_statement(self, node: ExpressionStatement):
        pass