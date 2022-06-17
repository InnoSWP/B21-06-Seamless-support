import React from "react";

const ReceiveMessage = (props) =>{
    return(
        <div className={'message'} style={{width: props.wid, backgroundColor: '#12152a',position: "relative", left: '10px'}}>
            <p>{props.what}</p>
        </div>
    );
}

export default ReceiveMessage;