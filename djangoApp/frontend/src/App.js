import ChatPage from "./components/chatPage/ChatPage";
import './App.css';
import MainPage from "./components/MainPage";
import React, {useState} from "react";



function App() {
    const [currPage, setCurrPage] = useState('Chat');
    const page = currPage === 'Main' ? <MainPage/>:<ChatPage/>
  return (
    <div className="App">
        {page}
    </div>
  );
}

export default App;
