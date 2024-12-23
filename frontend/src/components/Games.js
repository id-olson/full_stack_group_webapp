import React, { useState, useEffect } from "react";
import { Container, Row, Col, Button, Navbar, Nav } from "react-bootstrap";
import { Link, useNavigate } from "react-router-dom";
import { useUser } from "./UserContext";
const emailRegex = /^(.*?)@/;

/**
 * Games component that displays a list of game options.
 *
 * This component renders a welcome message and provides buttons
 * for different game options, such as playing Sudoku. It also includes
 * a logout button that redirects the user to the signin page. Additional
 * games can be added as commented out, like the Killer Sudoku option.
 *
 * @returns {React.Component} A React component representing the games
 *         selection interface, including navigation options for each game
 *         and a logout button.
 */

const Games = () => {
  const { username, sudokuStyle, setSudokuStyle } = useUser();
  const navigate = useNavigate();
  const displayName = username.match(emailRegex)?.[1] || username;

  const updateStyle = async (style) => {
    setSudokuStyle(style); // Save style in user context
    console.log("Sudoku style updated to:", style); // Log the intended style
    setTimeout(() => {
      console.log("Current sudokuStyle after delay:", sudokuStyle); // Log after delay
    }, 9000);
  };

  const handleKillerSudoku = () => {
    updateStyle("killer");
    //console.log("Current sudokuStyle:", sudokuStyle); // Log the current state value
  };

  const handleNormalSudoku = () => {
    updateStyle("normal");
  };

  return (
    <div>
      <Navbar bg="dark" data-bs-theme="dark">
        <Container>
          <Navbar.Brand>Sudoku</Navbar.Brand>
          <Link to="/">
            <Nav>Logout</Nav>
          </Link>
        </Container>
      </Navbar>
      <Container id="gamesContainer">
        <header>
          <br />
          <h1>
            <b>Welcome, {displayName}</b>
          </h1>
          <br />
        </header>
        <Row>
          <Col className="gamesCol">
            <h3>
              <b>Classic Sudoku</b>
              <p className="gamesDesc">The sudoku you're used to.</p>
            </h3>
            <br />
            <Link to="/components/SudokuGame">
              <Button
                variant="secondary"
                size="lg"
                onClick={handleNormalSudoku}
              >
                Play
              </Button>
            </Link>
          </Col>
          <Col className="gamesCol">
            <h3>
              <b>Killer Sudoku</b>
              <p className="gamesDesc">
                The sum of the cells in a cage must equal the total given for
                that cage. Each digit in the cage must be unique.
              </p>
              <p>
                <b>UNDER CONSTRUCTION</b>
              </p>
            </h3>
            <br />
            <Link to="/components/SudokuGame">
              <Button
                variant="secondary"
                size="lg"
                onClick={handleKillerSudoku}
              >
                Play
              </Button>
            </Link>
          </Col>
        </Row>
      </Container>
    </div>
  );
};

export default Games;
