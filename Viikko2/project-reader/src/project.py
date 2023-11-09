class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, authors, license):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.authors = authors
        self.license = license

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"
    
    def _stringify_authors(self, authors):
        return ", ".join(authors) if len(authors) > 0 else "-"
    
    def _stringify_devdependencies(self, devdependencies):
        return ", ".join(devdependencies) if len(devdependencies) > 0 else "-"

    def __str__(self):
        dep_keys = list(self.dependencies.keys())
        dev_dep_keys = list(self.dev_dependencies.keys())
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}"
            f"\n"
            f"\nAuthors:"
            f"\n- {self.authors[0]}"
            f"\n- {self.authors[1]}"
            f"\n"
            f"\nDependencies:"
            f"\n- {dep_keys[0]}"
            f"\n- {dep_keys[1]}"
            f"\n- {dep_keys[2]}"
            f"\n"
            f"\nDevelopment dependencies:"
            f"\n- {dev_dep_keys[0]}"
            f"\n- {dev_dep_keys[1]}"
            f"\n- {dev_dep_keys[2]}"
            f"\n- {dev_dep_keys[3]}"
        )
