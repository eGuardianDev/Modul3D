import React from "react";
import {Link} from "react-router-dom";
class Navigation extends React.Component{
render(){
 
  return(
    <div className="NavigationClass">
    <Link to="/"><button >Home</button></Link> 
   <Link to="/controls"><button >Controls</button></Link> 
   <Link to="/gcommand"><button >G-Code</button></Link> 
    <button>Camera</button>
    <button>Data</button>
    </div>
  );
}
}

export default Navigation;