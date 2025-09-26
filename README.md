# LeetCode Practice Repository

## Overview
This repository contains my solutions to various LeetCode problems and coding practice exercises. It serves as a collection of algorithms and data structures implementations in Python.

## Files Structure
- `leet_test.ipynb` - Jupyter notebook containing interactive problem solutions and testing
- `class.py` - Python class implementations and utility functions

## Problems Solved

### String Manipulation
- **Longest Substring Without Repeating Characters** - Finding the length of the longest substring without duplicate characters using sliding window technique
- **Fraction to Decimal** - Converting fractions to decimal representation with repeating decimal detection

### Array/List Problems  
- **Two Sum** - Finding two numbers in an array that add up to a target value
- **Count Subarrays** - Counting subarrays that meet specific criteria using recursive backtracking

### Data Structure Implementations
- **Stack using Queues** - Implementing a stack data structure using deque operations
- **Queue using Stacks** - Implementing a queue data structure using stack operations
- **Recent Counter** - Tracking recent requests within a time window using deque

## Technologies Used
- **Python 3.13+**
- **Jupyter Notebooks** for interactive development and testing
- **Collections module** for deque implementations
- **Math module** for mathematical operations
- **Itertools** for combination generation

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Leet
   ```

2. Set up Python virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   ```

3. Install Jupyter (if not already installed):
   ```bash
   pip install jupyter
   ```

4. Launch Jupyter notebook:
   ```bash
   jupyter notebook leet_test.ipynb
   ```

## Usage
- Open `leet_test.ipynb` in Jupyter to run and test solutions interactively
- Import classes from `class.py` for reusable implementations
- Each solution includes test cases and examples

## Problem Solving Approach
- **Sliding Window** technique for string problems
- **Hash Maps/Dictionaries** for fast lookups
- **Two Pointers** for array traversal
- **Recursive Backtracking** for combination problems
- **Deque operations** for efficient queue/stack implementations

## Learning Goals
- Master common algorithmic patterns
- Practice different data structure implementations
- Improve problem-solving speed and accuracy
- Build a reference collection of solutions

## Contributing
This is a personal practice repository, but feel free to suggest optimizations or alternative approaches via issues or pull requests.

## License
MIT License - Feel free to use these solutions for learning purposes.
