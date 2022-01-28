import axios from 'axios';
import React from "react";


function makeSteps(_axis,_steps,_rotation){
  var data = {
    axis: _axis,
    steps: _steps,
    rotation: _rotation
  };
  let config = {
    headers: {
      "Access-Control-Allow-Origin": "*"
    }
  }
  axios.post('http://192.168.0.106:5000/post_test', data, config).then(response => console.log(response.data));

}
class Controls extends React.Component {


  constructor(){
      super();
      this.state = {steps:1};
  }

  
  HandleStatee = (rotation) =>{
    if(this.state.steps === 0 || this.state.steps == null){
      this.state.steps = 0;
    }
    if(rotation === 0 ){
      this.setState({steps:this.state.steps+1});
    }else{
      if(this.state.steps > 1){
        this.setState({steps:this.state.steps-1});
      }
      
    }

  }
    
  render(){
      return(
        <div className='DisplayedPage'>
          <div>
            <h1>Controls</h1> 
            <div className='stepsButtons'>
            <button className='btn' onClick={() => this.HandleStatee(0)}>UP</button>
            <h1>{this.state.steps}</h1>
            <button className='btn' onClick={() => this.HandleStatee(1)}>DOWN</button>
            </div>
            <br/>
            <br/>
            <div className='moveButtons'>
            <button className='btn1' onClick={() => makeSteps("x", this.state.steps, "CW")}>Front</button>
            <br/>
            <button className='btn' onClick={() => makeSteps("y", this.state.steps, "CCW")}>Left</button>
            <button className='btn' onClick={() => makeSteps("hm", this.state.steps, "")}>Center</button>
            <button className='btn' onClick={() => makeSteps("y", this.state.steps, "CW")}>Right</button>
            <br/>
            <button className='btn1' onClick={() => makeSteps("x", this.state.steps, "CCW")}>Back</button>
            </div>
            
            <button>Up</button>
            <button>Down</button>
          </div>
        </div>
  );
  }
}

export default Controls;