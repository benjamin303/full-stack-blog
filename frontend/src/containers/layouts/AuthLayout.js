// AuthLayout.js

import React from 'react';
import { Navbar, Container, Nav } from 'react-bootstrap';

function AuthLayout({ children }) {
  return (
    <div>
      <Navbar bg="light">
        <Container>
          <Navbar.Brand href="#home">Authentication Navbar</Navbar.Brand>
          <Nav className="me-auto">
            {/* Add links specific to authentication pages */}
            <Nav.Link href="#login">Login</Nav.Link>
            <Nav.Link href="#register">Register</Nav.Link>
          </Nav>
        </Container>
      </Navbar>
      <br />
      {children}
    </div>
  );
}

export default AuthLayout;
