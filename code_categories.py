```python
class CodeCategories:
    def __init__(self):
        self.categories = {
            "data_manipulation": ["sorting", "filtering", "mapping", "reducing"],
            "file_handling": ["read", "write", "append", "delete"],
            "web_scraping": ["html_parsing", "api_request", "data_extraction"],
            # Add more categories and tasks as needed
        }

    def get_tasks(self, category):
        """Return a list of tasks for a given category."""
        return self.categories.get(category, [])

    def get_all_categories(self):
        """Return a list of all available categories."""
        return list(self.categories.keys())

    def validate_category(self, category):
        """Check if a given category exists."""
        return category in self.categories

    def validate_task(self, category, task):
        """Check if a given task exists in a given category."""
        return task in self.get_tasks(category)
```
