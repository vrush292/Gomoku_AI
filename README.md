# 🎮 Gomoku AI

An intelligent implementation of the classic **Gomoku (Five in a Row)** board game built with **Python** and **Pygame**, featuring an AI opponent powered by **Minimax**, **Alpha-Beta Pruning**, and a custom **heuristic evaluation function**.

The AI analyzes board positions, predicts future moves, blocks opponent threats, and searches for winning strategies to provide a challenging gameplay experience.

---

## 📸 Preview

> Add screenshots or a gameplay GIF here.

image.png

---

## ✨ Features

- 🎯 Human vs AI gameplay
- 🧠 Minimax Algorithm
- ⚡ Alpha-Beta Pruning
- 📊 Heuristic Board Evaluation
- 🎲 Intelligent Candidate Move Generation
- 🏆 Immediate Win Detection
- 🛡️ Immediate Threat Blocking
- 📈 Move Ordering Optimization
- ⏳ AI Thinking Delay for realistic gameplay
- 🔄 Restart Game
- ❌ Exit Button
- 🥇 Winner Detection
- 🎨 Clean graphical interface using Pygame

---

## 🛠 Tech Stack

- **Language:** Python
- **GUI:** Pygame
- **Algorithms:**
  - Minimax Search
  - Alpha-Beta Pruning
  - Heuristic Evaluation
  - Move Ordering
  - Candidate Move Generation

---

## 🧠 AI Implementation

The AI evaluates possible future game states using the **Minimax algorithm** while optimizing the search process with **Alpha-Beta Pruning**.

To improve both performance and gameplay quality, several optimizations have been implemented:

- Immediate winning move detection
- Immediate opponent threat blocking
- Candidate move generation (searches only relevant positions)
- Move ordering for efficient Alpha-Beta pruning
- Pattern-based heuristic evaluation

The evaluation function scores board positions using strategic patterns including:

- Five in a Row
- Open Four
- Closed Four
- Open Three
- Closed Three
- Open Two
- Closed Two

This allows the AI to make strategic decisions instead of relying on random or predefined moves.

---

## 📂 Project Structure

```text
gomoku_ai/
│
├── main.py
├── game.py
├── board.py
├── button.py
├── settings.py
│
└── ai/
    ├── ai_player.py
    ├── alpha_beta.py
    ├── evaluation.py
    └── move_generator.py
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/gomoku-ai.git
cd gomoku-ai
```

### Install dependencies

```bash
pip install pygame
```

### Run the game

```bash
python main.py
```

---

## 🎮 How to Play

- You play as **Black (●)**.
- The AI plays as **White (○)**.
- Click on any valid board intersection to place your stone.
- The first player to connect **five consecutive stones** horizontally, vertically, or diagonally wins the game.

---

## 🧩 AI Workflow

```text
Human Move
      │
      ▼
Generate Candidate Moves
      │
      ▼
Immediate Win Check
      │
      ▼
Immediate Block Check
      │
      ▼
Move Ordering
      │
      ▼
Minimax Search
      │
      ▼
Alpha-Beta Pruning
      │
      ▼
Best Move Selected
      │
      ▼
AI Places Stone
```

---

## 📈 Future Improvements

- Difficulty Levels (Easy / Medium / Hard)
- Transposition Table (Zobrist Hashing)
- Iterative Deepening Search
- Undo/Redo Feature
- AI vs AI Mode
- Game Save & Load
- Sound Effects & Animations
- Online Multiplayer

---

## 📚 Concepts Demonstrated

- Artificial Intelligence
- Adversarial Search
- Game Tree Search
- Decision Making
- Heuristic Evaluation
- Optimization Techniques
- Object-Oriented Programming
- Event-Driven Programming

---

## 👩‍💻 Author

**Vrushali Karlekar**

- GitHub: https://github.com/vrush292
- LinkedIn: https://www.linkedin.com/in/vrushali-karlekar-vk4876/

---

## ⭐ If you found this project interesting, consider giving it a star!
