


function upButtonClick(){
  alert("yes");
}
function leftButtonClick(){
  alert("yes");
}
function rightButtonClick(){
  alert("yes");
}
function downButtonClick(){
  alert("yes");
}


const Controls = () =>{
    return(
    <div className='DisplayedPage'>
      <div>
        <h1>Controls</h1>
        <button onClick={upButtonClick}>Front</button>
        <button onClick={leftButtonClick}>Left</button>
        <button onClick={upButtonClick}>Center</button>
        <button onClick={rightButtonClick}>Right</button>
        <button onClick={downButtonClick}>Back</button>

        <br/>
        <br/>
        <br/>
        <button>Up</button>
        <button>Down</button>
      </div>
    </div>
    )
}

export default Controls;