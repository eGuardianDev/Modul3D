import axios from 'axios';
import React from "react";

function IsWorkingState(props) {
  console.log(props.working)
  if (props.working) {
    return <h1>Working state: {props.State}%</h1>
  }
  return <></>;
}

class Home extends React.Component {
  constructor(){
    super();
  }
  // the react form
    state = {backend: false, working: false,workingState: 0,module:"No module currently"};
    async componentDidMount(){
         axios.get('http://127.0.0.1:5000')
        .then(response=>{this.setState({backend:true,working:response.data.Working,workingState:response.data.WorkingPercentage })})
        //.then(data => this.setState({backend:true,printing: data.printing, printingState: data.printingState}));    
      }
      render(){
        return(
    <div className='DisplayedPage'>
      <div>
        <h1>Main data</h1>
        <h1>Back end logic server status: {this.state.backend ? "online" : "offline"}</h1>
        <h1>Working: {this.state.working ? "Yes" : "no"}</h1>
        <IsWorkingState working={this.state.working} State={this.state.workingState} /> 
        <h1>Current module: {this.state.module}</h1>
  
        </div>
    </div>
    )
    }
}

export default Home;