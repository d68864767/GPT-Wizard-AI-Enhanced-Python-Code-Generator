```python
import re

class Security:
    def __init__(self):
        self.blacklist = ["os.system", "subprocess.run", "exec", "eval", "compile", "open", "file", "input"]

    def check(self, task_description):
        """Check if the task description contains any potentially harmful commands."""
        for command in self.blacklist:
            if command in task_description:
                raise SecurityException(f"Potentially harmful command detected: {command}")

class SecurityException(Exception):
    """Exception raised for security-related issues."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
```
