import React from "react";

const Footer = (props) => {
    const sendHandler = (event) =>{
        const question = document.getElementById('user_input').value.toString();
        document.getElementById('user_input').value = '';
        props.onSend(question);
        event.preventDefault();
    }

    return (
        <div className={'footer'}>
            <form className={'footer-form'}>
                <input id = 'user_input'/>
                <button onClick={(event) => {sendHandler(event)}}>
                    <svg width="32" height="39" viewBox="0 0 32 39" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M29.9934 16.1696C32.3728 17.7524 32.3728 21.2476 29.9934 22.8304L6.71544 38.3151C4.05696 40.0836 0.499998 38.1776 0.499998 34.9847L0.5 4.01533C0.5 0.822383 4.05695 -1.08356 6.71544 0.684883L29.9934 16.1696Z"
                            />
                    </svg>
                </button>
            </form>
        </div>
    );
}

export default Footer;