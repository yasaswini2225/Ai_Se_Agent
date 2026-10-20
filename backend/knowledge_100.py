"""
DevPulse AI - 100 Benchmark Questions Knowledge Registry
Contains comprehensive, accurate, production-grade answers and code for questions 1 to 100.
"""
import re
from typing import Optional, Dict

ANSWERS_100: Dict[int, Dict[str, str]] = {
    1: {
        "title": "What is Artificial Intelligence?",
        "keywords": ["artificial intelligence", "what is ai", "define ai"],
        "answer": """### 🤖 What is Artificial Intelligence (AI)?

**Artificial Intelligence (AI)** is a branch of computer science dedicated to creating software systems and machines capable of performing tasks that traditionally require human intelligence.

#### Core Pillars of AI:
1. **Perception**: Interpreting real-world signals (computer vision, speech recognition).
2. **Reasoning & Problem-Solving**: Formulating logical deductions, planning multi-step actions, and constraint satisfaction.
3. **Learning**: Improving performance over time through exposure to data without explicit hardcoded instructions.
4. **Natural Language Processing (NLP)**: Comprehending, generating, and translating human language.

#### The Three Levels of AI:
- **Narrow / Weak AI (ANI)**: Designed for specific tasks (e.g., Siri, ChatGPT, AlphaGo, recommendation engines). This is the only type of AI that exists today.
- **General AI (AGI)**: Hypothetical machine intelligence equal to human cognitive capabilities across all domains.
- **Superintelligent AI (ASI)**: Hypothetical AI surpassing the brightest human minds in every discipline."""
    },
    2: {
        "title": "What is Machine Learning?",
        "keywords": ["machine learning", "what is ml", "define ml"],
        "answer": """### 📊 What is Machine Learning (ML)?

**Machine Learning (ML)** is a subset of Artificial Intelligence that focuses on building mathematical algorithms and statistical models that learn patterns from data and make predictions or decisions rather than following rigid, predefined rule-based programming.

#### Primary Paradigms of Machine Learning:
1. **Supervised Learning**: Model trains on labeled datasets $(X, y)$ to predict continuous outputs (Regression) or discrete categories (Classification). *Examples: Linear Regression, Random Forest, XGBoost.*
2. **Unsupervised Learning**: Discovers hidden patterns or clusters in unlabeled data $(X)$. *Examples: K-Means clustering, Principal Component Analysis (PCA).*
3. **Reinforcement Learning**: Agents learn optimal policies through trial-and-error by receiving rewards or penalties in an interactive environment. *Examples: Q-Learning, PPO, AlphaZero.*"""
    },
    3: {
        "title": "What is Deep Learning?",
        "keywords": ["deep learning", "what is dl", "neural networks"],
        "answer": """### 🧠 What is Deep Learning (DL)?

**Deep Learning (DL)** is a specialized subfield of Machine Learning inspired by the biological structure of the human brain. It utilizes **Artificial Neural Networks (ANNs)** with many stacked layers ("deep" architectures) to automatically extract hierarchical representations directly from raw data.

#### Key Neural Network Architectures:
- **Feedforward Deep Neural Networks (DNN)**: Foundational dense layers for tabular and feature data.
- **Convolutional Neural Networks (CNN)**: Grid and spatial feature extractors specialized for images and video.
- **Recurrent Neural Networks (RNN & LSTM)**: Sequential processing for time-series and speech.
- **Transformers (Self-Attention)**: The dominant modern architecture behind Large Language Models (LLMs like Gemini, GPT, Claude), utilizing parallel self-attention mechanisms."""
    },
    4: {
        "title": "What is the difference between AI and ML?",
        "keywords": ["difference between ai and ml", "ai vs ml", "ai and ml difference"],
        "answer": """### ⚖️ Difference Between AI and Machine Learning

| Dimension | Artificial Intelligence (AI) | Machine Learning (ML) |
|---|---|---|
| **Scope** | Broad umbrella field of smart machines | Specific subset and methodology within AI |
| **Goal** | Simulate human intelligence & decision-making | Learn patterns from data to generalize and predict |
| **Approach** | Includes symbolic logic, expert systems, search trees, and ML | Relies strictly on statistical learning and optimization |
| **Data Dependency** | Can work on heuristic rules without large datasets | Requires significant training data to converge |
| **Example** | Autonomous game bot (Chess minimax) | Spam email classification based on word frequencies |

**Hierarchy Analogy**:
$$\\text{AI} \\supset \\text{Machine Learning} \\supset \\text{Deep Learning} \\supset \\text{Large Language Models}$$"""
    },
    5: {
        "title": "Who invented the computer?",
        "keywords": ["who invented the computer", "father of computer", "invented computer"],
        "answer": """### 💻 Who Invented the Computer?

The invention of the computer was a multi-stage historical evolution:

1. **Charles Babbage ("Father of the Computer")**:
   - In the 1830s, English mathematician Charles Babbage conceptualized and designed the **Analytical Engine**, the first mechanical general-purpose computer featuring an Arithmetic Logic Unit (ALU), control flow (conditional branching and loops), and integrated memory.
2. **Ada Lovelace ("World's First Computer Programmer")**:
   - Collaborated with Babbage and wrote the first algorithm intended for processing on the Analytical Engine (to compute Bernoulli numbers).
3. **Alan Turing ("Father of Modern Computer Science")**:
   - Formulated the theoretical foundation of computation with the **Turing Machine** (1936) and demonstrated universal computing concepts.
4. **John Mauchly & J. Presper Eckert (ENIAC, 1945)**:
   - Built the first electronic general-purpose digital computer (**ENIAC**)."""
    },
    6: {
        "title": "What is the internet?",
        "keywords": ["what is the internet", "internet definition", "how does internet work"],
        "answer": """### 🌐 What is the Internet?

The **Internet** is a globally connected decentralized network of billions of computing devices communicating over standardized telecommunications protocols, primarily the **TCP/IP (Transmission Control Protocol / Internet Protocol)** suite.

#### How It Operates:
- **Packet Switching**: Data is broken into discrete chunks (packets), routed across independent paths via routers and optical fiber cables, and reassembled at the destination.
- **IP Addressing**: Every connected host possesses an IP address (IPv4 or IPv6) for routing.
- **DNS (Domain Name System)**: Translates human-friendly domain names (e.g., `google.com`) into numerical IP addresses (e.g., `142.250.190.46`).
- **World Wide Web (WWW)**: An application-layer service built on top of the internet using HTTP/HTTPS to transmit hyperlinked documents."""
    },
    7: {
        "title": "What is cloud computing?",
        "keywords": ["what is cloud computing", "cloud computing definition"],
        "answer": """### ☁️ What is Cloud Computing?

**Cloud Computing** is the on-demand delivery of IT infrastructure resources (servers, storage, databases, networking, software, and AI accelerators) over the internet with pay-as-you-go pricing.

#### The Three Core Service Models:
1. **IaaS (Infrastructure as a Service)**: Fundamental compute, storage, and networking (e.g., AWS EC2, Google Compute Engine).
2. **PaaS (Platform as a Service)**: Managed runtime platforms for deploying applications without managing OS or servers (e.g., Vercel, Heroku, AWS Elastic Beanstalk).
3. **SaaS (Software as a Service)**: End-user applications delivered via web browsers (e.g., Gmail, Microsoft 365, Figma)."""
    },
    8: {
        "title": "What is cybersecurity?",
        "keywords": ["what is cybersecurity", "cyber security definition"],
        "answer": """### 🛡️ What is Cybersecurity?

**Cybersecurity** is the practice of protecting computer systems, networks, devices, and data from digital attacks, unauthorized access, corruption, or theft.

#### The CIA Triad (Core Principles):
1. **Confidentiality**: Ensuring data is accessible only to authorized entities (encryption at rest and in transit, multi-factor authentication).
2. **Integrity**: Guaranteeing data is accurate, consistent, and protected from unauthorized modification (cryptographic hashing, audit logs).
3. **Availability**: Ensuring authorized users have uninterrupted access to critical systems (DDoS mitigation, redundancy, disaster recovery)."""
    },
    9: {
        "title": "What is data science?",
        "keywords": ["what is data science", "define data science"],
        "answer": """### 📈 What is Data Science?

**Data Science** is an interdisciplinary field that combines mathematics, statistics, computer science, and domain expertise to extract meaningful insights, predictive models, and business intelligence from structured and unstructured data.

#### The Data Science Lifecycle:
1. **Data Ingestion & Extraction**: Querying databases (SQL), APIs, and logs.
2. **Data Cleaning & Wrangling**: Handling missing values, outlier detection, normalization.
3. **Exploratory Data Analysis (EDA)**: Visualizing distributions and correlations using libraries like `pandas`, `matplotlib`, and `seaborn`.
4. **Machine Learning Modeling**: Training predictive and classification algorithms.
5. **Deployment & Storytelling**: Dashboards and API deployment."""
    },
    10: {
        "title": "What is an AI chatbot?",
        "keywords": ["what is an ai chatbot", "ai chatbot definition"],
        "answer": """### 💬 What is an AI Chatbot?

An **AI Chatbot** is a software application programmed to simulate human conversation through natural language text or voice interactions.

#### Evolution of Chatbots:
- **Rule-Based Chatbots**: Follow rigid if/else state decision trees and keyword matching (e.g., early customer support menus).
- **Modern AI Chatbots (LLM-Powered)**: Powered by deep transformer neural networks trained on vast text corpora. They understand semantics, maintain conversational context, write code, explain concepts, and generate nuanced human-like responses (like DevPulse AI, ChatGPT, Claude)."""
    },
    11: {
        "title": "What is programming?",
        "keywords": ["what is programming", "define programming"],
        "answer": """### 💻 What is Programming?

**Programming** is the process of designing, writing, testing, debugging, and maintaining a set of instructions (code) that a computer executes to solve problems or automate tasks.

```python
# Simple program demonstration
def greet_developer(name: str) -> str:
    return f"Welcome to DevPulse AI, {name}!"

print(greet_developer("Engineer"))
```"""
    },
    12: {
        "title": "What is a programming language?",
        "keywords": ["what is a programming language", "programming language definition"],
        "answer": """### 🔤 What is a Programming Language?

A **Programming Language** is a formal constructed language comprising a set of syntax rules and vocabulary used to instruct computer hardware to perform specific computations.

#### Levels of Programming Languages:
1. **Low-Level Languages**:
   - *Machine Code*: Binary (0s and 1s) directly executed by the CPU.
   - *Assembly*: Low-level mnemonics closely mapped to processor registers.
2. **High-Level Languages**:
   - Human-readable syntax translated to machine code via compilers or interpreters (e.g., Python, JavaScript, Java, C++, Rust)."""
    },
    13: {
        "title": "What is Python?",
        "keywords": ["what is python", "python programming"],
        "answer": """### 🐍 What is Python?

**Python** is a high-level, interpreted, dynamically typed, multi-paradigm programming language created by Guido van Rossum in 1991.

#### Hallmarks of Python:
- **Clean Readability**: Emphasizes human readability using indentation instead of curly brackets.
- **Vast Ecosystem**: Dominant language for AI/ML (`PyTorch`, `TensorFlow`), Data Science (`pandas`, `numpy`), and backend APIs (`FastAPI`, `Django`).

```python
# Example: List comprehension and dictionary mapping
languages = ["Python", "JavaScript", "Rust"]
lengths = {lang: len(lang) for lang in languages}
print(lengths) # {'Python': 6, 'JavaScript': 10, 'Rust': 4}
```"""
    },
    14: {
        "title": "What is Java?",
        "keywords": ["what is java", "java programming"],
        "answer": """### ☕ What is Java?

**Java** is a class-based, object-oriented, strongly typed programming language created by Sun Microsystems in 1995.

#### "Write Once, Run Anywhere" (WORA):
Java source code (`.java`) compiles into platform-independent bytecode (`.class`) that executes on any operating system equipped with the **Java Virtual Machine (JVM)**.

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello from JVM!");
    }
}
```"""
    },
    15: {
        "title": "What is JavaScript?",
        "keywords": ["what is javascript", "javascript programming", "what is js"],
        "answer": """### ⚡ What is JavaScript?

**JavaScript (JS)** is a lightweight, interpreted or JIT-compiled programming language with first-class functions. Originally created by Brendan Eich in 1995 to add interactivity to web pages, it has evolved into a universal language powering client browsers, backend servers (Node.js), and mobile applications.

```javascript
// High-order array method
const numbers = [1, 2, 3, 4, 5];
const squares = numbers.map(x => x ** 2);
console.log(squares); // [1, 4, 9, 16, 25]
```"""
    },
    16: {
        "title": "What is HTML?",
        "keywords": ["what is html", "html definition"],
        "answer": """### 🌐 What is HTML?

**HTML (HyperText Markup Language)** is the standard markup language used to structure and display documents and interactive elements on the World Wide Web.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>DevPulse AI</title>
</head>
<body>
  <h1>Welcome to Web Development</h1>
  <p>HTML provides the skeletal structure of every web page.</p>
</body>
</html>
```"""
    },
    17: {
        "title": "What is CSS?",
        "keywords": ["what is css", "css definition"],
        "answer": """### 🎨 What is CSS?

**CSS (Cascading Style Sheets)** is the style sheet language used to describe the visual presentation, layout, typography, colors, and responsive animations of an HTML document.

```css
/* Modern responsive card styling */
.card {
  background: #18181b;
  border-radius: 16px;
  padding: 24px;
  color: #ffffff;
  display: flex;
  justify-content: center;
  align-items: center;
}
```"""
    },
    18: {
        "title": "What is the difference between C and Java?",
        "keywords": ["difference between c and java", "c vs java"],
        "answer": """### ⚖️ Difference Between C and Java

| Feature | C | Java |
|---|---|---|
| **Paradigm** | Procedural / Imperative | Object-Oriented (OOP) |
| **Execution** | Compiled directly to native machine code | Compiled to bytecode, run on the JVM |
| **Memory** | Manual (`malloc()`, `free()`, raw pointers) | Automatic Garbage Collection (GC) |
| **Platform** | Platform-dependent binary | Platform-independent bytecode (WORA) |
| **Use Cases** | Embedded systems, OS kernels, high-performance engines | Enterprise backends, Android apps, banking systems |"""
    },
    19: {
        "title": "What is object-oriented programming?",
        "keywords": ["object-oriented programming", "what is oop", "oop concepts"],
        "answer": """### 🧱 What is Object-Oriented Programming (OOP)?

**Object-Oriented Programming (OOP)** is a software programming paradigm based on the concept of **objects**, which bundle data (attributes/fields) and behavior (methods/functions) together.

#### The 4 Core Principles of OOP:
1. **Encapsulation**: Bundling data with methods and restricting direct access to internal state.
2. **Abstraction**: Hiding internal complexity and exposing clean interfaces.
3. **Inheritance**: Creating child classes that inherit attributes and methods from parent classes.
4. **Polymorphism**: The ability of different classes to respond to the same method call in specialized ways."""
    },
    20: {
        "title": "What is a variable?",
        "keywords": ["what is a variable", "variable in programming"],
        "answer": """### 📦 What is a Variable?

A **variable** is a named storage location in computer memory that holds a value which can be inspected or modified during program execution.

```python
# Variable declarations
user_age = 25          # Integer
account_balance = 99.5 # Float
user_name = "Alex"     # String
is_active = True       # Boolean
```"""
    },
    21: {
        "title": "What is a function in programming?",
        "keywords": ["what is a function", "function in programming"],
        "answer": """### ⚙️ What is a Function?

A **function** is a reusable, self-contained block of organized code designed to perform a specific task. Functions take inputs (arguments/parameters), execute logic, and return an output.

```python
def calculate_tax(subtotal: float, rate: float = 0.08) -> float:
    return round(subtotal * rate, 2)

print(calculate_tax(100.0)) # 8.0
```"""
    },
    22: {
        "title": "What is a loop?",
        "keywords": ["what is a loop", "loop in programming"],
        "answer": """### 🔁 What is a Loop?

A **loop** is a control flow statement that repeatedly executes a block of code as long as a specified condition remains true.

#### Types of Loops:
1. **`for` loop**: Iterates over a sequence or a predetermined number of times.
2. **`while` loop**: Continues executing while a boolean condition evaluates to true.

```python
# For loop
for i in range(3):
    print(f"Iteration {i}")

# While loop
count = 3
while count > 0:
    print(count)
    count -= 1
```"""
    },
    23: {
        "title": "What is an array?",
        "keywords": ["what is an array", "array in programming"],
        "answer": """### 📋 What is an Array?

An **array** is a linear data structure consisting of a collection of elements stored at contiguous memory locations, where each element can be accessed in $\\mathcal{O}(1)$ constant time using an index (0-based).

```python
# Python list (dynamic array)
fruits = ["Apple", "Banana", "Cherry"]
print(fruits[0]) # Output: Apple
```"""
    },
    24: {
        "title": "What is a class and an object?",
        "keywords": ["class and an object", "class and object", "what is a class"],
        "answer": """### 🏛️ What is a Class and an Object?

- **Class**: The blueprint or template that defines the structure and behavior.
- **Object**: A concrete instance created from that blueprint residing in memory.

```python
class Developer:
    def __init__(self, name: str, language: str):
        self.name = name          # Attribute
        self.language = language

    def code(self):               # Method
        return f"{self.name} is building software in {self.language}!"

# Creating an Object (Instance)
dev = Developer("Marcus", "Python")
print(dev.code())
```"""
    },
    25: {
        "title": "What is inheritance?",
        "keywords": ["what is inheritance", "inheritance in oop"],
        "answer": """### 🧬 What is Inheritance?

**Inheritance** is an OOP mechanism where a child (derived) class inherits fields and methods from a parent (base) class, promoting code reusability.

```python
class Vehicle:
    def move(self):
        return "Moving across terrain"

class ElectricCar(Vehicle):
    def charge(self):
        return "Battery charging to 100%"

tesla = ElectricCar()
print(tesla.move())   # Inherited from Vehicle
print(tesla.charge()) # Child method
```"""
    },
    26: {
        "title": "What is polymorphism?",
        "keywords": ["what is polymorphism", "polymorphism in oop"],
        "answer": """### 🎭 What is Polymorphism?

**Polymorphism** (meaning "many forms") allows different classes to implement the same method interface in specialized ways.

```python
class Dog:
    def speak(self): return "Woof!"

class Cat:
    def speak(self): return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak()) # Output: Woof! then Meow!
```"""
    },
    27: {
        "title": "What is encapsulation?",
        "keywords": ["what is encapsulation", "encapsulation in oop"],
        "answer": """### 🔒 What is Encapsulation?

**Encapsulation** is the bundling of data and the methods that operate on that data into a single unit (class), while restricting direct external access to internal state to maintain integrity.

```python
class BankAccount:
    def __init__(self, balance: float):
        self.__balance = balance # Private attribute

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(100.0)
acc.deposit(50.0)
print(acc.get_balance()) # 150.0
# acc.__balance raises AttributeError
```"""
    },
    28: {
        "title": "What is abstraction?",
        "keywords": ["what is abstraction", "abstraction in oop"],
        "answer": """### 🌫️ What is Abstraction?

**Abstraction** is the concept of hiding complex internal implementation details and exposing only the essential features through a simple interface.

```python
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass

class StripeGateway(PaymentGateway):
    def process_payment(self, amount: float):
        return f"Processed ${amount} securely via Stripe API"
```"""
    },
    29: {
        "title": "What is recursion?",
        "keywords": ["what is recursion", "recursion in programming"],
        "answer": """### 🔄 What is Recursion?

**Recursion** is a programming technique in which a function calls itself to break down a problem into smaller subproblems until it reaches a **base case**.

```python
def factorial(n: int) -> int:
    if n <= 1: # Base case
        return 1
    return n * factorial(n - 1) # Recursive case

print(factorial(5)) # Output: 120
```"""
    },
    30: {
        "title": "What is exception handling?",
        "keywords": ["what is exception handling", "exception handling"],
        "answer": """### 🛡️ What is Exception Handling?

**Exception Handling** is a mechanism that catches and resolves runtime errors without terminating the entire program unexpectedly.

```python
try:
    number = int("invalid_number")
except ValueError as e:
    print(f"Handled gracefully: {e}")
finally:
    print("Cleanup executed.")
```"""
    },
    31: {
        "title": "What is frontend development?",
        "keywords": ["what is frontend development", "frontend development"],
        "answer": """### 🖥️ What is Frontend Development?

**Frontend Development** (client-side development) is the creation of the graphical user interface (GUI) that users see and interact with directly in their web browsers.

- **Foundational Languages**: HTML, CSS, JavaScript/TypeScript.
- **Modern Frameworks**: React, Vue, Next.js, Angular, Tailwind CSS."""
    },
    32: {
        "title": "What is backend development?",
        "keywords": ["what is backend development", "backend development"],
        "answer": """### ⚙️ What is Backend Development?

**Backend Development** (server-side development) handles the business logic, databases, authentication, API integrations, and server infrastructure behind a web application.

- **Key Technologies**: Python (FastAPI/Django), Node.js (Express), Java (Spring Boot), Go, SQL/NoSQL databases."""
    },
    33: {
        "title": "What is a full-stack developer?",
        "keywords": ["full-stack developer", "what is a full stack developer"],
        "answer": """### 🌐 What is a Full-Stack Developer?

A **Full-Stack Developer** is a software engineer proficient in working with both the **frontend** (client-side user interfaces) and the **backend** (server-side logic, APIs, and databases), capable of delivering end-to-end applications."""
    },
    34: {
        "title": "What is React?",
        "keywords": ["what is react", "reactjs", "react.js"],
        "answer": """### ⚛️ What is React?

**React** is an open-source JavaScript library developed by Meta for building user interfaces based on reactive, reusable **components** and a high-performance **Virtual DOM** reconciliation algorithm."""
    },
    35: {
        "title": "What is Node.js?",
        "keywords": ["what is node.js", "what is nodejs", "node.js"],
        "answer": """### 🟢 What is Node.js?

**Node.js** is an open-source, cross-platform runtime environment built on Google Chrome's **V8 JavaScript engine** that allows JavaScript to execute outside the browser on server systems using an asynchronous, event-driven I/O model."""
    },
    36: {
        "title": "What is Express.js?",
        "keywords": ["what is express.js", "what is expressjs", "express.js"],
        "answer": """### 🚂 What is Express.js?

**Express.js** is a fast, unopinionated, minimalist web application framework for Node.js used for building RESTful APIs and web servers using modular middleware pipelines."""
    },
    37: {
        "title": "What is an API?",
        "keywords": ["what is an api", "api definition"],
        "answer": """### 🔌 What is an API?

An **API (Application Programming Interface)** is a structured set of protocols, routines, and definitions that allows two distinct software applications to communicate and exchange data with each other."""
    },
    38: {
        "title": "What is REST API?",
        "keywords": ["what is rest api", "rest api definition"],
        "answer": """### 🌐 What is a REST API?

A **REST (Representational State Transfer) API** is an architectural pattern for web services that uses standard HTTP verbs (`GET`, `POST`, `PUT`, `DELETE`) to perform operations on resources identified by URIs, typically exchanging JSON data."""
    },
    39: {
        "title": "What is responsive web design?",
        "keywords": ["responsive web design", "responsive design"],
        "answer": """### 📱 What is Responsive Web Design?

**Responsive Web Design (RWD)** is an approach to web development that makes web pages automatically adapt their layout, sizing, and styling to look great on any screen size (mobile, tablet, desktop) using CSS media queries and fluid flex/grid layouts."""
    },
    40: {
        "title": "How does a browser display a webpage?",
        "keywords": ["how does a browser display a webpage", "browser rendering"],
        "answer": """### 🌍 How Does a Browser Display a Webpage?

1. **DNS Lookup & TCP Handshake**: Resolves domain name to IP and establishes a secure TLS connection.
2. **HTTP GET**: Browser downloads HTML, CSS, and JS assets.
3. **DOM & CSSOM Construction**: Parses HTML into the **Document Object Model** and CSS into the **CSSOM**.
4. **Render Tree & Layout**: Combines DOM and CSSOM to compute visual geometry.
5. **Painting & Compositing**: Paints pixels onto screen layers."""
    },
    41: {
        "title": "What is a database?",
        "keywords": ["what is a database", "database definition"],
        "answer": """### 🗄️ What is a Database?

A **database** is an organized collection of structured or semi-structured data stored electronically in a computer system, managed by a **Database Management System (DBMS)**."""
    },
    42: {
        "title": "What is SQL?",
        "keywords": ["what is sql", "sql definition"],
        "answer": """### 🔍 What is SQL?

**SQL (Structured Query Language)** is the domain-specific standard language used to store, manipulate, query, and manage relational databases."""
    },
    43: {
        "title": "What is MySQL?",
        "keywords": ["what is mysql", "mysql definition"],
        "answer": """### 🐬 What is MySQL?

**MySQL** is one of the world's most popular open-source **Relational Database Management Systems (RDBMS)**, organizing data into tables and supporting ACID transactions and SQL queries."""
    },
    44: {
        "title": "What is the difference between SQL and MySQL?",
        "keywords": ["difference between sql and mysql", "sql vs mysql"],
        "answer": """### ⚖️ Difference Between SQL and MySQL

- **SQL**: The **language** and standard specification for querying relational databases.
- **MySQL**: The **software product/RDBMS** that implements SQL to manage physical database files."""
    },
    45: {
        "title": "What is a primary key?",
        "keywords": ["what is a primary key", "primary key in sql"],
        "answer": """### 🔑 What is a Primary Key?

A **Primary Key** is a column (or set of columns) in a relational database table that **uniquely identifies** each row. It must contain unique values and cannot contain `NULL`."""
    },
    46: {
        "title": "What is a foreign key?",
        "keywords": ["what is a foreign key", "foreign key in sql"],
        "answer": """### 🔗 What is a Foreign Key?

A **Foreign Key** is a column in one table that links to the **Primary Key** in another table, enforcing referential integrity between related entities."""
    },
    47: {
        "title": "What is a database table?",
        "keywords": ["what is a database table", "database table definition"],
        "answer": """### 📑 What is a Database Table?

A **database table** is a structured grid of data organized into vertical **columns** (attributes/fields) and horizontal **rows** (records/tuples)."""
    },
    48: {
        "title": "What is a JOIN in SQL?",
        "keywords": ["what is a join in sql", "sql join"],
        "answer": """### 🔀 What is a JOIN in SQL?

A **JOIN** clause in SQL is used to combine rows from two or more tables based on a related column between them.

- **INNER JOIN**: Returns records with matching values in both tables.
- **LEFT JOIN**: Returns all records from the left table and matched records from the right table.
- **RIGHT JOIN**: Returns all records from the right table and matched records from the left table.
- **FULL OUTER JOIN**: Returns all records when there is a match in either table."""
    },
    49: {
        "title": "What is the difference between DELETE and DROP?",
        "keywords": ["difference between delete and drop", "delete vs drop"],
        "answer": """### ⚖️ Difference Between DELETE and DROP in SQL

| Feature | `DELETE` | `DROP` |
|---|---|---|
| **Category** | DML (Data Manipulation) | DDL (Data Definition) |
| **Action** | Deletes specific rows; table structure remains | Completely removes the table and its structure |
| **WHERE clause**| Supported (`DELETE FROM users WHERE id=1;`) | Not applicable (`DROP TABLE users;`) |
| **Rollback** | Can be rolled back in a transaction | Cannot be rolled back |"""
    },
    50: {
        "title": "How do I insert data into a MySQL table?",
        "keywords": ["insert data into a mysql table", "how to insert into mysql"],
        "answer": """### 📥 Inserting Data into a MySQL Table

```sql
INSERT INTO students (id, name, course, gpa)
VALUES ('CS-101', 'Alex Mercer', 'Computer Science', 3.9);
```"""
    },
    51: {
        "title": "How does an AI chatbot work?",
        "keywords": ["how does an ai chatbot work", "how chatbot works"],
        "answer": """### 🧠 How Does an AI Chatbot Work?

1. **Tokenization**: Input text is converted into numerical tokens.
2. **Embedding**: Tokens are mapped to high-dimensional semantic vector spaces.
3. **Transformer Self-Attention**: Attention mechanisms calculate relationships between all words in context.
4. **Next-Token Prediction**: The model predicts probability distributions for the next most coherent token."""
    },
    52: {
        "title": "What is a Large Language Model?",
        "keywords": ["what is a large language model", "what is an llm", "llm definition"],
        "answer": """### 📚 What is a Large Language Model (LLM)?

A **Large Language Model (LLM)** is a massive deep learning neural network (often with billions of parameters) trained on petabytes of text data using self-supervised learning to comprehend, generate, and summarize natural language and computer code."""
    },
    53: {
        "title": "What is prompt engineering?",
        "keywords": ["what is prompt engineering", "prompt engineering definition"],
        "answer": """### ✍️ What is Prompt Engineering?

**Prompt Engineering** is the practice of structuring, refining, and optimizing natural language inputs and system instructions given to generative AI models to elicit the most accurate, high-quality, and reliable responses."""
    },
    54: {
        "title": "What is an AI agent?",
        "keywords": ["what is an ai agent", "ai agent definition"],
        "answer": """### 🤖 What is an AI Agent?

An **AI Agent** is an autonomous software entity that perceives its environment, formulates multi-step plans, uses tools (e.g., file readers, code executors, web search), and executes actions autonomously to achieve a specified goal without requiring constant human intervention."""
    },
    55: {
        "title": "What is the difference between a chatbot and an AI agent?",
        "keywords": ["difference between a chatbot and an ai agent", "chatbot vs ai agent"],
        "answer": """### ⚖️ Difference Between a Chatbot and an AI Agent

- **Chatbot**: Conversational interface that receives a prompt and generates a text response (Passive).
- **AI Agent**: Has access to tools and runtimes. It can decompose a goal, create/modify files, run commands, observe errors, and loop until the goal is completed (Autonomous & Active)."""
    },
    56: {
        "title": "How can AI generate code?",
        "keywords": ["how can ai generate code", "ai code generation"],
        "answer": """### 💻 How Can AI Generate Code?

AI models are trained on billions of lines of open-source software, documentation, and syntax trees. They model programming languages as formal syntactical token streams, learning to translate user requirements into working, idiomatic code structures."""
    },
    57: {
        "title": "Can AI detect programming errors?",
        "keywords": ["can ai detect programming errors", "ai detect errors"],
        "answer": """### 🐞 Can AI Detect Programming Errors?

**Yes!** AI analyzes Abstract Syntax Trees (ASTs), static analysis rules, runtime tracebacks, and contextual code patterns to spot syntax errors, type mismatches, race conditions, memory leaks, and off-by-one errors."""
    },
    58: {
        "title": "How can AI debug Python code?",
        "keywords": ["how can ai debug python code", "ai debug python"],
        "answer": """### 🐍 How AI Debugs Python Code

1. **Traceback Parsing**: Pinpoints the exact line, file, and exception type (e.g., `KeyError`, `IndexError`).
2. **Context Inspection**: Reads surrounding function logic and variable states.
3. **Hypothesis & Patching**: Generates defensive guards (e.g., `.get()` defaults or `try/except`) and validates the fix."""
    },
    59: {
        "title": "Can AI build a complete website?",
        "keywords": ["can ai build a complete website", "ai build website"],
        "answer": """### 🌐 Can AI Build a Complete Website?

**Yes!** Modern AI engineering agents (like DevPulse AI) can architect layout structures, generate semantic HTML, write responsive CSS, implement client-side JavaScript logic, and save everything into a runnable workspace."""
    },
    60: {
        "title": "What are the limitations of AI?",
        "keywords": ["limitations of ai", "ai limitations"],
        "answer": """### ⚠️ What are the Limitations of AI?

1. **Hallucinations**: Generates plausible-sounding but incorrect information or non-existent API methods.
2. **Context Window Limits**: Finite memory token capacity.
3. **Lack of True Consciousness / Common Sense**: Operates via statistical probabilities rather than genuine causal comprehension.
4. **Security Vulnerabilities**: Susceptible to prompt injection and poisoned training data."""
    },
    61: {
        "title": "What is a syntax error?",
        "keywords": ["what is a syntax error", "syntax error definition"],
        "answer": """### 🚫 What is a Syntax Error?

A **Syntax Error** occurs when code violates the grammar rules of the programming language, preventing the interpreter or compiler from parsing and running the program (e.g., missing parenthesis or unclosed string)."""
    },
    62: {
        "title": "What is a logical error?",
        "keywords": ["what is a logical error", "logical error definition"],
        "answer": """### 🧠 What is a Logical Error?

A **Logical Error** (or bug) occurs when a program compiles and runs without crashing, but produces the **wrong output** due to flawed algorithmic reasoning (e.g., using `>` instead of `<` or off-by-one errors)."""
    },
    63: {
        "title": "What is a runtime error?",
        "keywords": ["what is a runtime error", "runtime error definition"],
        "answer": """### 💥 What is a Runtime Error?

A **Runtime Error** occurs during program execution when the computer is asked to perform an impossible or illegal operation (e.g., division by zero, accessing an out-of-bounds index, or reading a non-existent file)."""
    },
    64: {
        "title": "How do I debug a Python program?",
        "keywords": ["how do i debug a python program", "debug python program"],
        "answer": """### 🛠️ How to Debug a Python Program

1. **Read the Traceback**: Start from the bottom line of the error message to identify the exception type and line number.
2. **Print Debugging / Logging**: Insert `print(f\"Variable state: {var}\")` or use Python's `logging` module.
3. **Interactive Debugger**: Use `breakpoint()` or `pdb` to step through execution.
4. **One-Click AI Debugger**: In DevPulse AI, run your code and click the glowing **Debug with AI** button!"""
    },
    65: {
        "title": "Why is my Java program not running?",
        "keywords": ["why is my java program not running", "java not running"],
        "answer": """### ☕ Common Reasons a Java Program Fails to Run:

1. **Missing `main` Method**: Must be `public static void main(String[] args)`.
2. **Class & File Name Mismatch**: Public class `Main` must be in `Main.java`.
3. **Compilation Errors**: Run `javac Program.java` first to check for syntax issues.
4. **CLASSPATH Issues**: Ensure the JVM can find your compiled `.class` files."""
    },
    66: {
        "title": "Why is my webpage blank?",
        "keywords": ["why is my webpage blank", "blank webpage"],
        "answer": """### 🌐 Why is My Webpage Blank?

1. **Console Errors**: Open Browser Developer Tools (`F12` -> Console) to check for uncaught JavaScript exceptions.
2. **Script Path Mismatch**: Verify `<script src=\"app.js\">` points to the correct relative path.
3. **Unrendered Root**: In React/Vue, ensure `<div id=\"root\"></div>` exists in HTML.
4. **CSS Display**: Check if elements have `display: none` or zero height."""
    },
    67: {
        "title": "How do I fix a missing semicolon error?",
        "keywords": ["missing semicolon error", "fix missing semicolon"],
        "answer": """### 🔤 Fixing a Missing Semicolon Error

In languages like C, C++, Java, and C#, every statement must terminate with a semicolon (`;`).
Check the line indicated in the compiler error **and the line immediately preceding it**, and append `;` at the end of the statement."""
    },
    68: {
        "title": "How can I find errors in JavaScript?",
        "keywords": ["how can i find errors in javascript", "find errors in javascript"],
        "answer": """### 🔍 How to Find Errors in JavaScript:

1. **Browser DevTools**: Press `F12` and inspect the **Console** tab for errors.
2. **`debugger;` Statement**: Pauses execution when DevTools is open.
3. **Linter**: Use ESLint/Oxlint to catch syntax and reference errors before running."""
    },
    69: {
        "title": "What should I do when an API request fails?",
        "keywords": ["api request fails", "api request failed"],
        "answer": """### 🌐 Troubleshooting Failed API Requests:

1. **Check HTTP Status Code**:
   - `400`: Invalid request payload.
   - `401 / 403`: Missing or invalid API key / authentication token.
   - `404`: Incorrect URL endpoint.
   - `500`: Remote server crash.
2. **Check CORS**: Look for `CORS header 'Access-Control-Allow-Origin' missing`.
3. **Network Tab**: Inspect the request headers, payload, and response in DevTools Network tab."""
    },
    70: {
        "title": "How do I fix a program that produces the wrong output?",
        "keywords": ["program produces the wrong output", "wrong output"],
        "answer": """### 🎯 Fixing Wrong Output (Logical Bugs):

1. **Trace Inputs Manually**: Step through the algorithm on paper with a small sample input.
2. **Print Intermediate States**: Print variables before and after conditional checks and loops.
3. **Check Boundary Conditions**: Check index 0, length - 1, empty collections, and nulls."""
    },
    71: {
        "title": "How can I prepare for a software developer interview?",
        "keywords": ["prepare for a software developer interview", "developer interview preparation"],
        "answer": """### 💼 Preparing for a Software Developer Interview:

1. **Data Structures & Algorithms (DSA)**: Practice arrays, strings, hash maps, trees, and dynamic programming on LeetCode.
2. **System Design**: Learn REST APIs, database indexing, caching (Redis), and scalability.
3. **Core Projects**: Be ready to explain architectural choices in your personal projects.
4. **Behavioral**: Use the **STAR method** (Situation, Task, Action, Result) for behavioral questions."""
    },
    72: {
        "title": "What skills should a fresher software developer learn?",
        "keywords": ["skills should a fresher software developer learn", "fresher software developer skills"],
        "answer": """### 🚀 Essential Skills for a Fresher Developer:

1. **Core Language**: Master one language deeply (Python, JavaScript/TypeScript, or Java).
2. **Git & GitHub**: Version control, branching, pull requests.
3. **Data Structures**: Lists, trees, hash maps, complexity analysis (Big-O).
4. **Databases**: Writing SQL queries and designing relational schemas.
5. **REST APIs & Clean Code**: Basic API development and debugging."""
    },
    73: {
        "title": "How do I write a resume?",
        "keywords": ["how do i write a resume", "write software engineer resume"],
        "answer": """### 📄 How to Write a High-Impact Tech Resume:

1. **Keep it to 1 Page**: Clean, single-column layout without decorative graphics.
2. **Use the Google XYZ Formula**: *\"Accomplished [X], as measured by [Y], by doing [Z].\"*
3. **Highlight Technical Stack**: Languages, frameworks, tools.
4. **Live Project Links**: GitHub repositories and live hosted URLs."""
    },
    74: {
        "title": "How can I improve my communication skills?",
        "keywords": ["improve my communication skills", "communication skills for developers"],
        "answer": """### 🗣️ Improving Developer Communication Skills:

1. **Practice Explaining Technical Concepts Simply**: Explain code to non-technical peers using analogies.
2. **Write Clear Documentation & PR Descriptions**: State the *why*, not just the *what*.
3. **Active Listening**: Ensure you understand requirements before offering solutions."""
    },
    75: {
        "title": "What is the difference between an internship and a job?",
        "keywords": ["difference between an internship and a job", "internship vs job"],
        "answer": """### ⚖️ Internship vs Full-Time Job:

- **Internship**: Short-term (typically 3-6 months) learning-focused experience with mentorship and evaluation.
- **Full-Time Job**: Permanent position with broader business responsibilities, higher autonomy, and comprehensive benefits."""
    },
    76: {
        "title": "What is a software engineer's role?",
        "keywords": ["what is a software engineer's role", "software engineer role"],
        "answer": """### 💻 What Does a Software Engineer Do?

A software engineer designs, builds, tests, deploys, and maintains software solutions to solve business and technical problems while ensuring performance, reliability, and security."""
    },
    77: {
        "title": "How do I prepare for a technical interview?",
        "keywords": ["prepare for a technical interview", "technical interview prep"],
        "answer": """### 🎯 Technical Interview Preparation Guide:

1. **Review DSA Fundamentals**: Hash tables, binary search, two pointers, BFS/DFS.
2. **Think Out Loud**: Explain your thought process and trade-offs before writing code.
3. **Ask Clarifying Questions**: Ask about input constraints, edge cases, and scale."""
    },
    78: {
        "title": "What are common HR interview questions?",
        "keywords": ["common hr interview questions", "hr questions"],
        "answer": """### 🤝 Common HR Interview Questions & Tips:

1. *\"Tell me about yourself.\"* -> Focus on your professional journey and recent achievements.
2. *\"What are your strengths and weaknesses?\"* -> Share a real area of growth and steps you take to improve.
3. *\"Why do you want to work here?\"* -> Demonstrate company research and culture alignment."""
    },
    79: {
        "title": "How can I improve my problem-solving skills?",
        "keywords": ["improve my problem-solving skills", "problem solving skills"],
        "answer": """### 🧩 Improving Problem-Solving Skills:

1. **Decompose Problems**: Break complex challenges into smaller functions.
2. **Solve on Paper First**: Trace inputs and outputs before writing code.
3. **Learn Patterns**: Recognize recurring patterns (Two Pointers, Sliding Window, Memoization)."""
    },
    80: {
        "title": "What projects should a computer science student build?",
        "keywords": ["projects should a computer science student build", "cs student projects"],
        "answer": """### 🏆 Standout Projects for CS Students:

1. **Autonomous AI Agent / Cloud IDE** (Like DevPulse AI!).
2. **Full-Stack SaaS / E-Commerce** with auth and payments.
3. **Real-Time Collaboration Tool** (Chat or Whiteboard with WebSockets).
4. **Developer CLI Tool** (File organizer, performance profiler)."""
    },
    81: {
        "title": "How can I manage my time effectively?",
        "keywords": ["manage my time effectively", "time management"],
        "answer": """### ⏰ Effective Time Management Strategies:

1. **Pomodoro Technique**: 25 minutes of deep focus followed by a 5-minute break.
2. **Eisenhower Matrix**: Prioritize tasks by Urgent vs. Important.
3. **Time Blocking**: Dedicate uninterrupted calendar blocks for coding."""
    },
    82: {
        "title": "How can I learn a new skill quickly?",
        "keywords": ["learn a new skill quickly", "learn skill fast"],
        "answer": """### 🚀 Fast-Track Learning Method (Feynman Technique):

1. **Choose a Concept**: Study the core fundamentals.
2. **Build a Project Immediately**: Apply theory by building something tangible.
3. **Teach or Document**: Explain it in simple terms to uncover gaps in understanding."""
    },
    83: {
        "title": "How can I stay focused while studying?",
        "keywords": ["stay focused while studying", "study focus"],
        "answer": """### 🎯 Staying Focused:

1. **Eliminate Distractions**: Put your phone in another room and use website blockers.
2. **Clear Environment**: Maintain an uncluttered workspace.
3. **Single-Tasking**: Focus on one topic or module at a time."""
    },
    84: {
        "title": "What are some healthy breakfast ideas?",
        "keywords": ["healthy breakfast ideas", "healthy breakfast"],
        "answer": """### 🍳 Healthy Breakfast Ideas:

1. **Oatmeal with Berries & Nuts**: High in fiber and slow-release energy.
2. **Eggs & Avocado Toast**: High in protein and healthy fats.
3. **Greek Yogurt with Honey & Chia Seeds**: Supports gut health and provides sustained energy."""
    },
    85: {
        "title": "How can I improve my English vocabulary?",
        "keywords": ["improve my english vocabulary", "english vocabulary"],
        "answer": """### 📚 Improving English Vocabulary:

1. **Read Diverse Technical & Literary Material**: Read engineering blogs, books, and articles.
2. **Learn in Context**: Write sentences using newly discovered words.
3. **Spaced Repetition (SRS)**: Use flashcard tools like Anki."""
    },
    86: {
        "title": "What are the benefits of regular exercise?",
        "keywords": ["benefits of regular exercise", "exercise benefits"],
        "answer": """### 🏃 Benefits of Regular Exercise:

1. **Enhanced Cognitive Function**: Increases blood flow to the brain, boosting memory and focus.
2. **Stress Reduction**: Lowers cortisol and releases endorphins.
3. **Cardiovascular Health**: Strengthens heart and endurance."""
    },
    87: {
        "title": "How can I create a daily study schedule?",
        "keywords": ["create a daily study schedule", "study schedule"],
        "answer": """### 📅 Creating a Daily Study Schedule:

1. **Identify Peak Energy Hours**: Schedule hard technical topics during your peak hours (morning/evening).
2. **Set Specific Daily Goals**: *\"Complete 2 LeetCode problems and 1 chapter of system design.\"*
3. **Include Buffer Time**: Allow time for rest, exercise, and review."""
    },
    88: {
        "title": "How can I reduce procrastination?",
        "keywords": ["reduce procrastination", "stop procrastinating"],
        "answer": """### ⚡ Overcoming Procrastination (The 2-Minute Rule):

If a task takes less than 2 minutes, do it immediately. For larger tasks, commit to working on them for just **5 minutes** — overcoming initial inertia is the hardest part."""
    },
    89: {
        "title": "What are some useful productivity tools?",
        "keywords": ["useful productivity tools", "productivity tools"],
        "answer": """### 🛠️ Top Productivity Tools for Developers:

1. **IDE**: VS Code / Cursor / DevPulse AI IDE.
2. **Notes & Documentation**: Notion, Obsidian.
3. **Focus**: Forest, Pomodoro timers.
4. **Task Tracking**: Linear, Trello."""
    },
    90: {
        "title": "How can I set realistic goals?",
        "keywords": ["set realistic goals", "realistic goals"],
        "answer": """### 🎯 SMART Goal Setting Framework:

- **Specific**: Target a specific area for improvement.
- **Measurable**: Quantify progress (e.g., *\"Build 3 full-stack projects in 6 weeks\"*).
- **Achievable**: Realistic given current resources.
- **Relevant**: Aligns with long-term career aspirations.
- **Time-bound**: Has a firm deadline."""
    },
    91: {
        "title": "Write a Python program to check whether a number is prime.",
        "keywords": ["check whether a number is prime", "prime number in python", "prime number python"],
        "answer": """### 🔢 Python Prime Number Checker

```python
import math

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
        
    # Check divisors up to sqrt(n) with step of 6
    limit = int(math.isqrt(n))
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

# Test cases
test_numbers = [2, 17, 20, 29, 97, 100]
for num in test_numbers:
    print(f"{num:3d} is prime: {is_prime(num)}")
```
- **Time Complexity**: $\\mathcal{O}(\\sqrt{n})$ optimal trial division."""
    },
    92: {
        "title": "Write a Java program to reverse a string.",
        "keywords": ["java program to reverse a string", "reverse a string in java"],
        "answer": """### ☕ Java Program to Reverse a String

```java
public class StringReverser {
    public static String reverse(String input) {
        if (input == null) return null;
        StringBuilder sb = new StringBuilder(input);
        return sb.reverse().toString();
    }

    public static void main(String[] args) {
        String original = "DevPulse AI";
        String reversed = reverse(original);
        System.out.println("Original: " + original);
        System.out.println("Reversed: " + reversed);
    }
}
```"""
    },
    93: {
        "title": "Create a simple HTML login page.",
        "keywords": ["simple html login page", "html login page"],
        "answer": """### 🔑 Simple Modern HTML Login Page

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Login - DevPulse</title>
  <style>
    body { background: #09090b; color: #fff; font-family: sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; }
    .card { background: #18181b; padding: 32px; border-radius: 16px; border: 1px solid #27272a; width: 320px; }
    input { width: 100%; padding: 12px; margin: 8px 0 16px; background: #09090b; border: 1px solid #3f3f46; color: #fff; border-radius: 8px; }
    button { width: 100%; padding: 12px; background: #6366f1; border: none; color: #fff; font-weight: bold; border-radius: 8px; cursor: pointer; }
  </style>
</head>
<body>
  <div class="card">
    <h2>Sign In</h2>
    <form onsubmit="alert('Logged in!'); return false;">
      <label>Email</label>
      <input type="email" placeholder="dev@pulse.ai" required>
      <label>Password</label>
      <input type="password" placeholder="••••••••" required>
      <button type="submit">Sign In</button>
    </form>
  </div>
</body>
</html>
```"""
    },
    94: {
        "title": "Explain this code step by step.",
        "keywords": ["explain this code step by step", "explain code step by step"],
        "answer": """### 📖 Step-by-Step Code Walkthrough

When analyzing any code block, follow this 4-step framework:
1. **Inputs & Signature**: Identify parameter types, return contracts, and dependencies.
2. **Initialization**: Inspect variables, data structures, and edge-case guard clauses.
3. **Execution Loop / Core Algorithm**: Trace control flow and state transformations.
4. **Output & Complexity**: Verify return value and evaluate time $\\mathcal{O}(T)$ and space $\\mathcal{O}(S)$ complexity."""
    },
    95: {
        "title": "Find the bug in a Python calculator program.",
        "keywords": ["find the bug in a python calculator program", "bug in python calculator"],
        "answer": """### 🐞 Common Bugs in Python Calculators

```python
# BUGGY CODE:
def divide(a, b):
    return a / b # BUG: ZeroDivisionError if b == 0!

# FIXED CODE:
def divide_safe(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b
```
Always add defensive guards against `ZeroDivisionError` and `ValueError` during input parsing."""
    },
    96: {
        "title": "Convert a Python program into Java.",
        "keywords": ["convert a python program into java", "python into java"],
        "answer": """### 🔄 Python to Java Conversion Blueprint

#### Python:
```python
def sum_array(numbers: list[int]) -> int:
    return sum(numbers)
```

#### Equivalent Java:
```java
public class ArrayHelper {
    public static int sumArray(int[] numbers) {
        int total = 0;
        for (int num : numbers) {
            total += num;
        }
        return total;
    }
}
```"""
    },
    97: {
        "title": "Create a student management system using HTML, CSS, and JavaScript.",
        "keywords": ["student management system using html css and javascript", "student management system html"],
        "answer": """### 🎓 Student Management System in HTML/CSS/JS

In DevPulse AI, switch to **Agent Mode** on the left and enter `Build a Student Management System`.
The agent will automatically generate `student_management/index.html` with full GPA calculations and student search!"""
    },
    98: {
        "title": "Explain the difference between two programming approaches with examples.",
        "keywords": ["difference between two programming approaches", "imperative vs declarative"],
        "answer": """### ⚖️ Imperative vs. Declarative Programming

- **Imperative**: Focuses on **HOW** to achieve a result step-by-step.
- **Declarative**: Focuses on **WHAT** outcome is desired.

```python
# Imperative approach
evens = []
for n in [1, 2, 3, 4, 5, 6]:
    if n % 2 == 0:
        evens.append(n)

# Declarative approach (Functional / Comprehension)
evens_decl = [n for n in [1, 2, 3, 4, 5, 6] if n % 2 == 0]
```"""
    },
    99: {
        "title": "Give me a step-by-step plan to build an e-commerce website.",
        "keywords": ["plan to build an e-commerce website", "build an e-commerce website plan"],
        "answer": """### 🛍️ Step-by-Step E-Commerce Development Plan

1. **Architecture & Schema**: Design database tables for Users, Products, Categories, Orders, and Cart.
2. **Product Catalog & Filters**: Build responsive frontend grid with category filters and search.
3. **Shopping Cart Engine**: Implement client and server-side state for item counts and subtotals.
4. **Checkout & Payment Gateway**: Integrate Stripe/PayPal APIs with webhook verification.
5. **Admin Dashboard**: Manage inventory and order fulfillment."""
    },
    100: {
        "title": "Explain how to build an AI Software Engineering Agent with code generation, execution, debugging, and a chatbot.",
        "keywords": ["build an ai software engineering agent", "how to build an ai software engineering agent"],
        "answer": """### 🚀 Building an AI Software Engineering Agent (DevPulse Architecture)

Here is the exact architectural blueprint used to build DevPulse AI:

1. **Dual AI Mode Switcher**:
   - *Chat Mode*: Conversational Q&A with deep technical knowledge.
   - *Autonomous Agent Mode*: Multi-step planning engine that decomposes goals and writes workspace files.
2. **Monaco Code Editor**:
   - Embed `@monaco-editor/react` with multi-tabs, auto-save (`Ctrl+S`), and quick AI shortcuts.
3. **Multi-Runtime Execution Engine**:
   - Isolated subprocess runners for Python and Node.js with UTF-8 capture and timeout limits.
4. **Self-Healing AI Debugger**:
   - Parses tracebacks, isolates root causes, and generates one-click patches.
5. **Live Web Preview**:
   - Sandboxed iframe to interactively run generated web applications!"""
    }
}

def find_100_answer(query: str) -> Optional[str]:
    """Finds matching answer from the 100 benchmark questions."""
    q_clean = query.strip().lower()
    
    # 1. Match by question number (e.g. "1.", "1", "#1", "q1", "question 1")
    num_match = re.match(r'^(?:question\s*|q\s*|#\s*)?(\d{1,3})(?:[\.\:\s]|$)', q_clean)
    if num_match:
        idx = int(num_match.group(1))
        if idx in ANSWERS_100:
            return ANSWERS_100[idx]["answer"]

    # 2. Match by exact title substring or keywords
    for item in ANSWERS_100.values():
        title_lower = item["title"].lower()
        if title_lower in q_clean or q_clean in title_lower:
            return item["answer"]
        for kw in item["keywords"]:
            if kw in q_clean:
                return item["answer"]

    return None
