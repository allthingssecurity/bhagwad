#!/usr/bin/env python3
"""
Bhagwad Programming Language - Main Entry Point
Execute .bhagwad files and explore spiritual programming
Inspired by the Bhagavad Gītā
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.interpreter import BhagwadInterpreter

def main():
    """Main entry point for Bhagwad interpreter"""
    print("🕉️  Welcome to Bhagwad Programming Language")
    print("   Inspired by the eternal wisdom of the Bhagavad Gītā")
    print("   'Just as the Gītā guides the soul toward moksha,")
    print("    Bhagwad guides the programmer toward computational enlightenment.'")
    print()
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python bhagwad.py <file.bhagwad>     # Execute file")
        print("  python bhagwad.py -c <file.bhagwad>  # Compile to Python")
        print("  python bhagwad.py -d <file.bhagwad>  # Debug mode")
        print("  python bhagwad.py -i                 # Interactive mode")
        print("  python bhagwad.py --examples         # Run example programs")
        print()
        print("Example files:")
        examples_dir = os.path.join(os.path.dirname(__file__), "examples")
        if os.path.exists(examples_dir):
            for file in sorted(os.listdir(examples_dir)):
                if file.endswith('.bhagwad'):
                    print(f"  examples/{file}")
        return
    
    interpreter = BhagwadInterpreter()
    
    if sys.argv[1] == '--examples':
        # Run all example programs
        examples_dir = os.path.join(os.path.dirname(__file__), "examples")
        if not os.path.exists(examples_dir):
            print("❌ Examples directory not found")
            return
        
        example_files = [f for f in os.listdir(examples_dir) if f.endswith('.bhagwad')]
        example_files.sort()
        
        for example_file in example_files:
            filepath = os.path.join(examples_dir, example_file)
            print(f"\n{'='*60}")
            print(f"🌟 Running: {example_file}")
            print(f"{'='*60}")
            
            try:
                interpreter.execute_file(filepath)
            except Exception as e:
                print(f"❌ Error in {example_file}: {e}")
        
        print(f"\n{'='*60}")
        print("🙏 All examples completed. Om Shanti.")
        return
    
    elif sys.argv[1] == '-i':
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