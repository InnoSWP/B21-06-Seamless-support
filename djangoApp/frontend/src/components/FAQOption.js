import React from "react";

const FAQOption = (props) =>{
  const clickHandler = () =>{
      const args = {
          chat_id: props.message.chat_id,
          user_id: props.message.user_id,
          vol_id: props.message.vol_id,
      }
      props.onSee(1,args);
  }
  return(
      <div className={'option'} onClick={clickHandler}>
        <svg width="23" height="25" viewBox="0 0 23 25" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M21 9.0359C23.6667 10.5755 23.6667 14.4245 21 15.9641L6.74999 24.1913C4.08333 25.7309 0.749999 23.8064 0.749999 20.7272L0.75 4.27275C0.75 1.19355 4.08333 -0.730944 6.75 0.808657L21 9.0359Z" fill="#12152A"/>
        </svg>
        <p>
          {props.message.question}
        </p>
      </div>
  )
}
export default FAQOption;