import Description from "./Body/Content/Description/Description";
import NavBar from "./NavBar/NavBar";
import WhatWeDo from "./Body/Content/WhatWeDo/WhatWeDo";
import Footer from "./Body/Content/Footer/Footer";

export default function Home(){

    return(

        <>
        <NavBar/>
        <Description/>
        <WhatWeDo/>
        <Footer/>
        </>
    )
}