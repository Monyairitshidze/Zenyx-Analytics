 import { useState } from "react"
import "./Login.css"
import { useNavigate } from "react-router-dom"

 export default function Login(){

    const [username,setUsername] = useState("")
    const [password,setPassword] = useState("")

    const navigate = useNavigate()

    const get = async()=>{
        
        try{
        const response = await fetch("http://127.0.0.1:8000/login",{
        
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify({

                username :username,
                password :password
            }
            )
        
        })

        const data = await response.json()
        console.log(data)

        if(response.ok){

            alert("Login successfully")
            navigate("/dashbord")
        }

    }catch(error){

     alert("Server error")
    }
    }


   const submit = (e) => {

    e.preventDefault(); 

    if(username.length > 0 && password.length > 8){

        get(); 
    } else {
        alert("Please enter a valid username and password");
    }
}


    return(

        <>
        <div className="outer_l_cover">

            <div className="form_cover">

                <h2>Welcome Back</h2>
                <h3>Login here</h3>

                <form onSubmit={submit}>

                    <label id="r">username</label>
                    <input type="text" 
                    placeholder="eg.zenyx@1+" 
                    required
                    onChange={(e)=>setUsername(e.target.value)}/>
                    <label id="r">password</label>
                    <input type="password" 
                    placeholder="eg.pa28hcdsju9236e" 
                    required
                    onChange={(e)=>setPassword(e.target.value)}/>

                    <button className="login" type="submit">Login</button>

                    <p>Don't have account? <a href="/register">Register here</a></p>
                </form>

            </div>

        </div>
        </>
    )
 }