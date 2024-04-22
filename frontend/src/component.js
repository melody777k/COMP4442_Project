import { useState } from "react";
import "./App.css";

export function NavBar() {

  let Links = [
    { name: "Home", link: "/" },
    { name: "Summary", link: "/summary" },
    { name: "Diagram", link: "/diagram" },
  ];

  return (
    <div className="navbar">
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