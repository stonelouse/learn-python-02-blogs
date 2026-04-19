# learn-python-02-blogs

- Python notes from blogs

- [learn-python-02-blogs](#learn-python-02-blogs)
  - [Python Tooling Setup (Workspace)](#python-tooling-setup-workspace)
    - [Why this path for the virtual environment?](#why-this-path-for-the-virtual-environment)
    - [Daily workflow](#daily-workflow)
    - [Before writing new code](#before-writing-new-code)
  - [Real Python](#real-python)
    - [Resources](#resources)
    - [To Study](#to-study)

## Python Tooling Setup (Workspace)

- One shared virtual environment is used for the whole workspace:
  `/home/vscode/.venvs/learn-python-02-blogs`
- The selected interpreter in VS Code is:
  `/home/vscode/.venvs/learn-python-02-blogs/bin/python`
- Linting and formatting tool:
  `ruff`
- Workspace configuration files:
  - `.vscode/settings.json`
  - `.vscode/extensions.json`
  - `pyproject.toml`

Configured behavior:

- Format Python files on save
- Run Ruff linting in-editor
- Keep imports organized via Ruff code actions

CLI checks:

```bash
/home/vscode/.venvs/learn-python-02-blogs/bin/ruff check .
/home/vscode/.venvs/learn-python-02-blogs/bin/ruff format --check .
```

Auto-fix and format:

```bash
/home/vscode/.venvs/learn-python-02-blogs/bin/ruff format .
/home/vscode/.venvs/learn-python-02-blogs/bin/ruff check .
```

### Why this path for the virtual environment?

Creating `.venv` directly in this workspace failed in the current container filesystem because
venv symlink creation (`lib -> lib64`) is not permitted here.
Using `/home/vscode/.venvs/...` avoids that issue and stays persistent across sessions.

### Daily workflow

1. Open workspace in the dev-container.
2. Ensure the interpreter is `/home/vscode/.venvs/learn-python-02-blogs/bin/python`.
3. Write code.
4. Save files and let Ruff format + lint automatically.
5. Before commit, run Ruff check/format commands once from terminal.

### Before writing new code

Minimal preparation checklist:

1. Confirm VS Code interpreter points to the workspace environment.
2. Confirm Ruff extension is enabled.
3. Run:

   ```bash
   /home/vscode/.venvs/learn-python-02-blogs/bin/ruff check .
   ```

4. If adding external dependencies:
   - install into this environment only
   - document them in project notes or dependency files

You do not need special extra steps for every new file beyond this checklist.

## Real Python

- <https://realpython.com/>

### Resources

- [Python Glossary](https://realpython.com/ref/glossary/)
- [Python Reference](https://realpython.com/ref/)
- [Python’s Built-in Data Types | Reference](https://realpython.com/ref/builtin-types/)
- [Basic Data Types in Python](https://realpython.com/python-data-types/)
- [Strings and Character Data in Python](https://realpython.com/python-strings/)

### To Study

- [Functional Programming in Python](https://realpython.com/python-functional-programming/)
- [Object-Oriented Programming (OOP) in Python](https://realpython.com/python3-object-oriented-programming/)
- [Python's Mutable vs Immutable Types: What's the Difference?](https://realpython.com/python-mutable-vs-immutable-types/)

### Explore dev container

- see [you should be using dev containers | Syntax](https://www.youtube.com/watch?v=kPMA9cnpScU)

1. Install `Dev Containers` extension
2. If you use `podman` adapt the settings:  

   ```json
   {
     "dev.containers.dockerPath": "podman"
   }
   ```

3. Create `.devcontainer` folder in the workspace
4. Create `.devcontainer.json` file in `.devcontainer` folder
5. Add `image` property and add a value from the [devcontainer template side](https://containers.dev/templates)
   for example

   ```json
   {
     "image": "mcr.microsoft.com/devcontainers/python"
   }
   ```

6. `Strg+Shift+P` (Command pallette): `Dev Containers: Reopen Folder Locally`
7. Work in this environment (as usual)
8. Stop the container: `Strg+Shift+P` (Command pallette): `Dev Containers: Reopen Folder Locally` or simply close VS Code  
   Clean up everything: `Strg+Shift+P` (Command pallette): `Dev Containers: Clean Up Dev Containers...`  
   … or use podman/ docker cli

---

- **Where is VS Code running in this scenario - GitHub Copilot**

  VS Code itself runs **outside** the container on your host machine. What happens is:

  - The VS Code **UI/window** runs on your host
  - A **VS Code Server** runs **inside** the container
  - The UI connects to the server over a secure connection

  This means:
  - Your workspace files are inside the container
  - Extensions run inside the container (with the server)
  - Terminal sessions are inside the container
  - But you interact with everything through the VS Code UI on your host

  This architecture gives you the benefit of a consistent, isolated development environment (the container) while keeping the responsive UI running natively on your machine.

---
