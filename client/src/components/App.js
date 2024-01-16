import React, { useEffect, useState } from "react";
import {
  createBrowserRouter,
  createRoutesFromElements,
  Route,
  RouterProvider,
} from "react-router-dom";
import Home from "./Pages/Home";
import NavBar from "./Pages/NavBar";
import ManageVolunteers from "./Pages/ManageVolunteers/ManageVolunteers";
import ManageEvents from "./Pages/ManageEvents/ManageEvents";

function App() {
  const [volunteers, setVolunteers] = useState([])

  useEffect(() => {
    fetch("/volunteers")
      .then((r) => r.json())
      .then(setVolunteers)
  }, []);
  //Navbar functionality
  const routes = createRoutesFromElements(
    <Route path="/" element={<NavBar />}>
      <Route index element={<Home />} />
      <Route path="manage-users" element={<ManageVolunteers volunteers={volunteers}/>} />
      <Route path="manage-events" element={<ManageEvents volunteers={volunteers}/>} />
    </Route>
  );

  const router = createBrowserRouter(routes);

  return (
    <>
      <RouterProvider router={router} />
    </>
  );
}

export default App;
