# assistant-Bot-Rescuing-Charger

**Part 1: Bot Rescuing Charger**

In a scenario set within a square grid, an autonomous bot is placed on the grid, with the critical task of locating and retrieving a trapped charger located in another square. The bot's primary objective is to skillfully navigate through the grid to find and rescue the charger.

**Input Format:**
The input begins with an integer \(N\) (\(1 < N < 100\)), which specifies the dimensions of the square grid. This is followed by \(N\) lines, each containing \(N\) characters, representing the grid itself. Empty cells are marked with '-', the bot's starting position is indicated by 'b', and the charger's location is denoted by 'c'. The grid's indexing follows the conventional Matrix Convention.

**Output Format:**
The output should detail the sequence of moves the bot will execute to reach the charger, with each move delineated by a newline ('\n'). The bot can move LEFT, RIGHT, UP, or DOWN, and these directions should be recorded in the output.txt file.

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
The bot is initially positioned at (2,2), with the charger at (1,1). To successfully rescue the charger, the bot must move one step DOWN followed by one step LEFT.

---

**Part 2: Assistant Implementation**

This part of the implementation leverages `pyttsx3` for converting text into speech, and the `os` module for accessing and reading the `output.txt` file. This setup ensures the bot's interactions are not only visually but also audibly accessible, enhancing the user experience.
