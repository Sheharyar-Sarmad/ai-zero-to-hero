# MCP Server Deployment to PyPI

A practical guide to packaging a Python MCP server and publishing it to the Python Package Index (PyPI) so other developers can install and use it.

This module focuses on **packaging, building, testing, publishing, and distributing** an MCP server using Python and `uv`.

## Prerequisites

**Complete the MCP theory and Python code implementation modules before starting this module.**

You should already understand:

- MCP architecture, hosts, clients, servers, tools, and transports.
- How to implement an MCP server and expose its tools.
- How Python packages, modules, dependencies, and entry points work.
- Basic command-line usage and Python virtual environments.

This module assumes you can already build an MCP server. Its purpose is to teach you how to package and distribute that implementation.

## Project Structure

```text
05_MCP_deployment/
├── src/
│   ├── agentic_terminal/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── tools.py
│   └── agentic_terminal.egg-info/
├── dist/
│   ├── agentic_terminal-0.1.0-py3-none-any.whl
│   └── agentic_terminal-0.1.0.tar.gz
├── .gitignore
├── .python-version
├── pyproject.toml
├── requirements.txt
├── README.md
├── test.py
└── uv.lock
```

The `dist/` directory contains the distribution files generated during the build process. The `.egg-info/` directory contains package metadata and may be generated during packaging.

These generated directories should not normally be edited manually.

## The Deployment Workflow

### 1. Understand What PyPI Does

[PyPI](https://pypi.org/) is the Python Package Index. It distributes Python packages so that other developers can install them using tools such as `pip` or `uv`.

Publishing your MCP server to PyPI means distributing your installable Python package. It does **not** automatically deploy a remotely accessible MCP server to a cloud provider.

### 2. Prepare the Package

Inspect `pyproject.toml` and verify that it contains the correct package metadata, dependencies, build configuration, and entry points.

Check the following:

- A unique package name.
- A valid version number.
- A short description and a useful README.
- Correct runtime dependencies.
- A configured build backend.
- Correct package discovery for the `src/` layout.
- A console script entry point, if users should run the server as a command.

Keep the distribution name and Python import package name distinct where appropriate. For example, the distribution might be named `agentic-terminal`, while its Python package is `agentic_terminal`.

### 3. Test the Implementation

Before packaging, run the server locally and verify that its tools work as expected.

Run your existing tests:

```powershell
uv run python test.py
```

Also test the MCP server using an MCP-compatible client. Verify tool discovery, tool execution, error handling, and any required environment variables.

### 4. Build the Distribution

Build both the source distribution and the wheel:

```powershell
uv build --no-sources
```

The generated files should appear in `dist/`:

- **Wheel (`.whl`)** — a built distribution that installers can install directly.
- **Source distribution (`.tar.gz`)** — the source package from which a distribution can be built.

Check that the build completes successfully. If you change package metadata or source files, rebuild before publishing.

### 5. Validate the Build

Install Twine temporarily and validate the generated package metadata:

```powershell
uv run --with twine python -m twine check dist/*
```

Resolve warnings or errors before proceeding.

For stronger validation, create a clean virtual environment and test whether the built distribution installs and imports correctly. This helps catch missing files and undeclared dependencies that might be hidden by your development environment.

### 6. Test the Publication with TestPyPI

[TestPyPI](https://test.pypi.org/) is a separate package index for practising and testing the publishing workflow.

Create a TestPyPI account and generate an API token from its account settings. TestPyPI credentials are separate from your regular PyPI credentials.

Upload your distributions:

```powershell
uv run --with twine python -m twine upload --repository testpypi dist/*
```

When prompted, enter `__token__` as the username and your TestPyPI token as the password.

Open the resulting package page on TestPyPI and verify that its metadata and release files appear correctly.

### 7. Create a PyPI Account and Token

When you are ready for the production release:

1. Create an account at [PyPI](https://pypi.org/account/register/).
2. Verify your email address and enable appropriate account security.
3. Generate a PyPI API token.
4. Use a project-scoped token when possible, once the project exists.

Never commit API tokens to source control or put them directly into your README.

For automated releases from a supported CI provider, consider [PyPI Trusted Publishing](https://docs.pypi.org/trusted-publishers/), which avoids storing a long-lived publishing token in your workflow.

### 8. Publish to PyPI

Confirm the package name and version in `pyproject.toml`. Then publish the validated distributions:

```powershell
uv run --with twine python -m twine upload dist/*
```

When prompted, enter `__token__` as the username and your production PyPI token as the password.

After a successful upload, visit:

```text
https://pypi.org/project/agentic-terminal/
```

Replace `agentic-terminal` with your actual distribution name if it differs.

**Important:** PyPI does not allow you to replace an already published file for the same package version. If you need to publish a correction, increase the version, rebuild, validate, and upload the new distributions.

### 9. Test Installation from PyPI

Once your package is available, test it outside the source directory in a clean environment:

```powershell
uv venv .venv-package-test
```

Activate the environment:

```powershell
.\.venv-package-test\Scripts\Activate.ps1
```

Install the published package:

```powershell
uv pip install agentic-terminal
```

Replace the name with your published distribution name.

Verify that the Python package imports correctly. If you configured a console script in `pyproject.toml`, test that command as well.

Finally, connect an MCP-compatible client to the installed server and verify that its tools are discoverable and executable.

### 10. Release Future Versions

For every subsequent release:

1. Update the implementation or metadata.
2. Run tests.
3. Increase the package version.
4. Build and validate the distributions.
5. Test the release where appropriate.
6. Publish the new version to PyPI.
7. Verify the published package and installation.

With `uv`, you can increment the patch version using:

```powershell
uv version --bump patch
```

For future automation, consider a CI/CD workflow with PyPI Trusted Publishing.

## Final Checklist

- [ ] MCP theory and local implementation completed.
- [ ] Package metadata and dependencies verified.
- [ ] MCP server and tools tested locally.
- [ ] Wheel and source distribution built successfully.
- [ ] Distribution metadata validated.
- [ ] TestPyPI publication tested.
- [ ] PyPI account and publishing credentials configured securely.
- [ ] Production distributions published.
- [ ] Package installed and tested outside the development environment.
- [ ] Versioning and future release workflow understood.

## Important Note

This module is for learning **MCP package deployment and distribution**, not for building a complete production application.

The objective is to understand how working MCP implementations become installable Python packages. Hosting a persistent remote MCP server, configuring production infrastructure, and building real-world MCP applications are separate topics to explore after completing this module.

## Official Resources

- [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [Building and publishing packages with uv](https://docs.astral.sh/uv/guides/package/)
- [PyPI publishing documentation](https://docs.pypi.org/publishing/publishing-to-pypi/)
- [TestPyPI guide](https://packaging.python.org/en/latest/guides/using-testpypi/)
- [PyPI Trusted Publishing](https://docs.pypi.org/trusted-publishers/)
