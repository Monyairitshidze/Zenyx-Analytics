import { useEffect, useState } from "react"
import "./Dashbord.css"

export default function Dashbord(){

    const [user,setUser] = useState(null)

    useEffect(()=>{

        fetch("http://127.0.0.1:8000/me")
        .then(
            (response)=>response.json())
        .then(
            (data)=>{
            setUser(data)
        })
        .catch((error)=>{
            console.log("Data displayed")
        })
    },[])

    if (!user) {
    return <h2>Loading...</h2>;
  }

    return(

        <>
        <div className="dashbord-cover">

            <div className="dashbord">

                <div className="button-cover">

                    <div className="button">

                        <ul className="button">

                            <li>
                                <h3>Dashboard</h3>
                            </li>

                            <li>
                            <button
                            className="home">Home</button>
                            </li>
                             <li>
                            <button
                            className="records">Records</button>
                            </li>
                             <li>
                            <button
                            className="analyse">Analyse</button>
                            </li>
                             <li>
                            <button
                            className="logout">Logout</button>
                            </li>

                        </ul>

                    </div>

                </div>

                <div className="left-side-cover">

                    <div className="left-side">

                        <h1>Welcome Back </h1>
                        <h2>Your details are</h2>
                        <table>

                            <th>fullName
                                <td>{ user.fullName }</td>
                            </th>
                            <th>username
                                <td>{ user.username }</td>
                            </th>
                            <th>email
                                <td>{ user.email }</td>
                            </th>
                             <th>password
                                <td>{ user.password }</td>
                            </th>
                             <th>confirmPassword
                                <td>{ user.confirmPassword }</td>
                            </th>
                        </table>

                    </div>

                    <div className="image-cover">

                        <img src="images/images3.jpg" 
                        alt="analyzing-image" 
                        className="analyze"/>

                    </div>

                </div>

            </div>
        </div>
        
        </>
    )
}