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
          <td>For checking the booking list from clients:</td>
          <td><a href="/bookinglist">Booking List</a></td>
        </tr>
        <tr>
          <td>For finding all the hairstylists (Hairstylists' List):</td>
          <td><a href="/hairstylists">All Hairstylists</a></td>
        </tr>
        <tr>
        <td>For finding all the hairstylists' holiday (Hairstylists' Holiday List):</td>
          <td><a href="/hairstylistholiday">Hairstylists Holiday List</a></td>
        </tr>
      </table>
    </div>
  );
}

export default home;