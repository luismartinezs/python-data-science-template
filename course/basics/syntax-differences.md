Here’s a summary of the key syntax differences between TypeScript and Python:

1. **Variable Declarations**:
   - **TypeScript**: Explicit `let`, `const`, or `var`. Types can be specified.
     ```typescript
     let x: number = 10
     ```
   - **Python**: No keyword needed, and types are inferred.
     ```python
     x = 10
     ```

2. **Type Annotations**:
   - **TypeScript**: Strongly typed (optional with `any`).
     ```typescript
     let y: string = "hello"
     ```
   - **Python**: Supports optional type hints, but dynamic by default.
     ```python
     y: str = "hello"
     ```

3. **Functions**:
   - **TypeScript**: Functions can be typed.
     ```typescript
     function greet(name: string): string {
       return `Hello, ${name}`
     }
     ```
   - **Python**: No function argument types by default, but can use type hints.
     ```python
     def greet(name: str) -> str:
         return f"Hello, {name}"
     ```

4. **Blocks & Indentation**:
   - **TypeScript**: Uses braces `{}` for code blocks.
     ```typescript
     if (condition) {
         // do something
     }
     ```
   - **Python**: Uses indentation to define code blocks.
     ```python
     if condition:
         # do something
     ```

5. **Conditionals**:
   - **TypeScript**: Uses `if`, `else if`, `else`.
     ```typescript
     if (x > 5) {
       // do something
     }
     ```
   - **Python**: Uses `if`, `elif`, `else`.
     ```python
     if x > 5:
         # do something
     ```

6. **Loops**:
   - **TypeScript**: Supports `for`, `while`, and `for...of` for iteration.
     ```typescript
     for (let i = 0; i < 5; i++) {
         console.log(i)
     }
     ```
   - **Python**: Uses `for` and `while`. No explicit C-style loops.
     ```python
     for i in range(5):
         print(i)
     ```

7. **Objects & Classes**:
   - **TypeScript**: Uses `class` with properties and methods.
     ```typescript
     class Person {
         name: string
         constructor(name: string) {
             this.name = name
         }
     }
     ```
   - **Python**: Similar `class` syntax but with `self` for instance variables.
     ```python
     class Person:
         def __init__(self, name: str):
             self.name = name
     ```

8. **Modules/Imports**:
   - **TypeScript**: Imports modules using `import`.
     ```typescript
     import { Component } from 'module'
     ```
   - **Python**: Uses `import` or `from ... import`.
     ```python
     from module import Component
     ```

9. **Arrays and Lists**:
   - **TypeScript**: Uses arrays with square brackets.
     ```typescript
     let arr: number[] = [1, 2, 3]
     ```
   - **Python**: Uses lists.
     ```python
     arr = [1, 2, 3]
     ```

10. **Null/Undefined**:
    - **TypeScript**: Has `null` and `undefined`.
    ```typescript
    let a: number | null = null
    ```
    - **Python**: Uses `None`.
    ```python
    a = None
    ```

These are the key differences, but overall Python has a more minimalist syntax compared to TypeScript, which emphasizes types and structure.