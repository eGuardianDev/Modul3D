
async function Test(){
    return(await fetch('http://192.168.0.106:5000')
    .then(response=>response.json()));
    

}

const Home = () =>{
    let data = Test();
    console.log(data)
    return(
    <div className='DisplayedPage'>
      <div>
        <h1>Main data</h1>
        <h1>Status: {}</h1>
        <h1>Printing: offline</h1>
        <h1>Printing state: 0%</h1>
        <h1>Back end status: offline</h1>
      </div>
    </div>
    )
}

export default Home;