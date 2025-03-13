<<<<<<< HEAD
# Co-Writer
=======
# Co-Writer

## Overview
A minimalist Python program that interacts with a local Language Model (LLM) to generate text.

## Setup
1. Ensure you have Python 3.8+ installed
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
Run the main script:
```
python main.py
```

## Configuration
- The script defaults to connecting to a local LLM at `http://127.0.0.1:1234`
- Modify the `base_url` in the `CoWriter` class to change the LLM endpoint

## Features
- Simple text generation from a given prompt
- Error handling for LLM communication
- Easily extensible base class
>>>>>>> 97a37e4 (Initial commit: Co-Writer project setup)
