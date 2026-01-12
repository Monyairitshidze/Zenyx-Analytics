import Home from "./Components/HomePage/Home"
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Register from "./Components/Authentication/Registration/Register";
import Login from "./Components/Authentication/Login/Login";

function App() {


  return (

    <>
    <Router>
      <Routes>
        <Route path="/login" element={<Login/>} />
         <Route path="/register" element={<Register/>} />
        <Route path="/" element={<Home />} />
      </Routes>
    </Router>
    </>
  )
}

export default App
