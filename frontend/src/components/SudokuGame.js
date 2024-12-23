import React, { useEffect, useState } from "react";
import SudokuGrid from "./SudokuGrid"; // Ensure this path is correct
import { Link } from "react-router-dom";
import {
  Container,
  Button,
  Navbar,
  Nav,
  ButtonGroup,
  DropdownButton,
  Dropdown,
} from "react-bootstrap";
import axios from "axios";
import Cookies from "js-cookie";
import { useUser } from "./UserContext";

/**
 * The SudokuGame component provides an interface for users to play Sudoku.
 * It allows users to start a new game or load a previously saved game.
 * The component has different modes, such as selecting a new game,
 * choosing difficulty, or loading a saved game.
 *
 * @returns {React.Component} A React component that displays game mode
 * selection, difficulty selection, and handles loading saved games. It
 * also has navigation elements to switch between the Sudoku game and other
 * parts of the application.
 */

const SudokuGame = () => {
  // Get 'sudokuStyle' from context
  const [gameMode, setGameMode] = useState(""); // 'new' or 'saved'
  //const [reset, trigReset] = useState(false); // triggers a page reload
  const [difficulty, setDifficulty] = useState(null);
  const [savedGames, setSavedGames] = useState([]);
  const [selectedGame, setSelectedGame] = useState(null);
  const { username, sudokuStyle } = useUser();

  const data = {
    username: username,
  };

  const loadSavedGame = async () => {
    try {
      const csrfToken = Cookies.get("csrfToken");
      const response = await axios.get(
        "http://localhost:8000/api/saved-game/",
        {
          params: { username, style: sudokuStyle },
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken,
          },
        },
      );
      setSavedGames(response.data);
    } catch (error) {
      console.error("Error fetching saved game data", error);
    }
  };

  const handleGameModeSelect = (mode) => {
    setGameMode(mode);
    if (mode === "saved") {
      loadSavedGame();
    }
  };

  const handleSavedGameSelect = (gameId) => {
    const game = savedGames.find((game) => game.id === gameId);
    setSelectedGame(game); // Set the specific saved game data
    setGameMode("saved"); // Change game mode
  };

  const handleDifficultySelect = (selectedDifficulty) => {
    setDifficulty(selectedDifficulty); // Change difficulty
  };

  return (
    <div>
      <div>
        <Navbar bg="dark" data-bs-theme="dark">
          <Container>
            <Link to="/components/Games">
              <Navbar.Brand>Sudoku</Navbar.Brand>
            </Link>
            <Link to="/">
              <Nav>Logout</Nav>
            </Link>
          </Container>
        </Navbar>
      </div>
      <div>
        <Container id="gameSpace">
          {!gameMode && (
            <div>
              <h3>What do you want to do?</h3>
              <p>
                Start a new board, or pick up where you left off with an old
                one.
              </p>
              <br></br>
              <ButtonGroup size="lg" className="mb-2">
                <Button
                  onClick={() => handleGameModeSelect("new")}
                  variant="primary"
                >
                  New Game
                </Button>
                <Button
                  onClick={() => handleGameModeSelect("saved")}
                  variant="primary"
                >
                  Load Saved Game
                </Button>
              </ButtonGroup>
              <br></br>
              <Link to="/components/Games">
                <Button variant="secondary">Back</Button>
              </Link>
            </div>
          )}
          {gameMode === "new" && !difficulty && (
            <div>
              <h3>Difficulty Select</h3>
              <p>
                An easy board will have fewer empty cells. A hard one will have
                the most.
              </p>
              <br></br>
              <ButtonGroup size="lg" className="mb-2">
                <Button
                  onClick={() => handleDifficultySelect("Easy")}
                  variant="primary"
                >
                  Easy
                </Button>
                <Button
                  onClick={() => handleDifficultySelect("Medium")}
                  variant="primary"
                >
                  Medium
                </Button>
                <Button
                  onClick={() => handleDifficultySelect("Hard")}
                  variant="primary"
                >
                  Hard
                </Button>
              </ButtonGroup>
              <br></br>
              <Button
                variant="secondary"
                onClick={() => {
                  setGameMode("");
                }}
              >
                Back
              </Button>
            </div>
          )}
          {!selectedGame && gameMode === "saved" && savedGames.length > 0 && (
            <div className="loaded-game">
              <h3>Choose one of your old games.</h3>
              <DropdownButton title="Load a game" size="lg">
                {savedGames.map((game) => (
                  <Dropdown.Item
                    as="button"
                    key={game.id}
                    variant="secondary"
                    onClick={() => handleSavedGameSelect(game.id)}
                  >
                    Load Game {game.id}
                  </Dropdown.Item>
                ))}
              </DropdownButton>
              <br></br>
              <Button
                variant="secondary"
                onClick={() => {
                  setGameMode("");
                }}
              >
                Back
              </Button>
            </div>
          )}
          {difficulty && (
            <SudokuGrid difficulty={difficulty} username={username} />
          )}
          {selectedGame && <SudokuGrid savedGrid={selectedGame} />}
        </Container>
      </div>
    </div>
  );
};

export default SudokuGame;
