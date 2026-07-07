The error message you're seeing typically occurs when there is a missing parenthesis or some other syntax issue. Without the actual line causing the error, I can only provide general guidance on how to debug a Python script. Here are some general tips:

1. Check all your function definitions and ensure they end with a colon (`:`) and that each statement in them ends with a newline or semicolon (`;`). 
2. Ensure that all control flow structures, like `if` statements, loops, etc., are closed properly by their respective closing constructs. For example, an `if` statement should end with an `elif`, `else`, or `endif` depending on the language syntax you're using.
3. Ensure that all your files start with a shebang line at the top (for Python scripts) which specifies the location of the interpreter and can be written as follows: `#!/usr/bin/env python3`
4. Check for any missing or unmatched quotes in strings, especially when using double quotes (`" "`). 
5. Look out for any commented code that might not have been closed properly by a comment syntax like `#;` in Python.
6. Ensure that all your functions are defined before they're called. If you define and call a function within the same file, this error can occur.
7. Make sure to close every open parenthesis with its matching closing one (like `(` with `)`, or `[` with `]`).
8. Check for any indentation issues in your Python code that might be causing syntax errors. 

Please provide the actual line causing the error so I could give a more precise solution to your problem.