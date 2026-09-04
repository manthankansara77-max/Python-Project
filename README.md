# 1. 🧮 MY CALCY

A feature-packed command-line scientific calculator built in Python — handles everything from basic arithmetic to trigonometry, logarithms, and factorials, all from your terminal.

## ✨ Features

| # | Operation | # | Operation |
|---|---|---|---|
| 1 | Addition | 8 | Power |
| 2 | Subtraction | 9 | Exponential (e) |
| 3 | Multiplication | 10 | Trigonometry (sin, cos, tan, cosec, sec, cot) |
| 4 | Division | 11 | Round Down |
| 5 | Square Root | 12 | Round Up |
| 6 | Percentage | 13 | Factorial |
| 7 | Logarithm | 14 | Greatest Common Divisor |

*Bonus:* the trigonometry module supports both *Degrees and Radians*, and even displays radian results as clean fractions of π (e.g. π/6 instead of 0.5236).

## 🛠️ Tech Stack

- Python 3
- math — core mathematical functions
- fractions — clean π-fraction display for trig results

## 🚀 How to Run

1. Clone the repo:
   bash
   git clone https://github.com/your-username/my-calcy.git
   cd my-calcy
   

2. Run it — no extra installs needed, only the Python standard library:
   bash
   python calcy.py
   

3. Follow the prompts:
   - Pick an operation (1-14)
   - Enter the required numbers
   - Get your result instantly

## 📸 Example Usage


1 - addition
2 - subtraction
3 - multiplication
4 - division
5 - square root
6 - percentage
7 - logarithm
8 - power
9 - exponential (e = 2.71)
10 - trigonometry
11 - Round Down
12 - Round up
13 - Factorial
14 - Greatest common divisor

which type you want? : 1
enter first number : 5
enter second number : 3
Processing Complete
your answer is 8


## 🐛 Bugs Found & Fixed

While building this, I ran into (and fixed) a few real bugs — worth documenting since they taught me a lot:

- *Python 2 vs 3 exception syntax* — except ValueError, IndexError: is Python 2 syntax and throws a SyntaxError in Python 3. Fixed by using except (ValueError, IndexError):.
- *Unhandled invalid menu option* — choosing a number outside 1-14 caused a NameError since result was never assigned. Fixed by adding an else clause with a friendly error message.
- *Unhandled division by zero* — dividing by 0 crashed with an uncaught ZeroDivisionError. Fixed by adding explicit except ZeroDivisionError handling around the calculation logic.

## 📚 What I Learned

- The difference between Python 2 and Python 3 exception-handling syntax
- Why try/finally alone doesn't catch errors — you still need except
- The importance of handling every possible input path, not just the "happy path"
- Using Fraction to display irrational angle results in a human-readable way

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.




# 2. Task Manager (CLI)

A simple command-line task manager built in Python. Add tasks, assign a priority level, and get them back as a clean, sorted table — most urgent first. Built as a beginner project to explore core scheduling concepts similar to how operating systems prioritize jobs.

## Features

- Add multiple tasks interactively from the terminal
- Assign each task a priority: `1` (High), `2` (Medium), `3` (Low)
- Automatically sorts tasks by priority using **pandas**
- Displays results in a clean grid table using **tabulate**
- Handles invalid input and early exit (`done`) gracefully

## Tech Stack

- Python 3
- pandas
- tabulate

## How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/task-manager.git
   cd task-manager
   ```

2. Install dependencies:
   ```bash
   pip install pandas tabulate
   ```

3. Run the program:
   ```bash
   python task_manager.py
   ```

4. Follow the prompts:
   - Enter a task name
   - Enter a priority (`1`, `2`, or `3`)
   - Type `yes` to add another task, or `done` to finish

## Example Output

```
Welcome to the Task Manager
Enter task you want to add:
Enter Tasks: task_1
Enter Level of Priority: 1 for High, 2 for Medium, 3 for Low: 2
Do you want to add more tasks? if yes just write yes OR type 'done' to exit: yes
Enter Tasks: Task_2
Enter Level of Priority: 1 for High, 2 for Medium, 3 for Low: 1
Do you want to add more tasks? if yes just write yes OR type 'done' to exit: done

+--------+------------+
| Jobs   |   Priority |
+========+============+
| Task_2 |          1 |
+--------+------------+
| task_1 |          2 |
+--------+------------+
```
## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
