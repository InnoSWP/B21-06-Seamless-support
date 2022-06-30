import React from "react";
import arrow from './img/arrowLeft.png'
import './css/BackHeader.css'

const BackHeader = () => {
    return(
        <div className={'back-header'}>
            <div className={'back-button'} onClick="history.back()">
                <img src = {arrow} alt={'afajfja'}/>
                <p>Back</p>
            </div>
        </div>
    );
}

export default BackHeader;