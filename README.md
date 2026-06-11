# University Database Management System (DBMS)

A robust relational database implementation modeled for a university network ecosystem. This repository serves as a comprehensive portfolio spanning foundational schema engineering, advanced data manipulation, relational algebra queries, and dynamic web application integration.

## 🛠️ Technology Stack
* **Database Engine:** MySQL[cite: 1]
* **Backend Framework:** Python (Flask Application)[cite: 1]
* **Frontend Interface:** HTML5 / CSS3[cite: 1]
* **Database Connector:** `mysql-connector-python`[cite: 1]

## 📊 Database Architecture & Features
The schema handles 11 interconnected relational tables to manage university operations cleanly[cite: 1]:
* **Core Entities:** `student`, `instructor`, `course`, `department`, `classroom`[cite: 1]
* **Operational Relations:** `section`, `teaches`, `takes`, `advisor`, `time_slot`, `prereq`[cite: 1]

### Advanced SQL Mechanics Implemented:
* **Relational Integrity:** Explicit constraints utilizing `FOREIGN KEY` references accompanied by cascading strategies (`ON DELETE CASCADE` / `ON DELETE SET NULL`)[cite: 1].
* **Complex Data Aggregations:** Multi-table structural joins, `GROUP BY`/`HAVING` qualifiers, and nested subqueries[cite: 1].
* **Conditional Algebra:** Integrated `CASE` workflows to handle procedural grading evaluations[cite: 1].
* **Simulated Full Outer Joins:** Structured sets using `UNION` commands over traditional Left/Right Outer joins[cite: 1].

## 🚀 Web Integration Interface
The project contains an interactive administrative web gateway[cite: 1]:
1. **Frontend Form (`templates/index.html`):** Captures real-time student details (`ID`, `name`, `dept_name`, `tot_cred`) with validation[cite: 1].
2. **Backend Controller (`app.py`):** Establishes a localhost connection pipeline, maps user data payloads into valid relational rows, and runs secure execution commits to the `university` database instance[cite: 1].
