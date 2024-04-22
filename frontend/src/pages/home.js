import { useState } from "react";
import '../App.css'

export function home() {

  return (
    <div>
      <div className="title position">Home</div>
      <Operations />
    </div>
  );
}

export function Operations() {

  return (
    <div>
      <div className="position text">Hello, you can jump to these two pages</div>
      <table className="text">
        <thead>
          <td>Operations</td>
          <td>Links</td>
        </thead>
        <tr>
          <td>For checking the driving behavior information:</td>
          <td><a href="/summary">Summary</a></td>
        </tr>
        <tr>
          <td>A diagram to visualize the driving speed of each driver:</td>
          <td><a href="/diagram">Diagram</a></td>
        </tr>
      </table>
    </div>
  );
}

export default home;