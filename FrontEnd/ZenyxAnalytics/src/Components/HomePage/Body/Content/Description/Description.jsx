import "./Description.css"
import {useNavigate} from "react-router-dom"

export default function Description(){

  const navigate = useNavigate()

  const navigation = ()=>{

       navigate("/login")
  }

    return(

        <>
        <div className="descCover">
            <div className="desc">

             <div className="para">
              <p className="d">
                Welcome to ZenyxAnalytics a smart data analysis system designed to support data-driven decision making. Turn information into insights and insights into action
              </p>

              </div>

              <img src="/images/7steps.png" alt="desc picturer" />
              

            </div>

            <button className="sign-in" onClick={navigation}>Sign In</button>
        </div>
        </>
    )
}