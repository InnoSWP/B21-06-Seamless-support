import React, {useEffect, useState} from "react";
import BackHeader from "../BackHeader";
import SendMessage from "./SendMessage";
import ReceiveMessage from "./ReceiveMessage";
import Footer from "./Footer";

import './css/ChatPage.css'
import axios from "axios";

const ChatPage = (props) => {

    const [messages, setMessages] = useState([]); //The list of messages
    const user_id = props.user_id; //User_id got from Auth page

    useEffect(()=>{
        getMessages()
    },[])

    const getMessages = () => {
        axios({
                method: 'GET',
                url: '/messages/',
                params: {
                    id: user_id
                }
            }
        ).then((response) => {
            const data = JSON.parse(response.data);
            console.log(data);
            console.log(data.vol_id);
            const msg = {
                from: data.vol_id,
                what: data.answer
            }

            console.log(msg);
            if (msg.what != '')
                setMessages(messages => [...messages, msg]);
        }).catch((error) => {
            console.log(error.response);
            console.log(error.response.status);
            console.log(error.response.headers);
        })
        clearInterval(k);
    }

    let k = setTimeout(getMessages, 8000);

    const sendMessage = (str) => {
        getMessages();
        if (str == '') return;
        console.log(str);
        axios({
                method: 'POST',
                url: 'send/',
                data: {
                    user_id: user_id,
                    question: str
                }
            }
        )
        setMessages(messages => [...messages, {from: user_id, what: str, key: messages.length + 1}]);
    }
    const chat = messages.map(
        (message) => {
            console.log(message);
            let len = Math.ceil(message.what.length / 2);
            len = Math.max(len, 9);
            len = Math.min(len, 40);
            const offset = 97 - len + '%';
            len += '%'
            if (message.from === user_id) {
                return <SendMessage key={message.key} what={message.what} wid={len} offset={offset}/>
            }
            return <ReceiveMessage key={message.key} what={message.what} wid={len}/>
        }
    )
    return (
      <div className={'chat-page'}>
          <BackHeader/>
          <div className={'chat-window'}> {chat}</div>
          <Footer/>
      </div>
    );
}

export default ChatPage;