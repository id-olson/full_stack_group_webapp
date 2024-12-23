import React, { useState, useEffect } from "react";
import axios from "axios";
import Cookies from "js-cookie";
import { useNavigate, Link } from "react-router-dom";
import { Container, Row, Col, Form, Button } from "react-bootstrap";
import { useUser } from "./UserContext";

axios.defaults.xsrfCookieName = "csrfToken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

/**
 * Represents an authentication form for signin and signup.
 *
 * This component allows a user to either sign in or sign up
 * based on the selected authentication mode. The mode can
 * be switched between 'signin' and 'signup'. The form submits
 * the data to a specified URL and then navigates to another
 * page upon successful authentication.
 *
 * @param {Object} props - The properties passed to the component.
 * @returns {React.Component} The `AuthForm` component.
 */

export default function AuthForm(props) {
  const [email, setEmail] = useState("");
  const [pwd, setPwd] = useState("");
  const [id, setId] = useState("");
  let [authMode, setAuthMode] = useState("signin");
  const [showSuccess, setShowSuccess] = useState(false);
  const { setUsername } = useUser(); // Get setUsername from context
  const navigate = useNavigate();

  useEffect(() => {
    const modeFromURL = new URLSearchParams(window.location.search).get("mode");
    if (modeFromURL && (modeFromURL === "signup" || modeFromURL === "signin")) {
      setAuthMode(modeFromURL);
    }
  }, []);

  //   TODO: This is where authentication needs to occur. Other pages will be blocked depending on auth token.

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (!email || !pwd) {
      console.error("Email and password are required.");
      return; // Prevent further execution
    }

    const url =
      authMode === "signin"
        ? "http://localhost:8000/sudoku/signin/"
        : "http://localhost:8000/sudoku/signup/";

    const data = authMode === "signin" ? { email, pwd } : { id, email, pwd };

    const csrfToken = Cookies.get("csrfToken");

    try {
      console.log(`Sending data to ${url}:`, JSON.stringify(data));
      let response = await axios.post(url, JSON.stringify(data), {
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,
        },
      });
      if (response.status === 200) {
        if (authMode === "signin") {
          setUsername(email); // Set username in context after successful sign in
        } else if (authMode === "signup") {
          setUsername(email); // Also set it after signing up
          setShowSuccess(true);
        }
        navigate("/components/Games"); // Navigate after setting the context
      }

      console.log(`${authMode} response:`, response.data);
      setShowSuccess(true);
    } catch (error) {
      console.error(`Error during ${authMode}:`, error);
    }
  };

  const changeAuthMode = () => {
    setAuthMode(authMode === "signin" ? "signup" : "signin");
    setShowSuccess(false);
  };

  return (
    <div id="wrapper">
      <div id="authContainer">
        <Container fluid>
          <Row>
            <Col id="authCol">
              {/* Success message! */}
              {showSuccess && (
                <div
                  style={{
                    color: "green",
                    backgroundColor: "lightgreen",
                    padding: "10px",
                    marginBottom: "10px",
                  }}
                >
                  Account created successfully!
                </div>
              )}
              <header>
                <h1 style={{ textAlign: "center" }}>
                  {authMode === "signin" ? "Sign In" : "Sign Up"}
                </h1>
              </header>
              <br></br>
              {/* depending on the authmode, the content of the screen is determined */}
              {authMode === "signin" && (
                <Form className="Auth-form">
                  <Form.Group className="mb-3" as={Row}>
                    <Form.Label column sm={2}>
                      Email Address
                    </Form.Label>
                    <Col sm={10}>
                      <Form.Control
                        type="email"
                        placeholder="Enter email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                      />
                    </Col>
                  </Form.Group>
                  <Form.Group as={Row}>
                    <Form.Label column sm={2}>
                      Password
                    </Form.Label>
                    <Col sm={10}>
                      <Form.Control
                        type="password"
                        placeholder="Enter password"
                        value={pwd}
                        onChange={(e) => setPwd(e.target.value)}
                      />
                    </Col>
                  </Form.Group>
                </Form>
              )}
              {authMode === "signup" && (
                <Form className="Auth-form">
                  <Form.Group className="mb-3" as={Row}>
                    <Form.Label column sm={2}>
                      ID
                    </Form.Label>
                    <Col sm={10}>
                      <Form.Control
                        type="text"
                        placeholder="Enter ID"
                        value={id}
                        onChange={(e) => setId(e.target.value)}
                      />
                    </Col>
                  </Form.Group>
                  <Form.Group className="mb-3" as={Row}>
                    <Form.Label column sm={2}>
                      Email Address
                    </Form.Label>
                    <Col sm={10}>
                      <Form.Control
                        type="email"
                        placeholder="Enter email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                      />
                    </Col>
                  </Form.Group>
                  <Form.Group as={Row}>
                    <Form.Label column sm={2}>
                      Password
                    </Form.Label>
                    <Col sm={10}>
                      <Form.Control
                        type="password"
                        placeholder="Enter password"
                        value={pwd}
                        onChange={(e) => setPwd(e.target.value)}
                      />
                    </Col>
                  </Form.Group>
                </Form>
              )}
              <br></br>
              <Button variant="primary" onClick={handleSubmit} size="lg">
                Submit
              </Button>
              {/* SIGNIN REROUTE */}
              <p className="text-center mt-2">
                {authMode === "signin"
                  ? "Need an account? "
                  : "Already registered? "}
                <Button variant="secondary" onClick={changeAuthMode} size="sm">
                  {authMode === "signin" ? "Sign Up" : "Sign In"}
                </Button>
              </p>
              <Link to="/">
                <Button variant="secondary">Back Home</Button>
              </Link>
            </Col>
          </Row>
        </Container>
      </div>
    </div>
  );
}
