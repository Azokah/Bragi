import React, { Component } from 'react'
import {fetchApi} from "./restMethods.js"
import '../App.css';
import Parser from 'html-react-parser';

var config = require('../config/bragi.config.json');

//const logo = require("../static/images/tenor.gif");//No me deja usar una constante de config.bragiPortrait


class Twitter extends Component {
  constructor(props){
    super(props)
    this.state = {helloString: "Twitter",text: "No records of tweets yet.", htmlText: "No records of tweets yet."};
    
    fetchApi("/twitter/get_timeline").then((result) => {
      this.setState({text:result});
      //this.setState({htmlText: this.createFeed()});
      //console.log(this.state.htmlText);
     });
  }
  
  handleSubmit(event) {
		event.preventDefault();
		//CE5J60664
		console.log("Mandando: ");
		console.log(event.target[0].value);
		console.log(event.target[1].value);

		fetch(config.url_api + '/twitter/post_tweet', {
			method: 'post',
			headers: {
				'Accept': 'text/plain',
    			'Content-Type': 'text/plain'
			  },
			body: JSON.stringify({
				mensaje: event.target[0].value,
			  })
		});
	}

  createFeed(){
    var html = "";
    console.log(this.state.text);
		for (var i = 0; i < this.state.text.length; i++) {
      html += "++++++++++++++++++++++++++++++++++++";
      html +=  "<p>" + this.state.text[i].user +': ' + this.state.text[i].mensaje + "</p>";
    }
    return html;
	}
  
  render() {
		return (
			<div>
				<header className="App-header">
					<p> Twitter</p>
				</header>
				<div>
					<p/>
					<form onSubmit={this.handleSubmit}>
						<p /><label>Tweet:
                		<input type="text" name="mensaje" className="MessageInputText" />
						</label>
						<p /><input type="submit" value="Submit" />
					</form>
				</div>
        <div className="ScrollBox">
          {Parser(this.createFeed())}
				</div>
			</div>
		);
	}
}

export default Twitter;