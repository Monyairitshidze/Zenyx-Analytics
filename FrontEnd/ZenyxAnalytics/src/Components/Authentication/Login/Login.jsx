 import { useState } from "react"
import "./Login.css"

 export default function Login(){

    const [username,setUsername] = useState("")
    const [password,setPassword] = useState("")

    const submit = async()=>{
        
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

        const data = response.json()
        console.log(data)

        if(response.ok){

            alert("Login successfully")
        }

    }catch(error){

     alert("Server error")
    }
    }

    return(

        <>
        <div className="outer_l_cover">

            <div className="form_cover">

                <h2>Welcome Back</h2>
                <h3>Login here</h3>

                <form>

                    <label id="r">username</label>
                    <input type="text" placeholder="eg.zenyx@1+" required/>
                    <label id="r">password</label>
                    <input type="password" placeholder="eg.pa28hcdsju9236e" required/>

                    <button className="login">Login</button>

                    <p>Don't have account? <a href="/register">Register here</a></p>
                </form>

            </div>

        </div>
        </>
    )
 }