# CyberGuard Design Documentation

## Problem Statement

Users may not know whether a password satisfies basic composition requirements. CyberGuard provides local, command-line feedback.

## Objectives

- Analyze password composition.
- Calculate a simple score.
- Estimate entropy.
- Detect selected common passwords.
- Give improvement recommendations.
- Demonstrate modular Python development.

## Non-Functional Requirements

1. **Usability:** Terminal prompts and reports should be simple to understand.
2. **Maintainability:** Functions are separated into focused modules.
3. **Reliability:** Invalid and empty input is handled without crashing the normal user flow.
4. **Resource Efficiency:** The analysis is local and uses lightweight standard-library operations.
5. **Privacy:** Passwords are analyzed locally and are not transmitted by the application.
6. **Error Handling:** Invalid menu choices and empty passwords are rejected with clear messages.

## Architecture Diagram

```text
+----------------+
|    main.py     |
| CLI controller |
+-------+--------+
        |
        v
+----------------+
|   analyzer.py  |
| Orchestrator   |
+---+---+---+----+
    |   |   |
    |   |   +------------------+
    |   |                      |
    v   v                      v
security.py              entropy.py
    |                         |
    v                         v
score/common/levels       entropy/levels

        +--------------------------+
        | recommendations.py       |
        +--------------------------+
                    |
                    v
             +-------------+
             |  report.py  |
             +-------------+

Supporting:
utils.py, config.py
```

## Workflow Diagram

```text
[Start]
   |
   v
[Enter Password]
   |
   v
[Validate Input] -- invalid --> [Ask Again]
   |
   v
[Analyze Composition]
   |
   v
[Calculate Score + Entropy]
   |
   v
[Check Common Password]
   |
   v
[Generate Recommendations]
   |
   v
[Display Report]
   |
   v
[Analyse Another?]
   | Yes                  | No
   v                      v
[Enter Password]        [Exit]
```

## Use Case Diagram (text form)

```text
                +---------------------------+
                |   CyberGuard System       |
                |                           |
User ---------->| Enter Password            |
User ---------->| Request Analysis          |
User ---------->| View Security Report      |
User ---------->| View Recommendations     |
User ---------->| Repeat / Exit             |
                +---------------------------+
```

## Component/Class Diagram

```text
PasswordAnalyzer
      |
      +----> PasswordAnalysis (dataclass)
      |
      +----> security.py
      +----> entropy.py
      +----> recommendations.py

main.py ----> PasswordAnalyzer
main.py ----> report.py
main.py ----> utils.py
```

## Sequence Diagram

```text
User -> main.py: enter password
main.py -> utils.py: validate input
main.py -> PasswordAnalyzer: analyze(password)
PasswordAnalyzer -> security.py: score/common/levels
PasswordAnalyzer -> entropy.py: calculate entropy
PasswordAnalyzer -> recommendations.py: generate advice
PasswordAnalyzer --> main.py: PasswordAnalysis
main.py -> report.py: display report
report.py --> User: security report
```

## Storage Design

No database or persistent password storage is used. Passwords are processed in memory during the current execution.
