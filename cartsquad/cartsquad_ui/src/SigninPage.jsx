// SigninPage.js

import { useState } from 'react';

import './styles.css';

function SignIn() {

const [email, setEmail] = useState('');

const [password, setPassword] = useState('');

const handleSubmit = async (e) => {

// submit logic

};

return (

<div className="form-container"> <h1>Sign In</h1> <form onSubmit={handleSubmit}>
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

<button type="submit" className="submit-btn">
Sign In

</button> </form> </div>
);

}

export default SignIn;