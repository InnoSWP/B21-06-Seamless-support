import "./index.css";
//
// import logo from "./logo.svg";
import "./App.css";
import React from "react";
import MainPage from "./components/mainPage/MainPage";
import ChatPage from "./components/chatPage/ChatPage";

const App = () => {

   return (
    <div className="App">
      <ChatPage user_id = {'101'}/>
    </div>
  );
}

export default App;