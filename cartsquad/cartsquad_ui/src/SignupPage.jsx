import { useState } from 'react';

import { Link } from 'react-router-dom';


function SignUp() {

  const [name, setName] = useState('');

  const [email, setEmail] = useState('');

  const [password, setPassword] = useState('');

  const [dob, setDob] = useState('');

  const [age, setAge] = useState('');

  const [gender, setGender] = useState('');

  const [phone, setPhone] = useState('');

  const [address, setAddress] = useState('');

  const [city, setCity] = useState('');

  const [state, setState] = useState('');

  const [country, setCountry] = useState('');

  const [pincode, setPincode] = useState('');

  const [memberType, setMemberType] = useState('parent');
  
  const [userType, setUserType] = useState('customer');

  const [products, setProducts] = useState('');

  const memberTypes = ['parent', 'child', 'family'];

  const handleSubmit = async (e) => {
    e.preventDefault();
    // submit logic
  };

  return (
    <div className="form-container">
      <h1>Sign Up</h1>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Name"
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

        <input
          type="date"
          placeholder="Date of Birth"
          value={dob}
          onChange={(e) => setDob(e.target.value)}
          className="form-input"
        />


        <select
          value={gender}
          onChange={(e) => setGender(e.target.value)}
          className="form-input"
        >
          <option value="male">Male</option>
          <option value="female">Female</option>
          <option value="other">Other</option>
        </select>

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

        <input
          type="text"
          placeholder="Country"
          value={country}
          onChange={(e) => setCountry(e.target.value)}
          className="form-input"
        />

        <input
          type="text"
          placeholder="Zipcode"
          value={pincode}
          onChange={(e) => setPincode(e.target.value)}
          className="form-input"
        />

        <button type="submit" className="submit-btn">
          Sign Up
        </button>
      </form>
      <div style={{padding: '10px 0'}}></div> 
     <Link to="/retailer-signup">
     <button className="other-btn">Retailer Sign Up</button> 
     </Link>
    <div style={{padding: '10px 0'}}></div> 
     <Link to="/signin">
     <button className="other-btn">Already have an account? Sign In</button>
     </Link>
    </div>
  );
}

export default SignUp;