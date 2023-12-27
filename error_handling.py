```python
import traceback

class ErrorHandler:
    def __init__(self):
        pass

    def handle(self, exception):
        """Handle the given exception."""
        self.log_error(exception)
        self.display_error_message(exception)

    def log_error(self, exception):
        """Log the error details for debugging purposes."""
        with open("error_log.txt", "a") as file:
            file.write(f"Error: {str(exception)}\n")
            file.write(f"Traceback:\n{traceback.format_exc()}\n")

    def display_error_message(self, exception):
        """Display an error message to the user."""
        print(f"An error occurred: {str(exception)}")
        print("Please check the error log for more details.")
```
