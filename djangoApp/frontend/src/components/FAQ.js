import React, {useState} from "react";
import FAQOption from "./FAQOption";
import AskVolunteer from "./AskVolunteer"
import './css/FAQ.css'

const FAQ = (props) => {
    const chooseHandling = (index, params) => {
        props.onChoose(index, params)
    }
    const options = props.questions;
    const ask = props.question === "" ? <div/> : <AskVolunteer question={props.question}
                                                                                 onAsk={chooseHandling}/>;
    const cls = (props.question === "") && (options.length === 0) ? 'none' : 'faq-box'
    console.log(props.questions)
    const faqOptions = options.map(
        (option, index) => {
            console.log(option);
            return <FAQOption
                key={index}
                message={
                    {
                        question: option.question_text,
                        chat_id: option.chat_id,
                        user_id: option.user_id,
                        vol_id: option.vol_id,
                    }
                }
                onSee={chooseHandling}/>
        }
    )
    return (
        <div className={cls}>
            {ask}
            {faqOptions}
        </div>
    )
}
export default FAQ;