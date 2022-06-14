import React from "react";

const SendMessage = (props) => {
    return (
        <div className={'message'} style={{width: props.wid, backgroundColor: '#078500',position: "relative", left: props.offset}}>
            <p>{props.what}</p>
        </div>
    );
}

export default SendMessage;