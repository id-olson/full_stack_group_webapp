import React from "react";
import { Link } from "react-router-dom";
import { Image, Button } from "react-bootstrap";

/**
 * HomePage component serving as the landing page of the Sudoku App.
 *
 * This component displays a welcome message and provides navigation options for
 * user authentication. It includes buttons for 'Signup' and 'Signin', each
 * directing the user to the corresponding authentication mode within the app.
 *
 * @returns {React.Component} A React component that represents the home page
 *         of the Sudoku App, including options to navigate to signup or signin.
 */

const HomePage = () => {
  return (
    <div id="wrapper">
      <div id="homeContainer">
        <header>
          <Image src="ll_logo.png" alt="logo" id="logo" rounded />
          <h1 className="hometext">
            <b>Welcome to Sudoku</b>
          </h1>
        </header>
        <br></br>
        <div className="hometext">
          <h5>Solve, save, and explore new board styles in one place.</h5>
          <h5>Register or Login to begin.</h5>
        </div>
        <br></br>
        <div className="home_buttons">
          <div className="d-grid gap-2">
            <Link to="/components/auth?mode=signup">
              <Button variant="secondary" size="lg">
                Register
              </Button>
            </Link>
            <Link to="/components/auth?mode=signin">
              <Button variant="secondary" size="lg">
                Login
              </Button>
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
