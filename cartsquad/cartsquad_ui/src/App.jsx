import { BrowserRouter, Routes, Route } from 'react-router-dom';
import HomePage from './HomePage';
import SignUp from './SignupPage';
import SignIn from './SigninPage';
import RetailerSignUp from './RetailerSignUp';
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/signin" element={<SignIn />} />
        <Route path="/retailer-signup" element={<RetailerSignUp />} /> 
      </Routes>
    </BrowserRouter>
  );
}
export default App;