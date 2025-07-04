# OpenAI API Prompt Engineering Modules

This repository contains commonly used functions and classes for efficient prompt engineering with the OpenAI API.

## Modules

### `chat_template`
A module designed to simplify the creation of chat templates. It includes two functions:

- **`begin_conversation()`**: Integrates a chat template with memory, which can be directly used in the backend.
- **`one_shot()`**: A concise function for creating a one-shot prompt question with a single line of code.

### `extraction`
Optimized for extracting data through one-shot prompting and returning it as a dictionary. This module requires two parameters:

- **`extraction_schema`**: A dictionary defining the structure of the extracted data. The key should represent the variable, and the value should describe it.  
  Example:  
  ```python
  { 'first_name': 'What was the person’s first name?', 'last_name': 'What was the person’s last name?' }
  ```
**example_schema:** Provides an example to guide the model in understanding what to expect.

This module is especially effective when chaining prompts to structure data. For detailed explanations, feel free to reach out.

## classification
Optimized for one-shot classification tasks. This module requires two parameters:

- **categories:** A list of categories to classify into.

- **examples:** A list of example pairs, where each pair is a tuple of the format `(input, category)`. Example:

```python
[ ('I loved dinner last night', 'positive'), ('I hated the dinner', 'negative') ]
```
## llm_chain
A simple chain of thought module, typically used with f-strings to process data from previous prompts. This module demonstrates how to integrate a series of prompts and results into a streamlined process.

## db_modules
Optimized functions for inserting data into a database. Currently, there is support for SQLite:

- **sqlite:** Takes in a dictionary, processes it to handle errors, and inserts it into an SQLite database. Ensure the dictionary keys match the table column names.

- **Database class:** A helper class to connect to the SQLite database. It accepts a single parameter, `DATABASE_URL`, for initialization.
