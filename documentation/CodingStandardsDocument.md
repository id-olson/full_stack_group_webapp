# Project Name: Coding Standards Document

## Table of Contents

- [Introduction](#introduction)
- [Naming Conventions](#naming-conventions)
- [Formatting and Style](#formatting-and-style)
- [Commenting and Documentation](#commenting-and-documentation)
- [Testing](#testing)

## Introduction

This document outlines the _Logic Luminaries_ coding standards and best practices for the Sudoku game generator. It's intended to guide the team in creating code that is functional, clean, consistent, and maintainable in both Python and JavaScript. (We may add more later).

## Naming Conventions

### Variables

- Python: Use snake_case for variable names.
- JavaScript: Use camelCase for variable names.
- Constants: Use UPPER_SNAKE_CASE in both languages.

### Functions

- Python: Use snake_case and start with a verb, eg., `fill_board`
- JavaScript: Use camelCase and start with a verb, e.g., `createScreen`.

### Classes

- Python & JavaScript: Use PascalCase and make names descriptive.

## Formatting and Style

### Python

- Use 4 spaces per indentation level.

```python
def fill_board(params):
    // Code block

```

### JavaScript

- Use 2 spaces for indentation.
- Place opening braces on the same line as the statement.

```javascript
if (condition) {
  // codee
}
```

## Commenting and Documentation

- Single line comments for confusing/unclear pieces of code in all languages

### Python

- Use docstrings for module, class, and function documentation.

```python
def calculate_total(numbers):
    """
    Calculates the total sum of numbers.

    :param numbers: List of numbers to sum.
    :return: The total sum.
    """
    return sum(numbers)

```

### JavaScript

- Use JSDoc for function documentation.

```javascript
/**
 * Calculates the total sum of numbers.
 * @param {number[]} numbers The numbers to sum.
 * @return {number} The total sum.
 */
function calculateTotal(numbers) {
  // code
}
```
