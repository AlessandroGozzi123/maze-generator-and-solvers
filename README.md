# 🗺️ Maze Generator & Solvers (Python)

Tento projekt obsahuje kompletní implementaci generátoru bludiště a několika vyhledávacích algoritmů pro hledání nejkratší cesty. Projekt vznikl v rámci studia na vysoké škole.

## 🚀 Funkce

* **Generátor bludiště:** Využívá algoritmus **Recursive Backtracking** k vytváření bludišť.
* **Vyhledávací algoritmy (Solvers):**
    * **BFS (Breadth-First Search):** Prohledávání do šířky, které garantuje nalezení nejkratší cesty v neohodnoceném grafu.
    * **Greedy Best-First Search:** Informované vyhledávání zaměřené čistě na heuristiku (Manhattan distance) pro rychlé nalezení cíle.
    * **A* Search:** Kombinuje cenu již ujeté cesty a heuristiku k cíli pro nalezení optimální nejkratší cesty.
* **Vizualizace:** Program automaticky vykresluje nalezenou cestu přímo do konzole pomocí hvězdiček `*`.

## 💻 Jak spustit

1. Vygenerujte bludiště:
   ```bash
   python maze_generator.py

2. Spuštění vyhledávání cest:
   ```bash
   python main.py
