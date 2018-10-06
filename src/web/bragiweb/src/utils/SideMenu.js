/* https://www.codeproject.com/Tips/1215984/Update-State-of-a-Component-from-Another-in-React */

import React, { Component } from 'react';
import SideNav, { Toggle, Nav, NavItem, NavIcon, NavText } from '@trendmicro/react-sidenav';
import './react-sidenav.css';
var config = require('../config/bragi.config.json');

class SideMenu extends Component {
    render(){
        return(
            <SideNav onSelect={(selected) => {
                // Add your code here
              }}>
              <SideNav.Toggle />
              <SideNav.Nav defaultSelected={config.dashboard_page_string}>
              <NavItem eventKey={config.historical_page_string}>
                  <NavIcon>
                    <img src={require("../static/images/historicals.png")} className="Nav-logo"/>
                  </NavIcon>
                  <NavText>
                    Historicos
                  </NavText>
                  <NavItem eventKey="Enero">
                      <NavText>
                        Enero2018
                      </NavText>
                  </NavItem>
                  <NavItem eventKey="Test">
                      <NavText>
                        Test2019
                      </NavText>
                  </NavItem>
                </NavItem>
              </SideNav.Nav>
            </SideNav>
        );
        
    }
}

export default SideMenu;