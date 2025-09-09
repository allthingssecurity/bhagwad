"""
Bhagwad Programming Language - Main Interpreter
Combines lexer, parser, and transpiler to execute Bhagwad code
Inspired by the Bhagavad Gītā
"""

import sys
import os
from pathlib import Path
from .lexer import BhagwadLexer
from .parser import BhagwadParser, ParseError
from .transpiler import transpile_bhagwad

class BhagwadInterpreter:
    def __init__(self):
        self.debug = False
    
    def set_debug(self, debug: bool):
        """Enable/disable debug output"""
        self.debug = debug
    
    def interpret_file(self, filepath: str) -> str:
        """Interpret a .bhagwad file and return Python code"""
        if not filepath.endswith('.bhagwad'):
            raise ValueError("File must have .bhagwad extension")
        
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            source = f.read()
        
        return self.interpret_source(source)
    
    def interpret_source(self, source: str) -> str:
        """Interpret Bhagwad source code and return Python code"""
        try:
            # Lexical analysis
            if self.debug:
                print("🕉️  Starting lexical analysis...")
            
            lexer = BhagwadLexer(source)
            tokens = lexer.tokenize()
            
            if self.debug:
                print(f"📿 Generated {len(tokens)} tokens")
                for token in tokens[:10]:  # Show first 10 tokens
                    print(f"   {token}")
                if len(tokens) > 10:
                    print("   ...")
            
            # Syntax analysis
            if self.debug:
                print("🧘 Starting syntax analysis...")
            
            parser = BhagwadParser(tokens)
            ast = parser.parse()
            
            if self.debug:
                print("✨ AST generated successfully")
            
            # Transpilation
            if self.debug:
                print("🔮 Transpiling to Python...")
            
            python_code = transpile_bhagwad(ast)
            
            if self.debug:
                print("🙏 Transpilation complete")
            
            return python_code
            
        except ParseError as e:
            error_msg = f"Dharmic Error (Syntax): {e}"
            if self.debug:
                print(f"❌ {error_msg}")
            raise SyntaxError(error_msg)
        
        except Exception as e:
            error_msg = f"Karmic Disturbance: {e}"
            if self.debug:
                print(f"❌ {error_msg}")
            raise RuntimeError(error_msg)
    
    def execute_file(self, filepath: str):
        """Execute a .bhagwad file directly"""
        python_code = self.interpret_file(filepath)
        
        if self.debug:
            print("🌟 Generated Python code:")
            print("=" * 50)
            print(python_code)
            print("=" * 50)
            print("🏃 Executing...")
        
        # Execute the generated Python code
        exec(python_code)
    
    def execute_source(self, source: str):
        """Execute Bhagwad source code directly"""
        python_code = self.interpret_source(source)
        
        if self.debug:
            print("🌟 Generated Python code:")
            print("=" * 50)
            print(python_code)
            print("=" * 50)
            print("🏃 Executing...")
        
        # Execute the generated Python code
        exec(python_code)
    
    def compile_to_file(self, source_file: str, output_file: str = None):
        """Compile .bhagwad file to .py file"""
        if output_file is None:
            output_file = source_file.replace('.bhagwad', '.py')
        
        python_code = self.interpret_file(source_file)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(python_code)
        
        if self.debug:
            print(f"📝 Compiled {source_file} -> {output_file}")
        
        return output_file

def main():
    """Command line interface for Bhagwad interpreter"""
    if len(sys.argv) < 2:
        print("🕉️  Bhagwad Programming Language")
        print("Inspired by the Bhagavad Gītā")
        print()
        print("Usage:")
        print("  python -m bhagwad <file.bhagwad>     # Execute file")
        print("  python -m bhagwad -c <file.bhagwad>  # Compile to Python")
        print("  python -m bhagwad -d <file.bhagwad>  # Debug mode")
        print("  python -m bhagwad -i                 # Interactive mode")
        return
    
    interpreter = BhagwadInterpreter()
    
    if sys.argv[1] == '-i':
        # Interactive mode
        print("🕉️  Bhagwad Interactive Mode")
        print("Enter Bhagwad code (type 'exit' to quit, 'help' for commands):")
        
        while True:
            try:
                line = input("bhagwad> ")
                
                if line.strip() == 'exit':
                    print("🙏 Om Shanti. May your code bring enlightenment.")
                    break
                elif line.strip() == 'help':
                    print("Commands:")
                    print("  exit     - Quit interpreter")
                    print("  help     - Show this help")
                    print("  debug on - Enable debug mode")
                    print("  debug off- Disable debug mode")
                    continue
                elif line.strip() == 'debug on':
                    interpreter.set_debug(True)
                    print("🔍 Debug mode enabled")
                    continue
                elif line.strip() == 'debug off':
                    interpreter.set_debug(False)
                    print("🔇 Debug mode disabled")
                    continue
                
                if line.strip():
                    interpreter.execute_source(line)
                    
            except KeyboardInterrupt:
                print("\n🙏 Om Shanti. May your code bring enlightenment.")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
    
    elif sys.argv[1] == '-c':
        # Compile mode
        if len(sys.argv) < 3:
            print("❌ Please specify a .bhagwad file to compile")
            return
        
        source_file = sys.argv[2]
        output_file = sys.argv[3] if len(sys.argv) > 3 else None
        
        try:
            interpreter.set_debug(True)
            result = interpreter.compile_to_file(source_file, output_file)
            print(f"✨ Compilation successful: {result}")
        except Exception as e:
            print(f"❌ Compilation failed: {e}")
    
    elif sys.argv[1] == '-d':
        # Debug mode
        if len(sys.argv) < 3:
            print("❌ Please specify a .bhagwad file to execute")
            return
        
        source_file = sys.argv[2]
        
        try:
            interpreter.set_debug(True)
            interpreter.execute_file(source_file)
        except Exception as e:
            print(f"❌ Execution failed: {e}")
    
    else:
        # Normal execution mode
        source_file = sys.argv[1]
        
        try:
            interpreter.execute_file(source_file)
        except Exception as e:
            print(f"❌ Execution failed: {e}")

if __name__ == "__main__":
    main()