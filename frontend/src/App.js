import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import DefaultLayout from './containers/layouts/DefaultLayout';
import AuthLayout from './containers/layouts/AuthLayout';

import Home from './containers/views/Home'
import Login from './containers/views/Login';
import Register from './containers/views/Register'

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          {/* Home, Create, and Edit Pages */}
          <Route
            path="/"
            element={
              <DefaultLayout>
                <Route index element={<Home />} />
              </DefaultLayout>
            }
          />

          {/* Login and Register Pages */}
          <Route
            path="/login"
            element={
              <AuthLayout>
                <Login />
              </AuthLayout>
            }
          />
          <Route
            path="/register"
            element={
              <AuthLayout>
                <Register />
              </AuthLayout>
            }
          />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
