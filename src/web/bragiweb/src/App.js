import React, { Component } from 'react';
import './App.css';
import {fetchApi} from "./utils/restMethods.js"


var config = require('./config/bragi.config.json');

const logo = require("./static/images/bragiportrait.jpg");//No me deja usar una constante de config.bragiPortrait

//import SideMenu from './utils/SideMenu.js'

class App extends Component {
  constructor(props){
    super(props)
    this.state = {helloString: "Hello world!"};
    fetchApi("/").then((result) => {
      this.setState({helloString:result});
     });
  }
  render() {
    
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} alt=""></img>
          <p> { this.state.helloString } </p>
        </header>
      </div>
    );
  }
}

export default App;
