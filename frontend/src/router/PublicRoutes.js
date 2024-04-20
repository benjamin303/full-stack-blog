// src/App.js

import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";





function PublicRoutes() {
  return (
    <BrowserRouter>
      <div className="App">
        <Routes>
          {/* Home, Create, and Edit Pages */}
          <Route
            path="/"
            element={
              <Layout header={<HeaderHome />}>
                <Route path="/" element={<Homepage />} />
                <Route path="/create" element={<Create />} />
                <Route path="/edit" element={<Edit />} />
              </Layout>
            }
          />

          {/* Login Page */}
          <Route
            path="/login"
            element={
              <Layout header={<HeaderLogin />}>
                <Login />
              </Layout>
            }
          />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default PublicRoutes;



// src/router/PublicRoutes.js

// src/App.js

// import React from "react";
// import {Routes, Route } from "react-router-dom";

// import HeaderHome from "../containers/layouts/headerHome";
// import Homepage from "../containers/views/home";
// import Create from "../containers/views/create";
// import Edit from "../containers/views/edit";

// import HeaderLogin from "../containers/layouts/headerLogin";
// import Login from "../containers/views/login";

// import Layout from '../containers/layouts/Layout';

// function PublicRoutes() {
//     return (
//       <Routes>
//         {/* Home, Create, and Edit Pages */}
//         <Route
//           path="/"
//           element={
//             <Layout header={<HeaderHome />}>
//               <Route index element={<Homepage />} />
//               <Route path="/create" element={<Create />} />
//               <Route path="/edit" element={<Edit />} />
//             </Layout>
//           }
//         />
  
//         {/* Login Page */}
//         <Route
//           path="/login"
//           element={
//             <Layout header={<HeaderLogin />}>
//               <Login />
//             </Layout>
//           }
//         />
//       </Routes>
//     );
//   }
  
//   export default PublicRoutes;