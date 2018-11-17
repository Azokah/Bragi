import React, { Component } from 'react'
import {fetchApi} from "./restMethods.js"
import '../App.css';

//var config = require('../config/bragi.config.json');
const logo = require("../static/images/bragiportrait.jpg");//No me deja usar una constante de config.bragiPortrait

//import SideMenu from './utils/SideMenu.js'

class Slack extends Component {
  constructor(props){
    super(props)
	  this.state = {helloString: "Slack"};
  }
  
  render() {
    return (
      <div>
        <header className="App-header">
          <p> { this.state.helloString } </p>
        </header>
      </div>
    );
  }
}

export default Slack;