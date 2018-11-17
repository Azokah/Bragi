import React, { Component } from 'react'
import { fetchApi } from "./restMethods.js"
import '../App.css';

var config = require('../config/bragi.config.json');


class SlackSendMessage extends Component {
	constructor(props) {
		super(props)
		this.state = { usersDestination: "null", channelsDestination: "null" };

		fetchApi("/slack/getUsers/").then((result) => {
			this.setState({ usersDestination: result });
		});

		fetchApi("/slack/getChannels/").then((result) => {
			this.setState({ channelsDestination: result });
		});
	}

	handleSubmit(event) {
		event.preventDefault();
		//CE5J60664
		console.log("Mandando: ");
		console.log(event.target[0].value);
		console.log(event.target[1].value);

		fetch(config.url_api + '/slack/sendMsg/', {
			method: 'post',
			headers: {
				'Accept': 'application/json, text/plain, */*',
    			'Content-Type': 'application/json'
			  },
			body: JSON.stringify({
				channel: event.target[0].value,
				mensaje: event.target[1].value,
			  })
		});

		//console log

	}

	render() {
		return (
			<div>
				<header className="App-header">
					<p> {JSON.stringify(this.state.usersDestination)} </p>
					<p> {JSON.stringify(this.state.channelsDestination)} </p>
				</header>
				<div>
					<form onSubmit={this.handleSubmit}>
						<label>Destinatario:
                <input type="text" name="channel" className="inputText" />
						</label>
						<p /><label>Mensaje:
                <input type="text" name="mensaje" className="MessageInputText" />
						</label>
						<p /><input type="submit" value="Submit" />
					</form>
				</div>
			</div>
		);
	}
}

export default SlackSendMessage;