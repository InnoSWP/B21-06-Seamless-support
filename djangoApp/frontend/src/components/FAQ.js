import React from "react";

class FAQ extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
    };
    this.handleClick = this.handleClick.bind(this);
  }
  
  render() {
    return (<div>{this.props.questions.map((elem,index) => <li key={index}> <button > {elem}</button></li>)}</div>)
  }
}
export default FAQ;