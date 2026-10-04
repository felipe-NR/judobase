# Contributing to Judobase

Thank you for considering contributing to **Judobase**! We appreciate your time and effort in improving our project. Please follow these guidelines to ensure a smooth collaboration.

---

## 🛠 How to Contribute

1. **Fork** the repository.
2. **Clone** your fork locally:
   ```sh
   git clone https://github.com/<your-username>/judobase.git
   ```
3. **Add the upstream repository**:
   ```sh
   git remote add upstream https://github.com/DavidDzgoev/judobase.git
   ```
4. **Create a new branch** for your changes:
   ```sh
   git checkout -b feature/my-new-feature
   ```
5. **Make your changes** and commit:
   ```sh
   git commit -m "Add feature: Short description of the change"
   ```
6. **Push to your fork**:
   ```sh
   git push origin feature/my-new-feature
   ```
7. **Create a Pull Request (PR)** on GitHub.

---

## 📜 Code Style Guidelines

### 1️⃣ Formatting & Linting
- Follow **PEP 8** (for Python) or the appropriate coding style for the project.
- Use `ruff` and `wemake-python-styleguide` for Python formatting and linting:
  ```sh
  uv sync --extra tests
  uv run make lint
  ```
- Keep code **clean, readable, and well-commented**.

### 2️⃣ Writing Tests

- Ensure all new features or fixes include tests.
- Run tests before submitting a PR:
  ```sh
  uv run make test
  ```
- If possible, write **unit tests** and **integration tests**.

### 3️⃣ Documentation
- Document your code and update relevant documentation.
- Use docstrings and type hints for functions:
  ```python
  def example_function(param: str) -> str:
      """Description of the function."""
      return param.upper()
  ```

---

## 🔥 Pull Request (PR) Process

1. Make sure your branch is **up to date** with the latest changes:
   ```sh
   git fetch upstream
   git merge upstream/master
   ```
2. Ensure **all tests pass** before submitting.
3. Follow the PR template (if available) and provide a **clear description**.
4. Wait for maintainers to review and **be open to feedback**.
5. Once approved, your PR will be merged!

---

## 🐛 Reporting Issues

If you find a bug, **please submit an issue** with:
- A **clear description** of the problem.
- Steps to reproduce it.
- Expected behavior vs. actual behavior.
- System details (OS, Python version, etc.).
- Screenshots (if applicable).

---

## 🤝 Code of Conduct

By participating in this project, you agree to follow our [Code of Conduct](CODE_OF_CONDUCT.md).

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the project's [MIT License](../LICENSE).

---

Thank you for your contributions! 🚀
