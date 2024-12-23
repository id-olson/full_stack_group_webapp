### Sudoku by Logic Luminaries

### Project Description:

Our team will create a Sudoku game application that generates puzzles of varying difficulty levels. The application will support different Sudoku variants and provide an engaging user interface that includes tools for solving puzzles. Users can save puzzles and their progress. A stretch goal is to allow users to solve puzzles within the application, with support for hints and puzzle-solving tools, and export puzzles for printing. (From canvas)

### Requirements:

#### Functional

1. **Puzzle Generation**

   - The game SHALL generate a 9x9 grid representing a Sudoku puzzle
   - The game SHALL allow users to select the difficulty level of the puzzle (ie., easy, medium, hard)
   - STRETCH The game SHALL support generating puzzles for different Sudoku variants (e.g., standard, arrow, killer)

2. **Puzzle Solution**

   - For each generated puzzle, the game SHALL generate a corresponding solution for the puzzle

3. **Puzzle Saving**

   - Users SHALL be able to save generated puzzles and their solutions to their account for future access

4. **User Account Management**

   - Users SHALL be able to create and manage their accounts. Account management includes login, logout, and password management functions.

5. **Puzzle Solving (Stretch Goal)**

   - Users SHALL be able to enter solutions directly into the application. The application SHALL provide immediate feedback on the correctness of the entered solution
   - The system SHALL provide puzzle-solving tools, such as pencil marking and coloring, to assist users in solving puzzles
   - The system SHALL provide hints upon user request

5. **Puzzle Progress and Timing**
   - Users SHALL be able to save their progress on a puzzle

#### Non-Functional

1. **Usability**

   - The application SHALL have an intuitive user interface, making it easy for users of all skill levels to generate and solve puzzles

2. **Performance**

   - Puzzle generation and solution display SHALL be completed within a reasonable time frame not exceeding 5 seconds

3. **Accessibility**

   - The application SHALL be accessible, providing support for users with disabilities according to WCAG 2.1 guidelines

4. **Security**
   - User data, including account information and saved puzzles, SHALL be securely stored. The application SHALL implement industry-standard security practices for data protection

### Use Cases and User Stories

Generator Stories
As a user, I want to be able to generate a sudoku puzzle
As a user, I want to be able to generate an answer for a generated puzzle
As a user, I want to be able to save a generated puzzle to my account
As a user, I want to be able to export a generated puzzle answer guide for printing
As a user, I want to be able to choose to use sudoku variants instead of standard sudoku
As a user, I want to be able to choose the difficulty of generated puzzles
As a user, I want to be able to generate a new puzzle

Solver Stories (extension)
As a user, I want to be able to be able to attempt to solve a puzzle by entering in values
As a user, I want to be able to be able to annotate cells with possible values
As a user, I want to be notified if my solution is correct
As a user, I want to be able to save my progress
As a user, I want to be able to see if any of my moves are invalid
