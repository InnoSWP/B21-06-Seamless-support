import ChatPage from './components/chatPage/ChatPage'
import MainPage from './components/MainPage'
import AskedPage from "./components/AskedQuestion/AskedPage";
import './App.css'
import React, {useState} from "react"
import axios from "axios";


function App() {
    const changePage = (index, parameters) => {
        if (index === 0){
            setCurrPage(currPage => <MainPage onPage={changePage}/>)
        }
        if (index === 1) {
            const chat_id = parameters.chat_id;
            const user_id = parameters.user_id;
            const vol_id = parameters.vol_id;
            console.log(parameters)
            axios({
                    method: "GET",
                    url: "chat/",
                    params: {
                        id: chat_id
                    }
                }
            ).then((response) => {
                    console.log("choose the page" + chat_id);
                    console.log(response.data)
                    setCurrPage(currPage => <AskedPage data={response.data} user_id={user_id} onBack={changePage}/>)
                }
            )
        } else if (index === 2) {
            const user_id = parameters.us_id;
            const question = parameters.quest;
            setCurrPage(currPage => <ChatPage user_id={user_id} first_question={question} onBack={changePage}/>)
        }
    }
    const [currPage, setCurrPage] = useState(<MainPage onPage={changePage}/>);
    return (
        <div className="App">
            {currPage}
        </div>
    );
}

export default App;
