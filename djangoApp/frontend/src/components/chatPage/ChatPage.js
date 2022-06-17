import React, {useEffect, useState} from "react";
import BackHeader from "../BackHeader";
import SendMessage from "./SendMessage";
import ReceiveMessage from "./ReceiveMessage";
import Footer from "./Footer";

import './css/ChatPage.css'
import axios from "axios";

const ChatPage = (props) => {

    const [messages, setMessages] = useState([]); //The list of messages
    const me = props.user_id; //User_id got from Auth page

    useEffect(() => {
        let interval = setInterval(() => {
            const res = getMessages();
        }, 5000);
        return () => {
            clearInterval(interval);
        };
    }, []);

    const getMessages = () => {
        axios({
                method: 'GET',
                url: 'send/',
            }
        ).then((response) => {
            const data = response.data[0];
            const msg = {
                from: data.vol_id,
                what: data.answer
            }
            console.log(msg);
            if (msg.what !== '-'){
                setMessages(messages => [...messages,msg]);
            }
        }).catch((error) => {
            console.log(error.response);
            console.log(error.response.status);
            console.log(error.response.headers);
        })

    }

    const sendMessage = (str) => {
        if (str == '') return;
        axios({
                method: 'POST',
                url: 'send/',
                data: {
                    user_id: me,
                    question: str
                }
            }
        )
        setMessages(messages => [...messages, {from: me, what: str, key: messages.length + 1}]);
    }
    const chat = messages.map(
        (message) => {
            let len = Math.ceil(message.what.length / 2);
            len = Math.max(len, 9);
            len = Math.min(len, 40);
            const offset = 97 - len + '%';
            len += '%'
            if (message.from === me) {
                return <SendMessage key={message.key} what={message.what} wid={len} offset={offset}/>
            }
            return <ReceiveMessage key={message.key} what={message.what} wid={len}/>
        }
    )

    return (
        <div className={'chat-page'}>
            <BackHeader/>
            <div className={'chat-window'}> {chat}</div>
            <Footer onSend={sendMessage}/>
        </div>
    );
}

export default ChatPage;