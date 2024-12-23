import React, { createContext, useContext, useState } from "react";

/**
 * This module defines a context and a provider for managing user-related information,
 * such as the current username, across different parts of a React application.
 *
 * The `UserContext` holds the current user information. The `UserProvider` component
 * allows other components to access and update the user context. The `useUser` hook
 * is a convenient way to consume the context within other components.
 *
 * - `UserContext`: The React context that stores the current user's information.
 * - `UserProvider`: A component that provides the user context to its children.
 * - `useUser`: A custom hook that allows components to access and update the user context.
 *
 * @returns {React.Component} The `UserProvider` component, providing user context to its children.
 */

// Creating the context
const UserContext = createContext(null);

// Exporting the context provider
export const UserProvider = ({ children }) => {
  const [username, setUsername] = useState("");
  const [sudokuStyle, setSudokuStyle] = useState("normal"); // Default value

  return (
    <UserContext.Provider
      value={{ username, setUsername, sudokuStyle, setSudokuStyle }}
    >
      {children}
    </UserContext.Provider>
  );
};

// Hook to use the context
export const useUser = () => useContext(UserContext);
