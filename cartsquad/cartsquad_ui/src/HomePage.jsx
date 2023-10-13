// HomePage.js

import { Link } from 'react-router-dom';

export default function HomePage() {

  return (
    <div className="home-wrapper">

      {/* Header */}
      <header>
        <nav>
          <Link to="/">Home</Link>
          <Link to="/signin">Sign In</Link>  
          <Link to="/signup">Sign Up</Link>
        </nav>
      </header>

      {/* Search Bar */}
      <div className="search-bar">
        <input 
          type="text" 
          placeholder="Search..."
          className="search-input"
        />
        <button className="search-button">Search</button>
      </div>

    </div>
  );
}