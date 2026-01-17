 import { useState } from "react"
 import { useNavigate } from "react-router-dom"
import "./Register.css"

 export default function Register(){

    const [fullName,setFullName] = useState("")
    const [username,setUserName] = useState("")
    const [email,setEmail] = useState("")
    const [password,setPassword] = useState("")
    const [confirmPassword,setconfirmPassword] = useState("")

    const navigate = useNavigate()

    const sendDatatoApi = async () => {
  try {
    const response = await fetch("http://127.0.0.1:8000/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        fullName:fullName,
        username: username,
        email:email,
        password:password,
        confirmPassword:confirmPassword
      }),
    });

    const data = await response.json();
    console.log(data);

    if (response.ok) {
      alert("Registration Successful");
      navigate("/login");
    } else {
      alert(data.detail || "Registration Failed");
    }
  } catch (error) {
    console.error(error);
    alert("Server error");
  }
};

    const submit = (e)=>{

        e.preventDefault()

        if (fullName.length>0 
            && username.length>0
            && email.length>10
            && password.length >8
            && confirmPassword.length >8){

                if(password === confirmPassword)
                  {
                    sendDatatoApi()
                    
                }
                else
                   {

                     alert("Registration Unuccessfully ")
                     alert("Try Again")
                }
            }
                else{

                    alert("Server error")
                }   
    }

    return(

        <>
        <div className="outer_r_cover">

            <div className="form_cover">

                <h2>Hello There</h2>
                

                <form onSubmit={submit}>

                    <label id="r">fullName</label>
                    <input type="text"
                     placeholder="eg.zenyxDev" 
                     required onChange={(e)=>setFullName(
                     e.target.value)}
                     />
                    <label id="r">username</label>
                    <input type="text"
                     placeholder="eg.zenyx@1+"
                     required
                     onChange={(e)=>setUserName(
                     e.target.value)}
                     />
                    <label id="r">email</label>
                    <input type="email" 
                     placeholder="eg.zenyx@gmail.com" 
                     required
                     onChange={(e)=>setEmail(
                     e.target.value)}
                     />
                    <label id="r">password</label>
                    <input type="password" 
                     placeholder="eg.pa28hcdsju9236e" 
                     required
                     onChange={(e)=>setPassword(
                     e.target.value)}
                     />
                    <label id="r">confirmPassword</label>
                    <input type="password" 
                    placeholder="eg.pa28hcdsju9236e" 
                    required
                    onChange={(e)=>setconfirmPassword(
                    e.target.value)}
                     />

                    <button className="register" type="submit">Register</button>

                    <p>Already Register? <a href="/login">Login here</a></p>
                </form>

            </div>

        </div>
        </>
    )
 }