import axios from 'axios';  
import React, {useState,useEffect} from "react";

import "./gCode.Style.css"

    
function Buton(prop){
    return(
        <div>
            <button onClick={() =>{axios.post("http://127.0.0.1:5000/openFile", {fileIndex: prop.number})}}>{prop.text}</button>
        </div>
    )
}

function DataInfo() {

    const [dataa, setData] = useState( [] );
  useEffect(() => axios.get("http://127.0.0.1:5000/getgcode").then(response =>  setData(response.data.files)), []);
   
  return (
    <div>
        {dataa.map ((name, index) => <Buton key={index} text={name} number={index} />)}
    </div>
  )
    
}

function Update() {

    const [dataa, setData] = useState( 0 );
     useEffect(() =>{setData(1)}, []);
    console.log("update")
  return;
    
}

function UploadGCode() {
    const [gcode, setCode] = useState("");
  
    const handleSubmit = (event) => {
      event.preventDefault();

      axios.post("http://127.0.0.1:5000/uploadOneGCode", {gcodes: gcode})

    }
  
    return (
      <form onSubmit={handleSubmit}>
        <label>Gcode:
          <input 
            type="text" 
            value={gcode}
            onChange={(e) => setCode(e.target.value)}
          />
        </label>
        <input type="submit" />
      </form>
    )
  }



function IsWorkingState(props) {
    console.log(props.working)
    if (props.working) {
      return <h1>Working state: {props.State}%</h1>
    }
    return <></>;
  }
class GCommands extends React.Component {
  constructor(){
      super();
  }
  state ={
      random:"yes",
      value: "",
      inputValue: ""
  }
  uploadFile = async (e) => {
    const file = e.target.files[0];
    if (file != null) {
      const data = new FormData();
      data.append('file_from_react', file);
      let response = await fetch('http://127.0.0.1:5000/upload_file',
        {
          method: 'post',
          body: data,
        }
      );
      let res = await response.json();
      if (res.status !== 1){
        alert('Error uploading file');
      }window.location.reload(false);
    }
  };



  uploadOneGCode = async (e) => {
      console.log(this.inputValue)
    if (this.state.gCodeCommand != null) {
      const data = new FormData();
      data.append('gCode', this.state.gCodeCommand);
      let response = await fetch('http://127.0.0.1:5000/uploadOneGCode',
        {
          method: 'post',
          body: data,
        }
      );
      let res = await response.json();
      if (res.status !== 1){
        alert('Error uploading file');
      }
    }
  };
 
  render(){
      return(
        <div className='DisplayedPage'> 
        <div>     
                <UploadGCode/>
                <h1>Files</h1>
                <form>
                    <input
                    type="file"
                    onChange={this.uploadFile}>
                    </input>
                </form>
                    
                    <br/>

                 <div>
                 
                 <DataInfo />
                     
                 </div>
                          

            </div>

        </div>
  );
  }
}

export default GCommands;