# assistant-Bot-Rescuing-Charger

**Part 1: Bot Rescuing Charger**

In a grid-based scenario, a bot finds itself situated in a square grid, while a vital charger is trapped in one of the squares. The bot's mission is to navigate the grid and rescue the charger.

**Input Format:**
The first line of the input comprises an integer \( N \) ( \(1 < N < 100\) ), indicating the size of the square grid. Following this, \( N \) lines are provided, each containing \( N \) characters. Each cell is represented by '-'. The bot's initial position is denoted by 'b', and the charger's location is indicated by 'c'. The grid follows the Matrix Convention for indexing.

**Output Format:**
The output should consist of a series of moves the bot will take to rescue the charger, separated by '\n' (newline). Permissible moves include LEFT, RIGHT, UP, or DOWN in output.txt file.

**Sample Input:**
```
3
---
-b-
c--
```

**Sample Output:**
```
DOWN
LEFT
```

**Explanation:**
The bot starts at position (2,2) and the charger is located at position (3,1). To rescue the charger, the bot needs to move one step DOWN and one step LEFT.

---

**Part 2: Assistant Implementation**

The assistant utilizes `pyttsx3` for text-to-speech conversion and `os` for opening and reading from the `output.txt` file.
