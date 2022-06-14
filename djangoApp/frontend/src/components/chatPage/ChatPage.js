import React from "react";
import BackHeader from "../BackHeader";
import SendMessage from "./SendMessage";
import ReceiveMessage from "./ReceiveMessage";
import Footer from "./Footer";

import './css/ChatPage.css'

const ChatPage = () =>{
    const user = 101;

    const messages = [
        {
            from: 101,
            to: 120,
            what: 'Registration?',
            key: 1
        },
        {
            from: 120,
            to: 101,
            what: 'Yes',
            key: 2
        },
        {
            from: 101,
            to: 120,
            what: 'When?',
            key: 3
        },
        {
            from: 120,
            to: 101,
            what: 'Tomorrow',
            key: 4
        }
    ]

    const chat = messages.map(
        (message) =>{
            let len = Math.ceil(message.what.length/2);
            len = Math.max(len, 15);
            len = Math.min(len, 40);
            const offset = 97 - len + '%';
            len += '%'
            if(message.from === user){
                return <SendMessage key = {message.key} what = {message.what} wid = {len} offset = {offset}/>
            }
            return <ReceiveMessage key = {message.key} what = {message.what} wid = {len}/>
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