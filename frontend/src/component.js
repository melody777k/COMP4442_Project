import { useState } from "react";
import "./App.css";

export function NavBar() {

  let Links = [
    { name: "Summary", link: "/summary" },
    { name: "Diagram", link: "/diagram" },
    { name: "Home", link: "/" },
  ];

  return (
    <div className="navbar">
      <div>
        <p className="title">Admin Page</p>
      </div>
      <ul className="links">
        {Links.map((link) => (
          <li key={link.name} className="link">
            <a href={link.link}>{link.name}</a>
          </li>
        ))}
      </ul>
    </div>
  );
}