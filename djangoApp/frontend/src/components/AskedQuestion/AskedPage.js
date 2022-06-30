import React from "react";
import BackHeader from "../BackHeader";
import SendMessage from "../chatPage/SendMessage";
import ReceiveMessage from "../chatPage/ReceiveMessage";


const AskedPage = (props) =>{
    const backHandler = () => {
        props.onBack(0, {})
    }
    const me = props.user_id;
    const messages = props.data;
    const chat = messages.map(
        (message, index) => {
            let len = Math.ceil(message.text.length / 2);
            len = Math.max(len, 9);
            len = Math.min(len, 40);
            const offset = 97 - len + '%';
            len += '%'
            console.log([message.from_id, me])
            if (message.from_id === me) {
                return <SendMessage key={index} what={message.text} wid={len} offset={offset}/>
            }
            return <ReceiveMessage key={index} what={message.text} wid={len}/>
        }
    )
    return(
        <div>
            <BackHeader onBack={backHandler}/>
            <div className={'chat-window'}>{chat}</div>
        </div>
    )
}

export default AskedPage;