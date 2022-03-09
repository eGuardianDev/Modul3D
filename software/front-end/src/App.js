
//libraires
import {BrowserRouter, Route, Switch} from "react-router-dom";

//css
import './App.css';

//importing elements
import Navigation from "./Elements/Navigation";
import Home from './Elements/Home';
import Controls from './Elements/Controls';
import GCommands from './Elements/GCommands'


function App() {
  return (
    <BrowserRouter>
    <div className="App">
    <style jsx global>{`
        body {
          overflow: hidden; /* Hide scrollbars */
        }
    `}</style>
      <Navigation />
      <Switch>
        <Route path="/" exact component={Home}/>
        <Route path="/controls" component={Controls}/>
        <Route path="/gcommand" component={GCommands}/>
        <Route path="/camera" component={Controls}/>
        <Route path="/data" component={Controls}/>
      </Switch>
    </div>
      </BrowserRouter>
  );
}

export default App;
