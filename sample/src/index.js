import React, {useState} from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from './App';

// function Salutation({ fname, lname }) {
//   return (
//     <h1>
//       Hello {fname} {lname}
//     </h1>
//   );
// }

// function SaluteAll() {
//   let info = [
//     ["1", "2"],
//     ["3", "4"],
//   ];
//   let info2 = [];
//   let shift = function () {
//     let item = info.pop();
//     info2.push(item);
//   }
//   return (
//     <div>
//     <button onClick={shift}>Click me</button>
//       <h1>List One</h1>
//       <div>
//         {info.map((item) => {
//           return <Salutation fname={item[0]} lname={item[1]} />;
//         })}
//       </div>
//       <h2>List 2</h2>
//       <div>
//       {info2.map((item) => {
//           return <Salutation fname={item[0]} lname={item[1]} />;
//         })}
//       </div>
//     </div>
//   );
// }

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  // <Salutation fame={"Anuj"} lname={'kuch'}/>,
  // <SaluteAll />,
  document.getElementById("root")
);
