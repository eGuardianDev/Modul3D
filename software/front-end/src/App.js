import './App.css';
import Navigation from "./Elements/Navigation"
import {BrowserRouter, Route, Switch} from "react-router-dom";
function App() {
  return (
    <BrowserRouter>
    <div className="App">
      <Navigation  />
      <Switch>
        
        <Route path="/" exact component={Home}/>
        <Route path="/whattheprintersees" component={Home}/>
      </Switch>
    </div>
      </BrowserRouter>
  );
}
//p 190 text stone превод
//p 191 
//p 46/47 Oral communicaiton translated (ex 4 too)
const Home = () =>{
  return <h1>Doge</h1>
}

export default App;
