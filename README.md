# 🕉️ Bhagwad Programming Language

> *"Just as the Gītā guides the soul toward moksha, Bhagwad guides the programmer toward computational enlightenment."*

**Bhagwad** is an esoteric programming language inspired by the timeless wisdom of the Bhagavad Gītā. It combines spiritual metaphors with programming constructs to create a meditative coding experience that reflects the philosophical journey of self-realization.

## 🌟 Features

- **Spiritual Syntax**: Programming constructs based on Sanskrit concepts from the Bhagavad Gītā
- **Complete Language**: Full lexer, parser, and transpiler implementation
- **Python Integration**: Transpiles to clean, executable Python code
- **Sacred Data Types**: Sattva (int), Rajas (string), Tamas (bool)
- **Dharmic Control Flow**: Dharma (if/else), Karma (loops), Moksha (return)
- **Modular Design**: Yuga (modules/namespaces) for organized code
- **Error Handling**: Meditation (try) and Disturbance (catch) blocks

## 🚀 Quick Start

### Installation
```bash
git clone <repository>
cd bhagwad
```

### Running Your First Bhagwad Program
```bash
# Create a simple program
echo 'arjuna { manifest "Om" }' > hello.bhagwad

# Execute it
python3 bhagwad.py hello.bhagwad

# Compile to Python
python3 bhagwad.py -c hello.bhagwad
```

## 📖 Language Overview

### Core Constructs

| Bhagwad | English | Python Equivalent | Spiritual Meaning |
|---------|---------|-------------------|-------------------|
| `arjuna` | main | `if __name__ == "__main__"` | The eternal seeker who begins the journey |
| `shloka` | function | `def` | Verse of computational wisdom |
| `dharma` | if | `if` | Righteous path based on conditions |
| `adharma` | else | `else` | Alternative path |
| `karma` | loop | `for`/`while` | Cycle of action and consequence |
| `manifest` | print | `print()` | Make the invisible visible |
| `moksha` | return | `return` | Liberation, return to source |
| `maya` | variable | variable | Temporary holder of changing states |
| `sankalpa` | constant | constant | Unwavering intention/resolve |
| `yuga` | module | `class` | Cosmic age of functionality |
| `meditation` | try | `try` | Focused awareness |
| `disturbance` | catch | `except` | When the mind wavers |

### Data Types (Gunas)

| Guna | Type | Description |
|------|------|-------------|
| `sattva` | Integer | Pure, balanced numbers (सत्त्व) |
| `rajas` | String | Active, passionate text (रजस्) |
| `tamas` | Boolean | Dark/light, true/false duality (तमस्) |

## 📝 Example Programs

### 1. Om Manifestation (Hello World)
```bhagwad
// Om Manifestation - The sacred sound that creates and sustains the universe
arjuna {
    manifest "Om"
}
```

### 2. Decimal Dharma (Loop Example)
```bhagwad
// Counting from 1 to 10 through the cycle of Karma
arjuna {
    manifest "The eternal cycle begins..."
    
    karma i from 1 to 10 {
        manifest i
    }
    
    manifest "The cycle is complete. Om Shanti."
}
```

### 3. Duality Detection (Conditional Example)
```bhagwad
// Determining the even or odd nature of numbers
shloka checkDuality(sattva number) {
    dharma (number % 2 == 0) {
        manifest number + " follows the even path of balance"
    } adharma {
        manifest number + " follows the odd path of uniqueness"  
    }
}

arjuna {
    manifest "🕉️  Exploring the duality of numbers..."
    
    sankalpa SACRED_SEVEN = 7
    sankalpa SACRED_EIGHT = 8
    sankalpa DIVINE_NUMBER = 108
    
    checkDuality(SACRED_SEVEN)
    checkDuality(SACRED_EIGHT)
    checkDuality(DIVINE_NUMBER)
    
    manifest "In duality, we find unity. In numbers, we find truth."
}
```

## 🛠️ Usage

