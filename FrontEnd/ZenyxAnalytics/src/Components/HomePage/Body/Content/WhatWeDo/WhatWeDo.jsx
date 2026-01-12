import "./WhatWeDo.css"

const whatwedo = [
   
    {
    
      id : "1",
      heading: "Data Collection & Processing",
      image : "/images/images.png",
      description : "Gather and organize data from different sources, ensuring it is clean, structured, and ready for analysis. This allows accurate and reliable results."
    },

    {
        
         id : "2",
        heading : "Data Analysis & Insights",
        image : "/images/images.jpg",
        description : "Analyze data to identify patterns, trends, and key insights. These insights help users understand information clearly and support smarter decision-making"
    },

    {
        
         id : "3",
        heading : "Decision Support & Reporting",
        image : "/images/images1.png",
        description : "Present results through clear reports and visual summaries, helping users make informed decisions quickly and confidently"
    }

]

export default function WhatWeDo(){

    return(

        <>
        <div className="whatWeDoCover">

                {whatwedo.map(
                    (data)=>(

                 <div className="whatWeDo" key={data.id}>
                 <h1> { data.heading } </h1>
                 <img src = {data.image} alt={data.heading} />
                 <p> { data.description } </p>

                </div>
                
            )
                )}
               
        </div>
        </>
    )

}