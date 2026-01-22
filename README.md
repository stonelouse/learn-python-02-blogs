# learn-python-02-blogs

- Python notes from blogs

- [learn-python-02-blogs](#learn-python-02-blogs)
  - [Real Python](#real-python)
    - [Resources](#resources)
    - [To Study](#to-study)

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
