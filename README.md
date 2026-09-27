# CyberGuard Password Analyzer

## 1. Overview

CyberGuard is a command-line Python application that analyzes password composition and provides a simple security assessment. It checks password characteristics, calculates a composition score, estimates entropy, detects a small set of commonly used passwords, and provides security recommendations.

This project was developed as an evaluated project for the **VITyarthi – Python Essentials** course.

## 2. Objectives

- Apply Python fundamentals to a practical problem.
- Demonstrate functions, control flow, strings, collections, modules, packages, error handling, and object-oriented programming.
- Provide a clear command-line workflow.
- Produce understandable password-security feedback.
- Demonstrate modular project organization and testing.

## 3. Major Functional Modules

### Module 1 – Password Analysis
Checks length, uppercase/lowercase characters, numbers, and special characters.

### Module 2 – Security Assessment
Calculates a composition score, classifies strength/security level, estimates entropy, and checks a small common-password list.

### Module 3 – Recommendations & Reporting
Generates recommendations and displays a structured terminal report.

## 4. Technologies

- Python 3
- Python Standard Library
- `dataclasses`
- `math`
- `unittest`

No third-party package is required.

## 5. Project Structure

```text
CyberGuard/
├── main.py
├── analyzer.py
├── security.py
├── entropy.py
├── recommendations.py
├── report.py
├── utils.py
├── config.py
├── tests/
│   └── test_cyberguard.py
├── README.md
├── statement.md
├── requirements.txt
└── .gitignore
```

## 6. Environment Setup

1. Install Python 3.
2. Open Command Prompt.
3. Move into the project folder.

Example:

```text
cd path\to\CyberGuard
```

4. Verify Python:

```text
python --version
```

## 7. Dependency Installation

This project uses only the Python Standard Library.

Therefore no external package installation is required.

If the evaluator wants to use the requirements file:

```text
pip install -r requirements.txt
```

The file intentionally contains no third-party dependencies.

## 8. Run the Project

From the project root:

```text
python main.py
```

The program will ask for a password and display a security report.

## 9. Run Tests

From the project root:

```text
python -m unittest discover -s tests -v
```

## 10. Example Workflow

```text
Start
  ↓
Enter password
  ↓
Validate input
  ↓
Analyze password composition
  ↓
Calculate score and entropy
  ↓
Check common-password list
  ↓
Generate recommendations
  ↓
Display report
  ↓
Analyze another password?
  ├── Yes → repeat
  └── No  → exit
```

## 11. Important Security Note

CyberGuard is an educational password-analysis project. It does not claim to prove that a password is safe against real-world attacks. The entropy value is an estimate based on the character categories detected by the program, and the common-password check uses a small built-in list.

For privacy, use a sample/test password when demonstrating the project.

## 12. Testing

The test suite checks:
- strong and weak password classification,
- common-password detection,
- entropy behavior,
- entropy levels,
- empty-password validation,
- score boundaries.

## 13. Future Enhancements

Possible future improvements include:
- a larger curated common-password dataset,
- detection of repeated/sequential patterns,
- configurable security policies,
- secure password generation,
- richer reports,
- optional persistent history with appropriate privacy controls.

## 14. License

This project is intended as an academic project for learning and evaluation.
