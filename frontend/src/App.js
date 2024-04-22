import './App.css';
import Summary from './pages/Summary.js';
import Diagram from './pages/Diagram.js';
import { BrowserRouter as Router, Link, Routes, Route } from 'react-router-dom';
import { NavBar } from "./component.js";

function App() {
  return (
    <div className="App">

    <Router>
        <NavBar />
        <hr className="hr"/>
      <div>
        <Routes>
          <Route path="/summary" element={<Summary />} />
          <Route path="/diagram" element={<Diagram />} />
        </Routes>
      </div>

    </Router>
  </div>
    
  );
}

export default App;