### Command Line Interface
```bash
# Execute a .bhagwad file
python3 bhagwad.py program.bhagwad

# Compile to Python
python3 bhagwad.py -c program.bhagwad [output.py]

# Debug mode (show compilation steps)
python3 bhagwad.py -d program.bhagwad

# Interactive mode
python3 bhagwad.py -i

# Run all examples
python3 bhagwad.py --examples
```

### Interactive Mode
```bash
$ python3 bhagwad.py -i
🕉️  Bhagwad Interactive Mode
Enter Bhagwad code (type 'exit' to quit, 'help' for commands):
bhagwad> manifest "Hello, World!"
Hello, World!
bhagwad> exit
🙏 Om Shanti. May your code bring enlightenment.
```

## 🏗️ Architecture

The Bhagwad interpreter consists of four main components:

1. **Lexer** (`src/lexer.py`) - Tokenizes Bhagwad source code
2. **Parser** (`src/parser.py`) - Converts tokens to Abstract Syntax Tree (AST)
3. **Transpiler** (`src/transpiler.py`) - Converts AST to Python code
4. **Interpreter** (`src/interpreter.py`) - Orchestrates the compilation and execution

### Project Structure
```
bhagwad/
├── bhagwad.py              # Main entry point
├── src/
│   ├── __init__.py         # Module initialization
│   ├── lexer.py           # Lexical analysis
│   ├── parser.py          # Syntax analysis
│   ├── transpiler.py      # Code generation
│   ├── interpreter.py     # Main orchestrator
│   └── ast_nodes.py       # AST node definitions
├── examples/
│   ├── om_manifestation.bhagwad
│   ├── decimal_dharma.bhagwad
│   ├── duality_detection.bhagwad
│   └── cosmic_mathematics.bhagwad
├── docs/
│   └── LANGUAGE.md        # Complete language specification
└── README.md              # This file
```

## 📚 Documentation

- [`LANGUAGE.md`](docs/LANGUAGE.md) - Complete language specification with spiritual parallels
- [`examples/`](examples/) - Sample programs demonstrating all language features

## 🎯 Sacred Numbers in Bhagwad

- **108**: Sacred number representing completeness
- **9**: Number of devotion (Navagraha)  
- **7**: Number of chakras and spiritual levels
- **3**: Trinity (Creator, Preserver, Destroyer)

## 🧘 Philosophy of Bhagwad Programming

1. **Mindful Coding**: Every line should be written with intention and awareness
2. **Dharmic Logic**: Code should follow righteous patterns and ethical algorithms  
3. **Karmic Loops**: Iterations should serve a higher purpose
4. **Detached Results**: Write code without attachment to outcomes
5. **Universal Truth**: Seek solutions that reflect cosmic principles

## 🚀 Advanced Features

### Cosmic Arrays
```bhagwad
cosmic sattva[] sacredNumbers = [108, 9, 7, 3]
```

### Meditation Blocks (Error Handling)
```bhagwad
meditation {
    sattva result = divide(108, 0)
} disturbance (error) {
    manifest "The mind encountered a disturbance: " + error
}
```

### Yuga Modules
```bhagwad
yuga Mathematics {
    shloka add(sattva a, sattva b) -> sattva {
        moksha a + b
    }
}
```

## 🤝 Contributing

We welcome contributions that align with the spiritual and philosophical goals of the Bhagwad language. Please ensure your code:

- Follows the spiritual metaphors and naming conventions
- Includes appropriate documentation with Sanskrit parallels
- Maintains the meditative and mindful approach to programming

## 📄 License

This project is released under the MIT License, dedicated to spreading computational dharma and programming enlightenment.

## 🙏 Acknowledgments

- Inspired by the eternal wisdom of the Bhagavad Gītā
- Built with reverence for the intersection of spirituality and technology
- Dedicated to all seekers on the path of computational enlightenment

---

*"In the battlefield of code, let dharma be your guide, karma your teacher, and moksha your destination."*

**Om Shanti Shanti Shanti** 🕉️