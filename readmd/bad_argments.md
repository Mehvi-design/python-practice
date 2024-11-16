
# Custom Annotation for Handling Bad Arguments

## Objective
Create a custom annotation (decorator) in Python that checks the arguments passed to a function. If any of the arguments are not integers, it raises a custom exception called `NonIntArgumentException`. This is useful for ensuring that only valid arguments are passed to functions.

## Task Requirements

1. **Create a custom exception:**
   - Define a custom exception class called `NonIntArgumentException` that will be raised when an argument is not an integer.

2. **Implement the custom annotation (decorator):**
   - Create a decorator called `handleNonIntArguments`. This decorator will check if any of the arguments passed to a function are not integers.
   - If any of the arguments are not integers, raise the `NonIntArgumentException`.
   - If all arguments are valid integers, the decorator should allow the function to execute and return its result.

3. **Understand the function signature:**
   - The decorator should take a function (`func`) as an argument and return a new function (the wrapper function).
   - The wrapper function should accept arbitrary arguments (`*args`) and pass them to the original function.

4. **Ensure the function returns a result:**
   - The wrapper function should execute the original function and return the result if all arguments are integers.

## Parameters

- `func`: The function that will be called with the arguments.
- `*args`: The arguments passed to `func`. These will be checked to ensure they are integers.

## Expected Results

- The function should return the result of the computation if all arguments are integers.
- If any argument is not an integer, the `NonIntArgumentException` should be raised.

## Example Usage

### Example 1
**Input to `sum`:**
```python
sum(1, 2, 3)
```
**Expected Result:**
```
6
```

### Example 2
**Input to `sum`:**
```python
sum(1.5, 'foo', 3)
```
**Expected Result:**
```
NonIntArgumentException
```

## Notes

- Make sure the custom exception (`NonIntArgumentException`) is appropriately raised when non-integer arguments are encountered.
- The decorator should properly wrap the function and handle the arguments.
- Verify that the wrapper function returns the result of the original function when no exception is raised.

## Conclusion
This task will help you practice writing custom decorators and exceptions in Python. By implementing the `handleNonIntArguments` decorator, you can ensure that only integer arguments are passed to certain functions, and handle errors gracefully when that is not the case.
```