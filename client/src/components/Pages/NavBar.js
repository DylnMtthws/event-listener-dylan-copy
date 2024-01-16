import React from "react";
import { NavLink, Outlet } from "react-router-dom";
import {
  AiFillHome,
  AiOutlineUser,
  AiOutlineCalendar,
} from "react-icons/ai/index";

function NavBar() {
  return (
    <div>
      <h1 className="app-title">
        <div className="link-container">
          <NavLink exact to="/" activeClassName="active-link">
            <AiFillHome className="icon"/>
          </NavLink>
          <NavLink to="/manage-users" activeClassName="active-link">
            <AiOutlineUser className="icon"/>
          </NavLink>
          <NavLink to="/manage-events" activeClassName="active-link">
            <AiOutlineCalendar className="icon"/>
          </NavLink>
        </div>
        Event Listener{" "}
      </h1>
      <main>
        <Outlet />
      </main>
    </div>
  );
}

export default NavBar;
