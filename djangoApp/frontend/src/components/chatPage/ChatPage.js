import React, {useEffect, useState} from "react";
import BackHeader from "../BackHeader";
import SendMessage from "./SendMessage";
import ReceiveMessage from "./ReceiveMessage";
import Footer from "./Footer";

import './css/ChatPage.css'
import axios from "axios";

const ChatPage = (props) =>{

    const [messages, setMessages] = useState([]); //The list of messages
    const user_id = props.user_id; //User_id got from Auth page

    // useEffect(()=>{
    //     getMessages()
    // },[])

    const getMessages = () =>{
        axios({
                method: 'GET',
                url: '/messages/',
                params: {
                    id: user_id
                }
            }
        ).then((response) => {
            const data = response.data;
            setMessages([...messages,data]);
        }).catch((error) => {
            console.log(error.response);
            console.log(error.response.status);
            console.log(error.response.headers);
        })
    } //Getting the

    const sendMessage = (str) => {
        console.log(str);
        axios({
                method: 'POST',
                url: '/send/',
                data: {
                    user_id: user_id,
                    question: str
                }
            }
        )

        setMessages([...messages, {from: user_id, what: str, key: messages.length + 1}]);
    }
    const chat = messages.map(
        (message) =>{
            let len = Math.ceil(message.what.length/2);
            len = Math.max(len, 9);
            len = Math.min(len, 40);
            const offset = 97 - len + '%';
            len += '%'
            if(message.from === user_id){
                return <SendMessage key = {message.key} what = {message.what} wid = {len} offset = {offset}/>
            }
            return <ReceiveMessage key = {message.key} what = {message.what} wid = {len}/>
        }
    )
    return (
      <div className={'chat-page'}>
          <BackHeader/>
          <div className={'chat-window'}> {chat}</div>
          <Footer onSend = {sendMessage}/>
      </div>
    );
}

export default ChatPage;