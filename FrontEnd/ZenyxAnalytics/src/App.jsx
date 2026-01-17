import Home from "./Components/HomePage/Home"
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Register from "./Components/Authentication/Registration/Register";
import Login from "./Components/Authentication/Login/Login";
import Dashbord from "./Components/Dashbord/Dashbord";

function App() {


  return (

    <>
    <Router>
      <Routes>
        <Route path="/login" element={<Login/>} />
         <Route path="/register" element={<Register/>} />
        <Route path="/" element={<Home /> }/>
        <Route path="/dashbord" element = {<Dashbord/>}/>
      </Routes>
    </Router>
    </>
  )
}

export default App
