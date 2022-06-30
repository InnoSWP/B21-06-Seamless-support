import React from "react";
import './css/FAQ.css'

const AskVolunteer = (props) => {
    const clickHandle = () => {
        console.log('Asking the volunteer')
        props.onAsk(2,{
            us_id: '101',
            quest: props.question,
        })
    }
    return (
        <div className={'ask-volunteer'} onClick={clickHandle}>
            <svg width="23" height="25" viewBox="0 0 23 25" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path
                    d="M21 9.0359C23.6667 10.5755 23.6667 14.4245 21 15.9641L6.74999 24.1913C4.08333 25.7309 0.749999 23.8064 0.749999 20.7272L0.75 4.27275C0.75 1.19355 4.08333 -0.730944 6.75 0.808657L21 9.0359Z"
                    fill="#078500"/>
            </svg>
            <p>Ask the question: <span className={'bold'}>"{props.question}?"</span> to the volunteer</p>
        </div>
    )
}

export default AskVolunteer;