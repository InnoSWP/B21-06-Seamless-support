import React from "react";
import arrow from './img/arrowLeft.png'
import './css/BackHeader.css'

const BackHeader = (props) => {
    const clickHandler = () => {
        props.onBack()
    }
    return(
        <div className={'back-header'}>
            <div className={'back-button'} onClick={clickHandler}>
                <img src = {arrow} alt={'arrow'}/>
                <p>Back</p>
            </div>
        </div>
    );
}

export default BackHeader;