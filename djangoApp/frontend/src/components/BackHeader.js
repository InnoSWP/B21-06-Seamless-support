import React, {useState} from "react";
import arrow from './img/arrowLeft.png'
import './css/BackHeader.css'

const BackHeader = () => {
    return(
        <div className={'back-header'}>
            <div className={'back-button'}>
                <img src = {arrow} alt={'afajfja'}/>
                <p>Back</p>
            </div>
        </div>
    );
}

export default BackHeader;