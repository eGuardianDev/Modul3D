import axios from 'axios';
import React from "react";

class Home extends React.Component {
    constructor(){
        super();
    }
    state = {backend: false, printing: false,printingState: 0};
    async componentDidMount(){
         axios.get('http://192.168.0.106:5000')
        .then(response=>{this.setState({backend:true,printing:response.data.printing})})
        //.then(data => this.setState({backend:true,printing: data.printing, printingState: data.printingState}));    
    }
    render(){
        return(
    <div className='DisplayedPage'>
      <div>
        <h1>Main data</h1>
        <h1>Status: {this.state.backend ? "online" : "offline"}</h1>
        <h1>Printing: {this.state.printing ? "online" : "offline"}</h1>
        <h1>Printing state: 0%</h1>
      </div>
    </div>
    )
    }
}

export default Home;