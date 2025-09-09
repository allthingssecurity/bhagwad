"""
Bhagwad Programming Language - Transpiler
Converts Bhagwad AST to executable Python code
Inspired by the Bhagavad Gītā
"""

from typing import Any
from .ast_nodes import *

class BhagwadTranspiler(ASTVisitor):
    def __init__(self):
        self.output = []
        self.indent_level = 0
    
    def indent(self) -> str:
        """Get current indentation"""
        return "    " * self.indent_level
    
    def emit(self, code: str):
        """Emit code with proper indentation"""
        if code.strip():
            self.output.append(self.indent() + code)
        else:
            self.output.append("")
    
    def emit_raw(self, code: str):
        """Emit code without indentation"""
        self.output.append(code)
    
    def transpile(self, ast: Program) -> str:
        """Transpile AST to Python code"""
        self.output = []
        self.indent_level = 0
        
        # Add header comment
        self.emit_raw("#!/usr/bin/env python3")
        self.emit_raw('"""')
        self.emit_raw("Generated from Bhagwad Programming Language")
        self.emit_raw("Inspired by the Bhagavad Gītā")
        self.emit_raw('"""')
        self.emit_raw("")
        
        self.visit_program(ast)
        return "\n".join(self.output)
    
    def visit_program(self, node: Program):
        for statement in node.statements:
            self.visit_statement(statement)
            self.emit("")
    
    def visit_statement(self, node: Statement):
        if isinstance(node, Arjuna):
            self.visit_arjuna(node)
        elif isinstance(node, Shloka):
            self.visit_shloka(node)
        elif isinstance(node, Yuga):
            self.visit_yuga(node)
        elif isinstance(node, VariableDeclaration):
            self.visit_variable_declaration(node)
        elif isinstance(node, Assignment):
            self.visit_assignment(node)
        elif isinstance(node, Manifest):
            self.visit_manifest(node)
        elif isinstance(node, Dharma):
            self.visit_dharma(node)
        elif isinstance(node, Karma):
            self.visit_karma(node)
        elif isinstance(node, Moksha):
            self.visit_moksha(node)
        elif isinstance(node, Meditation):
            self.visit_meditation(node)
        elif isinstance(node, Block):
            self.visit_block(node)
        elif isinstance(node, ExpressionStatement):
            self.visit_expression_statement(node)
    
    def visit_literal(self, node: Literal):
        if node.data_type == 'rajas':  # string
            return f'"{node.value}"'
        elif node.data_type == 'tamas':  # boolean
            return str(node.value).title()
        else:  # sattva (number)
            return str(node.value)
    
    def visit_identifier(self, node: Identifier):
        return node.name
    
    def visit_binary_operation(self, node: BinaryOperation):
        left = self.visit_expression(node.left)
        right = self.visit_expression(node.right)
        
        # Map operators
        op_map = {
            '==': '==',
            '!=': '!=',
            '<': '<',
            '>': '>',
            '<=': '<=',
            '>=': '>=',
            '+': '+',
            '-': '-',
            '*': '*',
            '/': '/',
            '%': '%'
        }
        
        operator = op_map.get(node.operator, node.operator)
        return f"({left} {operator} {right})"
    
    def visit_unary_operation(self, node: UnaryOperation):
        operand = self.visit_expression(node.operand)
        return f"({node.operator}{operand})"
    
    def visit_function_call(self, node: FunctionCall):
        args = [self.visit_expression(arg) for arg in node.arguments]
        return f"{node.name}({', '.join(args)})"
    
    def visit_array_access(self, node: ArrayAccess):
        array = self.visit_expression(node.array)
        index = self.visit_expression(node.index)
        return f"{array}[{index}]"
    
    def visit_array_literal(self, node: ArrayLiteral):
        elements = [self.visit_expression(elem) for elem in node.elements]
        return f"[{', '.join(elements)}]"
    
    def visit_member_access(self, node):
        """Handle member access expressions like Module.function"""
        object_expr = self.visit_expression(node.object)
        return f"{object_expr}.{node.member}"
    
    def visit_expression(self, node: Expression) -> str:
        if isinstance(node, Literal):
            return self.visit_literal(node)
        elif isinstance(node, Identifier):
            return self.visit_identifier(node)
        elif isinstance(node, BinaryOperation):
            return self.visit_binary_operation(node)
        elif isinstance(node, UnaryOperation):
            return self.visit_unary_operation(node)
        elif isinstance(node, FunctionCall):
            return self.visit_function_call(node)
        elif isinstance(node, ArrayAccess):
            return self.visit_array_access(node)
        elif isinstance(node, ArrayLiteral):
            return self.visit_array_literal(node)
        elif isinstance(node, MemberAccess):
            return self.visit_member_access(node)
        else:
            raise ValueError(f"Unknown expression type: {type(node)}")
    
    def visit_block(self, node: Block):
        for statement in node.statements:
            self.visit_statement(statement)
    
    def visit_variable_declaration(self, node: VariableDeclaration):
        if node.value:
            value = self.visit_expression(node.value)
            if node.is_constant:
                # Constants in Python are just uppercase variables
                name = node.name.upper()
                self.emit(f"# Sankalpa (Constant): {node.name}")
                self.emit(f"{name} = {value}")
            else:
                self.emit(f"# Maya (Variable): {node.name}")
                if node.data_type:
                    self.emit(f"# Type: {self.map_type(node.data_type)}")
                self.emit(f"{node.name} = {value}")
        else:
            # Uninitialized variable
            default_val = self.get_default_value(node.data_type)
            self.emit(f"# Maya (Variable): {node.name}")
            if node.data_type:
                self.emit(f"# Type: {self.map_type(node.data_type)}")
            self.emit(f"{node.name} = {default_val}")
    
    def map_type(self, bhagwad_type: str) -> str:
        """Map Bhagwad types to Python types"""
        type_map = {
            'sattva': 'int',
            'rajas': 'str', 
            'tamas': 'bool',
            'sattva[]': 'List[int]',
            'rajas[]': 'List[str]',
            'tamas[]': 'List[bool]'
        }
        return type_map.get(bhagwad_type, 'Any')
    
    def get_default_value(self, bhagwad_type: str) -> str:
        """Get default value for a type"""
        defaults = {
            'sattva': '0',
            'rajas': '""',
            'tamas': 'False',
            'sattva[]': '[]',
            'rajas[]': '[]',
            'tamas[]': '[]'
        }
        return defaults.get(bhagwad_type, 'None')
    
    def visit_assignment(self, node: Assignment):
        value = self.visit_expression(node.value)
        self.emit(f"{node.target} = {value}")
    
    def visit_manifest(self, node: Manifest):
        expr = self.visit_expression(node.expression)
        self.emit(f"print({expr})  # Manifest: Make visible the invisible")
    
    def visit_dharma(self, node: Dharma):
        condition = self.visit_expression(node.condition)
        self.emit(f"if {condition}:  # Dharma: Righteous path")
        
        self.indent_level += 1
        self.visit_block(node.then_block)
        
        if node.else_block:
            self.indent_level -= 1
            self.emit("else:  # Adharma: Alternative path")
            self.indent_level += 1
            self.visit_block(node.else_block)
        
        self.indent_level -= 1
    
    def visit_karma(self, node: Karma):
        if node.loop_type == "range":
            start = self.visit_expression(node.start)
            end = self.visit_expression(node.end)
            self.emit(f"for {node.variable} in range({start}, {end} + 1):  # Karma: Cycle of action")
            
            self.indent_level += 1
            self.visit_block(node.body)
            self.indent_level -= 1
        elif node.loop_type == "foreach":
            iterable = self.visit_expression(node.iterable)
            self.emit(f"for {node.variable} in {iterable}:  # Karma: Cycle through collection")
            
            self.indent_level += 1
            self.visit_block(node.body)
            self.indent_level -= 1
    
    def visit_moksha(self, node: Moksha):
        if node.expression:
            expr = self.visit_expression(node.expression)
            self.emit(f"return {expr}  # Moksha: Liberation, return to source")
        else:
            self.emit("return  # Moksha: Liberation")
    
    def visit_shloka(self, node: Shloka):
        # Function signature
        params = []
        for param in node.parameters:
            params.append(f"{param.name}")
        
        param_str = ", ".join(params)
        self.emit(f"def {node.name}({param_str}):  # Shloka: Verse of computational wisdom")
        
        # Add docstring with parameter types
        if node.parameters or node.return_type:
            self.indent_level += 1
            self.emit('"""')
            if node.parameters:
                self.emit("Parameters:")
                for param in node.parameters:
                    mapped_type = self.map_type(param.data_type)
                    self.emit(f"    {param.name}: {mapped_type} ({param.data_type})")
            if node.return_type:
                mapped_return = self.map_type(node.return_type)
                self.emit(f"Returns: {mapped_return} ({node.return_type})")
            self.emit('"""')
            self.indent_level -= 1
        
        # Function body
        self.indent_level += 1
        if not node.body.statements:
            self.emit("pass")
        else:
            self.visit_block(node.body)
        self.indent_level -= 1
    
    def visit_arjuna(self, node: Arjuna):
        self.emit('if __name__ == "__main__":  # Arjuna: The eternal seeker begins the journey')
        self.indent_level += 1
        self.emit("# The battlefield of Kurukshetra - where computation meets consciousness")
        if not node.body.statements:
            self.emit("pass")
        else:
            self.visit_block(node.body)
        self.indent_level -= 1
    
    def visit_yuga(self, node: Yuga):
        self.emit(f"# Yuga: {node.name} - A cosmic age of functionality")
        self.emit(f"class {node.name}:")
        self.indent_level += 1
        if not node.body.statements:
            self.emit("pass")
        else:
            self.visit_block(node.body)
        self.indent_level -= 1
    
    def visit_meditation(self, node: Meditation):
        self.emit("try:  # Meditation: Focused awareness")
        self.indent_level += 1
        self.visit_block(node.try_block)
        self.indent_level -= 1
        
        if node.catch_block:
            self.emit(f"except Exception as {node.catch_variable}:  # Disturbance: When the mind wavers")
            self.indent_level += 1
            self.visit_block(node.catch_block)
            self.indent_level -= 1
    
    def visit_expression_statement(self, node: ExpressionStatement):
        expr = self.visit_expression(node.expression)
        self.emit(expr)

def transpile_bhagwad(ast: Program) -> str:
    """Transpile Bhagwad AST to Python code"""
    transpiler = BhagwadTranspiler()
    return transpiler.transpile(ast)