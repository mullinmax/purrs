# Contributing to Purrs

Thank you for considering contributing to Purrs! We value your effort and want to make this process as easy and transparent as possible.

At this stage, Purrs is in alpha, and we're primarily focused on code development and bug reporting. Here are the ways you can contribute:

- Code development: Contribute to the codebase to enhance functionality, add features, or fix bugs.
- QA: File detailed bug reports, the more details you can give the better (e.g., screenshots).

## Your First Contribution

If you're unsure where to begin contributing to Purrs, you can start by looking through these issues:

- Bug issues: issues which are confirmed bugs.
- Feature issues: issues which are requesting new features.

## Code of Conduct

While participating in this project, please adhere to the respect and courtesy expected of a professional work environment. This goes for both project maintainers and anyone seeking to contribute.

## Setup

To set up the development environment for Purrs, you need to run:

```bash
pip install -r requirements.txt
```

## Style Guidelines

This project uses Python for the majority of the codebase. Therefore, contributors should follow the PEP8 style guide for Python. Additionally, please organize imports alphabetically and group them in the following order: standard library imports, related third party imports, local application/library specific imports.

In terms of commenting, the code should show *how* it's doing what it's doing. Comments should explain *why* the code is doing what it's doing.

## Testing

We use pytest for testing. Please add tests when possible and run the existing test suite to ensure your changes do not break existing functionality. If it is not feasible to add tests for your changes, please explain why in your pull request.

To run the tests, you can use the following command:

```bash
pytest
```

## Submitting Changes

Please follow these steps to have your contribution considered by the maintainers:

1. Navigate to the main page of the repository on [OneDev](https://dev.doze.dev/purrs).
2. Create a new branch for your changes using `git checkout -b name_of_your_new_branch`.
3. Make your changes in the new branch.
4. Test your changes to ensure they do not break existing functionality.
5. Push your changes to your branch on OneDev.
6. Submit a pull request from your branch to the main Purrs repository.

Please note that the project maintainers will review your pull request and may suggest changes. 

## Recognition of Contributors

We value your contributions and want to make sure you're recognized! All contributions will be thanked publicly in our project's README.