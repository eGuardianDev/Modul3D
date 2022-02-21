import axios from 'axios';
import React from "react";

class Home extends React.Component {
  constructor(){
    super();
  }
    state = {backend: false, printing: false,printingState: 0,module:"No module currently"};
    async componentDidMount(){
         axios.get('http://127.0.01:5000')
        .then(response=>{this.setState({backend:true,printing:response.data.printing})})
        //.then(data => this.setState({backend:true,printing: data.printing, printingState: data.printingState}));    
    }
    render(){
        return(
    <div className='DisplayedPage'>
      <div>
        <h1>Main data</h1>
        <h1>Back end logic server status: {this.state.backend ? "online" : "offline"}</h1>
        <h1>Working: {this.state.printing ? "Yes" : "no"}</h1>
        <h1>Working state: 0%</h1>
        <h1>Current module: {this.state.module}</h1>
      </div>
    </div>
    )
    }
}

export default Home;