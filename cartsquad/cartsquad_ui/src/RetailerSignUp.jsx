import { useState } from 'react';

import './styles.css'; 

function RetailerSignUp() {

  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [products, setProducts] = useState('');
  const [phone, setPhone] = useState('');
  const [address, setAddress] = useState('');
  const [city, setCity] = useState('');
  const [state, setState] = useState('');
  const productOptions = [
  'Home', 
  'Electronics',
  'Decor',
  'Accessories',
  'Other'
];

  const handleSubmit = (e) => {
    e.preventDefault();
    
    // submit form data to API
    console.log(name, email, password, products, phone, address, city, state);
  };

  return (
    <div className="form-container">
      <h1>Retailer Sign Up</h1>

      <form onSubmit={handleSubmit}>
        <input 
          type="text" 
          placeholder="Business Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          className="form-input" 
        />

        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="form-input"
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="form-input"
        />

       
    <select 
      className="product-select"
      value={products}
      onChange={(e) => setProducts(e.target.value)}
    >
      <option value="">Products</option>
      {productOptions.map(option => (
        <option key={option} value={option}>
          {option}
        </option>
      ))}
    </select>

        <div style={{padding: '10px 0'}}></div> 
  

        <input
          type="tel"
          placeholder="Phone Number"
          value={phone}
          onChange={(e) => setPhone(e.target.value)}
          className="form-input"
        />

        <input
          type="text"
          placeholder="Address"
          value={address}
          onChange={(e) => setAddress(e.target.value)}
          className="form-input"
        />

        <input
          type="text"
          placeholder="City"
          value={city}
          onChange={(e) => setCity(e.target.value)}
          className="form-input"
        />

        <input
          type="text"
          placeholder="State"
          value={state}
          onChange={(e) => setState(e.target.value)}
          className="form-input"
        />

        <button type="submit" className="submit-btn">
          Sign Up
        </button>
      </form>
    </div>
  );
}

export default RetailerSignUp;