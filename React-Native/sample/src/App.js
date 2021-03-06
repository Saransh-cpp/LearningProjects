// import logo from "./logo.svg";
import "./App.css";
import axios from "axios";

import React, { useState } from "react";

function App() {
  let [users, setUsers] = useState([]);
  // let [count, setCount] = useState(0);

  // let handleOnClick = () => {
  //   setCount(count + 1);
  // }

  let fetch = () => {
    axios.get("https://api.github.com/users").then((response) => {
      setUsers(response.data);
    });
  };

  return (
    <div className="App">
      <button onClick={fetch}>fetch users</button>
      <div>
        {users.map((user, index) => {
          return (
            <img key={index} alt="text" src={user.avatar_url} style={{
            width: "200px",
            height: "200px"
          }} />
          )
        })}
      </div>
      {/* <h1>{count}</h1> */}
      {/* <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header> */}
    </div>
  );
}

export default App;
